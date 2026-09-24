# 期货日内因子挖掘：文献研究 Skill

本 Skill 用于把阶段 2 的文献知识转化为后续特征设计的可调用研究资产。它不是自动生成正式因子入池结论，而是指导智能体在统一数据说明和研究约束下，引用文献机制、方法、证据和失败条件，提出可复现、可改进或可迁移的候选特征。

## 1. 当前知识库边界

本版为首轮归并样例，基于 15 篇文献的单篇结构化卡片：

- `03_cards/doc_*.json` 是唯一事实源。
- `04_review/cards_md/doc_*.card.md` 是人读复核视图。
- `05_topics/T01_日内信号标准化与事件触发.md` 和 `05_topics/T02_稳健性失败与过拟合控制.md` 是首批主题知识文档。
- `doc_01`, `doc_08`, `doc_09`, `doc_11` 当前为 validator v2 `machine_fail`，未进入 Skill references 和主题强结论，需 repair 或人工复核后再纳入。
- validator v2 `manual_pending` 样本可作为弱证据或方法启发，但必须在提案中标注待复核，不得当作强结论。

## 2. references 结构

- `references/data_dictionary.md`: 项目数据说明。
- `references/research_constraints.md`: 研究约束。
- `references/topics/`: 首批主题知识文档。
- `references/cards/`: 11 篇 validator v2 `machine_pass` 或 `manual_pending` 的单篇 JSON 卡片副本。根目录 `03_cards/` 仍是主账本；此处仅供 Skill 调用和交付打包。

## 3. 操作规程

### Step 1: 先读数据说明与研究约束

在提出任何特征前，必须先读取 `references/data_dictionary.md` 和 `references/research_constraints.md`。所有设计默认遵守：交易日内时序研究、候选窗口 `3/5/15/60` 秒、只使用当时可得信息、最终日内平仓、不得把同期关系写成未来预测。

### Step 2: 再读主题文档

优先使用 `references/topics/` 中的主题文档理解机制、共识、分歧和失败条件。主题文档中的“项目适配与后续扩展”只能作为研究方向，不能直接等同于已验证因子。

### Step 3: 必要时回查单篇卡片

如果需要引用具体公式、结论或限制条件，应回查 `references/cards/doc_*.json` 或根目录 `03_cards/doc_*.json`。引用文献来源时保留 `doc_id` 与 `source_locators`；如果 locator 当前是 warning 粒度，应在输出中标注“待人工复核”。

### Step 4: 区分三类内容

- `original`: 原文明确说过的内容，必须带真实 locator。
- `adaptation`: 项目适配判断，不挂 locator，不伪装成文献结论。
- `extensions`: 有依据的扩展假设，状态为待验证；若只是灵感，不能进入候选因子库，只能进入 idea backlog。

### Step 5: 输出特征提案

输出必须符合 `schemas/research_feature_idea.schema.json`。每个候选至少写清：特征名称、所需字段、计算公式、窗口和时间下标、设计理由、适用条件、异常处理、预测标签与 horizon、检验设计、预期方向和放弃条件。路线二额外记录文献出处。

## 4. 质量纪律

- 文献未说明的内容标为缺失或扩展，不补全。
- `doc_01`, `doc_08`, `doc_09`, `doc_11` 在修复前不得作为强证据。
- 图表/章节级 warning 可以进入人工复核队列，不能静默升级为强证据。
- 任何候选都要通过真实性门、预测门、交易门和冗余门；只通过样本内或无成本检验不足以入池。
