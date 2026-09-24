# references 说明

本目录放入阶段 2 归并后供 Skill 调用的材料。

建议结构：

```text
references/
├── data_dictionary.md
├── research_constraints.md
├── topics/
│   ├── T01_盘口失衡.md
│   └── T02_流动性冲击.md
└── cards/
    ├── doc_01.card.md
    └── doc_02.card.md
```

放入原则：

- 主题文档优先放入 `topics/`。
- 只放精选卡片，不放全量原文。
- 单篇 JSON 仍以项目根目录 `03_cards/` 为唯一事实源。
- 如果发现卡片 Markdown 与 JSON 不一致，重新从 JSON 渲染。
