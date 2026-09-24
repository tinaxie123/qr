# 期货日内因子挖掘 · 文献研究 Skill

本 Skill 用于后续智能体在设计期货日内因子特征时调用阶段 2 的文献知识。它不替代原文证据，也不允许把项目判断写成文献结论。

## 使用顺序

1. 先读取数据说明和研究约束。
   - 数据说明位于 `references/data_dictionary.md` 或项目根目录 `01_specs/data_dictionary.template.md`。
   - 研究约束位于 `references/research_constraints.md` 或项目根目录 `01_specs/research_constraints.md`。
2. 再读取相关主题知识文档。
   - 优先使用 `references/topics/` 中的主题文档。
   - 如果主题文档不足，再回查精选研究卡片。
3. 需要引用文献证据时，必须保留 `doc_id + evidence_id + chunk_id/page`。
4. 设计文献外的新特征时，必须明确说明：
   - 来自哪些文献机制或证据；
   - 哪些部分是项目适配判断；
   - 哪些部分是待验证扩展；
   - 计算公式、所需字段、适用条件、异常处理和放弃条件。

## 证据纪律

- `original`：只能写原文说过的内容。
- `adaptation`：只能写项目适配判断，不挂原文 locator。
- `extensions`：只能写待验证扩展，必须引用原文 evidence_id。
- 文献未说明的内容必须标为缺失，不允许补全。
- 必须区分同期关系和未来预测。
- 必须区分样本内、验证集和样本外。
- 文献间分歧要保留，不强行统一。

## 可用材料

- `references/topics/`：主题知识文档，3000-5000 字/主题。
- `references/cards/`：精选人读研究卡片。
- `references/data_dictionary.md`：数据说明。
- `references/research_constraints.md`：研究约束。
- `schemas/`：输出规范。
- `examples/`：设计示例、反例、缺失与分歧标注示例。

## 输出要求

当任务是“基于文献提出特征想法”时，输出必须使用 `schemas/research_feature_idea.schema.json`。由文献机制驱动的想法必须包含文献出处；字段直觉或项目假设不得伪造文献出处。

当任务是“解释某篇文献或主题”时，优先引用研究卡片或主题文档，不要重新编写无出处结论。
