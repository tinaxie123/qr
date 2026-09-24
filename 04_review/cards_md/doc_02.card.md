# 0DTE Options and the Price of Tail Protection
**Doc ID:** doc_02
**Authors:** James O'Donovan
**Year:** 2026

## 1. 原文事实 (Original)
### 研究场景 (Research Scenario)
The study examines the impact of introducing daily same-day-expiry (0DTE) SPX options on the implied volatility skew across different tenors, particularly focusing on the compression of put skew.
*Sources: <!-- page: 3 --> Section 1 Introduction*

### 经济机制 (Economic Mechanism)
The introduction of fully-daily 0DTE contracts affects non-0DTE skew through two channels: a reduction in the equilibrium compensation dealers require to warehouse put-side inventory and a shift in customer demand across tenors and moneyness.
*Sources: <!-- page: 19 --> Section 5.4 Mechanism*

### 特征公式 (Feature Formulas)
**Put-vs-ATM Skew**
$$ sk_{i,t,T} = IV_{i,t,T,-25\Delta}^{P} - IV_{i,t,T,-50\Delta}^{P} $$
*Sources: <!-- page: 8 --> Section 3 Data*
- 变量说明：
  - `IV_{i,t,T,-25\Delta}^{P}`: Implied volatility of a 25-delta put at tenor T
  - `IV_{i,t,T,-50\Delta}^{P}`: Implied volatility of an at-the-money put at tenor T

### 数据处理 (Data Processing)
Daily implied volatilities are constructed from raw option-level quotes in the OptionMetrics IvyDB U.S. database. For each (underlying, date), quotes with calendar-day time to expiration in [5, 400] and absolute delta in [0.10,0.60] are selected. Implied volatilities are interpolated using a monotone cubic spline within each expiration and linearly interpolated across expirations to exact target tenors.
*Sources: <!-- page: 7 --> Section 3 Data*

### 检验方法 (Testing Methods)
A cross-tenor difference-in-differences design is used to identify the effect of 0DTE options on skew compression. The design compares the differential change in skew between short and long tenors relative to a 365-day baseline.
*Sources: <!-- page: 9 --> Section 4 Empirical Strategy*

### 稳健性与失败 (Robustness & Failures)
Robustness checks include alternative data sources and skew-measurement conventions, alternative sample windows, and tests for discrete breaks versus smooth secular trends. The study finds that the May 2022 break is not explained by a smooth secular trend.
*Sources: <!-- page: 23 --> Section 6 Robustness*

### 交易可实现性 (Tradability)
The study notes that the compression in skew translates into a material reduction in the cost of equity tail insurance, with implied savings of $0.9 to $1.5 billion over the May 2022–June 2024 episode.
*Sources: <!-- page: 22 --> Section 5.5 Economic Magnitude*

## 2. 项目适配 (Adaptation)
### 与项目契合度
The study's focus on short-tenor options and intraday trading dynamics aligns well with the target project scenario of futures intraday trading. However, the specific focus on options rather than futures may limit direct applicability.
### 调整建议
To adapt the study's findings to futures intraday trading, the implied volatility skew measures would need to be translated into equivalent futures market metrics. Additionally, the study's reliance on option-specific data (e.g., delta, implied volatility) would require substitution with futures-specific data.
### 数据充分性
partial
### 复现模式
adjust
### 缺失字段
futures-specific volatility measures, intraday futures trading data

## 3. 扩展假设 (Extensions)
### 假设 1
**内容:** The introduction of daily expirations in futures markets could similarly compress short-term volatility skew, reducing the cost of tail protection for intraday traders.
**推导理由:** The study's findings on options suggest that increased availability of short-term instruments can reduce the cost of tail protection. This logic may extend to futures markets, where similar dynamics could apply.
**本文证据:** <!-- page: 19 --> Section 5.4 Mechanism
**跨文献证据ID:** L2 暂空，待 L3 回填

### 假设 2
**内容:** Intraday recycling of gamma exposure through same-session instruments could lower warehousing costs for dealers in futures markets, similar to the observed effect in options markets.
**推导理由:** The study identifies intraday recycling as a key mechanism for reducing warehousing costs in options markets. Futures markets, with their high liquidity and intraday trading, may exhibit similar cost reductions.
**本文证据:** <!-- page: 19 --> Section 5.4 Mechanism
**跨文献证据ID:** L2 暂空，待 L3 回填
