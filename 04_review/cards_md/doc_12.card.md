# 可转债定价与套利策略初探 CRR二叉树
**Doc ID:** doc_12
**Authors:** 任瞳, 王武蕾, 梁雨辰
**Year:** 2022

## 1. 原文事实 (Original)
### 研究场景 (Research Scenario)
可转债定价与套利策略研究，重点探讨CRR二叉树模型在可转债定价中的应用及基于DELTA对冲的波动率套利策略。
*Sources: <!-- page: 1 --> Section 1*

### 经济机制 (Economic Mechanism)
可转债同时具备债性和股性，内嵌强赎、下修和回售条款，定价难度高。CRR二叉树模型通过逆向推导和条款修正实现定价。
*Sources: <!-- page: 4 --> Section 1.1*

### 特征公式 (Feature Formulas)
**CRR二叉树定价**
$$ V(i,j) = max[V(i,j)_{EU}, S(i,j)] $$
*Sources: <!-- page: 5 --> Section 1.1 STEP3*
- 变量说明：
  - `V(i,j)`: 节点(i,j)的转债价值
  - `S(i,j)`: 节点(i,j)的正股价格

**DELTA计算**
$$ DELTA_{CRR} = \frac{V_{CRR}(S + \Delta S) - V_{CRR}(S - \Delta S)}{2\Delta S} $$
*Sources: <!-- page: 10 --> Section 1.2.3*
- 变量说明：
  - `\Delta S`: 正股价格微小变动量

### 数据处理 (Data Processing)
使用10年期国债利率作为无风险利率，正股近12个月股息率，近3个月年化波动率，债项评级下的信用利差。
*Sources: <!-- page: 7 --> Table 2*

### 检验方法 (Testing Methods)
对比CRR模型与BSM/BAW模型的定价误差，通过历史回测验证套利策略表现。
*Sources: <!-- page: 7 --> Section 1.2.1*

### 稳健性与失败 (Robustness & Failures)
CRR模型在2015-2016年误差较大，因存量转债数量少；融券对冲策略受限于标的范围和费率成本。
*Sources: <!-- page: 8 --> Figure 3, <!-- page: 18 --> Section 2.2.3*

### 交易可实现性 (Tradability)
融券对冲策略年化收益7.06%，最大回撤4.33%；期货对冲策略年化10.79%，最大回撤12.55%。
*Sources: <!-- page: 13 --> Table 4, <!-- page: 20 --> Table 10*

## 2. 项目适配 (Adaptation)
### 与项目契合度
可转债套利策略需正股对冲，与期货日内交易场景差异较大。DELTA计算和波动率特征可能部分适用于高频波动率交易。
### 调整建议
需将DELTA计算调整为基于日内高频数据，并替换对冲工具为期货合约。需验证高频下波动率预测的有效性。
### 数据充分性
partial
### 复现模式
adjust
### 缺失字段
日内高频波动率数据, 实时信用利差数据

## 3. 扩展假设 (Extensions)
### 假设 1
**内容:** 将CRR模型的波动率输入替换为高频已实现波动率，可能提升日内定价精度。
**推导理由:** 原文显示波动率参数对模型精度关键，高频数据可捕捉短期波动特征。
**本文证据:** <!-- page: 7 --> Table 2
**跨文献证据ID:** L2 暂空，待 L3 回填

### 假设 2
**内容:** 利用DELTA值的日内变化构建均值回归信号。
**推导理由:** 原文DELTA计算显示对价格变动敏感，高频场景下可能捕捉短期失衡。
**本文证据:** <!-- page: 10 --> Section 1.2.3
**跨文献证据ID:** L2 暂空，待 L3 回填
