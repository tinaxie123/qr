#!/usr/bin/env python3
"""Split parsed Markdown literature files into locator-preserving JSONL chunks."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

import yaml


PAGE_PATTERNS = [
    re.compile(r"^\s*<!--\s*page\s*[:=]\s*([0-9ivxlcdmIVXLCDM]+)\s*-->\s*$"),
    re.compile(r"^\s*\[page\s*[:=]\s*([0-9ivxlcdmIVXLCDM]+)\]\s*$"),
    re.compile(r"^\s*-{2,}\s*page\s+([0-9ivxlcdmIVXLCDM]+)\s*-{2,}\s*$", re.I),
    re.compile(r"^\s*#{1,6}\s*page\s+([0-9ivxlcdmIVXLCDM]+)\s*$", re.I),
    re.compile(r"^\s*第\s*([0-9一二三四五六七八九十百]+)\s*页\s*$"),
]
HEADING_RE = re.compile(r"^\s*(#{1,6})\s+(.+?)\s*$")


def load_config(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


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


def detect_page(line: str) -> Optional[str]:
    for pattern in PAGE_PATTERNS:
        match = pattern.match(line)
        if match:
            return match.group(1)
    return None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def flush_chunk(
    records: List[Dict],
    doc_id: str,
    chunk_index: int,
    lines: List[str],
    page: Optional[str],
    section: Optional[str],
    start_line: int,
    end_line: int,
) -> int:
    content = "\n".join(lines).strip()
    if not content:
        return chunk_index
    chunk_id = f"{doc_id}_chunk_{chunk_index:04d}"
    locator_parts = [doc_id, chunk_id]
    if page:
        locator_parts.append(f"p.{page}")
    if section:
        locator_parts.append(section)
    records.append(
        {
            "doc_id": doc_id,
            "chunk_id": chunk_id,
            "page": page,
            "section": section,
            "line_start": start_line,
            "line_end": end_line,
            "locator": " | ".join(locator_parts),
            "content_sha256": sha256_text(content),
            "content": content,
        }
    )
    return chunk_index + 1


def split_markdown(doc_id: str, text: str, max_chars: int) -> List[Dict]:
    records: List[Dict] = []
    current_page: Optional[str] = None
    current_section: Optional[str] = None
    chunk_page: Optional[str] = None
    chunk_section: Optional[str] = None
    chunk_lines: List[str] = []
    chunk_start_line = 1
    chunk_index = 1

    lines = text.splitlines()
    for line_no, line in enumerate(lines, start=1):
        page = detect_page(line)
        if page:
            current_page = page
            if not chunk_page:
                chunk_page = page

        heading = HEADING_RE.match(line)
        if heading:
            current_section = heading.group(2).strip()
            if not chunk_section:
                chunk_section = current_section

        if not chunk_lines:
            chunk_start_line = line_no
            chunk_page = current_page
            chunk_section = current_section

        projected_len = len("\n".join(chunk_lines)) + len(line) + 1
        should_flush_before_heading = bool(heading and chunk_lines and projected_len > max_chars * 0.45)
        if projected_len > max_chars or should_flush_before_heading:
            chunk_index = flush_chunk(
                records,
                doc_id,
                chunk_index,
                chunk_lines,
                chunk_page,
                chunk_section,
                chunk_start_line,
                line_no - 1,
            )
            chunk_lines = []
            chunk_start_line = line_no
            chunk_page = current_page
            chunk_section = current_section

        chunk_lines.append(line)

    if chunk_lines:
        flush_chunk(
            records,
            doc_id,
            chunk_index,
            chunk_lines,
            chunk_page,
            chunk_section,
            chunk_start_line,
            len(lines),
        )
    return records


def write_jsonl(path: Path, records: Iterable[Dict], force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config.yaml", type=Path)
    parser.add_argument("--doc-id", action="append", default=[])
    parser.add_argument("--batch", help="A, B, C, or a manifest batch prefix")
    parser.add_argument("--max-chars", type=int, default=6000)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config)
    root = args.config.resolve().parent
    parsed_dir = root / config["paths"]["parsed"]
    chunks_dir = root / config["paths"]["chunks"]
    manifest_path = root / config["paths"]["manifest"]

    doc_ids = select_doc_ids(manifest_path, args.doc_id, args.batch)
    if not doc_ids:
        print("No documents selected.")
        return 0

    failures = 0
    for doc_id in doc_ids:
        source = parsed_dir / f"{doc_id}.md"
        if not source.exists():
            print(f"[missing] {source}")
            failures += 1
            continue
        text = source.read_text(encoding="utf-8")
        records = split_markdown(doc_id, text, args.max_chars)
        target = chunks_dir / f"{doc_id}.jsonl"
        write_jsonl(target, records, args.force)
        print(f"[ok] {doc_id}: {len(records)} chunks -> {target}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
