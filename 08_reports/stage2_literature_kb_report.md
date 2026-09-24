# 阶段二文献知识工程产出报告

从 PDF 到可调用研究 Skill 的可溯源证据流水线（15 篇首轮归并样例）

| 项目 | 内容 |
|---|---|
| 项目阶段 | 阶段二：文献知识工程（研报路线前置准备） |
| 文档版本 | v0.3（首轮归并样例，补齐状态表） |
| 报告日期 | 2026-09-24 |
| 语料规模 | 15 篇，含中文金融工程研报与英文市场微观结构论文 |
| 当前模型 | `aliyun_bailian / deepseek-v3` |
| 提示词版本 | `v1` |

## 内容提要

本阶段不直接产出交易因子，而是把 15 篇中英文文献加工成可溯源、带质量状态、可被因子挖掘智能体调用的结构化研究资产。完整链路为：PDF 解析（MinerU） -> 文档切片（稳定 chunk 与 locator） -> 单篇结构化卡片 JSON（原文事实、项目适配、扩展想法分区） -> 人读复核卡片 -> 机器校验（validator v2 三态） -> 主题归并（T01、T02） -> 研究 Skill 封装。

首轮 15 篇中，3 篇为 `machine_pass`，8 篇为 `manual_pending`，4 篇因 locator 硬错误被判定为 `machine_fail`。`machine_fail` 文献暂不进入主题强结论与 Skill references；`manual_pending` 文献只能作为弱证据或方法启发。需要特别说明：全部卡片的人工复核尚未执行，因此当前没有任何一篇可称为“人工合格”。机器通过只代表结构与 locator 机器门通过，不等于最终质检通过。

## 1. 阶段目标与范围

因子挖掘智能体在“研报路线”上需要可靠的文献知识。若直接把 PDF 或论文摘要交给大模型，容易出现公式与变量定义丢失、结论无出处、把同期相关关系误写成未来预测、混淆样本内与样本外结果，以及编造看似合理但无法回到原文的引用位置。阶段二的目标，是建立一条“证据可回溯、结论分强弱、状态可审计”的文献知识工程流水线，把文献转换为符合本项目研究约束的结构化输入。

本阶段只建设知识资产与质量门，不产出正式入池因子，不给策略回测收益结论，也不进行参数寻优。卡片中的扩展想法一律标注为待验证，只能作为研究方向，不得等同于文献已确立的结论。

## 2. 流水线总览

| 环节 | 输入 | 产物位置 | 地位与说明 |
|---|---|---|---|
| 解析 | 原始 PDF | `01_parsed/doc_*.md` | MinerU 解析 Markdown，保留页锚点与公式，属中间产物 |
| 切片 | `01_parsed` Markdown | `02_chunks/doc_*.jsonl` | 稳定 `chunk_id` 与页定位，是 locator 回查基准 |
| 单篇抽取 | chunks、schema、提示词 | `03_cards/doc_*.json` | 结构化卡片，全流水线唯一事实源 |
| 人读渲染 | 卡片 JSON | `04_review/cards_md/doc_*.card.md` | 供人工复核阅读，由 JSON 渲染，不是事实源 |
| 机器校验 | cards 与 chunks | `scripts/validate_card.py` 输出，状态记录于 `04_review/review_table.csv` | validator v2 质量门，输出三态 |
| 主题归并 | 可用卡片 | `05_topics/T01...`, `T02...` | 跨文献综合，区分共识、分歧、判断与假设 |
| Skill 封装 | 主题、数据说明、约束 | `06_skill/` | 供后续因子智能体调用的研究资产包 |

贯穿原则有三条。第一，`03_cards/doc_*.json` 是唯一事实源，人读卡片与主题文档都由其渲染或归并。第二，`original / adaptation / extensions` 物理隔离：原文事实挂 locator，项目适配不挂 locator，扩展想法必须标为待验证。第三，机器校验与人工复核分离：`machine_pass` 不等于人工合格。

## 3. 各步骤产出

