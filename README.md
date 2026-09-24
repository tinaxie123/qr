# 阶段 2 文献知识工程流水线（研报路线前置准备）

本阶段目标是把金融工程研报和市场微观结构论文处理成可被智能体调用的研究 Skill。它是“研报路线”的前置准备，不是最终因子挖掘阶段。

首轮建议跑 15 篇文献（3 篇校准 + 9 篇试跑 + 3 篇留出），先验证结构稳定性、可追溯性和复核成本。

## 0. 两个卡片文件是不是一回事

`03_cards/doc_*.json` 和 `04_review/cards_md/doc_*.card.md` 的信息来源相同，但职责不同：

| 文件 | 性质 | 用途 | 是否事实源 |
|---|---|---|---|
| `03_cards/doc_*.json` | LLM 提取的结构化 JSON（extraction） | 给程序校验、主题归并、Skill 打包和后续检索使用 | 是，唯一事实源 |
| `04_review/cards_md/doc_*.card.md` | 由 JSON 渲染的人读版卡片 | 给人工复核和主题整理快速阅读 | 否 |

原则：JSON 是主账本，Markdown 卡片只是阅读视图。如果两者不一致，以 JSON 为准，并重新渲染 Markdown。

## 1. 阶段 2 真正要完成的三步

| 步骤 | 做什么 | 核心产物 | 质量门 |
|---|---|---|---|
| 1. 文献分析 | 用配置中的 LLM 对单篇文献做定向信息提取，当前为百炼兼容接口的 `deepseek-v3` | `03_cards/doc_*.json` + `04_review/cards_md/doc_*.card.md` | 公式和结论必须有原文位置；缺失即标记，不补全 |
| 2. 归并与复核 | 按主题综合多篇文献，去重、核对并保留分歧 | `05_topics/*.md`，3000-5000 字/主题 | 分歧、负面结果、适用条件和失效条件不能抹平 |
| 3. Skill 封装 | 把主题文档、研究卡片、输出规范、设计示例封装为研究 Skill | `06_skill/` | Skill 必须说明如何读数据说明、调用研究依据、提出扩展假设 |

本阶段不要求产出正式特征批次。特征提案 schema 和示例可以放进 Skill，作为下一阶段智能体调用 Skill 时的输出规范。

## 2. 单篇 JSON 为什么要隔离 original / adaptation / extensions

一张研究卡片是一个 JSON，里面有三个互相隔离的块：

| 块 | 谁写的 | 能挂原文位置吗 | 能有新公式吗 |
|---|---|---|---|
| `original` | 只记录原文说过什么 | 必须挂 `source_locators` | 不能新增 |
| `adaptation` | 我们对项目数据的适配判断 | 不挂 locator | 可以，但必须标注为项目判断 |
| `extensions` | 有依据的扩展假设 | L2 必须挂本文 `source_locators`；`basis_evidence_ids` 在 L3 建证据库后回填 | 可以，但状态恒为待验证 |

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
├── 03_cards/                  # 单篇 LLM 提取 JSON，唯一事实源
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
│   ├── parse_qc.csv           # 从 logs/qc/doc_*.json 汇总生成
│   ├── qc/                    # MinerU 解析 QC，每篇一个精简 JSON
│   └── prompts/
├── schemas/
│   ├── extraction.schema.json
│   └── research_feature_idea.schema.json
└── scripts/
    ├── parse_pdf_mineru.py        # 唯一解析入口：调用 MinerU middle_json 并渲染 page 锚点
    ├── chunk_split.py
    ├── extract_card_llm.py
    ├── validate_card.py
    └── render_research_card.py
```

## 4. 模型配置与切换

如果需要更换大语言模型（比如换成 `deepseek-r1`，或者切回官方的接口），只需修改 `config.yaml` 里的 `model_name` 和 `base_url` 即可，**完全不用动代码**。API Key 请配置在项目根目录的 `.env` 文件中以保证安全。

`config.yaml` 中的相关配置段落如下：

```yaml
# ---------- 提取模型 ----------
model:
  provider: aliyun_bailian
  model_name: deepseek-v3
  base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
  api_key_env: BAILIAN_API_KEY
