# doc_01 日内动量独立复现与统计审计 Beat the Market Revisited

- source_path: `/Users/xiehaotong/Desktop/literature_pipeline/00_raw/期货日内因子_精选文献15篇/01_英文论文_微观结构与方法/01_日内动量独立复现与统计审计(Beat the Market Revisited).pdf`
- parser: `MinerU`
- mineru_version: `4.0.7`
- mineru_tier: `basic`
- ocr_mode: `auto`
- lang: en
- type: paper
- page_count: 23

<!-- page: 1 -->

## Page 1

# “Beat the Market" Revisited

# An Independent Replication and Statistical Audit of an Intraday Momentum Strategy

José Enrique Delgado

Independent Research

August 2026

Research status. This study independently replicates and extends Zarattini, Aziz, and Barbon's Swiss Finance Institute Research Paper No. 24-97. It is not affiliated with the original authors or the Swiss Finance Institute. The published strategy is reproduced on an independent one-minute TradeStation dataset, extended through 14 August 2026, and subjected to a documented search and statistical audit covering 80 SPY strategy alternatives. The final modified configuration is frozen for prospective observation and is explicitly classified as retrospectively significant but not prospectively validated. This revision also reconciles the authors' August 2025 post-publication update with the subsequent, previously unpublished 2025–2026 stretch and expands the cross-asset adverse-evidence discussion.

<!-- page: 2 -->

## Page 2

“Beat the Market"' Revisited

Independent Replication and Statistical Audit

## Abstract

Zarattini, Aziz, and Barbon report that a simple intraday time-series momentum strategy applied to SPY produced a total return of 1,985%, an annualized return of 19.6%, and a Sharpe Ratio of 1.33 from May 2007 through April 2024. This paper performs an independent replication and a post-publication extension using approximately 2.6 million one-minute SPY observations from TradeStation spanning January 2000 through August 2026. After reconciling two material implementation details against the authors' published Python reference code—the use of typical-price Volume Weighted Average Price (VWAP) and VWAP confirmation at entry—the original result is reproduced almost exactly: 1,989% total return and a Sharpe Ratio of 1.317 on the paper window under the closest paper-matching convention. The independent update also closely reproduces the authors' September 2025 FAQ update: 2024 returns are 31.8% versus their 32.2%, and January–August 2025 returns are 1.4% versus their 1.0%.

The longer sample changes the interpretation, but not in the simple form suggested by the pooled May 2024–August 2026 Sharpe of 0.35. Disaggregating the post-publication path reveals two sharply different regimes. Under a Q24-comparable monthly convention, May 2024–29 August 2025 returns 19.3% with Sharpe 1.057; using the exact first trading day after the 10 May 2024 publication, the corresponding return is 23.3% with Sharpe 1.284. By contrast, the subsequent 2 September 2025–14 August 2026 stretch returns -8.1% with Sharpe -0.461. Thus the evidence does not support a narrative of immediate post-publication alpha decay; it supports a strong initial post-publication period followed by a materially weak recent regime. A systematic search then evaluates asymmetric short filters, relative-volume sizing, volatility overlays, persistence filters, profit locks, breakeven rules, trade caps, daily loss limits, VWAP-dominance rules, intraday decay, regime overlays, and performance-based overlays. Only a small subset survives the consistent multi-window standard applied during the extension stage. The final frozen selected specification reaches a valid-period Sharpe Ratio of 1.274, a -14.8% maximum drawdown, and a 2110.6% total return over 2000–2026, while deliberately sacrificing terminal wealth relative to the baseline

To address multiple testing, a research ledger of 129 trials is reconstructed and 80 SPY search alternatives are identified. Combinatorially Symmetric Cross-Validation yields a Probability of Backtest Overfitting of 38.49% under the historical convention and 40.87% on a common-valid sample. The Deflated Sharpe Ratio of the final candidate, using N = 80 as the primary multiple-testing count, is 99.999986796%. These statistics support a strong retrospective edge but do not provide a genuine prospective validation because the search was adaptive and the 2024–2026 data were observed during model development. The correct next experiment is therefore not another retrospective optimization, but the passage of time with frozen parameters.

Keywords: Intraday Momentum; SPY; Time-Series Momentum; VWAP; Replication; Post-Publication Performance; Backtest Overfitting; Probability of Backtest Overfitting (PBO); Deflated Sharpe Ratio (DSR); Researcher Degrees of Freedom; Prospective Validation.

## 1 Introduction

Momentum is one of the most persistent and widely studied empirical regularities in asset prices. At medium horizons, the canonical evidence of Jegadeesh and Titman documents continuation in relative equity performance, while later work extends the idea to time-series momentum and, increasingly, to intraday horizons [2, 6]. Gao et al. document intraday continuation in the U.S. equity market [3]; Rosa emphasizes that the strength of intraday predictability can decay or become regime-dependent [4]; and Baltussen et al. link intraday momentum to hedging demand and market microstructure [5]. These strands motivate systematic attempts to distinguish directional price moves from ordinary intraday noise.

Zarattini, Aziz, and Barbon (hereafter ZAB) propose one such mechanism in Beat the Market, Swiss Finance Institute Research Paper No. 24-97 [1]. Their strategy constructs a time-varying “Noise Area" around the opening price, enters trend-following positions when price action indicates an abnormal demand/supply imbalance, applies a dynamic trailing stop based on the current Noise Area boundary and Volume Weighted Average Price (VWAP), and scales exposure toward a daily volatility target. In the version dated 22 September

1

<!-- page: 3 -->

## Page 3

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

2025, the authors report a total return of 1,985%, an annualized return of 19.6%, volatility of 14.3%, and a Sharpe Ratio of 1.33 over May 2007–April 2024. Their Frequently Asked Questions (FAQ) section subsequently adds code links, parameter-sensitivity tables, a more sophisticated market-impact exercise, cross-asset extensions, and—most importantly for this study—an updated equity curve through 29 August 2025 with the post-publication period explicitly shaded. Their decision to publish executable reference code and maintain a living FAQ is unusual and materially increases the falsifiability of the research. It makes the present study possible as a genuine reproduction exercise rather than a reverse-engineering exercise from prose alone; throughout, disagreements are therefore treated as testable specification or data questions rather than as reasons to presume error in the original work.

The present study is designed around three questions.

First, can the original result be independently reproduced on a different data source and a separately written engine? A strong historical result is substantially more credible if its main statistics survive a clean implementation and a different vendor feed.

Second, what happened after publication? This is not merely a rhetorical question. The 2025 edition of the original paper makes the post-publication equity path observable, and the independent TradeStation history extends another year through August 2026. That additional period cannot prove permanent alpha decay, but it provides a direct test of whether the spectacular in-sample behavior remained representative.

Third, can the risk-adjusted profile be improved without hiding failed experiments? Rather than present only successful modifications, we maintain a research ledger recording both adopted and rejected ideas. The resulting search contains 80 SPY alternatives that could have influenced final selection. This permits a more honest treatment of multiple testing than a single polished backtest.

The contribution is therefore not intended as a refutation of the original paper. In fact, the first and strongest result of this study is that the original backtest is reproducible to a remarkably close degree. The contribution is to separate four statements that are often conflated: (i) the historical backtest existed, (ii) the underlying historical edge is statistically distinguishable from pure chance, (iii) the parameter optimum is stable, and (iv) the edge will persist prospectively. The evidence strongly supports the first two, weakens the third, and leaves the fourth unresolved.

## 2 The Published Strategy

## 2.1 Noise Area

Let
O _ { t }
denote the regular-session open on day t, and let
C _ { t - 1 }
denote the previous regular-session close. For each intraday checkpoint h, define the absolute move from the open on prior day t – i as

