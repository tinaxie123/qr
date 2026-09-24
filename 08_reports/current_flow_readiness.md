# 阶段 2 当前流程状态与交付判断

更新时间：2026-09-24

## 结论

阶段 2 的主流程已经跑通到“可进行首轮交付复核”的状态：

- 15/15 篇完成 MinerU 解析：`01_parsed/doc_*.md`
- 15/15 篇完成切块：`02_chunks/doc_*.jsonl`
- 15/15 篇完成结构化提取：`03_cards/doc_*.json`
- 15/15 篇完成人工复核视图渲染：`04_review/cards_md/doc_*.card.md`
- `manifest.csv` 的 `extract_status` 已全部回写为 `done`
- 已产出 2 篇主题知识文档样例：`05_topics/T01_日内信号标准化与事件触发.md`、`05_topics/T02_稳健性失败与过拟合控制.md`
- 已把主题文档和 11 篇可用卡片装入 `06_skill/references/`

当前不建议声称“最终质量闭环完成”，因为 `doc_01`, `doc_08`, `doc_09`, `doc_11` 仍为 validator v2 硬失败，repair pass 尚未实现。但可以准确表述为：**解析 -> 切块 -> 提取 -> 校验 -> 渲染 -> 首批主题归并 -> Skill 初版封装，已经完整跑通。**

## 当前校验状态

validator v2 结果：

- `machine_pass`: `doc_02`, `doc_04`, `doc_07`
- `manual_pending`: `doc_03`, `doc_05`, `doc_06`, `doc_10`, `doc_12`, `doc_13`, `doc_14`, `doc_15`
- `machine_fail`: `doc_01`, `doc_08`, `doc_09`, `doc_11`

硬失败处理原则：

- `doc_01`: 存在 page-only locator 和章节级 locator，暂不进入 Skill 强证据。
- `doc_08`: 多处 page-only locator，暂不进入主题结论。
- `doc_09`: 多处 fabricated_locator，且该文献本身为图片表格识别困难样本，暂不进入主题结论。
- `doc_11`: 存在 fabricated_locator，暂不进入 Skill 强证据。
- 四篇都保留在 `03_cards/` 和 `04_review/cards_md/`，但在 `04_review/review_table.csv` 标记为 `machine_fail_human_needed`。

warning 处理原则：

- warning 主要来自图表、章节或正文片段级 locator 未与 original 精确命中，或 extension 证据未在 original 精确登记。
- 这些样本可进入主题文档，但只能作为弱证据或方法启发，并在主题元信息里标注待人工复核。
- 不把 warning 静默升级为强证据。

## 已完成产物

### 单篇层

- `01_parsed/doc_*.md`: MinerU 解析 Markdown。
- `02_chunks/doc_*.jsonl`: 带 chunk/page 信息的切块。
- `03_cards/doc_*.json`: DeepSeek 提取的结构化研究卡片，唯一事实源。
- `04_review/cards_md/doc_*.card.md`: 由 JSON 渲染的人读卡片。
- `04_review/review_table.csv`: 15 篇的机器校验状态与人工复核待办。

### 主题层

- `05_topics/T01_日内信号标准化与事件触发.md`
  - 覆盖 `doc_06`, `doc_07`, `doc_10`, `doc_15`
  - 聚焦 Z-score、Hysteresis 双阈值、量价事件和弱信号融合。
- `05_topics/T02_稳健性失败与过拟合控制.md`
  - 覆盖 `doc_04`, `doc_05`, `doc_10`, `doc_14`, `doc_15`
  - 聚焦样本内外落差、实盘失败、虚假发现、冗余暴露、交易成本和可实现性。

### Skill 层

- `06_skill/SKILL.md`: 已更新为当前真实流程和质量边界。
- `06_skill/references/topics/`: 已放入首批主题文档。
- `06_skill/references/cards/`: 已放入 11 篇 validator v2 `machine_pass` 或 `manual_pending` 的精选 JSON 卡片。
- `06_skill/schemas/research_feature_idea.schema.json`: 后续路线一/路线二特征提案输出规范。
- `06_skill/examples/literature_feature_example.md`: 示例材料。

## 当前仍需补齐的工程能力

### 1. Validator 后续增强

当前 `scripts/validate_card.py` 已经实现 chunk 真实存在校验和失败码分层，包括 `missing_original_evidence`, `locator_granularity_mismatch`, `fabricated_locator`, `schema_violation`。但它尚未实现：

- 图注/正文证据簇更细粒度合并
- inspiration 分级与限量
- first pass 与 final pass after repair 分开统计
- 自动写回 review table 或 manifest 的校验摘要

### 2. Schema v2

建议下一步补：

- `statement_type: rejected_alternative`
- `extensions.evidence_refs`
- `extensions.inspiration_locators`
- `extensions.extrapolation_rationale`
- 对旧字段 `basis_evidence_ids` 做兼容映射

### 3. Repair 闭环

当前没有 `repair_card.py`。建议 repair 只处理两类自动修复：

- `missing_original_evidence`: 原文有、original 漏抽，补 original 证据。
- `locator_granularity_mismatch`: 图注/正文同簇或章节粒度偏差，改引用或合并 locator。

`fabricated_locator` 直接转人工，不自动补。

## 建议交付清单

建议这次交“阶段 2 首轮流程样例包”，而不是声称最终质量闭环完成：

1. `manifest.csv`
2. `logs/parse_qc.csv`
3. `03_cards/doc_*.json`
4. `04_review/cards_md/doc_*.card.md`
5. `04_review/review_table.csv`
6. `05_topics/T01_日内信号标准化与事件触发.md`
7. `05_topics/T02_稳健性失败与过拟合控制.md`
8. `06_skill/`
9. `08_reports/current_flow_readiness.md`
10. `08_reports/stage2_literature_kb_report.md`

推荐说明口径：

> 首轮 15 篇已完成解析、切块、提取、校验和渲染；其中 3 篇 machine_pass、8 篇 manual_pending、4 篇 machine_fail。当前先用 11 篇可用或待复核样本产出首批主题文档并封装 Skill references，4 篇硬失败样本进入 repair/人工复核队列。当前交付用于确认文档形态、证据边界、主题归并方式和 Skill 封装方式；下一步补 schema v2、inspiration 通道和 repair 闭环。
