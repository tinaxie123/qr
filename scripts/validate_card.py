#!/usr/bin/env python3
"""Validate research card JSON files and cross-check evidence references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

from jsonschema import Draft202012Validator


ORIGINAL_FIELDS = [
    "research_setting",
    "research_objective",
    "economic_mechanism",
    "assumptions",
    "raw_data",
    "feature_definition",
    "preprocessing",
    "operators_parameters",
    "computation_boundaries",
    "prediction_target",
    "evaluation_method",
    "data_split",
    "main_results",
    "incremental_value",
    "robustness_failures",
    "trading_feasibility",
    "author_limitations_open_questions",
]


def load_json(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def collect_evidence(card: Dict) -> Tuple[Set[str], List[str]]:
    evidence_ids: Set[str] = set()
    errors: List[str] = []
    doc_id = card.get("doc_id")

    for field in ORIGINAL_FIELDS:
        records = card.get("original", {}).get(field, []) or []
        for index, record in enumerate(records):
            evidence_id = record.get("evidence_id")
            if not evidence_id:
                errors.append(f"original.{field}[{index}] missing evidence_id")
                continue
            if evidence_id in evidence_ids:
                errors.append(f"duplicate evidence_id: {evidence_id}")
            evidence_ids.add(evidence_id)

            for locator_index, locator in enumerate(record.get("source_locators", [])):
                locator_doc_id = locator.get("doc_id")
                if locator_doc_id != doc_id:
                    errors.append(
                        f"{evidence_id}.source_locators[{locator_index}] doc_id={locator_doc_id!r}, expected {doc_id!r}"
                    )
                if not locator.get("chunk_id"):
                    errors.append(f"{evidence_id}.source_locators[{locator_index}] missing chunk_id")

    return evidence_ids, errors


def cross_check(card: Dict) -> List[str]:
    errors: List[str] = []
    evidence_ids, evidence_errors = collect_evidence(card)
    errors.extend(evidence_errors)

    index = card.get("source_locators_index", {}) or {}
    for evidence_id in evidence_ids:
        if evidence_id not in index:
            errors.append(f"source_locators_index missing {evidence_id}")

    for extension in card.get("extensions", []) or []:
        extension_id = extension.get("extension_id", "<unknown>")
        for basis_id in extension.get("basis_evidence_ids", []) or []:
            if basis_id not in evidence_ids:
                errors.append(f"extension {extension_id} references unknown basis_evidence_id {basis_id}")

    for missing_index, item in enumerate(card.get("missing_fields", []) or []):
        if not str(item).strip():
            errors.append(f"missing_fields[{missing_index}] is empty")

    return errors


def validate_one(path: Path, schema: Dict) -> List[str]:
    card = load_json(path)
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(card), key=lambda e: list(e.path)):
        loc = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"schema {loc}: {error.message}")
    errors.extend(cross_check(card))
    return errors


def iter_card_paths(args: argparse.Namespace) -> Iterable[Path]:
    if args.cards:
        for card in args.cards:
            yield card
        return
    cards_dir = args.cards_dir
    if not cards_dir.exists():
        return
    for path in sorted(cards_dir.glob("doc_*.json")):
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, default=Path("schemas/research_card.schema.json"))
    parser.add_argument("--cards-dir", type=Path, default=Path("03_cards"))
    parser.add_argument("cards", nargs="*", type=Path)
    args = parser.parse_args()

    schema = load_json(args.schema)
    paths = list(iter_card_paths(args))
    if not paths:
        print("No card JSON files found.")
        return 0

    total_errors = 0
    for path in paths:
        errors = validate_one(path, schema)
        if errors:
            total_errors += len(errors)
            print(f"[fail] {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[ok] {path}")

    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