### 3.1 PDF 解析为 Markdown

使用 MinerU 将 PDF 转为 Markdown，解析产物保留 `<!-- page: N -->` 页锚点。解析 QC 独立存放在 `logs/qc/doc_*.json`，汇总到 `logs/parse_qc.csv`。MinerU 原生 Markdown 中可能出现长 `base64` 图片内容，正式流水线使用 `scripts/parse_pdf_mineru.py` 清理后写入 `01_parsed`。

### 3.2 文档切片

每篇文献切成 `02_chunks/doc_*.jsonl`，每行一个 chunk，包含 `doc_id`、`chunk_id`、`page`、`section`、`content` 等字段。validator v2 以 chunk 为 locator 存在性校验的基准。

### 3.3 单篇结构化卡片

15 篇均已产出 `03_cards/doc_*.json`，并由 `manifest.csv` 记录抽取状态、模型版本、提示词版本、更新时间和输出路径。当前 manifest 显示：15/15 均为 `extract_status=done`，`extract_model_version=deepseek-v3`，`extract_prompt_version=v1`。

### 3.4 人读复核卡片

15 篇均已渲染为 `04_review/cards_md/doc_*.card.md`。人读卡片只用于阅读与复核，不作为事实源；如发现内容不一致，应回到 JSON 修改或重抽，再重新渲染。

### 3.5 validator v2

validator v2 已实现 chunk 真实存在校验与失败码分层。当前三态定义如下：

| 状态 | 含义 | 在主题与 Skill 中的处置 |
|---|---|---|
| `machine_pass` | 结构完整、locator 可回到 chunk；仍待人工复核 | 可进入主题，但仍需人工签核 |
| `manual_pending` | locator 偏粗或 extension 未在 original 精确登记 | 只能作为弱证据或方法启发，并显式标注 |
| `machine_fail` | page-only locator、fabricated locator 或 schema 硬错误 | 暂不进入主题强结论与 Skill references |

## 4. 首轮结果与质量状态

### 4.1 状态总览

| 状态 | 篇数 | doc_id | 处置 |
|---|---:|---|---|
| `machine_pass` | 3 | `doc_02`, `doc_04`, `doc_07` | 可进入主题或 references，仍待人工签核 |
| `manual_pending` | 8 | `doc_03`, `doc_05`, `doc_06`, `doc_10`, `doc_12`, `doc_13`, `doc_14`, `doc_15` | 仅作弱证据或方法启发 |
| `machine_fail` | 4 | `doc_01`, `doc_08`, `doc_09`, `doc_11` | 不进强结论与 references，待 repair 或人工复核 |
| 合计 | 15 | pass 与 pending 合计 11 篇进入 `06_skill/references/cards` | 人工复核状态仍全部待执行 |

严格首次通过率（`machine_pass / 15`）为 20.0%；可进入弱证据池比例（`machine_pass + manual_pending`）为 73.3%；硬失败比例为 26.7%。

### 4.2 逐篇状态与主题去向

