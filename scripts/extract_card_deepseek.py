#!/usr/bin/env python3
"""Call DeepSeek to extract one research-card JSON from parsed chunks."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

import yaml


DEFAULT_BASE_URL = "https://api.deepseek.com/chat/completions"


def load_config(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_json(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_chunks(path: Path) -> List[Dict]:
    records = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                records.append(json.loads(line))
    return records


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def select_doc_ids(manifest: Path, doc_ids: Sequence[str], batch: Optional[str]) -> List[str]:
    if doc_ids:
        return list(doc_ids)
    rows = read_manifest(manifest)
    if batch:
        batch_norm = batch.strip().upper()[0]
        rows = [row for row in rows if row.get("batch", "").strip().upper().startswith(batch_norm)]
    return [row["doc_id"] for row in rows if row.get("doc_id")]


def metadata_for_doc(manifest: Path, doc_id: str) -> Dict[str, str]:
    for row in read_manifest(manifest):
        if row.get("doc_id") == doc_id:
            return row
    return {"doc_id": doc_id}


def strip_json_fence(text: str) -> str:
    stripped = text.strip()
    match = re.match(r"^```(?:json)?\s*(.*?)\s*```$", stripped, flags=re.S)
    if match:
        return match.group(1).strip()
    return stripped


def build_user_prompt(doc_id: str, metadata: Dict, chunks: List[Dict], schema: Dict) -> str:
    chunk_payload = [
        {
            "doc_id": item.get("doc_id"),
            "chunk_id": item.get("chunk_id"),
            "page": item.get("page"),
            "section": item.get("section"),
            "locator": item.get("locator"),
            "content": item.get("content"),
        }
        for item in chunks
    ]
    payload = {
        "doc_id": doc_id,
        "manifest_metadata": metadata,
        "schema": schema,
        "chunks": chunk_payload,
    }
    return "请从以下 JSON 输入中抽取研究卡片，输出必须是符合 schema 的 JSON 对象：\n\n" + json.dumps(
        payload, ensure_ascii=False
    )


def call_deepseek(
    api_key: str,
    base_url: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    retries: int,
) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "response_format": {"type": "json_object"},
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    last_error: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(base_url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = json.loads(response.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
        except (urllib.error.URLError, urllib.error.HTTPError, KeyError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(2 * attempt)
    raise RuntimeError(f"DeepSeek request failed after {retries} attempts: {last_error}")


def write_card(path: Path, raw_text: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")
    parsed = json.loads(strip_json_fence(raw_text))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")


def append_run_log(path: Path, row: Dict[str, str]) -> None:
    fieldnames = [
        "doc_id",
        "model_name",
        "prompt_version",
        "input_chunk_hash",
        "output_card_hash",
        "batch",
        "reviewer",
        "review_date",
        "status",
        "error_message",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    with path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if not exists or path.stat().st_size == 0:
            writer.writeheader()
        writer.writerow({key: row.get(key, "") for key in fieldnames})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("config.yaml"))
    parser.add_argument("--doc-id", action="append", default=[])
    parser.add_argument("--batch", help="A, B, C, or a manifest batch prefix")
    parser.add_argument("--dry-run", action="store_true", help="Write assembled prompts only; do not call API")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    config = load_config(args.config)
    root = args.config.resolve().parent
    chunks_dir = root / config["paths"]["chunks"]
    cards_dir = root / config["paths"]["cards"]
    prompt_path = root / config["model"]["system_prompt_file"]
    schema_path = root / config["paths"]["card_schema"]
    manifest_path = root / config["paths"]["manifest"]
    prompt_log_dir = root / config["paths"]["prompts"]
    run_log_path = root / config["paths"]["logs"] / "run_log.csv"

    system_prompt = prompt_path.read_text(encoding="utf-8")
    schema = load_json(schema_path)
    model = os.environ.get("DEEPSEEK_MODEL", config["model"]["model_name"])
    base_url = os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_BASE_URL)
    api_key = os.environ.get("DEEPSEEK_API_KEY")

    doc_ids = select_doc_ids(manifest_path, args.doc_id, args.batch)
    if not doc_ids:
        print("No documents selected.")
        return 0

    if not args.dry_run and not api_key:
        raise EnvironmentError("DEEPSEEK_API_KEY is required unless --dry-run is set")

    failures = 0
    for doc_id in doc_ids:
        chunk_path = chunks_dir / f"{doc_id}.jsonl"
        if not chunk_path.exists():
            print(f"[missing] {chunk_path}")
            failures += 1
            continue
        chunks = load_chunks(chunk_path)
        metadata = metadata_for_doc(manifest_path, doc_id)
        user_prompt = build_user_prompt(doc_id, metadata, chunks, schema)

        if args.dry_run:
            prompt_log_dir.mkdir(parents=True, exist_ok=True)
            target = prompt_log_dir / f"{doc_id}.extraction_user_prompt.md"
            target.write_text(user_prompt, encoding="utf-8")
            print(f"[dry-run] {doc_id}: prompt -> {target}")
            continue

        raw_text = call_deepseek(
            api_key=api_key or "",
            base_url=base_url,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=args.temperature,
            retries=args.retries,
        )
        target = cards_dir / f"{doc_id}.json"
        write_card(target, raw_text, args.force)
        append_run_log(
            run_log_path,
            {
                "doc_id": doc_id,
                "model_name": model,
                "prompt_version": str(config["model"]["prompt_version"]),
                "input_chunk_hash": file_sha256(chunk_path),
                "output_card_hash": file_sha256(target),
                "batch": metadata.get("batch", ""),
                "status": "extracted",
            },
        )
        print(f"[ok] {doc_id}: card -> {target}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