m _ { t - i , h } = \left| \frac { C _ { t - i , h } } { O _ { t - i } } - 1 \right| .\tag{1}

Using a lookback of L = 14 trading days, the time-of-day noise estimate is

\sigma _ { t , h } = \frac { 1 } { L } \sum _ { i = 1 } ^ { L } m _ { t - i , h } .\tag{2}

The gap-aware upper and lower boundaries are then

U B _ { t , h } = \operatorname* { m a x } ( O _ { t } , C _ { t - 1 } ^ { * } ) \left( 1 + \sigma _ { t , h } \right) ,\tag{3}

L B _ { t , h } = \operatorname* { m i n } ( O _ { t } , C _ { t - 1 } ^ { * } ) \left( 1 - \sigma _ { t , h } \right) ,\tag{4}

where
C _ { t - 1 } ^ { * }
denotes the previous close after the dividend convention used by the relevant engine. The strategy only evaluates signals at semi-hourly checkpoints, h ∈ {10:00, 10:30, . . . , 16:00}.

2

<!-- page: 4 -->

## Page 4

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

## 2.2 VWAP and entry/exit logic

The authors' published reference implementation computes VWAP from the regular-session typical price, consistent with the VWAP-based framework discussed in their earlier work [1, 9],

T P _ { t , j } = \frac { H _ { t , j } + L _ { t , j } + C _ { t , j } } { 3 } , \qquad V W A P _ { t , h } = \frac { \sum _ { j \leq h } T P _ { t , j } V _ { t , j } } { \sum _ { j \leq h } V _ { t , j } } .\tag{5}

For a long position, the dynamic stop is

\begin{array} { r } { \mathit { S t o p } _ { t , h } ^ { L } = \operatorname* { m a x } ( U B _ { t , h } , V W A P _ { t , h } ) , } \end{array}\tag{6}

and for a short position,

\begin{array} { r } { S t o p _ { t , h } ^ { S } = \operatorname* { m i n } ( L B _ { t , h } , V W A P _ { t , h } ) . } \end{array}\tag{7}

The public reference code also requires VWAP confirmation at entry: a long signal is valid only when price is above both the upper band and VWAP; a short signal requires price below both the lower band and VWAP. This entry requirement is operationally important because a band-only entry rule generates materially more signals and was the principal source of the gap between our first textual replication and the published Sharpe Ratio.

## 2.3 Volatility targeting and costs

The flagship variant scales daily exposure using recent SPY volatility. Let
\widehat { \sigma } _ { t } ^ { S P Y }
denote the sample standard deviation of the prior 14 daily SPY returns. The base leverage multiplier is

\ell _ { t } = \operatorname* { m i n } \left( 4 , \frac { 0 . 0 2 } { \widehat { \sigma } _ { t } ^ { S P Y } } \right) ,\tag{8}

with share count approximately

Q _ { t } = \left\lfloor \frac { A U M _ { t - 1 } \ell _ { t } } { O _ { t } } \right\rfloor .\tag{9}

The paper models a commission of $0.0035 per share and slippage of $0.001 per share. In FAQ Q15, ZAB additionally report an I-Star market-impact sensitivity, based on the Kissell–Malamut framework, in which the Sharpe Ratio falls from 1.33 to 1.17 but remains positive [1, 12]. This is relevant to interpretation: more conservative transaction-cost assumptions weaken the edge but do not, on the authors' own analysis, eliminate the historical result.

## 3 Data, Engines, and Replication Protocol

## 3.1 Independent dataset

The primary replication uses SPY one-minute regular-session data exported from TradeStation, covering 3 January 2000 through 14 August 2026 and containing approximately 2.6 million bars. QQQ data over a comparable span are used as an external generalization check. The original paper instead uses one-minute IQFeed data from May 2007 through April 2024. The data-source difference is therefore nontrivial: agreement cannot be attributed to simply rerunning the authors' original database.

3

<!-- page: 5 -->

## Page 5

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

## 3.2 Three distinct engine states

A central lesson of the audit is that “the strategy" is not a single immutable code path. We therefore preserve three distinct states:

**[table]**

Table 1: Engine states preserved in the research history.
<table><tr><td>Component</td><td>PRE_VWAP_FIX</td><td>CORRECTED</td><td>selected specification</td></tr><tr><td>VWAP</td><td>Close-only</td><td>Typical price</td><td>Typical price</td></tr><tr><td>VWAP confirmation at entry</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Dividend adjustment</td><td>Off</td><td>On</td><td>On</td></tr><tr><td>Actual leverage hard cap</td><td>No</td><td>No</td><td>Yes, 4x</td></tr><tr><td>Minimum commission</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Early-close session fix</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Role</td><td>Historical search state</td><td>Historical search state</td><td>Frozen final engine</td></tr></table>

The PRE_VWAP_FIX state is retained because 31 genuine search trials were observed before the reference-code discrepancy was discovered. The CORRECTED state contains 49 subsequent SPY search trials. The final engine adds operational corrections after the parameter search: a true 4x leverage cap applied after all size multipliers, minimum commission handling, and correct liquidation on shortened sessions These distinctions are essential for reconstructing the true multiple-testing history rather than retroactively pretending that all trials were run under the final engine.

## 3.3 Replication findings and unresolved paper-code convention

Our first implementation, based only on the textual description, produced a broadly similar but materially weaker flagship result. Line-by-line comparison with the authors' published Python notebook identified two economically meaningful discrepancies: close-only VWAP instead of typical-price VWAP, and band-only entry without VWAP confirmation. Correcting those two issues closes almost the entire gap.

**[table]**

Table 2: Flagship strategy: published result versus independent replication on May 2007–April 2024.
<table><tr><td>Metric</td><td>ZAB paper</td><td>Independent replication</td></tr><tr><td>Total return</td><td>1,985%</td><td>1,989.0%</td></tr><tr><td>Annualized return</td><td>19.6%</td><td>19.6%</td></tr><tr><td>Annualized volatility</td><td>14.3%</td><td>14.4%</td></tr><tr><td>Sharpe Ratio</td><td>1.33</td><td>1.317</td></tr><tr><td>Hit ratio</td><td>43.0%</td><td>43.6%</td></tr><tr><td>Maximum drawdown</td><td>-25.0%</td><td>-24.5%</td></tr><tr><td>Trades</td><td>7,668</td><td>7,742</td></tr></table>

The closest paper-matching replication omits the dividend adjustment because this produces the closest match to the official 1,985% figure. Applying the dividend adjustment found in the authors’ public code yields approximately 1,965.4%, Sharpe 1.314, and 7,700 trades. The residual paper-versus-code convention is documented rather than forced away.

4

<!-- page: 6 -->

## Page 6

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

The replication is therefore sufficiently close to support the conclusion that the paper's central historical result is not dependent on an idiosyncratic data vendor or on our particular implementation. The historical phenomenon is also present in independent data.

## 4 Post-Publication Evidence

## 4.1 Recreating the authors'2025 update

The September 2025 edition adds FAQ Q24, “How has the strategy performed since the paper was published?’ [1], and plots the strategy against SPY with the post-publication region shaded in green. We reproduce the same visual convention using the independent TradeStation series and extend the endpoint to 14 August 2026. The extension adds a second shade because the authors’ latest published update stops at 29 August 2025: green denotes the period covered by their Q24 update, while light red denotes the subsequent interval for which no author update was available at the time of this study

Intraday Momentum Strategy - Independent Update
Figure 1: Independent recreation and extension of the authors' Q24 chart. The blue line is the frozen independent replication of the published strategy and the red line is SPY buy-and-hold. Green marks post-publication observations covered by ZAB's Q24 update through 29 August 2025; light red marks the subsequent observations through 14 August 2026. The vertical dashed line is the first-version publication date, 10 May 2024.

