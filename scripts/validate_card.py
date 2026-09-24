import glob
import json
import os
import re
from pathlib import Path

import yaml


PAGE_RE = re.compile(r"<!--\s*page\s*:\s*([^>]+?)\s*-->")
WHITESPACE_RE = re.compile(r"\s+")
LOCATOR_PREFIX_RE = re.compile(r"^\s*<!--\s*page\s*:\s*[^>]+?\s*-->\s*")
CONTEXT_LOCATOR_MARKERS = ("Section", "图表", "图", "表", "Figure", "Table")
ROOT_REQUIRED_KEYS = ["doc_id", "metadata", "original", "adaptation", "extensions"]
ORIGINAL_REQUIRED_KEYS = [
    "research_scenario",
    "economic_mechanism",
    "data_processing",
    "testing_methods",
    "robustness_and_failures",
    "tradability",
]


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def issue(code, message):
    return {"code": code, "message": message}


def extract_page(locator):
    match = PAGE_RE.search(locator or "")
    return match.group(1).strip() if match else None


def locator_fragment(locator):
    return LOCATOR_PREFIX_RE.sub("", locator or "", count=1).strip()


def normalize_text(text):
    normalized = WHITESPACE_RE.sub("", text or "")
    return (
        normalized.replace("（", "(")
        .replace("）", ")")
        .replace("：", ":")
        .replace("，", ",")
        .replace("。", ".")
        .replace("“", '"')
        .replace("”", '"')
        .lower()
    )


def locator_search_variants(fragment):
    variants = {fragment.strip()}
    stripped = fragment.strip()
    for prefix in ("Section ", "Figure ", "Table "):
        if stripped.startswith(prefix):
            variants.add(stripped[len(prefix) :].strip())
    return [variant for variant in variants if variant]


def load_chunk_records(chunks_dir, doc_id):
    path = Path(chunks_dir) / f"{doc_id}.jsonl"
    if not path.exists():
        return []

    records = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def classify_locator_in_chunks(locator, chunk_records):
    page = extract_page(locator)
    fragment = locator_fragment(locator)

    if not locator or not locator.strip():
        return "schema_violation", "locator 为空"

    if page is None:
        return "schema_violation", "locator 缺少 page 注释"

    page_marker = f"<!-- page: {page} -->"
    page_candidates = []
    for record in chunk_records:
        record_page = str(record.get("page", "")).strip()
        content = record.get("content", "")
        if record_page == page or page_marker in content:
            page_candidates.append(record)
    if not page_candidates:
        return "fabricated_locator", f"未在 chunks 中找到 page {page}"

    if not fragment:
        return "schema_violation", "locator 只有页码，没有正文/图表/章节锚点"

    normalized_variants = [normalize_text(item) for item in locator_search_variants(fragment)]
    for record in page_candidates:
        normalized_content = normalize_text(record.get("content", ""))
        if any(variant and variant in normalized_content for variant in normalized_variants):
            return "found", f"命中 chunk {record.get('chunk_id')}"

    if any(marker.lower() in fragment.lower() for marker in CONTEXT_LOCATOR_MARKERS):
        return "locator_granularity_mismatch", "locator 看起来是图表/章节级引用，但未在页内精确命中"

    return "fabricated_locator", "locator 片段未在对应页 chunks 中找到"


def classify_original_miss(locator, all_locators):
    locator_page = extract_page(locator)
    if locator_page and any(extract_page(existing) == locator_page for existing in all_locators):
        return "locator_granularity_mismatch", "与 original 属同页引用，但未精确复用已有证据"
    return "missing_original_evidence", "locator 能在 chunks 中找到，但 original 未登记这条证据"


def validate_locator_group(source_name, locators, chunk_records, errors, warnings):
    if not isinstance(locators, list):
        errors.append(issue("schema_violation", f"{source_name}.source_locators 必须是数组"))
        return

    for idx, loc in enumerate(locators):
        code, detail = classify_locator_in_chunks(loc, chunk_records)
        if code in {"schema_violation", "fabricated_locator"}:
            errors.append(
                issue(code, f"{source_name}.source_locators[{idx}] 无效: {detail}; locator={loc!r}")
            )
        elif code == "locator_granularity_mismatch":
            warnings.append(
                issue(
                    code,
                    f"{source_name}.source_locators[{idx}] 需要人工复核: {detail}; locator={loc!r}",
                )
            )


