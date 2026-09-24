#!/usr/bin/env python3
"""Render research card JSON into a compact Markdown review card."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List


SECTION_TITLES = {
    "research_setting": "研究场景",
    "research_objective": "研究目标",
    "economic_mechanism": "经济机制",
    "assumptions": "成立条件",
    "raw_data": "原始数据",
    "feature_definition": "特征公式",
    "preprocessing": "数据处理",
    "operators_parameters": "算子与参数",
    "computation_boundaries": "计算边界",
    "prediction_target": "预测标签",
    "evaluation_method": "检验方法",
    "data_split": "数据划分",
    "main_results": "主要结果",
    "incremental_value": "增量价值",
    "robustness_failures": "稳健性与失效",
    "trading_feasibility": "交易可实现性",
    "author_limitations_open_questions": "局限与未解问题",
}


def load_json(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def locator_text(record: Dict) -> str:
    parts: List[str] = []
    for locator in record.get("source_locators", []):
        loc = locator.get("chunk_id", "")
        if locator.get("page"):
            loc += f" p.{locator['page']}"
        if locator.get("section"):
            loc += f" {locator['section']}"
        parts.append(loc.strip())
    return "; ".join(part for part in parts if part)


def render_card(card: Dict) -> str:
    metadata = card.get("metadata", {})
    lines: List[str] = []
    lines.append(f"# {card.get('doc_id', '')} 研究卡片")
    lines.append("")
    lines.append(f"- 标题：{metadata.get('title', '')}")
    lines.append(f"- 作者：{metadata.get('author', '')}")
    lines.append(f"- 年份：{metadata.get('year', '')}")
    lines.append(f"- 语言/类型：{metadata.get('lang', '')} / {metadata.get('type', '')}")
    lines.append(f"- 覆盖范围：{card.get('coverage', {}).get('input_scope', '')}")
    lines.append("")

    lines.append("## 原文信息")
    for key, title in SECTION_TITLES.items():
        records = card.get("original", {}).get(key, []) or []
        if not records:
            continue
        lines.append("")
        lines.append(f"### {title}")
        for record in records:
            loc = locator_text(record)
            prefix = f"- `{record.get('evidence_id', '')}` [{record.get('statement_type', '')}]"
            if loc:
                prefix += f" ({loc})"
            lines.append(f"{prefix}: {record.get('content', '')}")

    lines.append("")
    lines.append("## 项目适配")
    adaptation = card.get("adaptation", {})
    lines.append(f"- 评估范围：{adaptation.get('assessment_scope', '')}")
    lines.append(f"- 方法适用性：{adaptation.get('method_applicability', '')}")
    data_support = adaptation.get("data_support", {}) or {}
    lines.append(f"- 可直接支持：{data_support.get('available', '')}")
    lines.append(f"- 可派生：{data_support.get('derivable', '')}")
    lines.append(f"- 缺失：{data_support.get('missing', '')}")
    lines.append(f"- 代理与损失：{data_support.get('proxy_and_loss', '')}")

    changes = adaptation.get("required_changes", []) or []
    if changes:
        lines.append("")
        lines.append("### 需要修改")
        for change in changes:
            lines.append(f"- 原方法：{change.get('original', '')}")
            lines.append(f"  调整原因：{change.get('why', '')}")
            lines.append(f"  调整方式：{change.get('how', '')}")
            if change.get("revalidate"):
                lines.append(f"  需重验：{change.get('revalidate', '')}")

    extensions = card.get("extensions", []) or []
    if extensions:
        lines.append("")
        lines.append("## 扩展假设")
        for extension in extensions:
            basis = ", ".join(extension.get("basis_evidence_ids", []))
            lines.append(f"- `{extension.get('extension_id', '')}` 基于 {basis}: {extension.get('hypothesis', '')}")
            lines.append(f"  特征想法：{extension.get('proposed_feature', '')}")
            lines.append(f"  验证：{extension.get('validation_plan', '')}")

    factors = card.get("candidate_factor_cards", []) or []
    if factors:
        lines.append("")
        lines.append("## 候选因子")
        for factor in factors:
            fields = ", ".join(factor.get("input_fields", []))
            lines.append(f"- {factor.get('feature_name', '')}: `{factor.get('formula', '')}`")
            lines.append(f"  字段：{fields}")
            lines.append(f"  复现状态：{factor.get('repro_status', '')}")

    missing = card.get("missing_fields", []) or []
    if missing:
        lines.append("")
        lines.append("## 缺失信息")
        for item in missing:
            lines.append(f"- {item}")

    lines.append("")
    return "\n".join(lines)


def iter_cards(cards: List[Path], cards_dir: Path) -> Iterable[Path]:
    if cards:
        yield from cards
        return
    if cards_dir.exists():
        yield from sorted(cards_dir.glob("doc_*.json"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cards-dir", type=Path, default=Path("03_cards"))
    parser.add_argument("--out-dir", type=Path, default=Path("04_review/cards_md"))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("cards", nargs="*", type=Path)
    args = parser.parse_args()

    paths = list(iter_cards(args.cards, args.cards_dir))
    if not paths:
        print("No card JSON files found.")
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for path in paths:
        card = load_json(path)
        target = args.out_dir / f"{card.get('doc_id', path.stem)}.card.md"
        if target.exists() and not args.force:
            raise FileExistsError(f"{target} already exists; pass --force to overwrite")
        target.write_text(render_card(card), encoding="utf-8")
        print(f"[ok] {path} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