The independent series also reproduces the authors' own updated annual figures with striking accuracy:

5

<!-- page: 7 -->

## Page 7

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

**[table]**

Table 3: Authors' Q24 update versus independent TradeStation replication.
<table><tr><td>Period</td><td>ZAB Q24</td><td>Independent replication</td><td>Difference</td></tr><tr><td>2024 full year</td><td>32.2%</td><td>31.8%</td><td>-0.4 pp</td></tr><tr><td>2025 Jan-Aug</td><td>1.0%</td><td>1.4%</td><td>+0.4 pp</td></tr><tr><td>2025 full year</td><td></td><td>-2.6%</td><td></td></tr><tr><td>2026 through 14 Aug</td><td></td><td>-4.2%</td><td></td></tr></table>

The match through August 2025 is important. It provides a second, chronologically post-publication replication target beyond the original 2007–2024 window. At the monthly level, all 20 independently reconstructed returns from January 2024 through August 2025 lie within 0.65 percentage points of the authors Q24 values, with a mean absolute difference of approximately 0.25 percentage points. The month-by-month reconciliation is included in the reproducibility package. The result also forces a correction to an overly coarse interpretation of our own earlier analysis. Pooling all observations from May 2024 through August 2026 gives a Sharpe Ratio near 0.35, but that single number hides two qualitatively different subperiods.

## 4.2 Disaggregating the post-publication path

Table 4 separates the period covered by the authors' latest Q24 update from the subsequent interval. Because Q24 reports monthly returns, we show both a Q24-comparable convention beginning 1 May 2024 and an exact publication convention beginning with the first trading session after the paper's 10 May 2024 first-version date.

**[table]**

Table 4: Post-publication performance disaggregated by information set.
<table><tr><td>Window</td><td>Total return</td><td>Sharpe</td><td>Vol.</td><td>MDD</td><td>Interpretation</td></tr><tr><td>1 May 2024–29 Aug 2025</td><td>19.3%</td><td>1.057 13.4%</td><td></td><td>-9.4%</td><td>Q24-comparable monthly convention; 16 calendar months and includes seven trading sessions before first publica-</td></tr><tr><td>13 May 2024–29 Aug 2025</td><td></td><td></td><td></td><td>23.3% 1.284 13.3% -9.4%</td><td>tion. Exact post-publication convention, starting on the first trading session after 10 May 2024.</td></tr><tr><td>2 Sep 2025–14 Aug 2026</td><td></td><td></td><td></td><td>-8.1% -0.461 16.4% -17.4%</td><td>Subsequent weak stretch, not covered by the authors&#x27; latest published Q24 update.</td></tr><tr><td>1 May 2024–14 Aug 2026</td><td>9.7%</td><td></td><td></td><td></td><td>0.35 14.7% -21.0% Pooled statistic used in our earlier anal- ysis; descriptively correct but econom- ically heterogeneous.</td></tr></table>

This disaggregation materially changes the narrative. The strategy did not immediately weaken after publication. The independent reconstruction shows a strong first post-publication phase that is consistent with the authors' own public update, followed by a much weaker roughly twelve-month stretch beginning after August 2025. The pooled Sharpe of 0.35 remains numerically correct for May 2024–August 2026, but it should not be interpreted as evidence of continuous or immediate publication-induced decay.

Figure 2 removes the optical effect created by 17 years of compounding and shows the recent period on a rebased scale. The two background regimes correspond to the information available in the authors’ last

6

<!-- page: 8 -->

## Page 8

“Beat the Market" Revisited

Independent Replication and Statistical Audit

public update and the later observations added by this study.

2023-2026 Detail: Reconciliation of Post-Publication Performance
Figure 2: Recent-period detail, rebased to 100 on 3 January 2023. The strategy performs strongly through the authors 29 August 2025 update and weakens materially thereafter. This is a more informative decomposition than a single pooled May 2024–August 2026 statistic.

For continuity with the earlier analysis, Table 5 still reports the broad pre-paper, paper-window, and pooled post-paper partitions under the frozen baseline convention: corrected typical-price VWAP, joint band-plus-VWAP entry confirmation, dividend-adjusted gap anchor, and no later operational hard cap.

**[table]**

Table 5: Published-strategy replication by broad subperiod under baseline.
<table><tr><td>Period</td><td>Total return</td><td>CAGR</td><td>Sharpe</td><td>MDD</td></tr><tr><td>Pre-paper: Jan 2000-Apr 2007</td><td>70.1%</td><td>7.6%</td><td>0.53</td><td>-20.5%</td></tr><tr><td>Paper window: May 2007–Apr 2024</td><td>1965.7%</td><td>19.5%</td><td>1.314</td><td>-24.6%</td></tr><tr><td>Pooled post-paper: May 2024–Aug 2026</td><td>9.7%</td><td>4.1%</td><td>0.35</td><td>-21.0%</td></tr><tr><td>Full valid sample: Jan 2000–Aug 2026</td><td>3753.5%</td><td>14.7%</td><td>0.996</td><td>-24.6%</td></tr></table>

The longer historical sample still weakens any claim that 1.33 is a stationary unconditional Sharpe estimate: the pre-paper Sharpe is only 0.53, the paper-window Sharpe is approximately 1.31, and the most recent twelve-month stretch is negative. What changes is the causal story. The evidence now supports regime dependence and recent weakening, not a simple claim that public disclosure immediately caused the edge to disappear.

The rolling risk-adjusted return in Figure 3 is consistent with that interpretation. The post-publication period begins from a historically strong state, stays strong well into the authors' public update window, and then declines sharply during late 2025–2026.

7

<!-- page: 9 -->

## Page 9

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

Rolling 252-Session Sharpe - Published Strategy
Figure 3: Rolling 252-session annualized Sharpe Ratio of the published strategy. Green denotes the post-publication period covered by the authors' latest Q24 update; light red denotes the subsequent stretch. The recent decline is economically material, but the available interval is too short to identify permanent alpha decay.

## 5 Parameter Robustness, PBO, and Generalization

## 5.1 The 25-configuration grid

To evaluate whether the default lookback and Volatility Multiplier (VM) sit on a stable plateau or on an isolated spike, the historical PRE_VWAP_FIX engine was reconstructed and the original 5-by-5 parameter grid was recovered in full. The lookbacks are {7, 14, 21, 30, 60} sessions and VM values are {0.7, 1.0, 1.3, 1.6, 2.0}.

8

<!-- page: 10 -->

## Page 10

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

Figure 4: Annualized Sharpe Ratio on the 25-configuration common-valid grid. The solid blue box marks the paper default (lookback 14, VM 1.0); the dashed red box marks the highest-Sharpe grid point (lookback 30, VM 1.3). The broad
\mathbf { V M } \approx 1 . 0 \mathbf { - } 1 . 6
plateau argues against a single fragile optimum, while the movement of the optimum across subperiods argues against treating any one point as permanent.

The grid produces an important distinction. The existence of a broad profitable region is evidence against a purely accidental isolated optimum. Yet the best point changes across time and market regimes. Long lookbacks tend to perform better during persistent crisis trends, while shorter lookbacks fare better in choppier periods. This is exactly the form of instability that a visually appealing full-sample heatmap can hide.

## 5.2 Probability of Backtest Overfitting

We apply Combinatorially Symmetric Cross-Validation (CSCV) following Bailey, Borwein, Lopez de Prado, and Zhu [10]. The 25-strategy panel is divided into S = 10 contiguous blocks, producing
{ \binom { 1 0 } { 5 } } = \bar { 2 5 2 }
train/test partitions. In each split, the best in-sample strategy is selected and ranked out-of-sample. The Probability of Backtest Overfitting (PBO) is the proportion of splits in which the selected in-sample winner ranks at or below the OOS median under the historical
\lambda \leq 0
convention.

