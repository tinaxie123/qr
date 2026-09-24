# 首轮 15 篇试跑交付说明

本阶段是“文献知识工程”，也就是研报路线的前置准备。首轮目标不是直接交特征批次，也不是证明因子有效，而是证明：

- 配置中的 LLM（当前为百炼兼容接口的 `deepseek-v3`）能稳定抽取单篇文献信息；
- 每条公式和结论能回到原文位置；
- 多篇文献能按主题归并、去重、核对并保留分歧；
- 这些材料能封装成一个研究 Skill，供后续智能体设计特征时调用。

## 当前首轮结果

截至 2026-09-24，首轮 15 篇已经完整跑过解析、切块、提取、校验和渲染：

- 15/15 篇完成 MinerU 解析：`01_parsed/doc_*.md`
- 15/15 篇完成切块：`02_chunks/doc_*.jsonl`
- 15/15 篇完成结构化提取：`03_cards/doc_*.json`
- 15/15 篇完成人读卡片渲染：`04_review/cards_md/doc_*.card.md`
- validator v2 当前结果：3 篇 `machine_pass`、8 篇 `manual_pending`、4 篇 `machine_fail`
- 首批主题文档已产出：`05_topics/T01_日内信号标准化与事件触发.md`、`05_topics/T02_稳健性失败与过拟合控制.md`
- Skill 初版已封装：`06_skill/`，其中 `references/cards/` 只放 11 篇 `machine_pass` 或 `manual_pending` 卡片副本

四篇 `machine_fail` 为 `doc_01`, `doc_08`, `doc_09`, `doc_11`。它们仍保留在根目录 `03_cards/` 和 `04_review/cards_md/`，但修复前不进入 Skill references 和主题强结论。

补齐版产出报告位于 `08_reports/stage2_literature_kb_report.md`，其中已整理逐篇状态、主题去向、当前局限和下一步修改计划。

## 阶段 2 交付物

1. `manifest.csv`
   - 15 篇文献清单、批次 A/B/C、语言、类型、是否扫描件、是否含公式/负面结果。
2. `03_cards/doc_*.json`
   - 每篇一张 LLM 提取的结构化研究卡片。
   - 这是唯一事实源，后续主题归并和 Skill 打包都以它为准。
3. `04_review/cards_md/doc_*.card.md`
   - 从 JSON 渲染出来的人读版卡片。
   - 它和 JSON 来源相同，但不是事实源，只是方便人工复核和主题整理快速阅读。
4. `04_review/review_table.csv`
   - 每篇文献的人工复核记录：公式、locator、臆造、缺失标注、同期/预测、样本内/外。
5. `05_topics/*.md`
   - 主题知识文档，每个主题 3000-5000 字。
   - 首轮已产出 2 个主题样例：`T01_日内信号标准化与事件触发`、`T02_稳健性失败与过拟合控制`。
6. `06_skill/`
   - 阶段 2 最终产出：研究 Skill。
   - 包含 `SKILL.md`、`references/`、`schemas/`、`examples/`。

阶段 2 不交正式特征批次或正式特征清单；这些属于后续“调用 Skill 设计特征并验证”的阶段。

## 三步执行

### 1. 文献分析

用 MinerU 将原始 PDF/Word 转为 markdown，并保留页码、公式、表格：

```bash
python3 scripts/parse_pdf_mineru.py --batch A --force
```

```text
01_parsed/doc_01.md
01_parsed/doc_02.md
...
```

解析层只使用 MinerU。`parse_pdf_mineru.py` 调用 MinerU `middle_json`，再渲染成带 `<!-- page: n -->` 锚点的 Markdown；旧的简易 PDF 文本解析不再作为流程入口。

MinerU 原生命令可用于单篇冒烟测试：

```bash
.venv-mineru/bin/mineru-kit parse "你的PDF路径.pdf" -o 输出目录 --format markdown --tier basic --ocr-mode auto
```

注意：MinerU 原生 markdown 可能包含很长的 `base64` 图片内容，正式流水线不要直接把它喂给 LLM。正式解析统一使用 `scripts/parse_pdf_mineru.py`，它会在写入 `01_parsed/doc_*.md` 前清理 `data:image` / `base64` 内容；如发生清理，会记录在 `logs/qc/doc_*.json` 的 `warnings[]` 中。

解析 QC 不放在 `01_parsed/`。每篇精简 QC 写入 `logs/qc/doc_*.json`，汇总表由脚本自动生成到 `logs/parse_qc.csv`。QC 只保留复现和复核需要的字段，不写 MinerU 进度条日志。

切 chunks：

```bash
python3 scripts/chunk_split.py --batch A --force
```

校准时可以先跑 A 批；当前首轮 15 篇已经跑完，如需重跑可按 A/B/C 分批执行：

```bash
python3 scripts/extract_card_llm.py --batch A --force
python3 scripts/validate_card.py
python3 scripts/render_research_card.py --force
```

文献分析 JSON 必须覆盖：

- 研究场景；
- 经济机制；
- 特征公式；
- 数据处理；
- 检验方法；
- 稳健性与失败；
- 交易可实现性；
- 项目适配；
- 扩展建议。

纪律：公式和结论保留原文位置；文献没说的内容标缺失，不补全。

### 2. 归并与复核

按主题综合多篇通过复核的卡片，例如：

- 盘口失衡；
- 流动性冲击；
- 持仓量与价量关系。

每个主题文档建议包含：

- 主题边界；
- 机制共识；
- 公式与特征谱系；
- 实证证据；
- 文献间分歧；
- 负面结果和失败条件；
- 对本项目数据的适配判断；
- 可扩展研究想法。

归并时不要把分歧写没。不同市场、不同频率、不同样本期导致的方向差异，要并列保留。

### 3. Skill 封装

`06_skill/` 是本阶段最终交付目录：

```text
06_skill/
├── SKILL.md
├── references/
├── schemas/
└── examples/
```

Skill 要规定智能体：

- 先读数据说明和研究约束；
- 再按主题调用文献知识；
- 区分原文证据、项目适配判断和扩展假设；
- 对文献中没有直接给出的新特征，必须说明扩展依据、计算定义、适用条件和放弃条件；
- 输出时遵守 `schemas/` 中的规范；
- 引用文献时保留 `doc_id + evidence_id + chunk_id/page`。

## 首轮复核要判断什么

- JSON 和人读卡片是否一致，且 JSON 是唯一事实源。
- 关键公式和结论能否回查到原文 chunk。
- LLM 是否把未说明内容标为缺失，而不是补全。
- 主题文档是否真的综合多篇文献，而不是单篇摘要拼接。
- 是否保留了负面结果、分歧和失效条件。
- Skill 是否足够清楚，能指导后续智能体使用这些文献知识设计特征。

## 首轮建议规模

- 文献：15 篇。
- 单篇 JSON：15 张。
- 人读卡片：15 张。
- 主题文档：1-2 个。
- Skill：一个最小可用版本。

## 暂时不要做的事

- 不要急着交正式特征清单。
- 不要急着跑大规模回测。
- 不要把 JSON 卡片和 Markdown 卡片当成两份独立事实源。
- 不要把所有原文全文都塞进 Skill。
- 不要把“扩展想法”写成“文献已经证明”。