def validate_card(card_data, chunk_records):
    errors = []
    warnings = []

    for key in ROOT_REQUIRED_KEYS:
        if key not in card_data:
            errors.append(issue("schema_violation", f"缺少根级别字段: {key}"))

    if errors:
        return errors, warnings

    original = card_data.get("original", {})
    all_locators = set()

    for key in ORIGINAL_REQUIRED_KEYS:
        section = original.get(key)
        if not section:
            errors.append(issue("schema_violation", f"original 缺少字段: {key}"))
            continue

        desc = section.get("description")
        locators = section.get("source_locators", [])

        if desc != "原文未提及" and not locators:
            errors.append(issue("schema_violation", f"original.{key} 有内容，但缺失 source_locators"))
            continue

        validate_locator_group(f"original.{key}", locators, chunk_records, errors, warnings)
        for loc in locators:
            all_locators.add(loc)

    formulas = original.get("feature_formulas", [])
    if not isinstance(formulas, list):
        errors.append(issue("schema_violation", "original.feature_formulas 必须是数组"))
    else:
        for idx, formula in enumerate(formulas):
            if "formula" not in formula or "source_locators" not in formula:
                errors.append(
                    issue(
                        "schema_violation",
                        f"original.feature_formulas[{idx}] 缺少公式或 source_locators",
                    )
                )
                continue
            locators = formula.get("source_locators", [])
            validate_locator_group(
                f"original.feature_formulas[{idx}]",
                locators,
                chunk_records,
                errors,
                warnings,
            )
            for loc in locators:
                all_locators.add(loc)

    adaptation = card_data.get("adaptation", {})
    if adaptation.get("data_sufficiency") not in {"sufficient", "partial", "insufficient"}:
        errors.append(
            issue(
                "schema_violation",
                "adaptation.data_sufficiency 必须是 sufficient / partial / insufficient 之一",
            )
        )
    if adaptation.get("replication_mode") not in {"direct", "adjust", "infeasible"}:
        errors.append(
            issue(
                "schema_violation",
                "adaptation.replication_mode 必须是 direct / adjust / infeasible 之一",
            )
        )

    extensions = card_data.get("extensions", [])
    if not isinstance(extensions, list):
        errors.append(issue("schema_violation", "extensions 必须是数组"))
        return errors, warnings

    for idx, ext in enumerate(extensions):
        ext_locators = ext.get("source_locators", [])
        if not ext.get("hypothesis"):
            errors.append(issue("schema_violation", f"extensions[{idx}] 缺少 hypothesis"))
        if not ext_locators:
            errors.append(issue("schema_violation", f"extensions[{idx}] 缺少 source_locators"))
            continue

        basis_ids = ext.get("basis_evidence_ids", [])
        if basis_ids and not isinstance(basis_ids, list):
            errors.append(
                issue("schema_violation", f"extensions[{idx}].basis_evidence_ids 必须是数组")
            )

        for loc in ext_locators:
            chunk_code, chunk_detail = classify_locator_in_chunks(loc, chunk_records)
            if chunk_code == "schema_violation":
                errors.append(
                    issue(
                        "schema_violation",
                        f"extensions[{idx}] 的 locator 不合规: {chunk_detail}; locator={loc!r}",
                    )
                )
                continue
            if chunk_code == "fabricated_locator":
                errors.append(
                    issue(
                        "fabricated_locator",
                        f"extensions[{idx}] 的 locator 在 chunks 中找不到: {chunk_detail}; locator={loc!r}",
                    )
                )
                continue
            if chunk_code == "locator_granularity_mismatch":
                warnings.append(
                    issue(
                        "locator_granularity_mismatch",
                        f"extensions[{idx}] 的 locator 需要人工复核: {chunk_detail}; locator={loc!r}",
                    )
                )
                continue

            if loc in all_locators:
                continue

            code, detail = classify_original_miss(loc, all_locators)
            warnings.append(
                issue(
                    code,
                    f"extensions[{idx}] 引用未在 original 精确登记: {detail}; locator={loc!r}",
                )
            )

    return errors, warnings


def main():
    config = load_config()
    cards_dir = config["paths"]["cards"]
    chunks_dir = config["paths"]["chunks"]

    json_files = glob.glob(os.path.join(cards_dir, "*.json"))
    if not json_files:
        print("未找到任何 JSON 卡片文件以供校验。")
        return 0

    total_files = len(json_files)
    machine_fail = 0
    manual_pending = 0
    machine_pass = 0

    for jf in sorted(json_files):
        filename = os.path.basename(jf)
        doc_id = os.path.splitext(filename)[0]

        with open(jf, "r", encoding="utf-8") as f:
            try:
                card_data = json.load(f)
            except json.JSONDecodeError:
                machine_fail += 1
                print(f"❌ [{doc_id}] machine_fail")
                print("   - [schema_violation] JSON 格式错误，无法解析。")
                continue

        chunk_records = load_chunk_records(chunks_dir, doc_id)
        if not chunk_records:
            machine_fail += 1
            print(f"❌ [{doc_id}] machine_fail")
            print("   - [schema_violation] 未找到对应的 chunk 文件，无法校验 locator。")
            continue

        errors, warnings = validate_card(card_data, chunk_records)
        if errors:
            machine_fail += 1
            print(f"❌ [{doc_id}] machine_fail")
            for entry in errors:
                print(f"   - [{entry['code']}] {entry['message']}")
            for entry in warnings:
                print(f"   ! [{entry['code']}] {entry['message']}")
            continue

        if warnings:
            manual_pending += 1
            print(f"⚠️ [{doc_id}] manual_pending")
            for entry in warnings:
                print(f"   ! [{entry['code']}] {entry['message']}")
            continue

        machine_pass += 1
        print(f"✅ [{doc_id}] machine_pass")

    print(
        f"\n校验完成: 总计 {total_files} 篇, "
        f"machine_pass {machine_pass} 篇, "
        f"manual_pending {manual_pending} 篇, "
        f"machine_fail {machine_fail} 篇。"
    )
    return 1 if machine_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
