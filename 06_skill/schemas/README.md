# schemas 说明

本目录放 Skill 对外输出规范。

当前阶段建议包含：

- `research_feature_idea.schema.json`：后续调用 Skill 形成文献驱动特征想法时的输出规范。

根目录 `schemas/` 是开发时的规范源。单篇文献提取契约使用根目录下的 `extraction.schema.json`，人读卡片通过渲染脚本生成，不再在 Skill 目录维护第二份提取 schema 副本。