**[table]**

Table 6: CSCV/PBO on the reconstructed 25-strategy grid.
<table><tr><td>Sample convention</td><td>PBO <eq>( \lambda \leq 0 )</eq></td><td>PBO <eq>( \lambda &lt; 0 )</eq></td><td>Common start</td></tr><tr><td>Historical replication</td><td>38.49%</td><td>29.37%</td><td>3 Jan 2000, warm-up zeros retained</td></tr><tr><td>Common-valid</td><td>40.87%</td><td>33.33%</td><td>30 Mar 2000</td></tr></table>

A PBO near 39–41% is neither a clean bill of health nor a rejection of the strategy class. It says that the

9

<!-- page: 11 -->

## Page 11

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

exact in-sample winner is unstable often enough to matter. The conclusion is therefore more nuanced than the parameters are not optimized because 14 and 1.0 are not the best." There is a real edge region, but the exact best parameterization is not temporally invariant.

## 5.3 Cross-asset generalization: QQQ success, IWM adverse evidence

As a separate robustness check, the corrected flagship rules are applied without parameter recalibration to other U.S. equity ETFs. QQQ is a clear positive result: over the full available history, the base specification produces approximately 3,572% total return, a 14.5% annualized return, a Sharpe Ratio of 0.987, and a -30.3% maximum drawdown. This is remarkably close to SPY's own full-history Sharpe and supports the proposition that the base mechanism is not unique to SPY.

The extension also preserves a deliberately adverse validation on IWM (Russell 2000 ETF). The unmodified base engine produces only Sharpe 0.450 over the ledger's 2004–2026 validation window, and the trial was explicitly classified ADVERSE_EVIDENCE; no attempt was made to optimize IWM after that result Because the exact IWM daily return series is not part of the frozen SPY return-matrix package, we do not import finer subperiod claims into the statistical audit. The overall result is nevertheless useful: generalization is heterogeneous rather than universal.

A second qualification is equally important. SPY-specific improvements do not automatically transfer to QQQ. The frozen ledger records QQQ Sharpe 0.987 for the unmodified base engine, versus 0.809 for the SPY-derived asymmetric Config J, 0.913 for the SPY relative-volume sizing recipe, and 0.967 for the SPY performance-reversion overlay. None improves on the QQQ base Sharpe. This is direct evidence that the base mechanism can generalize while the optimization layers remain asset-specific.

Figure 5: Cross-asset evidence preserved in the frozen ledger. Left: full-history/base-validation Sharpe for SPY, QQQ, and IWM. Right: applying SPY-selected layers to QQQ does not improve on QQQ's unmodified base specification IWM is reported as adverse evidence and was not subsequently optimized.

These independent checks do not verify the broader FAQ claims [1] that the same rules work across many stocks, ETFs, or 33 futures markets; those remain author-reported evidence. They do, however, sharpen the conclusion: the published mechanism shows meaningful transfer to another large-cap index ETF, but neither universal cross-asset validity nor universal transfer of our SPY-specific tuning is supported.

10

<!-- page: 12 -->

## Page 12

“Beat the Market"' Revisited

Independent Replication and Statistical Audit

## 6 Systematic Search for Extensions

## 6.1 Research discipline and search universe

The extension stage was explicitly adaptive: each family of ideas was motivated by the observed behavior of the previous stage. To prevent the final result from being presented as if it emerged from a single predeclared hypothesis, every SPY alternative that could plausibly have affected selection was logged. The final search universe contains 80 SPY trials: 31 under PRE_VWAP_FIX and 49 under CORRECTED. The 31 pre-fix trials comprise the 25-point grid, three asymmetric short filters, two trade-cap experiments, and one lookback retuning experiment. The 49 corrected trials cover the families summarized below.

**[table]**

Table 7: Corrected-engine search families. All failures remain part of the multiple-testing count.
<table><tr><td>Family</td><td>Trials</td><td>Research question</td><td>Outcome</td></tr><tr><td>Asymmetric short filter</td><td>4</td><td>Should short entries require wider bands Adopted and/or smaller size?</td><td></td></tr><tr><td>Binary relative-volume filter</td><td>4</td><td>Should low-participation signals be ex- Rejected cluded?</td><td></td></tr><tr><td>Continuous relative-volume sizing</td><td>2</td><td>Should size scale smoothly with intraday Adopted participation?</td><td></td></tr><tr><td>VIX sizing</td><td>2</td><td>Should implied volatility replace or over- Rejected lay realized-vol sizing?</td><td></td></tr><tr><td>Persistence filter</td><td></td><td>Should a breakout persist for two check- Rejected points before entry?</td><td></td></tr><tr><td>Profit-lock stops</td><td>5</td><td>Can gains be protected more aggres- Rejected sively after favorable moves?</td><td></td></tr><tr><td>VWAP-dominance rules</td><td>5</td><td>Are VWAP-binding signals structurally Continuous discount adopted better than band-binding signals?</td><td></td></tr><tr><td>Intraday decay</td><td>2</td><td>Should position size decay later in the Rejected session?</td><td></td></tr><tr><td>Risk controls</td><td>7</td><td>Do daily loss limits, per-trade caps, or Rejected hard breakeven improve robustness?</td><td></td></tr><tr><td>Whipsaw regime overlays</td><td>3</td><td>Can recent trade-count intensity forecast Rejected choppy regimes?</td><td></td></tr><tr><td>Performance overlay</td><td>14</td><td>Should size respond to the strategy&#x27;s Reversal overlay adopted own recent performance?</td><td></td></tr></table>

The selected research path should not be mistaken for a monotonic maximization of full-sample Sharpe Figure 6 shows the actual sequence. Config J has the highest Sharpe among some intermediate stages; later layers were retained because they improved multi-window robustness, recent-period behavior, or the risk/return trade-off, not because every added layer mechanically increased the single full-sample Sharpe statistic.

11

<!-- page: 13 -->

## Page 13

“Beat the Market"' Revisited

Independent Replication and Statistical Audit

Evolution of the Selected Specification (not a monotonic Sharpe optimization)
Figure 6: Evolution of the selected specification. The path is intentionally non-monotonic in full-sample Sharpe: selection used a multi-window robustness standard and explicit risk/return trade-offs, not a greedy maximization of the displayed scalar. The final bar is the audited frozen candidate after operational corrections.

## 6.2 Asymmetric short filter

The long and short legs are both profitable historically, but the long leg is materially stronger: in the frozen baseline, the long-only Sharpe is approximately 0.90 versus 0.56 for short-only. This motivates asymmetric entry thresholds and short sizing. The progression under the corrected engine is shown below.

**[table]**

Table 8: Asymmetric short-filter research path (research-engine metrics).
<table><tr><td>Configuration</td><td>Sharpe</td><td>Total return</td><td>MDD</td></tr><tr><td>Symmetric baseline, VM=1.0</td><td>0.994</td><td>3,753.5%</td><td>-24.6%</td></tr><tr><td>Symmetric VM=1.3</td><td>1.184</td><td>4,870.1%</td><td>-17.5%</td></tr><tr><td><eq>\mathrm{VM}_{L}=1.3, \mathrm{VM}_{S}=1.6</eq></td><td>1.258</td><td>4,639.4%</td><td>-19.9%</td></tr><tr><td><eq>+ \mathrm { s h o r t } \; \mathrm { s i z e } = 0 . 7 5</eq></td><td>1.314</td><td>3,145.5%</td><td>-16.2%</td></tr></table>

The final row, called “Config J’ in the research ledger, becomes the base for subsequent tests. This is not simply a higher-threshold short filter; it is an explicit admission that the two directional legs do not have equal historical quality

