#!/usr/bin/env python3
"""Parse manifest PDFs with MinerU and render page-anchored Markdown."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import yaml


DATA_IMAGE_MARKDOWN_RE = re.compile(r"!\[[^\]]*\]\(\s*data:image/[^;\s)]+;base64,[A-Za-z0-9+/=\s]+\)", re.S)
DATA_IMAGE_URI_RE = re.compile(r"data:image/[A-Za-z0-9.+-]+;base64,[A-Za-z0-9+/=\s]{200,}", re.S)
LONG_BASE64_LINE_RE = re.compile(r"(?m)^[A-Za-z0-9+/]{1000,}={0,2}$")


def load_config(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def read_manifest(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def select_rows(rows: List[Dict[str, str]], doc_ids: Sequence[str], batch: Optional[str]) -> List[Dict[str, str]]:
    if doc_ids:
        wanted = set(doc_ids)
        return [row for row in rows if row.get("doc_id") in wanted]
    if batch:
        batch_norm = batch.strip().upper()[0]
        return [row for row in rows if row.get("batch", "").strip().upper().startswith(batch_norm)]
    return [row for row in rows if row.get("doc_id")]


def resolve_path(root: Path, value: str) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return root / path


def collect_text(value: Any, parts: List[str]) -> None:
    if value is None:
        return
    if isinstance(value, str):
        if value.strip():
            parts.append(value.strip())
        return
    if isinstance(value, list):
        for item in value:
            collect_text(item, parts)
        return
    if isinstance(value, dict):
        if "content" in value:
            collect_text(value["content"], parts)
        elif "text" in value:
            collect_text(value["text"], parts)


def block_text(block: Dict[str, Any]) -> str:
    parts: List[str] = []
    collect_text(block.get("content"), parts)
    return "\n".join(parts).strip()


def render_block(block: Dict[str, Any]) -> Optional[str]:
    text = block_text(block)
    if not text:
        return None

    block_type = block.get("type", "")
    if block_type == "doc_title":
        return f"# {text}"
    if block_type == "paragraph_title":
        level = int(block.get("level") or 2)
        level = min(max(level, 2), 4)
        return f"{'#' * level} {text}"
    if block_type == "table":
        return f"**[table]**\n\n{text}"
    if block_type == "image":
        return f"**[image_text]**\n\n{text}"
    return text


def render_middle_json(doc_id: str, row: Dict[str, str], data: Dict[str, Any], source_path: Path, tier: str, ocr_mode: str) -> str:
    metadata = data.get("metadata", {})
    producer = metadata.get("producer", {})
    document = metadata.get("document", {})
    pages = data.get("pages", [])

    header = [
        f"# {doc_id} {row.get('title', '').strip()}".strip(),
        "",
        f"- source_path: `{source_path}`",
        "- parser: `MinerU`",
        f"- mineru_version: `{producer.get('version', '')}`",
        f"- mineru_tier: `{tier}`",
        f"- ocr_mode: `{ocr_mode}`",
        f"- lang: {row.get('lang', '')}",
        f"- type: {row.get('type', '')}",
        f"- page_count: {document.get('page_count', len(pages))}",
        "",
    ]

    body: List[str] = []
    for page in pages:
        page_no = int(page.get("page_idx", len(body))) + 1
        body.extend([f"<!-- page: {page_no} -->", "", f"## Page {page_no}", ""])
        for block in page.get("blocks", []):
            rendered = render_block(block)
            if rendered:
                body.extend([rendered, ""])

    return "\n".join(header + body).rstrip() + "\n"


def strip_embedded_base64(text: str) -> tuple[str, int]:
    replacements = 0
    text, count = DATA_IMAGE_MARKDOWN_RE.subn("[embedded image base64 removed]", text)
    replacements += count
    text, count = DATA_IMAGE_URI_RE.subn("[embedded image base64 removed]", text)
    replacements += count
    text, count = LONG_BASE64_LINE_RE.subn("[long base64 line removed]", text)
    replacements += count
    return text, replacements


def find_single_json(path: Path) -> Path:
    candidates = sorted(path.glob("*.json"))
    if not candidates:
        raise FileNotFoundError(f"MinerU did not create a middle_json file in {path}")
    if len(candidates) > 1:
        raise RuntimeError(f"MinerU created multiple JSON files in {path}: {candidates}")
    return candidates[0]


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_parse_qc_summary(qc_dir: Path, summary_path: Path) -> None:
    fieldnames = [
        "doc_id",
        "mineru_version",
        "ocr_mode",
        "tier",
        "source_file",
        "output_markdown",
        "page_count_rendered",
        "block_count",
        "char_count",
        "started_at",
        "finished_at",
        "warnings",
    ]
    rows: List[Dict[str, Any]] = []
    if qc_dir.exists():
        for path in sorted(qc_dir.glob("doc_*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            row = {key: data.get(key, "") for key in fieldnames}
            row["warnings"] = json.dumps(row.get("warnings") or [], ensure_ascii=False)
            rows.append(row)

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run_mineru(
    mineru_bin: Path,
    source_path: Path,
    output_dir: Path,
    pages: str,
    tier: str,
    ocr_mode: str,
    verbose: bool,
) -> subprocess.CompletedProcess[str]:
    command = [
        str(mineru_bin),
        "parse",
        str(source_path),
        "-o",
        str(output_dir),
        "--pages",
        pages,
        "--format",
        "middle_json",
        "--tier",
        tier,
        "--ocr-mode",
        ocr_mode,
    ]
    if verbose:
        command.append("--verbose")
    return subprocess.run(command, text=True, capture_output=True, check=True)


def parse_one(
    root: Path,
    row: Dict[str, str],
    parsed_dir: Path,
    qc_dir: Path,
    mineru_bin: Path,
    pages: str,
    tier: str,
    ocr_mode: str,
    force: bool,
    keep_middle_json: bool,
    verbose: bool,
) -> None:
    doc_id = row["doc_id"]
    source_path = resolve_path(root, row["source_path"])
    target_md = parsed_dir / f"{doc_id}.md"
    target_qc = qc_dir / f"{doc_id}.json"
    target_middle = parsed_dir / f"{doc_id}.mineru.middle.json"

    if target_md.exists() and not force:
        raise FileExistsError(f"{target_md} already exists; pass --force to overwrite")
    if not source_path.exists():
        raise FileNotFoundError(source_path)

    with tempfile.TemporaryDirectory(prefix=f"mineru_{doc_id}_") as tmp:
        tmp_dir = Path(tmp)
        started_at = datetime.now(timezone.utc)
        run_mineru(mineru_bin, source_path, tmp_dir, pages, tier, ocr_mode, verbose)
        middle_path = find_single_json(tmp_dir)
        data = json.loads(middle_path.read_text(encoding="utf-8"))
        rendered = render_middle_json(doc_id, row, data, source_path, tier, ocr_mode)
        rendered, embedded_payload_removed_count = strip_embedded_base64(rendered)
        warnings: List[str] = []
        if embedded_payload_removed_count:
            warnings.append(f"removed {embedded_payload_removed_count} embedded base64/data-image payload(s)")

        parsed_dir.mkdir(parents=True, exist_ok=True)
        target_md.write_text(rendered, encoding="utf-8")
        if keep_middle_json:
            target_middle.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        elif target_middle.exists():
            target_middle.unlink()

        pages_data = data.get("pages", [])
        block_count = sum(len(page.get("blocks", [])) for page in pages_data)
        qc = {
            "doc_id": doc_id,
            "mineru_version": data.get("metadata", {}).get("producer", {}).get("version"),
            "ocr_mode": ocr_mode,
            "tier": tier,
            "source_file": str(source_path),
            "output_markdown": str(target_md),
            "page_count_rendered": len(pages_data),
            "block_count": block_count,
            "char_count": len(rendered),
            "started_at": started_at.isoformat(),
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "warnings": warnings,
        }
        write_json(target_qc, qc)
        print(f"[ok] {doc_id}: {len(pages_data)} pages, {block_count} blocks -> {target_md}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config.yaml", type=Path)
    parser.add_argument("--doc-id", action="append", default=[])
    parser.add_argument("--batch", help="A, B, C, or a manifest batch prefix")
    parser.add_argument("--pages", default=None, help="MinerU page range, e.g. all or 1-5,8")
    parser.add_argument("--tier", default=None, help="MinerU tier: flash/basic/standard/advanced")
    parser.add_argument("--ocr-mode", default=None, help="MinerU OCR mode: auto/txt/ocr")
    parser.add_argument("--mineru-bin", default=None, type=Path)
    parser.add_argument("--keep-middle-json", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config)
    root = args.config.resolve().parent
    parser_config = config.get("parser", {})
    paths = config["paths"]

    mineru_bin = args.mineru_bin or Path(parser_config.get("mineru_bin", ".venv-mineru/bin/mineru-kit"))
    mineru_bin = resolve_path(root, str(mineru_bin))
    tier = args.tier or parser_config.get("tier", "basic")
    ocr_mode = args.ocr_mode or parser_config.get("ocr_mode", "auto")
    pages = args.pages or parser_config.get("pages", "all")

    manifest_path = root / paths["manifest"]
    parsed_dir = root / paths["parsed"]
    qc_dir = root / paths.get("qc", "logs/qc/")
    parse_qc_summary_path = root / paths.get("parse_qc_summary", "logs/parse_qc.csv")
    rows = select_rows(read_manifest(manifest_path), args.doc_id, args.batch)
    if not rows:
        print("No documents selected.")
        return 0

    failures = 0
    for row in rows:
        try:
            parse_one(
                root=root,
                row=row,
                parsed_dir=parsed_dir,
                qc_dir=qc_dir,
                mineru_bin=mineru_bin,
                pages=pages,
                tier=tier,
                ocr_mode=ocr_mode,
                force=args.force,
                keep_middle_json=args.keep_middle_json,
                verbose=args.verbose,
            )
        except Exception as exc:
            failures += 1
            print(f"[failed] {row.get('doc_id')}: {exc}")

    write_parse_qc_summary(qc_dir, parse_qc_summary_path)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
