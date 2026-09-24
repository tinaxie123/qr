# references 说明

本目录放入阶段 2 归并后供 Skill 调用的材料。根目录 `03_cards/` 仍是单篇 JSON 的唯一事实源；本目录中的卡片副本用于 Skill 打包、主题归并和人工复核。

当前版本为首轮归并样例，已纳入：

- `topics/T01_日内信号标准化与事件触发.md`
- `topics/T02_稳健性失败与过拟合控制.md`
- `cards/doc_02.json`, `doc_03.json`, `doc_04.json`, `doc_05.json`, `doc_06.json`, `doc_07.json`, `doc_10.json`, `doc_12.json`, `doc_13.json`, `doc_14.json`, `doc_15.json`

`doc_01`, `doc_08`, `doc_09`, `doc_11` 当前 validator v2 硬失败，暂不放入 Skill references。

目录结构：

```text
references/
├── data_dictionary.md
├── research_constraints.md
├── topics/
│   ├── T01_日内信号标准化与事件触发.md
│   └── T02_稳健性失败与过拟合控制.md
└── cards/
    ├── doc_02.json
    └── ...
```

放入原则：

- 主题文档优先放入 `topics/`。
- 只放 validator v2 `machine_pass` 或 `manual_pending` 的精选卡片，不放全量原文。
- 单篇 JSON 仍以项目根目录 `03_cards/` 为唯一事实源。
- 如果发现卡片 Markdown 与 JSON 不一致，重新从 JSON 渲染。
- warning 样本进入主题时必须标注待复核；硬失败样本不得作为强证据。