## 6.3 Continuous relative-volume sizing

A binary volume filter initially seemed attractive: exclude breakouts when cumulative volume participation is low. It failed. Every tested threshold reduced total return, and aggressive thresholds nearly eliminated the strategy. The failure suggested that participation contains useful information but should not be converted into a hard yes/no gate.

The successful formulation is continuous. Let cumulative relative volume at checkpoint h be

R V _ { t , h } = \frac { C u m V o l _ { t , h } } { \frac { 1 } { 1 4 } \sum _ { i = 1 } ^ { 1 4 } C u m V o l _ { t - i , h } } .\tag{10}

12

<!-- page: 14 -->

## Page 14

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

The size multiplier is

s_{t,h}^{RV} = \min \left(1.5, \max(0.5, RV_{t,h})\right).\tag{11}

This specification improved total return in all four predeclared validation windows (2000–2012, 2013–2020, 2021–2024, and 2025–2026) without materially increasing average leverage. It is the cleanest modification found in the search.

## 6.4 VWAP dominance as a continuous discount

The 2024–2026 diagnostics suggest that signals are weaker when the Noise Area boundary, rather than VWAP, is the binding component of the dynamic stop. A binary rule requiring VWAP to be binding improves the recent period but reduces historical total return by roughly
9 0 \%
, demonstrating that many early band-dominant signals are essential to the historical edge

The adopted compromise retains those signals but discounts their size:

s_{t,h}^{D}=\left\{\begin{aligned} & 1, & & \text { VWAP is the binding stop component, } \\ & 0.7, & & \text { the Notice Area band is binding. } \end{aligned}\right.\tag{12}

This is explicitly a trade-off rather than a free improvement. Stronger discounts improve the recent window further but reduce long-run terminal wealth substantially

## 6.5 Performance-reversal overlay

The intuitive version of a performance overlay—increase size after good recent strategy performance and decrease after poor performance—failed. Direct measurement of the strategy's own trailing-versus-forward performance revealed why: over the long historical subperiods, recent strategy performance tends to mean-revert rather than persist.

The selected overlay therefore reverses the intuitive logic. Let

R _ { t - 1 } ^ { 3 0 } = \sum _ { i = 1 } ^ { 3 0 } r _ { t - i } ^ { s h a d o w } ,\tag{13}

where
r ^ { s h a d o w }
is the return of the same configuration without the overlay and the signal is shifted one full day to avoid look-ahead. The multiplier is

s_{t}^{P}=\begin{cases}0.9, & R_{t-1}^{30}>0, \\ 1.1, & R_{t-1}^{30} \leq 0,\end{cases}\tag{14}

with a neutral factor of 1.0 during the 30-day warm-up. More aggressive reversal factors yield higher in-sample Sharpe but progressively lower terminal wealth. The chosen 0.9/1.1 setting deliberately stays near the broad calibration plateau rather than selecting the numerical maximum.

## 7 What Did Not Work

A credible extension study should be at least as explicit about failures as successes. Table 9 summarizes the ideas that did not meet the multi-window standard.

13

<!-- page: 15 -->

## Page 15

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

**[table]**

Table 9: Rejected modifications and why they failed.
<table><tr><td>Modification</td><td>Finding</td></tr><tr><td>Binary relative-volume filter</td><td>Higher Sharpe at some thresholds came at the cost of lower total return in every major validation window; high thresholds removed most of the strategy.</td></tr><tr><td>VIX replacement sizing</td><td>The strategy became systematically under-exposed; implied volatility appears to embed a structural risk premium that is not equivalent to realized-volatility targeting.</td></tr><tr><td>VIX overlay</td><td>Improved three of four historical windows but failed to solve the 2025–2026 deteriora- tion.</td></tr><tr><td>Two-checkpoint persistence</td><td>Reduced false signals in some periods but roughly halved return in important 2013–2024 windows.</td></tr><tr><td>Profit locks</td><td>Nearly no incremental benefit; the existing current-band/VWAP stop already performs much of this function.</td></tr><tr><td>Hard breakeven</td><td>Increased trade count by approximately 23% and cut off genuine recoveries; both costs and premature exits worsened results.</td></tr><tr><td>Daily loss limits / trade caps</td><td>Small recent-period improvements did not compensate for lower full-sample Sharpe and return.</td></tr><tr><td>Per-trade loss caps</td><td>Essentially no effect in the historically reconstructed configuration.</td></tr><tr><td>Whipsaw regime overlay</td><td>Recent trade-count intensity did not persist strongly enough from day to day; all tested versions worsened the four-window evaluation.</td></tr><tr><td>ter</td><td>Binary VWAP-dominance fil- Helped the recent sample but removed the majority of historical edge; the continuous discount was superior.</td></tr><tr><td>Intraday decay</td><td>Lowered both Sharpe and return.</td></tr><tr><td>Intuitive performance momen- tum overlay</td><td>Failed; the strategy&#x27;s own long-history performance exhibited mean reversion, motivat- ing the inverted rule instead.</td></tr></table>

Two author FAQ results are consistent with these failures. ZAB report that conditioning short trades on high VIX does not improve compounded profitability and that restricting shorts to bear-market states defined by long-term simple moving averages sacrifices substantial historical profit. They also test a VWAP-only trailing stop: the Sharpe Ratio falls from 1.35 to 1.17 and maximum drawdown increases from 25% to 27%. The independent search therefore reaches a similar conclusion by a different route: seemingly obvious ways to “clean up" the strategy often remove profitable trend exposures together with the unwanted noise.

## 8 Diagnosing the 2024–2026 Whipsaw

The post-publication weakening motivated trade-level reconstruction. Over May 2024–August 2026 in the diagnostic sample, 110 trades were winners with an average return near +0.41%, 72 were approximately breakeven, and 167 were losers averaging about -0.22%. Of the losing trades, 91% exited through the dynamic stop and the remainder reached the forced session close while losing. The losses were not merely a transaction-cost artifact: the exit price crossed through the entry price in every losing case.

The recurrent pattern is a classic whipsaw. A breakout entry is directionally plausible, price pulls back enough to cross the dynamic band/VWAP stop, and then the original trend resumes after the position has been closed. Tightening the stop appears attractive ex post, but the same pullback shape also occurs before genuine recoveries. The attempted mitigations—hard breakeven, trade caps, daily loss limits, and choppy-regime overlays—generally provide benefits that are too small to compensate for the performance they forgo elsewhere.

This matters for interpretation. The post-publication decay is not well described as “the strategy suddenly has no signal." Instead, the signal appears to remain present on some days, but the timing structure

14

<!-- page: 16 -->

## Page 16

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

produces more failed entries and repeated stop-outs. That is compatible with either a temporary regime change or structural adaptation. The available two-year post-publication interval does not distinguish those explanations reliably.

## 9 The Frozen Candidate

## 9.1 Rules

The final selected specification is the product of the documented search, not a claim that every retained modification is structurally causal. Its frozen parameters are:

**[table]**

Table 10: Frozen selected specification specification.
<table><tr><td>Component</td><td>Frozen rule</td></tr><tr><td>Noise Area lookback</td><td>14 sessions</td></tr><tr><td>Long VM</td><td>1.3</td></tr><tr><td>Short VM</td><td>1.6</td></tr><tr><td>Short size multiplier</td><td>0.75</td></tr><tr><td>Relative-volume sizing</td><td>clip(RV, 0.5, 1.5)</td></tr><tr><td>Band-dominant size discount</td><td>0.7</td></tr><tr><td>Performance overlay window</td><td>30 sessions</td></tr><tr><td>After positive trailing performance</td><td>0.9 multiplier</td></tr><tr><td>After non-positive trailing performance 1.1 multiplier</td><td></td></tr><tr><td>Maximum actual leverage</td><td>hard cap at 4.0x after all size multipliers</td></tr><tr><td>Other operational corrections</td><td>dividend-aware gap anchor, minimum commission, shortened-session liquidation</td></tr></table>

In compact form, before the final leverage cap, long and short requested exposure can be written as

\mathcal { Q } _ { t , h } ^ { L } = \mathcal { Q } _ { t } ^ { b a s e }   s _ { t , h } ^ { R V } s _ { t , h } ^ { D } s _ { t } ^ { P } ,\tag{15}

Q _ { t , h } ^ { S } = 0 . 7 5   Q _ { t } ^ { b a s e }   s _ { t , h } ^ { R V } s _ { t , h } ^ { D } s _ { t } ^ { P } .\tag{16}

The engine then enforces actual leverage
\leq 4
after all multipliers, avoiding the subtle error of capping only the base volatility multiplier.

## 9.2 Frozen result

The final audit stores 4,170 entries and 8,340 entry/exit trade-log rows, with zero entries above the 4x leverage cap. The backtest reference object reports a total return of 2110.6%, a maximum drawdown of -14.8%, and a trade hit ratio of 44.4%. For the statistical audit, the 15-session model warm-up is removed, yielding an annualized Sharpe Ratio of 1.274, CAGR of 12.4%, and volatility of 9.5% from 25 January 2000 through 14 August 2026.

15

<!-- page: 17 -->

## Page 17

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

**[table]**

Table 11: Full-history comparison of the frozen baseline and final candidate.
<table><tr><td>Metric</td><td>baseline</td><td>selected specification</td></tr><tr><td>Total return</td><td>3753.5%</td><td>2110.6%</td></tr><tr><td>CAGR</td><td>14.7%</td><td>12.4%</td></tr><tr><td>Annualized volatility</td><td>15.0%</td><td>9.5%</td></tr><tr><td>Sharpe Ratio</td><td>0.996</td><td>1.274</td></tr><tr><td>Maximum drawdown</td><td>-24.6%</td><td>-14.8%</td></tr><tr><td>Trade hit ratio</td><td>42.5%</td><td>44.4%</td></tr><tr><td>Trade-log rows</td><td>12,638</td><td>8,340</td></tr></table>

The candidate does not maximize terminal wealth. It intentionally gives up a large fraction of compounded return in exchange for lower volatility and a materially shallower drawdown. Figure 7 makes that trade-off visible.

Figure 7: Full-history equity curves from $100, 000, plotted on a logarithmic scale. selected specification is smoother and has a smaller maximum drawdown than the baseline, but lower terminal wealth. Because the candidate was selected using the same historical record, this curve is retrospective evidence only.

The candidate's May 2024–August 2026 retrospective return is approximately 25.9% with a Sharpe Ratio near 0.97. Those numbers are not treated as post-selection validation because this same interval influenced model development. The distinction between chronological post-paper data and epistemologically clean out-of-sample data is maintained throughout the analysis.

16

<!-- page: 18 -->

## Page 18

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

## 10 Multiple Testing and Statistical Audit

## 10.1 Why the search count is 80

A preliminary version of the research process used a coarse count of 27 family-by-asset clusters as a proxy for the number of trials. That approach was discarded. A 25-point grid cannot be treated as one test merely because all points share a family label, and bug fixes or diagnostic reruns should not be counted as strategy alternatives if they were not selection candidates.

The final rule is therefore explicit:

N _ { r a w , S P Y } = 8 0 = 3 1 _ { P R E \_ V W A P \_ F I X } + 4 9 _ { C O R R E C T E D } ,\tag{17}

where a trial counts only if it is a SPY SEARCH observation marked as selection-relevant. Of the 80, daily return series were reconstructed for 70. The remaining 10—seven CORRECTED and three PRE_VWAP_FIX remain documented as unresolved historical reconstructions or historical target conflicts. Importantly, they still count toward N because the tests were actually observed during research.

## 10.2 Deflated Sharpe Ratio

The Deflated Sharpe Ratio (DSR) adjusts the observed Sharpe for multiple testing and return non-normality [11]. When excess kurtosis κ is used, the asymptotic denominator must include

1 - \gamma _ { 3 } S R + \frac { \kappa + 2 } { 4 } S R ^ { 2 } ,\tag{18}

not
\kappa S R ^ { 2 } / 4
. The latter was an earlier implementation error discovered during the audit. Correcting it has negligible numerical impact in this specific dataset, but the corrected form is frozen.

For the 25-point grid, the best reconstructed strategy is lookback 30 / VM 1.3, with Sharpe 1.196. Its DSR is 99.999995%. This result applies to the grid winner, not automatically to the final candidate.

For selected specification, the primary DSR retains
N = 8 0
but estimates the dispersion of Sharpe ratios only from 78 full-history-comparable trials, excluding two trials whose preserved Sharpe was measured only over 2024–2026. Candidate moments and sample length are computed from the model-ready date, 25 January 2000. The principal result is

D S R _ { \mathrm { s e l e c t e d } } = 9 9 . 9 9 9 9 8 6 7 9 6 \%\tag{19}

with a preserved-only sensitivity of 99.999984715%.

## 10.3 Effective dimensionality as a sensitivity, not a discount

The 70 reconstructed strategy return series are highly correlated, with average daily-return correlation near 0.835. A direct eigenvalue participation-ratio calculation on raw returns produces an effective dimension close to 1.4, which would be dangerously optimistic if substituted for the 80 actually observed research alternatives.

As a sensitivity exercise, we instead use synchronized moving-block bootstrap resampling and calculate the correlation matrix of the estimated Sharpe ratios across strategies. The corresponding effective dimensions are 1.527, 1.561, and 1.685 for block lengths of 10, 20, and 60 sessions. These values are reported descriptively only. Replacing
N = 8 0
with
N _ { e f f } \approx 1 . 5 6
would mechanically make the DSR even larger, because it assumes away most multiple testing. That is the opposite of a conservative correction.

17

<!-- page: 19 -->

## Page 19

“Beat the Market"' Revisited

Independent Replication and Statistical Audit

## 10.4 Why no single PBO is reported for the full ledger

PBO/CSCV requires a flat matrix of genuinely comparable strategies over the same observations. The full 80-trial ledger violates that structure: it combines two engine states, heterogeneous families, adaptive sequencing, different warm-up requirements, and 10 missing exact daily series. Forcing all 80 into one CSCV matrix would produce a precise-looking number without the method's underlying exchangeability assumptions. We therefore report PBO only where it is structurally defensible: the 25-point grid.

## 11 Revisiting the Authors' 2025 FAQ Claims

The expanded 2025 FAQ materially improves the transparency of the original paper and is central to a fair assessment.

Simplified published model. In Q11 the authors explicitly state that the published strategy is a simplified model, not a ready-to-use trading system, and that they trade a slightly modified version in their own accounts. Accordingly, this paper evaluates the published and reproducible rules. It cannot test undisclosed private modifications.

Over-optimization. In Q14 the authors argue that the model is unlikely to be over-optimized because it has few main parameters and because the paper defaults are not the ex-post Sharpe-maximizing choices. That is useful evidence, but it is not by itself a multiple-testing correction. Our 25-point PBO of 38.49%–40.87% adds a more direct result: the grid contains a broad profitable plateau, but the exact winner is unstable across samples.

Market impact. In Q15 the authors report that an I-Star impact model lowers Sharpe from 1.33 to 1.17 while preserving strong historical profitability. Our work does not independently reproduce the I-Star implementation, so the 1.17 figure remains author-reported. Nevertheless, it weakens the hypothesis that the entire historical result is an artifact of the paper's simple slippage assumption.

Alpha decay. In Q16 the authors state that they believe alpha-decay risk is minimal, citing SPY liquidity, trend-following structure, and institutional constraints. Our disaggregated evidence is more supportive of that claim than the pooled May 2024–August 2026 Sharpe of 0.35 initially suggested: the strategy performs strongly through the authors' August 2025 update (Sharpe 1.057 under the Q24-comparable convention, or 1.284 from the exact post-publication start). The caution arises from the subsequent interval, which returns -8.1% with Sharpe -0.461. This is evidence of nonstationarity and recent weakness, not proof that publication caused permanent alpha decay.

Short-side filters and volatility. Q19–Q21 report that VIX does not materially explain short-trade profitability and that restricting shorts to high-volatility or bear-market states sacrifices historical return. Our own VIX and regime filters similarly fail to solve the recent weakness cleanly.

VWAP-only stop. Q22 shows that removing the current-band component and using VWAP alone reduces risk-adjusted performance. Our binary VWAP-dominance filter fails for a related reason: too much of the historical edge resides in signals that begin before VWAP becomes the dominant stop component.

Q24 post-publication update. The close match between the authors'2024/2025 update and our independent reconstruction is one of the strongest replication results in this study. It shows that the first post-publication phase was genuinely strong rather than a discrepancy between feeds. It also makes the subsequent September 2025–August 2026 weakening difficult to dismiss as a data-vendor artifact. The methodological lesson is that a pooled post-publication statistic can obscure both facts simultaneously

18

<!-- page: 20 -->

## Page 20

“Beat the Market" Revisited

Independent Replication and Statistical Audit

## 12 Limitations and Prospective Protocol

The evidence is strong, but several limitations materially restrict interpretation.

First, the search was adaptive rather than preregistered. DSR adjusts for observed multiple testing but cannot fully eliminate researcher degrees of freedom when later hypotheses were generated after inspecting earlier results.

Second, 10 of the 80 SPY search alternatives could not be reconstructed exactly. They are not removed from the multiple-testing count, but their missing daily series prevent inclusion in any panel-based CSCV extension.

Third, the 2024–2026 period is chronologically post-paper but not a clean holdout for selected specification. Those data were repeatedly inspected and influenced which modifications were retained. Candidate post-2024 metrics are therefore descriptive, not OOS evidence.

Fourth, the published strategy and the frozen candidate use different engines in small but economically relevant ways. The candidate's actual 4x cap, minimum commission, and early-close handling were introduced after the parameter search. The final statistical audit intentionally evaluates the candidate as frozen rather than retroactively rewriting the historical search.

Fifth, cross-asset evidence remains limited. QQQ is independently supportive and IWM is preserved as adverse evidence, but the authors’ much broader FAQ claims across multiple ETFs, equities, and 33 futures markets are not independently reproduced here and remain separate evidence.

The prospective protocol follows directly from these limitations. Parameters are frozen. No rule, threshold, or overlay should be modified in response to future performance without starting a new research version and resetting the epistemic status. New sessions after the freeze constitute the first genuinely prospective evidence for selected specification.

## 13 Conclusion

The central result of this study is not that the Beat the Market strategy fails. The historical backtest is independently reproducible. On the authors' official 2007–2024 window, a separately implemented engine on TradeStation data produces 1,989% total return and Sharpe 1.317, nearly matching the published 1,985% and 1.33. The authors' own 2025 post-publication update is also independently reproduced to within a few tenths of a percentage point.

The central qualification is temporal stability, but the timing matters. The pooled May 2024–August 2026 baseline Sharpe of 0.35 initially suggested broad post-publication deterioration. A finer decomposition corrects that interpretation: the first 16 calendar months in the Q24-comparable window return 19.3% with Sharpe 1.057, closely matching the authors' own update, whereas the subsequent September 2025–August 2026 stretch returns -8.1% with Sharpe -0.461. The evidence therefore supports a real historical edge with substantial regime sensitivity and uncertain current strength, but not a claim of immediate publication-induced decay.

The extension search finds no universal repair. Many intuitive mechanisms fail: VIX filters, persistence, profit locks, hard breakeven, daily loss limits, trade caps, whipsaw-regime overlays, intraday decay, and binary VWAP filters all sacrifice too much elsewhere. A smaller set of modifications—asymmetric short treatment continuous relative-volume sizing, a VWAP-dominance size discount, and a weak performance-reversal overlay—improves the historical risk-adjusted profile. The resulting selected specification posts a Sharpe Ratio of 1.274 and maximum drawdown of -14.8% over the full historical sample, but its attractive post-2024 behavior cannot be called validation because those data participated in selection. Cross-asset evidence adds another boundary condition: the base engine transfers well to QQQ but only weakly to IWM, and the

19

<!-- page: 21 -->

## Page 21

“Beat the Market"' Revisited

Independent Replication and Statistical Audit

SPY-selected layers do not improve QQQ's base Sharpe. The edge should therefore be treated as a mechanism with heterogeneous asset dependence, not a universal recipe.

The statistical audit reinforces the same distinction. The grid-level PBO is moderate rather than extreme, the DSR remains extraordinarily high even after counting 80 observed SPY alternatives, and the broad historical edge is difficult to explain as pure multiple-testing noise. Yet none of those calculations can manufacture a holdout that no longer exists.

The scientifically defensible status is therefore:

## selected specification = retrospectively significant edge, not prospectively validated.

The next methodological milestone is not another retrospective calculation. It is the passage of time: accumulating performance under frozen rules on sessions that did not exist when this research was completed ZAB's publication of executable code and a living FAQ deserves explicit credit: that level of transparency is what made independent reproduction, disagreement resolution, and the present self-correcting extension possible. Future revisions of this record should follow the same principle and update only when genuinely new prospective data accumulate.

## A Research Ledger and Reconstruction Coverage

The final ledger contains 129 recorded trials across SPY and external validation work. The statistical selection universe is restricted to 80 SPY trials with trial_role=SEARCH and selection_relevant=1. Of those. 31 belong to PRE_VWAP_FIX and 49 to CORRECTED. Exact or usable daily return series are available for 70: 28 PRE and 42 CORRECTED. The 10 missing exact series consist of seven CORRECTED unresolved reconstructions and three PRE cases (two historical target conflicts and one unresolved reconstruction). These 10 are retained in N = 80.

The PRE block itself is composed of 25 parameter-grid trials, three asymmetric short-filter trials, two trade-cap trials, and one short-lookback retuning trial. The full 25-point grid is recovered, including To010, whose initially transcribed Sharpe value was corrected after reconciling the source figure with the reconstructed return series.

## B Selected Experiment Metrics

**[table]**

Table 12: Selected research-stage experiments. Metrics are historical search-engine outputs, not the final audited candidate unless explicitly stated.
<table><tr><td>Trial / family</td><td>Configuration</td><td>Sharpe</td><td>Total return</td><td>Decision / interpretation</td></tr><tr><td>T0054</td><td>Symmetric VM 1.3</td><td>1.184</td><td>4,870.1%</td><td>Keep; clear baseline improvement.</td></tr><tr><td>T0055</td><td><eq>\mathrm { V M } _ { L } \: 1 . 3 \: / \: \mathrm { V M } _ { S } \: 1 . 6</eq></td><td>1.258</td><td>4,639.4%</td><td>Keep; improved asymmetric filter.</td></tr><tr><td>T0057</td><td>Above + short size 0.75</td><td>1.314</td><td>3,145.5%</td><td>Keep; base for later research.</td></tr><tr><td>T0058-</td><td>Binary relative-volume</td><td>1.298 to</td><td>2,742.1%</td><td>Reject; total return falls sharply as</td></tr><tr><td>T0061</td><td>thresholds</td><td>0.475</td><td>to 111.2%</td><td>the gate tightens.</td></tr><tr><td>T0064</td><td>Continuous RV sizing [0.5,1.5]</td><td>1.232</td><td>5,557.2%</td><td>Keep; first modification improving all four validation windows.</td></tr><tr><td>T0065</td><td>Continuous RV sizing [0.5,2.0]</td><td>1.176</td><td>6,728.6%</td><td>Diagnostic; more return, weaker Sharpe.</td></tr><tr><td>T0066</td><td>Two-checkpoint persis- tence</td><td>1.330</td><td>1,566.0%</td><td>Reject; loses too much return in 2013–2024.</td></tr></table>

20

<!-- page: 22 -->

## Page 22

“Beat the Market'Revisited

Independent Replication and Statistical Audit

**[table]**

<table><tr><td>Trial / family</td><td>Configuration</td><td>Sharpe</td><td>Total return</td><td>Decision / interpretation</td></tr><tr><td>T0067-</td><td>Profit-lock family</td><td>1.222-</td><td>5,439.9-</td><td>Reject; almost no incremental</td></tr><tr><td>T0071</td><td></td><td>1.233</td><td>5,599.9%</td><td>effect.</td></tr><tr><td>T0072</td><td>Require VWAP binding</td><td>0.851</td><td>510.7%</td><td>Reject; recent improvement but substantially reduces the historical</td></tr><tr><td>T0075</td><td>Band-dominant discount 0.85</td><td>1.232</td><td>3,502.8%</td><td>edge. Keep as reasonable trade-off candi- date.</td></tr><tr><td>T0076</td><td>Band-dominant discount 0.70</td><td>1.224</td><td>2,176.4%</td><td>Keep; selected aggressive drawdown/recent-period trade-off.</td></tr><tr><td>T0077-</td><td>Intraday decay</td><td>1.162</td><td>3,039.9/</td><td>Reject.</td></tr><tr><td>T0078 T0079</td><td>Daily loss, trade-loss,</td><td>/1.122 1.185-</td><td>2,479.2% mixed</td><td>Reject; no clean multi-window</td></tr><tr><td>T0085</td><td>breakeven controls</td><td>1.313</td><td></td><td>benefit.</td></tr><tr><td>T0086-</td><td>Choppy-regime overlay</td><td>about</td><td>2,441-</td><td>Reject; whipsaw does not persist</td></tr><tr><td>T0088</td><td></td><td>1.26</td><td>2,619%</td><td>predictably day-to-day.</td></tr><tr><td>T0089</td><td>Intuitive performance- momentum overlay</td><td></td><td></td><td>Reject; motivated direct autocorre- lation measurement.</td></tr><tr><td>T0091</td><td>Inverted/reversal overlay</td><td>1.296</td><td>2,143.1%</td><td>Keep; validates reversal direction.</td></tr><tr><td>T0099</td><td>30d, 0.9 after wins / 1.1</td><td>1.264</td><td>2,182.3%</td><td>Keep; selected mild calibration.</td></tr><tr><td>Final</td><td>after losses selected specification audited engine</td><td>1.274</td><td>2110.6%</td><td>Frozen; hard-cap/min- commission/early-close fixes</td></tr></table>

## C Statistical Audit Summary

**[table]**

Table 13: Frozen statistical results.
<table><tr><td>Statistic</td><td>Definition / role</td><td>Result</td></tr><tr><td>PBO, historical</td><td>25-grid CSCV, <eq>\lambda \leq 0 ,</eq> , warm-up zeros retained</td><td>38.49%</td></tr><tr><td>PBO, common-valid</td><td>Same grid, all 25 models simultaneously valid</td><td>40.87%</td></tr><tr><td>DSR, grid winner</td><td>Lookback 30 / VM 1.3</td><td>99.999995%</td></tr><tr><td>Raw multiple-testing count</td><td>All selection-relevant SPY SEARCH alternatives</td><td>80</td></tr><tr><td>Reconstructed daily series</td><td>PRE 28 + CORRECTED 42</td><td>70</td></tr><tr><td>sensitivity <eq>N _ { e f f , S R }</eq></td><td>5,000 synchronized block bootstraps, 20-session block</td><td>1.561</td></tr><tr><td>DSR, selected specification</td><td>Primary: N = 80, <eq>\sigma _ { S R }</eq> history trials</td><td>from 78 comparable full- 99.999986796%</td></tr></table>

21

<!-- page: 23 -->

## Page 23

“Beat the Market"’ Revisited

Independent Replication and Statistical Audit

## D Cross-Asset Evidence Preserved in the Ledger

**[table]**

Table 14: Selected cross-asset trials from the frozen research ledger.
<table><tr><td>Trial</td><td>Asset / specification</td><td>Sharpe</td><td>Total return</td><td>Status</td></tr><tr><td>T0051</td><td>QQQ base, lb14 / VM1.0</td><td>0.987</td><td>3,572.1%</td><td>KEEP / validation</td></tr><tr><td>T0105</td><td>QQQ + SPY Config J</td><td>0.809</td><td>708.6%</td><td>REJECT</td></tr><tr><td>T0106</td><td>QQQ + SPY rel-volume sizing</td><td>0.913</td><td>4,705.1%</td><td>DIAGNOSTIC / mixed</td></tr><tr><td>T0107</td><td>QQQ + SPY performance overlay</td><td>0.967</td><td>3,148.1%</td><td>REJECT</td></tr><tr><td>T0123</td><td>IWM base, 2004–2026</td><td>0.450</td><td></td><td>ADVERSE_EVIDENCE</td></tr></table>

The table intentionally reports only quantities preserved in the frozen ledger. In particular, no finer IWM subperiod statistics are imported from secondary drafts without a corresponding frozen series artifact.

## References

[1] C. Zarattini, A. Aziz, and A. Barbon. Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY). Swiss Finance Institute Research Paper Series No. 24-97. First version May 2024; version dated September 22, 2025.