```

> **注意**：请确保 `.env` 中设置了对应环境变量（如 `BAILIAN_API_KEY=your_key_here`），且该文件已被加入 `.gitignore`。

## 5. 首轮试跑命令

先补全 `manifest.csv`，并用 MinerU 把文献转成：

```text
01_parsed/doc_01.md
01_parsed/doc_02.md
...
```

解析层只保留 MinerU。项目本地环境已经安装在 `.venv-mineru/`，批量解析命令如下：

```bash
python3 scripts/parse_pdf_mineru.py --batch A --force
```

MinerU 原生命令可用于单篇冒烟测试或人工查看：

```bash
.venv-mineru/bin/mineru-kit parse "你的PDF路径.pdf" -o 输出目录 --format markdown --tier basic --ocr-mode auto
```

注意：MinerU 原生 `--format markdown` 可能把部分图片写成很长的 `base64`，如果直接喂给 LLM，会让 prompt 明显膨胀。因此正式流水线不要直接使用原生 markdown 结果作为 LLM 输入，而是使用 `scripts/parse_pdf_mineru.py`。该脚本调用 MinerU 的 `middle_json` 输出，再渲染为带 `<!-- page: n -->` 的 Markdown，并在写入 `01_parsed/doc_*.md` 前自动清理 `data:image` / `base64` 图片内容；如发生清理，会记录在 `logs/qc/doc_*.json` 的 `warnings[]` 中。

扫描件和公式受损文献仍通过 MinerU 的 `--ocr-mode auto/ocr` 处理。每篇解析 QC 写入 `logs/qc/doc_*.json`，只保留 `doc_id`、MinerU 版本、OCR 模式、tier、源文件、输出文件、页数、block 数、字符数、起止时间和 `warnings[]`；脚本会从这些 JSON 自动汇总生成 `logs/parse_qc.csv`。MinerU 进度条日志不写入 QC。

切 chunks：

```bash
python3 scripts/chunk_split.py --batch A --force
```

只跑 A 批 3 篇做校准：

```bash
python3 scripts/extract_card_llm.py --batch A --force
python3 scripts/validate_card.py
python3 scripts/render_research_card.py --force
```

`extract_card_llm.py` 会在 `manifest.csv` 中回写 `extract_status`、`extract_model_version`、`extract_prompt_version`、`extract_updated_at`、`extract_output_path` 和 `extract_error`。不带参数直接运行时，默认只处理 `extract_status != done` 的文献；`--force` 可强制重跑。

A 批复核通过后再跑 B/C：

```bash
python3 scripts/parse_pdf_mineru.py --batch B --force
python3 scripts/parse_pdf_mineru.py --batch C --force
python3 scripts/chunk_split.py --batch B --force
python3 scripts/chunk_split.py --batch C --force
python3 scripts/extract_card_llm.py --batch B --force
python3 scripts/extract_card_llm.py --batch C --force
python3 scripts/validate_card.py
python3 scripts/render_research_card.py --force
```

## 6. 交付内容

首轮交付包建议包括：

1. `manifest.csv`：15 篇文献清单和批次划分。
2. `03_cards/doc_*.json`：单篇结构化提取结果，唯一事实源。
3. `04_review/cards_md/doc_*.card.md`：JSON 渲染的人读卡片。
4. `04_review/review_table.csv`：人工复核结果。
5. `05_topics/T*.md`：1-2 个主题知识文档样例。
6. `06_skill/`：研究 Skill 初版，含 `references/`、`schemas/`、`examples/`。

重点检查：是否可追溯、是否缺失不补全、是否保留分歧、是否能支撑后续智能体基于文献知识设计新特征。
