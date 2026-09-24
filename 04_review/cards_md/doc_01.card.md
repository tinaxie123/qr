# “Beat the Market" Revisited: An Independent Replication and Statistical Audit of an Intraday Momentum Strategy
**Doc ID:** doc_01
**Authors:** José Enrique Delgado
**Year:** 2026

## 1. 原文事实 (Original)
### 研究场景 (Research Scenario)
The study independently replicates and extends Zarattini, Aziz, and Barbon's intraday momentum strategy applied to SPY, using a one-minute TradeStation dataset from January 2000 through August 2026.
*Sources: <!-- page: 1 -->*

### 经济机制 (Economic Mechanism)
The strategy constructs a time-varying 'Noise Area' around the opening price, enters trend-following positions when price action indicates an abnormal demand/supply imbalance, and applies a dynamic trailing stop based on the current Noise Area boundary and Volume Weighted Average Price (VWAP).
*Sources: <!-- page: 3 --> Section 1*

### 特征公式 (Feature Formulas)
**Noise Area**
$$ \sigma_{t,h} = \frac{1}{L} \sum_{i=1}^{L} m_{t-i,h} $$
*Sources: <!-- page: 3 --> Section 2.1*
- 变量说明：
  - `L`: lookback period of 14 trading days
  - `m_{t-i,h}`: absolute move from the open on prior day t-i at checkpoint h

**VWAP**
$$ VWAP_{t,h} = \frac{\sum_{j \leq h} TP_{t,j} V_{t,j}}{\sum_{j \leq h} V_{t,j}} $$
*Sources: <!-- page: 4 --> Section 2.2*
- 变量说明：
  - `TP_{t,j}`: typical price at time j on day t
  - `V_{t,j}`: volume at time j on day t

**Volatility targeting**
$$ \ell_t = \min\left(4, \frac{0.02}{\widehat{\sigma}_t^{SPY}}\right) $$
*Sources: <!-- page: 4 --> Section 2.3*
- 变量说明：
  - `\widehat{\sigma}_t^{SPY}`: sample standard deviation of the prior 14 daily SPY returns

### 数据处理 (Data Processing)
The primary replication uses SPY one-minute regular-session data exported from TradeStation, covering 3 January 2000 through 14 August 2026. The original paper uses one-minute IQFeed data from May 2007 through April 2024.
*Sources: <!-- page: 3 --> Section 3.1*

### 检验方法 (Testing Methods)
The study performs an independent replication and a post-publication extension, reconciling implementation details against the authors' published Python reference code. It also subjects the strategy to a documented search and statistical audit covering 80 SPY strategy alternatives.
*Sources: <!-- page: 1 --> Abstract, <!-- page: 3 --> Section 3*

### 稳健性与失败 (Robustness & Failures)
The study finds that the strategy's performance is regime-dependent, with strong initial post-publication performance followed by a materially weak recent regime. Many intuitive modifications fail to improve the strategy's performance across all validation windows.
*Sources: <!-- page: 6 --> Section 4.2, <!-- page: 15 --> Section 7*

### 交易可实现性 (Tradability)
The strategy models a commission of $0.0035 per share and slippage of $0.001 per share. The authors report that more conservative transaction-cost assumptions weaken the edge but do not eliminate the historical result.
*Sources: <!-- page: 4 --> Section 2.3*

## 2. 项目适配 (Adaptation)
### 与项目契合度
The strategy's focus on intraday momentum and use of high-frequency data align well with the target project scenario of期货日内单合约交易. However, the strategy's reliance on VWAP and Noise Area boundaries may require adjustments for different markets or data sources.
### 调整建议
The strategy may need to be adjusted to use only historical information for feature calculation, as required by the target project. The VWAP calculation and Noise Area boundaries may also need to be adapted to the specific market and data source used in the project.
### 数据充分性
partial
### 复现模式
adjust
### 缺失字段
无

## 3. 扩展假设 (Extensions)
### 假设 1
**内容:** A modified version of the strategy that uses only historical information for feature calculation could be developed for期货日内单合约交易.
**推导理由:** The original strategy's reliance on intraday momentum and high-frequency data makes it a good candidate for adaptation to期货日内单合约交易, but adjustments are needed to ensure that all features are calculated using only historical information.
**本文证据:** <!-- page: 3 --> Section 2.1, <!-- page: 4 --> Section 2.2
**跨文献证据ID:** L2 暂空，待 L3 回填

### 假设 2
**内容:** The strategy's performance could be improved by incorporating additional filters or overlays based on market regime or volatility.
**推导理由:** The study finds that the strategy's performance is regime-dependent, suggesting that additional filters or overlays based on market regime or volatility could improve its robustness.
**本文证据:** <!-- page: 6 --> Section 4.2, <!-- page: 15 --> Section 7
**跨文献证据ID:** L2 暂空，待 L3 回填