[2] N. Jegadeesh and S. Titman. Returns to buying winners and selling losers: implications for stock market efficiency. Journal of Finance, 48(1):65–91, 1993.

[3] L. Gao, Y. Han, S. Z. Li, and G. Zhou. Market intraday momentum. Journal of Financial Economics, 129(2):394–414, 2018.

[4] C. Rosa. Understanding intraday momentum strategies. Journal of Futures Markets, 42(12):2218–2234, 2022.

[5] G. Baltussen, Z. Da, S. Lammers, and M. Martens. Hedging demand and market intraday momentum. Journal of Financial Economics, 142(1):377–403, 2021.

[6] T. J. Moskowitz, Y. H. Ooi, and L. H. Pedersen. Time series momentum. Journal of Financial Economics, 104(2):228–250, 2012.

[7] A. Frazzini. The disposition effect and underreaction to news. Journal of Finance, 61(4):2017–2046, 2006.

[8] D. Duffie. Presidential address: asset price dynamics with slow-moving capital. Journal of Finance, 65(4):1237–1267, 2010.

[9] C. Zarattini and A. Aziz. Volume Weighted Average Price (VWAP): the holy grail for day trading systems. SSRN Electronic Journal, 2023.

[10] D. H. Bailey, J. M. Borwein, M. Lopez de Prado, and Q. J. Zhu. The Probability of Backtest Overfitting SSRN research paper; later published in The Journal of Computational Finance.

[11] D. H. Bailey and M. Lopez de Prado. The Deflated Sharpe Ratio: correcting for selection bias, backtest overfitting, and non-normality. SSRN research paper, 2014.

[12] R. Kissell. The Science of Algorithmic Trading and Portfolio Management. Academic Press, 2014.

22
