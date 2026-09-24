# 文献驱动特征设计示例模板

## 输入依据

- 主题：
- 文献来源：`doc_id + evidence_id + chunk_id/page`
- 原文机制：
- 项目适配判断：

## 输出示例

```json
{
  "idea_id": "idea_example_001",
  "proposal_kind": "adapt",
  "feature_name": "示例特征名称",
  "required_fields": [
    {
      "field": "bid_volume_1",
      "role": "买一挂单量",
      "availability": "当前快照可得"
    }
  ],
  "formula": {
    "expression": "写清完整公式",
    "variables": [
      {
        "symbol": "x_t",
        "definition": "变量定义",
        "unit": "单位"
      }
    ],
    "window_sec": [3, 5, 15, 60],
    "denominator": "分母定义及为零处理",
    "time_alignment": "只使用 t 时点及以前信息",
    "unit": "特征单位"
  },
  "design_reason": "说明文献机制如何迁移到本项目。",
  "applicable_conditions": "适用品种、市场状态和窗口。",
  "exception_handling": {
    "insufficient_history": "历史不足时置缺失或跳过。",
    "zero_denominator": "分母为零时置缺失。",
    "missing_values": "关键字段缺失时置缺失。",
    "other": "其他异常。"
  },
  "validation_plan": {
    "target": "未来收益或方向",
    "horizon_sec": 15,
    "price_benchmark": "mid_price",
    "metrics": ["IC", "Rank IC", "方向准确率"],
    "baseline": "与基础盘口失衡特征比较",
    "sample_split": "训练/验证/测试按时间切分",
    "ablation_or_controls": "控制已有同类特征"
  },
  "expected_direction": "预期方向及不确定性。",
  "abandon_conditions": "什么结果下放弃该想法。",
  "adaptation_notes": "说明哪些原文结论需要重新验证。",
  "literature_sources": [
    {
      "doc_id": "doc_01",
      "evidence_id": "e_001",
      "chunk_id": "doc_01_chunk_0001",
      "page": "1",
      "quote": "不超过短句的原文摘录"
    }
  ]
}
```
