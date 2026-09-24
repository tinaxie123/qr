# Diversification of Equity Factors - Hierarchical Clustering for better risk allocation
**Doc ID:** doc_05
**Authors:** Robert Smith, PhD, Berowne Hlavaty, Ada Lau, Evan Hu, Marko Kolanovic, PhD
**Year:** 2018

## 1. 原文事实 (Original)
### 研究场景 (Research Scenario)
Investigation of various risk allocation techniques on equity factors capturing Equity Risk Premia or Smart Beta, including traditional approaches like Equal Weight, Minimum Variance, and Risk Parity, as well as newer methods incorporating hierarchical clustering (HRP and HCP).
*Sources: <!-- page: 3 --> Section 'Diversification of Factors'*

### 经济机制 (Economic Mechanism)
Hierarchical clustering is used to group similar factors, allowing risk allocation schemes to be applied at the cluster level, which removes redundant exposures and improves diversification. This approach is particularly beneficial for simpler allocation schemes like Equal Weight and Inverse Volatility.
*Sources: <!-- page: 3 --> Section 'Diversification of Factors', <!-- page: 13 --> Figure 9*

### 特征公式 (Feature Formulas)
**Distance Metric**
$$ d_{i,j} = \sqrt{(1 - \rho_{i,j}) / 2} $$
*Sources: <!-- page: 9 --> Section 'Distance metric'*
- 变量说明：
  - `d_{i,j}`: Distance between assets i and j
  - `\rho_{i,j}`: Correlation between assets i and j

### 数据处理 (Data Processing)
The study uses 70 core equity factors in long-only and long-short forms, plus market hedges. Pairwise correlations are calculated over 12, 36, and 60-month lookback periods, with longer periods providing more stable results. Hierarchical clustering is performed using Python’s Sci-Kit Learn package with various linkage methods (Single, Complete, Average, Ward).
*Sources: <!-- page: 3 --> Section 'Diversification of Factors', <!-- page: 9 --> Section 'Assumptions'*

### 检验方法 (Testing Methods)
Backtests are conducted from January 2000 to May 2018, comparing performance of different weighting schemes (EW, IV, HRP, HCP, CRP, MVP, MDP, MVO, ECR, TW) applied to individual factors and clusters. Performance is measured using risk-adjusted returns, with sensitivity tests on cluster distance thresholds.
*Sources: <!-- page: 10 --> Section 'Backtests', <!-- page: 30 --> Appendix I*

### 稳健性与失败 (Robustness & Failures)
Clustering improves performance up to a point; excessive reduction in cluster count leads to overly coarse representations of factor exposures. HRP and HCP, which embed clustering, start strong but show less incremental benefit from additional clustering.
*Sources: <!-- page: 13 --> Figure 9, <!-- page: 21 --> Figure 19*

### 交易可实现性 (Tradability)
The approach simplifies portfolio construction by reducing the number of assets to manage. Implementation can be flexible, e.g., by selecting the best-performing factor within each cluster (based on Sharpe ratio, liquidity, etc.), which further boosts performance.
*Sources: <!-- page: 25 --> Section 'Best in Cluster', <!-- page: 5 --> Section 'Our approach'*

## 2. 项目适配 (Adaptation)
### 与项目契合度
The hierarchical clustering approach is conceptually applicable to期货日内单合约交易, especially for portfolio construction using multiple factors. However, the original study focuses on monthly rebalancing and equity factors, which differ from高频或快照数据.
### 调整建议
The clustering and allocation methods would need to be adapted to高频数据, with shorter lookback periods for correlations and faster rebalancing. Feature formulas must rely solely on historical information without未来数据.
### 数据充分性
partial
### 复现模式
adjust
### 缺失字段
高频数据的具体字段（如tick数据、订单簿深度等）, 日内波动率估计

## 3. 扩展假设 (Extensions)
### 假设 1
**内容:** 基于层次聚类的日内因子组合优化：在期货日内交易中，对高频因子进行层次聚类，然后在聚类层面上应用风险平价或波动率倒数加权。
**推导理由:** 原文显示聚类能有效去除冗余因子并改善风险调整后收益。在日内场景中，高频因子可能也存在高度相关性，聚类后加权可能提升组合稳定性。
**本文证据:** <!-- page: 3 --> Section 'Diversification of Factors', <!-- page: 17 --> Section 'HCP and HRP'
**跨文献证据ID:** L2 暂空，待 L3 回填

### 假设 2
**内容:** 动态聚类阈值调整：根据市场波动率水平自动调整聚类距离阈值，在高波动时段使用更宽松的聚类（减少聚类数量）以降低风险。
**推导理由:** 原文发现存在最优聚类数量（见Page 13 Figure 9）。日内波动率变化剧烈，动态调整阈值可能更好适应不同市场状态。
**本文证据:** <!-- page: 13 --> Figure 9, <!-- page: 4 --> Section 'Static is really Dynamic'
**跨文献证据ID:** L2 暂空，待 L3 回填
