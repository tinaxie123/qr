# 阶段 2 文献知识工程流水线（研报路线前置准备）

本阶段目标是把金融工程研报和市场微观结构论文处理成可被智能体调用的研究 Skill。它是“研报路线”的前置准备，不是最终因子挖掘阶段。

首轮建议跑 12 篇文献（3 篇校准 + 6 篇试跑 + 3 篇留出），让 mentor 先看结构、可追溯性和复核成本。

## 0. 两个卡片文件是不是一回事

`03_cards/doc_*.json` 和 `04_review/cards_md/doc_*.card.md` 的信息来源相同，但职责不同：

| 文件 | 性质 | 用途 | 是否事实源 |
|---|---|---|---|
| `03_cards/doc_*.json` | DeepSeek 提取的结构化 JSON | 给程序校验、主题归并、Skill 打包和后续检索使用 | 是，唯一事实源 |
| `04_review/cards_md/doc_*.card.md` | 由 JSON 渲染的人读版卡片 | 给 mentor/人工复核快速阅读 | 否 |

原则：JSON 是主账本，Markdown 卡片只是阅读视图。如果两者不一致，以 JSON 为准，并重新渲染 Markdown。

## 1. 阶段 2 真正要完成的三步

| 步骤 | 做什么 | 核心产物 | 质量门 |
|---|---|---|---|
| 1. 文献分析 | 用 DeepSeek V4 对单篇文献做定向信息提取 | `03_cards/doc_*.json` + `04_review/cards_md/doc_*.card.md` | 公式和结论必须有原文位置；缺失即标记，不补全 |
| 2. 归并与复核 | 按主题综合多篇文献，去重、核对并保留分歧 | `05_topics/*.md`，3000-5000 字/主题 | 分歧、负面结果、适用条件和失效条件不能抹平 |
| 3. Skill 封装 | 把主题文档、研究卡片、输出规范、设计示例封装为研究 Skill | `06_skill/` | Skill 必须说明如何读数据说明、调用研究依据、提出扩展假设 |

本阶段不要求产出正式特征批次。特征提案 schema 和示例可以放进 Skill，作为下一阶段智能体调用 Skill 时的输出规范。

## 2. 单篇 JSON 为什么要隔离 original / adaptation / extensions

一张研究卡片是一个 JSON，里面有三个互相隔离的块：

| 块 | 谁写的 | 能挂原文位置吗 | 能有新公式吗 |
|---|---|---|---|
| `original` | 只记录原文说过什么 | 必须挂 `source_locators` | 不能新增 |
| `adaptation` | 我们对项目数据的适配判断 | 不挂 locator | 可以，但必须标注为项目判断 |
| `extensions` | 有依据的扩展假设 | 通过 `basis_evidence_ids` 反向引用原文证据 | 可以，但状态恒为待验证 |

这样做是为了防止三类错误：

1. 把项目判断伪装成文献结论。
2. 把文献没说的内容补全。
3. 把同期关系、样本内结论误用成可预测、样本外结论。

## 3. 目录结构

```text
literature_pipeline/
├── config.yaml
├── manifest.csv
├── README.md
├── 00_raw/                    # 原始 PDF/Word，只读
├── 01_parsed/                 # MinerU 输出 md，带页码锚点
├── 02_chunks/                 # 文献切片，带 doc_id/chunk_id/page/section
├── 03_cards/                  # 单篇 DeepSeek 提取 JSON，唯一事实源
├── 04_review/
│   ├── cards_md/              # 由 JSON 渲染的人读卡片
│   ├── review_table.csv       # 人工复核记录
│   └── fixes/                 # 退回重抽版本
├── 05_topics/                 # 主题知识文档，3000-5000 字/主题
├── 06_skill/                  # 阶段 2 最终交付：研究 Skill
│   ├── SKILL.md
│   ├── references/            # 主题文档、精选卡片、数据说明、研究约束
│   ├── schemas/               # 输出规范
│   └── examples/              # 正例、反例、缺失/分歧标注示例
├── 08_reports/                # 首轮交付说明
├── logs/
│   ├── run_log.csv
│   └── prompts/
├── schemas/
│   ├── research_card.schema.json
│   └── research_feature_idea.schema.json
└── scripts/
    ├── parse_pdf_pymupdf.py       # 无 MinerU 时的临时 PDF 文本解析
    ├── chunk_split.py
    ├── extract_card_deepseek.py
    ├── validate_card.py
    └── render_research_card.py
```

## 4. 首轮试跑命令

先补全 `manifest.csv`，并用 MinerU 把文献转成：

```text
01_parsed/doc_01.md
01_parsed/doc_02.md
...
```

如果本机暂时没有 MinerU，可以先用 PyMuPDF fallback 打通流程：

```bash
python3 scripts/parse_pdf_pymupdf.py --batch A --force
```

注意：PyMuPDF fallback 不能可靠保留公式和表格，正式复核前仍建议用 MinerU/OCR 重跑解析层，尤其是扫描件和公式受损文献。

切 chunks：

```bash
python3 scripts/chunk_split.py --batch A --force
```

只跑 A 批 3 篇做校准：

```bash
DEEPSEEK_API_KEY=... python3 scripts/extract_card_deepseek.py --batch A --force
python3 scripts/validate_card.py
python3 scripts/render_research_card.py --force
```

A 批复核通过后再跑 B/C：

```bash
python3 scripts/chunk_split.py --batch B --force
python3 scripts/chunk_split.py --batch C --force
DEEPSEEK_API_KEY=... python3 scripts/extract_card_deepseek.py --batch B --force
DEEPSEEK_API_KEY=... python3 scripts/extract_card_deepseek.py --batch C --force
python3 scripts/validate_card.py
python3 scripts/render_research_card.py --force
```

## 5. 给 mentor 看什么

首轮交付包建议包括：

1. `manifest.csv`：12 篇文献清单和批次划分。
2. `03_cards/doc_*.json`：单篇结构化提取结果，唯一事实源。
3. `04_review/cards_md/doc_*.card.md`：JSON 渲染的人读卡片。
4. `04_review/review_table.csv`：人工复核结果。
5. `05_topics/T*.md`：1-2 个主题知识文档样例。
6. `06_skill/`：研究 Skill 初版，含 `references/`、`schemas/`、`examples/`。

mentor 主要看：是否可追溯、是否缺失不补全、是否保留分歧、是否能支撑后续智能体基于文献知识设计新特征。