| doc_id | 文献简称 | 类型 | validator 状态 | 主题/Skill 去向 |
|---|---|---|---|---|
| `doc_01` | 日内动量独立复现与统计审计 | 英文论文 | `machine_fail` | 因 page-only locator 暂不进入强结论 |
| `doc_02` | 0DTE 期权与尾部保护价格 | 英文论文 | `machine_pass` | 进入 references，暂未进入 T01/T02 |
| `doc_03` | 分数阶导数识别市场效率状态与粗糙波动 | 英文论文 | `manual_pending` | 进入 references，状态识别方法启发 |
| `doc_04` | 预测悖论：ML 加密货币实盘失败 | 英文论文 | `machine_pass` | T02 |
| `doc_05` | 股票因子分散的层次聚类 | 英文论文 | `manual_pending` | T02，弱证据 |
| `doc_06` | 日内资金流策略标准化与信号化 | 中文研报 | `manual_pending` | T01，弱证据 |
| `doc_07` | 量价事件驱动信号在绝对收益策略 | 中文研报 | `machine_pass` | T01 |
| `doc_08` | 量价指纹模型迭代 | 中文研报 | `machine_fail` | page-only locator，排除 |
| `doc_09` | 筹码分布因子系统构建 | 中文研报 | `machine_fail` | fabricated locator，排除 |
| `doc_10` | 噪声 Alpha 环境下信号筛选与分散化 | 中文研报 | `manual_pending` | T01、T02，弱证据 |
| `doc_11` | 期权高频：凸性套利机会解析 | 中文研报 | `machine_fail` | fabricated locator，排除 |
| `doc_12` | 可转债定价与套利策略初探 CRR 二叉树 | 中文研报 | `manual_pending` | references，公式边界样本 |
| `doc_13` | 转债蒙特卡洛定价改进 | 中文研报 | `manual_pending` | references，公式受损样本 |
| `doc_14` | 商品期限结构：展期规律统计与时点优化 | 中文研报 | `manual_pending` | T02，商品期货展期参考 |
| `doc_15` | FOF 跨资产风险平价与时序因子增强配置 | 中文研报 | `manual_pending` | T01、T02，方法启发 |

### 4.3 主题覆盖

T01《日内信号标准化与事件触发》纳入 `doc_06`, `doc_07`, `doc_10`, `doc_15`。其中 `doc_07` 为 `machine_pass`，其余三篇为 `manual_pending`，因此 T01 当前更适合作为方法启发样例，强结论尚待人工复核。

T02《稳健性失败与过拟合控制》纳入 `doc_04`, `doc_05`, `doc_10`, `doc_14`, `doc_15`。其中 `doc_04` 为 `machine_pass`，其余为 `manual_pending`。T02 的价值在于固化“预测不等于交易收益、复杂化不等于稳健、冗余暴露需管理、交易可实现性必须前置”的检查框架。

### 4.4 证据可回溯链

设计上，每条原文事实都应能沿“卡片 `source_locators` -> `02_chunks` 对应 chunk -> `01_parsed` 原文页锚点”回溯。validator v2 已完成 locator 是否能回到 chunks 的机器校验；下一步需要补强图注/正文证据簇、引文文本归一化匹配和校验报告落盘。

## 5. 关键设计决策

| 决策 | 放弃的做法 | 理由 |
|---|---|---|
| JSON 为唯一事实源 | 在 Markdown 中维护事实 | 避免事实多处漂移，便于统一校验与重渲染 |
| `original / adaptation / extensions` 分区 | 一段式总结 | 区分文献事实、项目判断与待验证假设 |
| 原文事实强制 locator | 让模型补全缺口 | 宁可显式缺失，也不允许无出处补全 |
| validator 三态 | 只有通过/不通过 | 区分弱证据、硬错误和机器可通过状态 |
| `machine_fail` 排除，`manual_pending` 降权 | 尽量多纳入 | 防止弱证据污染后续特征设计 |
| 研究约束写入 Skill | 临时写在提示词里 | 统一防未来函数、跨日状态和同期/预测混淆 |
| manifest 记录版本 | 无版本的一次性抽取 | 保证可审计、可复现、可断点重跑 |

## 6. 已发现问题与处理原则

### 6.1 问题类型

当前失败和 warning 主要分为四类：

- `missing_original_evidence`: extension 引用的证据能在 chunks 中找到，但未在 original 精确登记。
- `locator_granularity_mismatch`: 图表、章节或正文片段级 locator 粒度不一致，需要证据簇匹配。
- `fabricated_locator`: locator 片段在对应页 chunks 中找不到，属于硬错误。
- `schema_violation`: 结构不符合 schema，或 locator 只有页码没有正文/章节锚点。

此外，扫描件、公式乱码、表格为图片等属于解析层 `parse_gap`，应回到解析/OCR 处理，不应靠重抽卡片掩盖。

### 6.2 典型处置原则

