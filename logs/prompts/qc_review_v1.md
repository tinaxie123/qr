# 研究卡片质检提示词 v1

请对一张研究卡片和对应 chunks 做复核，只输出问题清单，不重写卡片。

重点检查：

- `original` 中每条 evidence 是否能在 source locator 指向的 chunk 中找到支持。
- 是否把项目判断写成了原文结论。
- 是否把原文未说明的内容补全了。
- 公式、变量下标、窗口、分母、单位是否抄错或漏写。
- 是否混淆同期关系与未来预测。
- 是否混淆样本内、验证集和样本外。
- `extensions[].basis_evidence_ids` 是否真实存在并足以支持扩展方向。
- `candidate_factor_cards` 是否误把不可得字段当成可用字段。

输出字段：

- `doc_id`
- `severity`: `pass` / `minor` / `major` / `reject`
- `issues`: 问题数组，每条包含 `location`、`problem`、`evidence`、`fix_suggestion`
- `review_summary`
