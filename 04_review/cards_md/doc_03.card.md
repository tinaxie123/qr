# (In)Efficient Market States and Rough Volatility Detected via Grünwald-Letnikov Fractional Derivative
**Doc ID:** doc_03
**Authors:** Daniele Angelini
**Year:** 2026

## 1. 原文事实 (Original)
### 研究场景 (Research Scenario)
The study focuses on testing self-similarity in fractional processes under long-range dependence, particularly in financial applications such as realized volatility and equity index prices.
*Sources: <!-- page: 1 --> Section 1 Introduction*

### 经济机制 (Economic Mechanism)
The paper introduces a regime-adaptive KS/GL–KS framework based on the discrete Grünwald–Letnikov (GL) fractional derivative to remove low-frequency long-memory singularity while preserving finite-dimensional H-self-similarity.
*Sources: <!-- page: 2 --> Section 2 Preliminaries and problem statement*

### 特征公式 (Feature Formulas)
**Grünwald-Letnikov derivative**
$$ \Delta _ { h } ^ { { G L } , \alpha } f ( x ) = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } ( - 1 ) ^ { k } \binom { \alpha } { k } f ( x - k h ) $$
*Sources: <!-- page: 8 --> Definition 3.1*
- 变量说明：
  - `\alpha`: Order of the derivative
  - `h`: Step size
  - `f(x)`: Real-valued function

**Fractional Brownian motion covariance**
$$ \mathbb { E } \left[ B _ { t } ^ { H } B _ { s } ^ { H } \right] = \frac { 1 } { 2 } \left( t ^ { 2 H } + s ^ { 2 H } - | t - s | ^ { 2 H } \right) $$
*Sources: <!-- page: 3 --> Section 2 Preliminaries and problem statement*
- 变量说明：
  - `B_t^H`: Fractional Brownian motion at time t with Hurst exponent H
  - `H`: Hurst exponent

### 数据处理 (Data Processing)
The paper uses crossed fractional Gaussian noises and applies the GL filter to transform the data into a short-memory regime for analysis.
*Sources: <!-- page: 4 --> Section 2.1 Problem Statement and the Long-Memory Issue*

### 检验方法 (Testing Methods)
The study employs a Kolmogorov-Smirnov type statistic to compare empirical distribution functions of rescaled increments.
*Sources: <!-- page: 5 --> Section 2.1 Problem Statement and the Long-Memory Issue*

### 稳健性与失败 (Robustness & Failures)
The paper discusses the phase transition in the asymptotic behavior of the KS statistic at H = 1/2 and the slow convergence rates in the long-memory regime.
*Sources: <!-- page: 6 --> Proposition 2.3*

### 交易可实现性 (Tradability)
The method is applied to financial time series to detect rough volatility and market efficiency states, suggesting practical applicability in trading strategies.
*Sources: <!-- page: 3 --> Section 1 Introduction*

## 2. 项目适配 (Adaptation)
### 与项目契合度
The GL-KS framework is highly relevant for high-frequency trading as it provides a robust method to detect market inefficiencies and rough volatility, which are critical for intraday strategies.
### 调整建议
The method needs to be adapted to use only historical data within the trading day, ensuring no look-ahead bias. The GL filter parameters may need optimization for high-frequency data.
### 数据充分性
sufficient
### 复现模式
adjust
### 缺失字段
无

## 3. 扩展假设 (Extensions)
### 假设 1
**内容:** A new feature based on the GL-filtered Hurst exponent could be developed to predict short-term mean reversion or momentum in intraday futures prices.
**推导理由:** The GL-KS method effectively identifies persistent and anti-persistent market states, which can be leveraged to design trading signals.
**本文证据:** <!-- page: 25 --> Section 5.1.2 Weak-Form Market Efficiency
**跨文献证据ID:** L2 暂空，待 L3 回填

### 假设 2
**内容:** The GL filter could be applied to volatility surfaces to detect rough volatility regimes in real-time, enhancing option pricing models.
**推导理由:** The paper demonstrates the GL filter's effectiveness in neutralizing long-memory effects, making it suitable for real-time volatility estimation.
**本文证据:** <!-- page: 25 --> Section 5.1.1 Rough volatility
**跨文献证据ID:** L2 暂空，待 L3 回填