不建议盲目整篇重跑。对漏抽 original 的问题，应定向补登记证据或修 prompt/schema；对图注与正文同簇问题，应升级证据簇匹配；对 fabricated locator，一律转人工或回到解析层；对 page-only locator，应要求 repair 只在给定 chunk 范围内补具体锚点。

## 7. 当前局限

- 人工复核尚未执行，全部卡片的 `review_status` 仍应视为 pending。
- validator v2 仍偏结构校验，尚未完成图注/正文证据簇、引文归一化匹配和自动落盘。
- 定向 repair 尚未上线，`machine_fail` 与部分 warning 仍依赖人工处理或整篇重抽。
- 主题数量有限，当前只有 T01/T02；且每个主题只有 1 篇 `machine_pass` 支撑强证据骨架。
- 扫描件与公式受损文献仍需专项 OCR/解析策略。

## 8. 下一步修改计划

| 优先级 | 工作内容 | 产出 |
|---|---|---|
| P0 | 补齐人工复核入口：给 `04_review/review_table.csv` 增加 `review_status`、`review_notes` 或单独复核表；先人工签核 T01/T02 涉及卡片 | 人工复核记录、T01/T02 可确认版本 |
| P1 | 升级 schema v2：增加 `rejected_alternative`，拆分 `extensions.evidence_refs / inspiration_locators / extrapolation_rationale` | `schemas/extraction.schema.json` v2 与 prompt v2 |
| P1 | 增强 validator：证据簇匹配、原因码 JSON 落盘、validate 状态写回 manifest/review table | `logs/validation/*.json` 与状态闭环 |
| P1 | 实现最小 `repair_card.py`：只允许补 original、relink extension、降级 inspiration，最多 1 轮，留痕到 `04_review/fixes/` | 可审计 repair 闭环 |
| P2 | 优先 repair `doc_01`，其日内动量复现审计价值高；再处理 `doc_08/doc_11`；`doc_09` 回到 OCR/解析层 | 回收高价值失败文献 |
| P2 | 自下而上扩展主题，不预设标题凑材料 | 新主题文档与更新后的 Skill references |
| P3 | 进入特征路线：路线一仅凭字段说明，路线二结合文献证据，统一输出特征提案 schema | 候选特征提案与登记册 |

## 9. 需要确认的问题

1. 是否同意把扩展引用拆成“强证据”和“灵感来源”两级，灵感来源只进 backlog，不进候选因子库？
2. `manual_pending` 是否可以继续作为主题中的方法启发，但不得支撑强结论？
3. 一个主题至少需要多少篇 `machine_pass`、多少独立来源，才可称为“正式主题结论”？
4. 下一步优先顺序是否为：人工复核与质量门加固 -> repair 高价值失败文献 -> 扩展主题 -> 再进入特征路线？
5. `doc_01` 方法论价值高但 locator 硬失败，是否列为第一优先 repair 对象？

## 附录 A：当前产物清单

- `manifest.csv`: 15 篇文献清单、批次、抽取状态、模型版本。
- `01_parsed/doc_*.md`: MinerU 解析 Markdown。
- `02_chunks/doc_*.jsonl`: 文档切片。
- `03_cards/doc_*.json`: 单篇结构化卡片，唯一事实源。
- `04_review/cards_md/doc_*.card.md`: 人读卡片。
- `04_review/review_table.csv`: 当前机器状态与人工待办。
- `05_topics/T01_日内信号标准化与事件触发.md`
- `05_topics/T02_稳健性失败与过拟合控制.md`
- `06_skill/`: Skill 初版，含 references、schemas、examples。

## 附录 B：状态枚举

- validator 三态：`machine_pass`, `manual_pending`, `machine_fail`
- 当前 review 状态：人工复核未执行，均应视为 pending
- manifest 当前抽取状态：15/15 `done`
- 模型与提示词：15/15 为 `deepseek-v3 / v1`

## 附录 C：提交前仍需人工填写

- 汇报人、指导人姓名（如正式版需要）。
- 人工复核签核人、复核日期与逐篇意见。
- P0/P1/P2 的具体时间节点。
