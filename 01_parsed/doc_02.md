# doc_02 0DTE期权与尾部保护价格 修订稿

- source_path: `/Users/xiehaotong/Desktop/literature_pipeline/00_raw/期货日内因子_精选文献15篇/01_英文论文_微观结构与方法/02_0DTE期权与尾部保护价格(修订稿2026-09).pdf`
- parser: `MinerU`
- mineru_version: `4.0.7`
- mineru_tier: `basic`
- ocr_mode: `auto`
- lang: en
- type: paper
- page_count: 51

<!-- page: 1 -->

## Page 1

# 0DTE Options and the Price of Tail Protection

James O'Donovan City University of Hong Kong

First Draft: May 2026 This Draft: September 7, 2026*

## ABSTRACT

On May 16, 2022, the addition of Tuesday and Thursday weekly expirations extended SPX same-day-expiry (0DTE) options to every weekday. SPX put skew compressed across tenors, peaking at 72 basis points at 30 days. A cross-tenor difference-in-differences design shows that the decline is concentrated in the put wing and is absent in date and asset placebos, supporting a causal interpretation. Customer net put buying rises within one week of maturity, concentrated at zero to two days, while gap risk that daily expirations cannot remove limits compression at the shortest tenor. The implied reduction in the cost of equity tail insurance over the May 2022–June 2024 episode is $0.9 to $1.5 billion Post-2022 skew partly reflects intermediation-cost changes alongside tail-risk preferences

Keywords: 0DTE Options, Implied Volatility Skew, Dealer Hedging, Tail Risk, Market Microstructure

JEL Classification Numbers: G12, G13, G14, G23

*James O'Donovan (james.odonovan@cityu.edu.hk) is at the City University of Hong Kong. All errors are my own. The work described in this paper was supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China [Project No. CityU 11505322]. C2026.

<!-- page: 2 -->

## Page 2

# 0DTE Options and the Price of Tail Protection

## ABSTRACT

On May 16, 2022, the addition of Tuesday and Thursday weekly expirations extended SPX same-day-expiry (0DTE) options to every weekday. SPX put skew compressed across tenors, peaking at 72 basis points at 30 days. A cross-tenor difference-in-differences design shows that the decline is concentrated in the put wing and is absent in date and asset placebos, supporting a causal interpretation. Customer net put buying rises within one week of maturity, concentrated at zero to two days, while gap risk that daily expirations cannot remove limits compression at the shortest tenor. The implied reduction in the cost of equity tail insurance over the May 2022–June 2024 episode is $0.9 to $1.5 billion Post-2022 skew partly reflects intermediation-cost changes alongside tail-risk preferences

Keywords: 0DTE Options, Implied Volatility Skew, Dealer Hedging, Tail Risk, Market Microstructure

JEL Classification Numbers: G12, G13, G14, G23

<!-- page: 3 -->

## Page 3

## 1 Introduction

The implied volatility skew on S&P 500 index options, the premium of out-of-the-money puts over at-the-money puts, reduced sharply in the period Surrounding May 2022. The compression is not uniform across maturities. The cross-tenor compression is humpshaped, peaking at the 30-day tenor and attenuating at both ends—the central empirical fact we document and interpret. The timing coincides with a discrete change in market structure. On May 16, 2022—the Monday that began the first full trading week in which S&P 500 options were available expiring on every calendar day of the week—the CBOE completed its expansion of zero-day-to-expiry (0DTE) SPX expirations.1 The 0DTE share of total SPX option volume averaged approximately 20% before treatment and 45% after treatment over the main estimation window, and reached approximately 60% by 2025.

We identify the effect using a cross-tenor difference-in-differences design. A date fixed effect absorbs every aggregate shock that affects all tenors equally on a given day. The identifying variation is the differential change between short and long tenors. We find a differential break that peaks at the 30-day tenor and attenuates near the long end: the 30-day skew falls 0.72 pp more than the 365-day base while the 182-day tenor falls 0.51 pp. We verify that this shape is unusual relative to typical pre-period aggregate shocks which have a stable cross-tenor shape (steep at the short end, flat at the long end) that the May 2022 break departs from. The difference-in-differences design identifies the differential break across tenors; the break begins only after May 16 within the treatment quarter, is concentrated in the put wing, persists through June 2024, and is absent in date and low-correlation asset placebos

1CBOE listed Tuesday weekly expirations on April 26, 2022, and Thursday weekly expirations on May 11, 2022 (first Thursday 0DTE expiry: May 19); May 16 is the operative event date throughout.

2

<!-- page: 4 -->

## Page 4

We examine an intermediation channel using customer activity and variation in non-trading time. The new expirations give customers a same-session instrument and let dealers recycle intraday exposure; neither reaches the risk carried overnight. Cboe Open-Close data show that customer net put buying rises primarily within one week of maturity, with the largest increases at 0 and 1-2 days. When the shortest tenor contains more market holidays, its post-treatment compression is 0.29 pp smaller (t = 2.9); the effect is near zero at longer tenors. This concentration at 7 days is consistent with an unhedgeable gap-risk floor.

The compression translates into a material reduction in the cost of equity tail insurance. Predictive models fit on pre-treatment non-option state variables place post-treatment 30-day skew 1.27 to 2.22 pp below its counterfactual level. For an investor hedging a $1 billion equity portfolio with 30-day 25-delta SPX puts, this corresponds to approximately $0.6-$1.0 million per 30-day roll. The price reduction is a transfer from option writers to buyers except to the extent that it reflects a genuine fall in the cost of producing tail insurance.

Related literature. This paper contributes to three literatures. First, a growing literature studies the empirical and theoretical implications of 0DTE options. Adams, Dim Eraker, Fontaine, Ornthanalai, and Vilkov (2025) document the role of liquidity providers in 0DTE markets and argue that dealer hedging attenuates volatility. Vasquez, Amaya Pearson, and Garcia-Ares (2025) study the relationship between 0DTE introduction and underlying-asset volatility. Beckmeyer, Branger, and Gayda (2023) study retail participation in 0DTE markets. The CBOE's own research (Cboe Global Markets, 2023, 2024a) argues that 0DTE flow is sufficiently balanced across customers to leave dealers with limited net gamma exposure and therefore minimal market impact. That evidence concerns

3

<!-- page: 5 -->

## Page 5

dealer inventory; we show that the expansion nonetheless moved the price of downside protection at maturities well beyond the newly listed expirations.

Second, we connect to the literature on the joint determination of option prices by endinvestor demand and intermediary capacity. Garleanu, Pedersen, and Poteshman (2008) provide the canonical demand-based option-pricing framework. Atmaz and Basak (2019 show the impact of short sale costs on option spreads, and Christoffersen, Goyenko, Jacobs, and Karoui (2017) study the role of illiquidity in option pricing. Baltussen, Da, Lammers, and Martens (2021) show that dealer hedging demand creates intraday momentum patterns in the underlying. Terstegge (2024) documents that the option risk premium is concentrated over nights and weekends precisely because dealers cannot rebalance delta-hedges when equity markets are closed. We exploit a change in market structure that added a same-session option every weekday and trace its effect through the term structure of equity-index skew

Third, we contribute to the literature on the measurement of equity tail risk and the recovery of pricing-kernel features from option prices. Jackwerth and Rubinstein (1996) Jackwerth (2020) discuss the inference of the pricing kernel from index options. Bollen and Whaley (2004) examine net buying pressure as a determinant of skew. Our finding that expiration-menu design affects longer-term skew has implications for how skew-based measures of tail-risk preferences should be interpreted: they reflect market design and intermediation conditions as well as end-investor preferences over downside risk

The remainder of the paper is organized as follows. Section 2 describes the institutional setting. Section 3 describes data sources. Section 4 formalizes the cross-tenor differencein-differences design. Section 5 presents the empirical results, additional identification, the counterfactual level effect, mechanism evidence, and the economic magnitude. Section

4

<!-- page: 6 -->

## Page 6

6 contains robustness checks. Section 7 concludes.

## 2 Institutional Background

The introduction of daily 0DTE expirations. The CBOE's expansion of S&P 500 weekly options proceeded in stages over more than a decade. Friday weekly SPX options have existed since 2005 and were the only weekday outside the standard third-Friday monthly cycle that supported a same-day-expiry contract for most of the 2010s. Monday and Wednesday weekly expiration dates were added in 2016, completing a Mon/Wed/Fri schedule that prevailed until early 2022. Tuesday weekly expiration dates launched on April 26, 2022, and Thursday weekly expiration dates on May 11th, 2022 (first Thursday expiry: May 19th), completing the fully-daily SPX menu from the week of May 16th 2022. From May 16th, 2022 onward, an SPX option expiring on the close of each trading session has been available to trade every weekday, and intraday SPX trading volume in such "zero-day-to-expiry" (0DTE) contracts grew rapidly: from approximately 20% of total SPX option volume in 2021 to approximately 50% in 2024.2

The same expansion path applies to the major equity-index ETFs that track the SPX universe. The SPDR S&P 500 ETF (SPY), being an ETF on the same underlying index as SPX, transitioned to fully-daily 0DTE around November 14th, 2022. In the Russell 2000 complex, the cash index (RUT) reached its first week with 0DTE coverage on every trading day beginning January 15th, 2024, and the iShares Russell 2000 ETF (IWM, options on the same underlying) followed fourteen weeks later beginning April 22nd, 2024 (Cboe Global Markets, 2024b)—approximately 20 and 23 months after SPX, respectively

2The exact-date verification of these intro dates from contract-level OptionMetrics data is documented in Appendix Table A.6; we use May 16, 2022 (the start of the first full five-day week) as our operative treatment date

5

<!-- page: 7 -->

## Page 7

SPX was the first underlying to complete the daily menu; every other listed underlying followed at least four months later.

Appendix Table A.6 audits the 0DTE rollout for the broader set of S&P 500, Russell 2000, Nasdaq-100, commodity, and bond underlyings. Appendix Figure A.4 plots the 0DTE volume series for the eight of these underlyings that achieved fully-daily 0DTE coverage. SPX is by far the largest of these contracts by premium volume—averaging $10.1 billion per day in 2024 (Table A.6)

## 3 Data

Our primary data source is the OptionMetrics IvyDB U.S. database. We construct daily implied volatilities at fixed tenors and fixed deltas directly from raw option-level quotes in the opprcd files, applying the same construction to every underlying analyzed in the paper. For each (underlying, date) we select put and call quotes with calendar-day time to expiration in the range [5, 400] and absolute delta in [0.10,0.60], and require a positive bid, an offer above the bid, and a positive implied volatility. The lower bound on time to expiration excludes pure 0DTE quotes from the headline skew construction; we treat 0DTE separately when needed (Section 5.4.1). For each target tenor
T \in
{7, 14, 30, 60, 91, 182, 365} we take the closest available expirations on either side of
T
within a tenor-specific tolerance window
( \pm 4 ,   \pm 7 ,   \pm 1 0 ,   \pm 1 4 ,   \pm 2 1 ,   \pm 3 0 ,   \mathrm { a n d }   \pm 6 0
calendar days at the respective targets), interpolate implied volatility as a function of delta within each expiration using a monotone (Hermite) cubic spline, and linearly interpolate the resulting fixed-delta implied volatilities across the two expirations to the exact target tenor; when only one side of the target is available within the tolerance window we use the single nearest expiration. We do not extrapolate in delta: when the available delta

6

<!-- page: 8 -->

## Page 8

grid does not bracket the target, the implied volatility for that (underlying, date, tenor is recorded as missing. The delta filter
| \Delta | \in [ 0 . 1 0 , 0 . 6 0 ]
comfortably brackets the target deltas at ±0.25 and ±0.50 on essentially every (underlying, date): coverage of the putvs-ATM skew measure is 99.4–100% of (date, tenor) cells for SPX across 1,926 trading days, and 83–100% for TLT and LQD at the six tenors they enter. We evaluate the spline at -50∆ and -25∆ on the put side

Our central skew measure follows the put-versus-at-the-money convention:

s k _ { i , t , T } = I V _ { i , t , T , - 2 5 \Delta } ^ { P } - I V _ { i , t , T , - 5 0 \Delta } ^ { P } ,\tag{1}

the difference between the implied volatility of a 25-delta put and the at-the-money put We use this measure throughout the main results. For the appendix decomposition, callwing skew is at-the-money implied volatility minus 25-delta call implied volatility, and put-wing minus call-wing skew is the difference between the two wing measures.

For the customer-flow analysis, we use the customer-category opening and closing buy and sell volumes in the Cboe Open-Close Volume Summary data. We aggregate net customer put buying into seven mutually exclusive and exhaustive days-to-expiration buckets:
\{ 0 , 1   -   2 , 3   -   7 , 8   -   3 0 , 3 1   -   9 1 , 9 2   -   3 6 5 , 3 6 6   + \}
days.

We use the daily skew panel over 2018-01-02 to 2025-08-29; the available constructed panel and underlying opprcd option-level history extend to 2011 for SPX (2014 for SPY, QQQ, IWM, and RUT) and are used in tests requiring a longer pre-period (the 82-date placebo of Section 5.2 and the discrete-break test of Section 6). The main differencein-differences and customer-flow analyses use the [-6,8] quarter window (2020-10-01 to 2024-06-30). Summary statistics for this window are reported in Table 1.

7

<!-- page: 9 -->

## Page 9

## 4 Empirical Strategy

The basic challenge in identifying a 0DTE-driven shift in the SPX skew is that the May 2022 introduction coincided with a number of macroeconomic events: the Federal Reserve continued its post-pandemic tightening cycle and the Russia-Ukraine war began two months earlier. Any of these events, or other shocks, could in principle drive a coincident change in the equilibrium price of skew.

Our identification strategy is a cross-tenor difference-in-differences with 365-day skew as the within-asset base. The 365-day tenor is the most distant maturity from the 0DTE horizon with reliable data. Differencing against it,
\hat { \beta } _ { T }
measures compression at tenor
T
relative to this long-dated benchmark; Section 5.3 estimates the level effect separately Our empirical setup measures the differential change between skew at each short tenor and 365 days at the treatment date; identification requires parallel trends in this cross-tenor differential absent treatment. We therefore estimate

s k _ { t , T } = \alpha _ { T } + \delta _ { t } + \sum _ { T ^ { \prime } \neq 3 6 5 } \beta _ { T ^ { \prime } } \cdot \mathtt { 1 } _ { } { [ T = T ^ { \prime } ] } \cdot \mathtt { 1 } _ { } { [ t \geq t ^ { * } ] } + \varepsilon _ { t , T }\tag{2}

where
s k _ { t , T }
is the put-vs-ATM skew of equation (1),
\alpha _ { T }
is a tenor fixed effect,
\delta _ { t }
is a date fixed effect,
t ^ { * }
is the treatment date, and
\beta _ { T ^ { \prime } }
measures the differential post-period change at tenor
T ^ { \prime }
relative to the 365-day base. The date fixed effect
\delta _ { t }
absorbs every aggregate shock that affects all tenors equally on a given day, including the level of the VIX, macroeconomic news, and contemporaneous variance-risk-premium movements. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.

The identifying assumption is that, absent treatment, the relative skew between any two

8

<!-- page: 10 -->

## Page 10

tenors would have followed parallel trends. Subsection 5.2 below provides a quarterly event study with multi-period normalization and a Q2 2022 calendar-quarter split that places the May 16 break within the treatment quarter. Joint pre-trend F-tests (Appendix Table A.8 Panel A) reject strict pre-period equality, driven by a transient Q1 2022 deviation. A Newey-West HAC slope test does not indicate a smooth declining pretrend, and a linear-extrapolation bias correction leaves the headline 30-day coefficient at -0.65 pp (10% below the headline -0.72 pp)

## 5 Identification, Mechanism, and Magnitude

## 5.1 The Cross-Tenor Skew Compression

In Panel A of Figure 1 we plot the 30-day SPX put-vs-ATM skew alongside the share of total SPX option volume traded as 0DTE contracts. The 0DTE share rises from an annual average of approximately 8% in 2018 to 19% in 2021; following the full-daily introduction in the week of May 16, 2022, its 21-day moving average reaches 45% by September 2022 and approximately 60% by 2025. The 30-day skew averages approximately 4.8 percentage points before treatment and 2.4 percentage points after treatment over the main estimation window. In Panel B we aggregate the term-structure shift across the full set of tenors. Skew falls by approximately 2.4 pp at the 30-day peak, with broad post-pre compression of 2.2-2.4 pp across intermediate tenors attenuating to 1.7 pp at 365 days. The cross-tenor difference-in-differences specification of Table 2 estimates the differential break above this common-tenor shift.

We formalize this in the cross-tenor difference-in-differences specification of equation (2),

9

<!-- page: 11 -->

## Page 11

estimated on the
[ - 6 , 8 ]
quarter window (2020-10-01 to 2024-06-30). Table 2 reports the estimated
\beta _ { T }
. In column (1), the differential between long-tenor and short-tenor skew is -0.10 pp at 7 days, -0.50 pp at 14 days, -0.72 pp at 30 days, −0.66 pp at 60 days, -0.64 pp at 91 days, and -0.51 pp at 182 days. The compression peaks at the 30-day tenor and attenuates monotonically at longer tenors; at the very short end the
7 -
and 14- day coefficients sit below the 30-day peak, consistent with the gap-risk-floor mechanism developed in Section 5.4.2.3 Section 5.3 estimates the implied level effect separately and reconciles it with the difference-in-differences coefficient.

Figure 5 verifies empirically that aggregate confounds load on a stable cross-tenor shape that the design absorbs. For each pre-period shock we compute the cross-tenor differential
\beta _ { T } \equiv \Delta s k _ { T }   -   \Delta s k _ { 3 6 5 }
across tenors and rescale so
\beta _ { 3 0 } = 1
, isolating shape from magnitude The blue line plots the median
\beta _ { T }
profile across the top
5 \%
of pre-period absolute daily
\Delta s k _ { \mathrm { 3 0 } }
moves; the shaded band is the interquartile range. The profile declines steeply and monotonically from
\beta _ { 1 4 } \approx 1 . 5
to
\beta _ { 3 6 5 } \equiv 0
with a tight IQR around the median. For skew aggregate shocks move short tenors more than long tenors with a stable cross-tenor shape. Date fixed effects absorb the per-date level shift on each day; tenor fixed effects absorb the average pre-period cross-tenor slope, including the consistent steep decline that characterizes typical aggregate shocks. What remains in the residual—and is what
\hat { \beta } _ { T }
estimates—is each date's deviation from the typical slope. The May 2022 cumulative break (red line in Figure 5) has a fundamentally different shape: hump-shaped, peaking at the 30-day tenor and attenuating toward both ends, with
\beta _ { 1 4 }
below the typical IQR and
\beta _ { 9 1 } , \beta _ { 1 8 2 }
above it. These results suggest that the expansion of 0DTE trading to every weekday affected skew differentially at short, intermediate, and long tenors.4

3Appendix Table A.1 shows that the compression is concentrated in the put wing; call-wing changes are generally small, except at the 7-day tenor.

4Appendix Figure A.2 replicates the comparison on a longer pre-period beginning January 2018, with qualitatively identical results.

10

<!-- page: 12 -->

## Page 12

Columns (2)-(4) of Table 2 address two robustness concerns. Column (2) adds two realized state variables of the underlying (lagged 21 day realized volatility and skewness each entering with tenor-specific dummies (one coefficient per control tenor combination), so no functional-form assumption on the tenor dependence is imposed.5 The headline
\hat { \beta } _ { 3 0 } = - 0 . 7 2
pp attenuates modestly to -0.66 pp; the cross-tenor shape is preserved at every tenor.

A natural follow-up is whether the magnitude of compression scales with the intensity of 0DTE activity rather than the binary post-indicator. Columns (3) and (4) replace the post-dummy with the continuous daily 0DTE share of total SPX option volume, which averaged 19.5% over the pre-treatment window (driven by Mon/Wed/Fri 0DTE expirations that pre-dated the May 2022 expansion) and 45.1% over the post-treatment window. The dose-response specification identifies the effect using within-regime dayto-day variation in 0DTE intensity rather than the pre/post regime jump; the resulting hump-shaped tenor profile mirrors the results of the differences in differences design peaking at the 30-day tenor with attenuation toward both ends.6

5Results are essentially identical under log(T), √T, or T interactions; the saturated tenor-dummy form is the most flexible and is reported in the main table. We deliberately exclude option-derived variables (VIX, VVIX, ATM IV, and PCs of the IV surface) because the treatment moves the option surface: these variables are downstream outcomes, and conditioning on them with tenor-varying loadings would absorb part of the treatment effect.

6The daily 0DTE share is endogenous to skew (customers facing expensive tail hedges may shift to 0DTE, mechanically generating a negative correlation between share and skew). A clean instrumental variable for 0DTE share is unavailable in our setting because the contract-availability change is essentially a 3-to-5-day expansion of the weekly menu (Mon/Wed/Fri pre-2022; Tuesday added April 26, 2022 and Thursday added May 11, 2022, with the brief intervening four-day window April 26–May 10 too short to deliver continuous within-regime exogenous variation) rather than continuous within-regime variation. The dose-response coefficient should therefore be read as an associated within-regime correlation rather than a causal elasticity; the binary post-indicator specification is the headline result.

11

<!-- page: 13 -->

## Page 13

## 5.2 Pre-Trends, Persistence, and Placebo Tests

The cross-tenor design's identifying assumption is parallel trends in the cross-tenor differential
s k _ { T } - s k _ { 3 6 5 }
: absent treatment, this differential would have continued on its pre-period trajectory. The persistence diagnostics in Panel C of Appendix Table A.8 show the differential is mean-reverting noise in the pre-period with a short half-life
\left( \hat { \rho } = 0 . 8 3 5 ,   3 . 8 - \right.
day half-life); the post-treatment regime is a sustained level shift the pre-period process does not generate. We test the parallel-trends assumption directly with a quarterly event study around the treatment quarter (Q2 2022). For each calendar quarter
q \in [ - 6 , 8 ]
we compute the difference
s k _ { 3 0 , q } - s k _ { 3 6 5 , q }
averaged across days in the quarter. We normalize to the average of all six pre-treatment quarters
q \in [ - 6 , - 1 ]
, so coefficients measure deviation from the pre-period mean. The calendar quarter that contains the treatment date,
q = 0
(Q2 2022), is split into two bins: q-pre (April 1 to May 15, 2022) and q-post (May 16 to June 30, 2022), separating pre- and post-treatment observations within the contaminated calendar quarter. We plot the resulting series in Figure 2 with 95% confidence intervals from Newey-West HAC standard errors at 63 trading days (1 quarter) of lags.

Pre-treatment coefficients fluctuate around the reference mean and do not display a monotonic decline prior to the May 2022 expansion: Q1 2022 (q = −1) appears as a 0.37 pp single-quarter spike (t = 3.20), with other pre-treatment quarters scattered between -0.34 and 0.17 pp. A Newey-West HAC slope test on the daily SPX 30-day pre-period differential gives
\hat { \gamma } _ { \mathrm { p r e } } = - 0 . 0 0 0 0 6 ~ \mathrm { p p / d a y } ~ ( t = - 0 . 1 3 )
, with no evidence of a smooth declining pretrend. The split of
q = 0
shows the decline appears after the event date, not as a continuation of mean reversion from the Q1 2022 spike: q-pre (April 1 to May 15, 2022) is
\mathrm { a t } \: - 0 . 0 8   \mathrm { p p } \: \left( t \: = \: - 0 . 8 3 \right.
, statistically indistinguishable from the pre-period mean), while q-post (May 16 to June 30, 2022) is already at
- 0 . 5 7   \mathrm { { p p }   \left( t   =   - 1 2 . 1 7 \right) }
. Post-

12

<!-- page: 14 -->

## Page 14

treatment coefficients remain persistently negative through
q = + 8 ( \mathrm { Q } 2 2 0 2 4 )
, with average
\hat { \theta } _ { \mathrm { p o s t } } = - 0 . 7 2 ~ \mathrm { p p }
(t = -11.12). Appendix Figure A.1 confirms the result when the entire contaminated quarter
q = 0
is excluded from the regression. Appendix Table A.8 Panel A reports formal pre-trend tests across three pre-window lengths.

Linear-extrapolation bias-correction. We bias-correct the headline DiD against any unmodelled pre-period linear trend, a stricter requirement than the slope diagnostic above. The panel specification adds tenor-specific pre-period linear trends
\gamma _ { T }   t \times
\mathrm { P r e } _ { t } \times \mathbf { 1 } [ T ]
to equation (2), so that
\gamma _ { T }
is identified from pre-period variation only and
\beta _ { T }
captures the level shift conditional on the pre-period slope. The bias-corrected average post-treatment effect at each short tenor is
\beta _ { T }   -   \gamma _ { T } \bar { t } _ { \mathrm { p o s t } }
We obtain
\hat { \beta } _ { T } ^ { \mathrm { B C } } =
\{ - 0 . 0 5 , - 0 . 5 3 , - 0 . 6 5 , - 0 . 5 6 , - 0 . 6 1 , - 0 . 4 7 \}
pp at
T   \in   \{ 7 , 1 4 , 3 0 , 6 0 , 9 1 , 1 8 2 \}
days. The 7-day estimate remains near zero, and the estimates at 14 days and longer are within 16% of their corresponding headline coefficients (Appendix Table A.8 Panel B), conditional on the same realized volatility and skewness controls used in Column (2) of Table 2 The pre-period slope is too small to mechanically explain the post-period shift. Standard errors on the bias-corrected estimates are nonetheless wider than the headline because the pre-period slope is imprecisely estimated on the 19-month headline pre-window. The complementary discrete-break test on the longer 2018-2022 pre-window remains statistically significant at 30 days and longer after accounting for uncertainty in the fitted pre-period model (Appendix Table A.7); in the controlled specification, the corrected t-statistics range from -3.18 to -6.94.

Persistence asymmetry and rolling-window placebo. The cross-tenor differential is stationary in the pre-period (ADF
p < 0.0001)
with a short 3.8-day half-life (Appendix Table A.8 Panel C): pre-event it is mean-reverting noise with short memory, whereas it

13

<!-- page: 15 -->

## Page 15

holds at its new level throughout the post-treatment window ending June 2024. Two rolling-window placebos make this formal. First, no pre-period 6-month rolling-window mean lies below -1.57 pp, while the post-period mean is -2.03 pp, outside the support of any comparable-length pre-period window.7 Second, measuring the forward-minusbackward shift at matched horizons, the actual May 2022 shift is -0.89 pp at W = 63 trading days and -0.79 pp at W = 126, matched or exceeded by zero pre-period windows at either horizon (most negative pre-period shifts -0.65 and -0.31 pp); at the transient W = 21 horizon the actual shift of -0.70 pp is matched by 19.7% of pre-period windows. The break is unprecedented at the persistent horizons that match the paper's measurement window; the Q1 2022 single-quarter spike that drives the joint pre-trend F-test rejection (Panel A) is the kind of transient deviation the pre-period occasionally produces; a 26-month sustained shift of post-period magnitude is not. Across 86 overlapping two-year windows beginning between 2013 and March 2020, none has a more negative two-year mean at 30, 60, or 91 days (Appendix Table A.2)

Date placebo. For each of eighty-two pseudo-treatment dates between January 2015 and October 2021—monthly placebos with ±6-month windows—we re-estimate the cross-tenor DiD using the pseudo-date in place of May 2022 on the SPX panel. The actual May 2022 SPX cross-tenor coefficient sits in the bottom 4–6% of this distribution at the 30–182 day tenors and in the bottom 12% at the 14-day tenor (Table 3 Panel B), with placebo distribution standard deviations of 0.25-0.73 pp.8 Figure 3 re-runs the same exercise as a quarterly event study with the placebo treatment quarter set to Q2 2021— one year before the actual event—and confirms that no break appears at the placebo date

7In untabulated results, extending the pre-period to the full opprcd history (2014-01-02 onward, 2,046 trading days) yields a minimum 6-month rolling-window mean of —1.85 pp (August 2016), still well above the post-period mean. The persistence asymmetry strengthens with longer pre-history.

8The 7-day tenor is omitted from Table 3 because LQD's 7-day coverage is incomplete on the estimation window (72% of trading days); estimating SPX on a 6-tenor panel matching Table 2 Column (1) makes the SPX coefficients and t-statistics in Panel A identical to the headline.

14

<!-- page: 16 -->

## Page 16

while the actual May 2022 break appears at
q = + 4

Asset placebo. The same logic applies in the cross-section. If the May 2022 break reflected an aggregate regime shock rather than the SPX rollout, low-correlation option markets should display comparable cross-tenor compression on the same date. We test this using TLT (long-duration Treasuries;
\rho \big ( \Delta s k _ { \mathrm { T L T } } ^ { 3 0 } , \Delta s k _ { \mathrm { S P X } } ^ { 3 0 } \big )   =   - 0 . 0 3 )
and LQD (investment-grade corporate bonds;
\rho = 0 . 0 4 )
9

Estimating equation (2) on each over the headline window (2020-10-01 to 2024-06-30) we obtain
\hat { \beta } _ { T }   \in   [ - 0 . 1 1 , 0 . 1 2 ]
pp across short tenors for TLT and [-0.11, 0.09] pp for LQD, with mixed signs across tenors and no coefficient reaching conventional significance
( | t | < 1 . 7
throughout).10 Figure 4 reports the same coefficients alongside SPX as a bar chart with 95% confidence intervals: SPX compresses sharply at every short tenor while TLT and LQD exhibit no economically or structurally comparable compression pattern on the same calendar date.

Endogeneity of the treatment date. CBOE's decision to complete the daily expiration menu in May 2022 was itself a response to demand and market conditions; the treatment is not strictly exogenous. The relevant concern is that the listing decision could itself reflect a contemporaneous shift in customer demand for short-horizon optionality, which would be short-tenor-specific by construction and therefore not absorbed by the date fixed effect. One feature of the institutional setting constrains this concern CBOE's weekly-option listings require a Self-Regulatory Organization rule filing under

9Correlations computed on first-differenced 30-day put-vs-ATM skew over the full sample 2018-01-02 to 2024-06-30, differencing each series on its own trading-day grid.

0.12,0.07,0.09, 0.01, -0.11 pp

10TLT coefficients (14, 30, 60, 91, 182 days): 0.12,0.07,0.09,0.01,−0.11 pp. LQD coefficients: -0.11, -0.05,0.09,0.08,-0.01 pp. Both estimated with date and tenor fixed effects and Newey-West HAC standard errors at 63 trading days (1 quarter) of lags.

15

<!-- page: 17 -->

## Page 17

§19(b)(1) of the Securities Exchange Act and SEC review under §19(b)(2). The Tuesday and Thursday SPXW expirations that completed the daily SPX menu were filed by CBOE on February 8, 2022 (SR-CBOE-2022-005), approved by the SEC on April 12, 2022, and listed on April 18 and May 11, 2022.11 The 14-week lead time between the original filing and the operative full-week treatment date constrains how finely the listing can be timed: a contemporaneous demand confound capable of explaining the May 2022 break would have had to be anticipated in early February 2022 and incorporated into the filing.

## 5.3 Level Effect: Counterfactual Skew Model

Our cross-tenor difference-in-differences specification in Table 2 identifies the differential change in skew relative to a 365-day baseline. To complement it, we fit a pre-period predictive model of 30-day skew and project it forward, measuring the post-treatment gap between realized and predicted skew. The predictor set captures realized behavior of the underlying, macro-announcement timing, and index-state variables, all observable on the underlying or the macro calendar rather than the option surface: 5-, 10-, 21-, 63-, and 126-day rolling realized volatility of SPX returns; 21- and 63-day realized return skewness; 5-, 21-, and 63-day cumulative returns; 21- and 63-day downside realized semivariance; log(SP500), 21-day deviation from moving average, and 252-day drawdown; FOMC and CPI announcement-day dummies; and days-since-last-FOMC / days-to-next

11See Federal Register notice of fling for SR-CBOE-2022-005, 87 Fed. Reg. 11178 (Feb. 28, 2022), and the approval order, 87 Fed. Reg. 23150 (Apr. 18, 2022).

16

<!-- page: 18 -->

## Page 18

FOMC counters.1213

We fit a Random Forest (500 trees, default depth) on the pre-treatment sample (2020 10-01 to 2022-05-15, n = 408 trading days, 19 predictors) and project it forward into the post-period. Realized post-treatment 30-day skew averages 2.22 pp below its prediction OLS and gradient boosting produce gaps of -1.27 and -2.12 pp, respectively. Across functional forms, realized skew is 1.27 to 2.22 pp below its predicted level. Figure 6 plots the time series; Appendix Table A.3 compares the three models and reports boundedepisode roll-cost equivalents through the same 2024Q2 endpoint

The two estimates answer different questions. The DiD identifies the differential change at each short tenor relative to 365 days, while the predictive counterfactual estimates the 30-day level gap against relationships fitted before the rollout, so it absorbs commontenor movements as well as maturity-specific ones. The gap between them is therefore not evidence on how much of the common-tenor decline 0DTE caused. We identify the relative maturity effect from the DiD and take the predictive range of -1.27 to -2.22 pp as its economic magnitude.

Longer pre-period as a consistency check. Re-fitting the same predictor set on a longer pre-period beginning January 2018 yields post-period gaps of -1.99 pp (OLS) -2.48 pp (Random Forest), and -2.45 pp (gradient boosting), comparable to or slightly larger than the headline-window estimates (Appendix Figure A.3). Expanding-window CV on the longer pre-period gives positive OOS R2 in two of five folds and negative

12Option-derived variables—VIX, VIX9D, VIX3M, VIX6M, VVIX, ATM IV at any tenor, or slopes/PCs thereof—are deliberately excluded: when the treatment moves the option surface, conditioning on them absorbs part of the treatment by construction.

yt-63)

(yt-21

13As a robustness check, augmenting the predictor set with long-lag own-skew (yt-21 only, or both yt-21 and yt-63) leaves the Random Forest post-period gap essentially unchanged (-2.24 pp and -2.23 pp respectively).

17

<!-- page: 19 -->

## Page 19

OOS
R ^ { 2 }
in three, suggesting the longer pre-window contains regime breaks that complicate extrapolation. We therefore report the headline-window results as the cleaner counterfactual and the longer-window results as a consistency check.

## 5.4 Mechanism

The introduction of fully-daily 0DTE contracts adds a same-session SPX option that does not bear overnight gap risk, where the previous Mon/Wed/Fri schedule had left two of five trading sessions without a same-day-expiring contract. A structural change of this kind could plausibly affect non-0DTE skew through two non-mutually-exclusive channels: a reduction in the equilibrium compensation dealers require to warehouse put-side inventory, since they can recycle intraday gamma exposure through a same-session instrument (Garleanu et al., 2008; Terstegge, 2024)—though this recycling reaches only the intraday wedge and leaves an unhedgeable overnight gap-risk floor at the very short end (Section 5.4.2); and a shift in customer demand across tenors and moneyness, since investors who previously bought short-tenor puts for session-level hedging now have a same-session alternative (Bollen and Whaley, 2004). We test the customer-demand channel with Cboe Open-Close volumes and the gap-risk limit on intraday recycling with calendar variation in non-trading time. Warehousing cost itself is not observable in these data; the holiday test bounds where the recycling channel can operate rather than measuring its size.

## 5.4.1 Customer Net Put Flow by Maturity

Let
\mathrm { c u s t \_ n e t } _ { t , b , p }
denote net customer directional volume (open buys plus close buys minus open sells minus close sells) in tenor bucket b and call/put indicator
p ,
summed across all SPX option contracts on day t. We estimate pre/post means on the headline DiD window

18

<!-- page: 20 -->

## Page 20

(2020-10-01 to 2024-06-30). Post-treatment, customer net 0DTE put buying rises from 3,525 to 14,799 contracts per day, an increase of 11,274. In the 1–2 day bucket, customers move from net selling 1,487 to net buying 5,620 contracts per day, an increase of 7,107 Customer net buying also rises by 3,430 contracts per day at 3-7 days. Beyond seven days, the changes are considerably smaller: -1,747 at 8–30 days, -1,010 at 31–91 days +1,224 at 92–365 days, and +214 beyond 365 days. The activity response is therefore concentrated within the first seven days. It does not coincide with the tenors at which the price effect is largest: the 7-day coefficient is -0.10 pp and indistinguishable from zero, while compression peaks at 30 to 91 days, where customer flow changes little. The flow evidence shows where trading migrated, not where the price effect was produced

Total SPX option volume rises from 1.41 to 2.83 million contracts per day over the same window. 0DTE accounts for 68.4% of that increase, and its volume share rises from 19.1% to 44.8%,14while the shares at 1–10 and 11–74 days fall from 38.9% to 27.4% and from 28.9% to 17.5%, respectively. The 0DTE-to-positive-DTE volume ratio was already trending upward before May 2022, so this reallocation is descriptive rather than a second treatment estimate.

## 5.4.2 Gap-Risk Floor

Daily expirations allow intraday exposure to be recycled through a same-session option but they do not remove the gap risk borne while the market is closed. If this gap risk limits skew compression, the post-treatment decline should be smaller when a short-tenor window contains more market holidays. The prediction is strongest at 7 days, where each additional non-trading day represents the largest share of the remaining contract life.

14Cboe Open–Close file; Table 1 gives 19.5% and 45.1% from OptionMetrics volume.

19

<!-- page: 21 -->

## Page 21

We exploit calendar variation in non-trading time to test this floor directly. For each observation date t and tenor
T \in \{ 7 , 1 4 , 3 0 , 6 0 , 9 1 , 1 8 2 \}
, let
\operatorname { H o l C o u n t } _ { t , T }
count the NYSE market holidays in the next
T
calendar days, mechanically increasing the share of unhedgeable non-trading time within the dealer's warehousing window. Table 4 reports the pooled-panel triple-DiD coefficient
\hat { \gamma } _ { T }
on
\mathrm { P o s t } _ { t } \times \mathrm { H o l C o u n t } _ { t , T } \times \mathbf { 1 } [ T ]
across three control specifications. The regression includes date and tenor fixed effects, per-tenor
\mathrm { P o s t } _ { t }
main effects, and per-tenor HolCountt,T main effects, with the 365-day tenor as the omitted reference. At 7 days,
\hat { \gamma } _ { 7 } = 0 . 2 9 \mathrm { p p } ( t = 2 . 9 )
, essentially invariant across the three control specifications. The coefficient at every longer tenor is small and not statistically distinguishable from zero
\left( \hat { \gamma } _ { 1 4 }   =   0 . 0 5 , \hat { \gamma } _ { 3 0 }   =   - 0 . 0 1 , \hat { \gamma } _ { 6 0 }   =   - 0 . 0 2 , \hat { \gamma } _ { 9 1 }   =   - 0 . 0 5 , \hat { \gamma } _ { 1 8 2 }   =   0 . 0 1 \right.
percentage points)—the cross-tenor shape the gap-risk-floor mechanism predicts: a binding floor at the very short end and no effect at intermediate or long tenors. The variation in the NYSE holiday calendar that we exploit is exogenous to 0DTE customer flow and directly identifies the gap-risk floor.

## 5.5 Economic Magnitude

We translate the predictive level gap in put-vs-ATM skew into the dollar cost of a representative tail hedge. To the extent that this gap reflects 0DTE-driven compression, the calculation measures the associated reduction in hedging costs. We compare the actual post-period price of a 30-day 25∆ SPX put with its predictive counterfactual price, holding the at-the-money volatility and the underlying (post-period mean of 4,370) fixed so that only the put-vs-ATM skew differs. The actual price uses the observed post-period
2 5 \Delta
put implied volatility of 18.8% (the sum of the at-the-money implied volatility and skew rows of Table 1), giving $3,603 per contract under Black-Scholes; the counterfactual adds back the -2.22 pp Random Forest level-effect estimate from the Section 5.3 model,

20

<!-- page: 22 -->

## Page 22

raising the 25∆ implied volatility to 21.0% and the price to $4,044 per contract.

The implied price reduction is therefore $440 per 25∆ contract. For an investor hedging a $1 billion equity portfolio with 30-day 25∆ SPX puts, this implies 2,288 contracts and a saving of approximately $1.0 million per 30-day roll, equivalent to 10 basis points of notional per roll (roughly 1.2% per year if rolled monthly). The OLS gap of -1.27 pp gives approximately $0.6 million on the same calculation.

Applying each model's per-contract saving at 25 delta to open interest in 30–90 day puts with deltas between -0.30 and -0.20 (a post-treatment daily average of approximately 252k contracts) over May 16, 2022 through June 30, 2024 gives a bounded-episode total of $0.87–$1.52 billion under the turnover implied by the band's open-interest-weighted maturity of 58 days, or $1.64–$2.87 billion if every open contract rolls monthly.15 A broaderuniverse extrapolation across the 10–40 delta, 5-90 day OTM-put surface would yield a multiple of this figure, but the assumption of homogeneous per-contract savings across the surface is contradicted by the cross-tenor results (the compression is concentrated at intermediate tenors and intermediate moneyness); we do not report a broader-universe headline figure. The aggregate saving is a price-level reduction in the cost of insurance: end-investors pay less for tail-risk insurance and option writers (predominantly dealers and institutional tail-hedge writers) receive less per-contract compensation for warehousing the same exposure. The split between (i) a transfer from option writers to buyers (no first-order welfare implication absent risk-sharing or intermediation frictions) and (ii) a deadweight reduction (the part reflecting genuinely lower hedging costs) depends on a model of dealer compensation we do not undertake here. Existing demand-system evidence (Garleanu et al., 2008) suggests the deadweight component is non-trivial in option markets, but we do not attempt to quantify it.

15Appendix Table A.3 reports the calculation for each predictive model.

21

<!-- page: 23 -->

## Page 23

## 6 Robustness

Data sources and skew-measurement conventions. Appendix Table A.4 replicates the headline DiD across two data sources (opprcd-reconstructed and OptionMetrics vsurfd kernel-smoothed surface) and across alternative skew-measurement conventions (fixed dollar moneyness
K / S { = } 0 . 9 5
and standardized moneyness z=1.0). The hump-shape across tenors—negative coefficient at every short tenor with a 30-day peak—survives in every
\sigma { \sqrt { T } } .
-aware specification: the delta-based opprcd and vsurfd reconstructions both peak at 30 days, as does the standardized-moneyness z=1.0 measure (pre-treatment mean deltas of approximately —0.20 to —0.22). The magnitude of the hump is amplified by the delta convention because at short tenors the 25-delta put strike sits much closer to the at-the-money point than at long tenors (where
\sigma \sqrt { T }
is larger), suppressing the visible 14-day compression in the delta-based measure; under
z { = } 1 . 0
the 14-day-to-30-day gap shrinks to 0.13 pp (vs 0.22 pp under
s k _ { \mathrm { 2 5 , A T M } } )
. Fixed dollar moneyness flips the apparent tenor shape to monotone-decreasing (column 3 of Table A.4: -2.51 pp at 14 days, attenuating to -0.28 pp at 182 days), but the
K { = } 0 . 9 5   S
strike walks across the smile from a pre-treatment mean delta of approximately -0.13 at 14 days to -0.37 at 365 days, so it is not an apples-to-apples cross-tenor comparison—it conflates where on the smile the compression was largest in dollar terms (deep-OTM short-tenor, where pre-treatment implied volatility was most elevated) with the cross-tenor signature itself. The structurally cleanest cross-tenor comparison is therefore
\sigma { \sqrt { T } } .
-normalized, and it confirms the 30-day peak with a flatter cross-tenor shape than the delta convention suggests.

Alternative windows. Appendix Table A.5 reports two alternative pre-period win dows ([-8,8] and [-4,8]); all coefficients are negative and significant in both. The headline window [-6,8] starts in 2020-Q4 to exclude the COVID dislocation; longer

22

<!-- page: 24 -->

## Page 24

pre-windows mix the pre-COVID and post-COVID skew regimes.

Discrete break or smooth secular trend? Dew-Becker and Giglio (2025) document a secular decline in the variance risk premium, which they attribute to dealers bearing a smaller amount of unhedgeable S&P 500 risk. A natural reading of this evidence is that the May 2022 cross-tenor break we identify could be a discrete piece of this ongoing trend rather than a distinct shock. We test this directly. For each tenor
T ,
we fit a model of the daily cross-tenor differential
s k _ { T } - s k _ { 3 6 5 }
on the long pre-window (2018-01-02 to 2022-05-13), project the fit forward into the post-treatment window, and estimate the residual May 2022 break. Two specifications: a linear time trend only, and a linear time trend plus controls (log of weekly realized SPX volatility, weekly realized return skewness, 21-day cumulative SPX return). We deliberately exclude option-derived controls—per the bad-controls reasoning of Section 5.1, option-derived controls absorb the treatment by construction because the treatment moved the option surface. Appendix Table A.7 reports the results. At every tenor 30 days and longer, the partialled-out break exceeds the headline coefficient in magnitude (-0.76 pp at 30 days, -0.78 at 60 days, -0.75 at 91 days, -0.65 at 182 days, all statistically significant), showing that the May 2022 break is not explained by the fitted smooth secular trend. At 14 days the partialled-out coefficient drops to -0.19 pp (t = -0.62, not significant): the long pre-window has a substantia pre-existing widening of the 14-day-vs-365-day differential
( - 0 . 1 9 ~ \mathrm { p p / y e a r } )
, of roughly the same magnitude as the post-2022 break, and the discrete-break interpretation cannot be cleanly distinguished from a continuation of trend at this tenor. The weaker 14- day evidence is consistent with the overnight gap-risk-floor interpretation in Section 5.1, while the discrete-break evidence is cleanest at 30 days and longer. A complementary endogenous-break test (Andrews, 1993) on the daily 30-day cross-tenor differential locates

23

<!-- page: 25 -->

## Page 25

the break at 2022-05-11 , within three trading days of the May 16 treatment.16

Realized-volatility channel. Adams et al. (2025) document that the presence of 0DTE trading lowers intraday S&P500 realized volatility by approximately 60 annualized basis points, identified using exogenous Tuesday/Thursday variation in 0DTE presence prior to May 2022. This raises the alternative interpretation that our cross-tenor skew compression mechanically reflects lower realized volatility post-treatment rather than an independent dealer-warehousing-cost channel acting on the put-side price of risk. We examine this directly by re-estimating the headline cross-tenor difference-in-differences with additional per-tenor interactions on contemporaneous daily realized volatility computed from SPY 15-minute data. At 14 days and longer, the post coefficients change by at most 3% under linear interactions and 7% under log interactions. At 7 days, the estimates remain small and statistically insignificant: —0.11 pp (t = —0.60) and —0.13 pp (t = -0.69), respectively (Appendix Table A.9). The cross-tenor compression therefore survives conditioning on contemporaneous realized volatility.17

16Quandt-Andrews sup-Wald test: the Wald statistic for a single structural break is computed at every candidate date and the largest is reported, using Newey-West HAC errors at 63 trading days to match the paper-wide standard-error policy. The mean-only specification tests for a shift in the average level of the differential; the linear-trend specification adds a deterministic time trend and tests for a shift over and above it, guarding against attributing a smooth trend to a discrete break. The search trims the first and last 15% of the sample—the standard Andrews (1993) restriction that keeps each candidate subsample large enough to estimate—so the break date is drawn from the central 70%. Mean-only: sup-F = 24.76, rejecting at the 1% level; with linear trend: sup-F = 12.43, also rejecting at the 1% level (Andrews 1993 ·F = 12.43 critical values 8.85 at 5% and 12.16 at 1% under 15% trimming)

17Mean SPY intraday realized volatility on our headline window is 1,134 bp pre and 1,144 bp post (annualized).

24

<!-- page: 26 -->

## Page 26

## 7 Conclusion

Completing the daily SPX expiration menu in May 2022 compressed put-side skew across the term structure, with the largest effect at 30 days. The timing, cross-tenor and cross-moneyness patterns, and falsification tests are difficult to reconcile with aggregatevolatility or broad preference-shock explanations. The episode shows how hard skew is to interpret in a dealer-intermediated, zero-net-supply market: the price reflects not only what investors will pay for downside protection but also what dealers require to warehouse the other side, so a fall in the cost of intermediation lowers it with no change in underlying preferences. Across the predictive models in Section 5.3, post-2022 30-day SPX skew sits 1.27 to 2.22 pp below the levels predicted by macro and volatility-state variables. The quantity and holiday evidence point to lower intermediation costs, rather than a broad change in tail-risk preferences, as an important source of this gap. Studies that infer tail-risk preferences from SPX skew over time should therefore account for the May 2022 expiration-menu regime shift

Two limits bound the interpretation. Welfare depends on a model of dealer compensation we do not develop, so we cannot separate the transfer to option buyers from the deadweight reduction in hedging costs; and our estimates price the change at the existing 30–90 day, 25-delta margin, not across the full surface. Within those limits, the episode shows that a change in the expiration calendar reprices protection at maturities many times longer than the contracts introduced.

25

<!-- page: 27 -->

## Page 27

## References

Adams, G., C. Dim, B. Eraker, J.-S. Fontaine, C. Ornthanalai, and G. Vilkov (2025) Do s&p500 options increase market volatility? evidence from 0dtes. Working Paper 5641974, SSRN

Andrews, D. W. K. (1993). Tests for parameter instability and structural change with unknown change point. Econometrica 61 (4), 821–856.

Atmaz, A. and S. Basak (2019). Option prices and costly short-selling. Journal of Financial Economics 134 (1), 1–28.

Baltussen, G., Z. Da, S. Lammers, and M. Martens (2021). Hedging demand and market intraday momentum. Journal of Financial Economics 142(1), 377–403.

Beckmeyer, H., N. Branger, and L. Gayda (2023). Retail traders love 0dte options.. . but should they? Working Paper 4404704, SSRN

Bollen, N. P. B. and R. E. Whaley (2004). Does net buying pressure affect the shape of implied volatility functions? Journal of Finance 59(2), 711–753.

Cboe Global Markets (2023). Volatility insights: Much ado about 0dtes — evaluating the market impact of spx 0dte options. Cboe Insights Research Note.

Cboe Global Markets (2024a). 0dtes decoded: Positioning, trends, and market impact. Cboe Insights Research Note.

Cboe Global Markets (2024b). Cboe options to list Tuesday and Thursday expiring weekly options on IWM. https://cdn.cboe.com/resources/product_update/2024/Cboe-Options-to-List-Tuesday-and-Thursday-Expiring-Weekly-Options-on-IWM.pdf. Product update announcement.

26

<!-- page: 28 -->

## Page 28

Christoffersen, P., R. Goyenko, K. Jacobs, and M. Karoui (2017). Illiquidity premia in the equity options market. The Review of Financial Studies 31 (3), 811–851

Dew-Becker, I. and S. Giglio (2025). The decline of the variance risk premium: Evidence from traded and synthetic options. Working Paper WP 2025-17, Federal Reserve Bank of Chicago.

Garleanu, N., L. H. Pedersen, and A. M. Poteshman (2008). Demand-based option pricing. The Review of Financial Studies 22(10), 4259–4299.

Jackwerth, J. (2020). What do index options teach us about covid-19? The Review of Asset Pricing Studies 10(4), 618–634.

Jackwerth, J. C. and M. Rubinstein (1996). Recovering probability distributions from option prices. The Journal of Finance 51 (5), 1611–1631.

Terstegge, J. (2024). Intermediary option pricing. Working paper, Copenhagen Business School.

Vasquez, A., D. Amaya, N. D. Pearson, and P. A. Garcia-Ares (2025). 0dte index options and market volatility: How large is their impact? Working Paper 5113405, SSRN.

27

<!-- page: 29 -->

## Page 29

## Figures

## Figure 1: SPX put-vs-ATM skew, 0DTE volume share, and cross-tenor pre-and post-treatment means

This figure contains the 30-day SPX put-vs-ATM skew alongside the 0DTE share of total SPX option volume (Panel A), and pre- and post-treatment means of the put-vs-ATM skew across tenors (Panel B). Skew is the 25-delta put implied volatility minus the 50- delta put implied volatility at the indicated tenor, in percentage points. The 0DTE share is the share of total SPX option volume, in percent. Panel A: 21-day moving averages from 2018 through August 2025; skew on the left axis, 0DTE share on the right axis; the vertical dashed line marks May 16, 2022, the start of the first full five-day week with SPX 0DTE on every weekday. Panel B: pre- and post-treatment means at tenors of 7, 14, 30, 60, 91, 182, and 365 days on the main estimation window (pre: October 1, 2020 to May 15, 2022; post: May 16, 2022 to June 30, 2024); annotated values are post-minus-pre differences. Data are from OptionMetrics.

Panel A: 30-day SPX put-vs-ATM skew and 0DTE share, 2018-2025

Panel B: Pre- and post-treatment means across tenors

28

<!-- page: 30 -->

## Page 30

Figure 2: Quarterly event study of the SPX cross-tenor skew differential around the May 2022 0DTE expansion

This figure contains a quarterly event study of the SPX cross-tenor skew differential around the May 2022 0DTE expansion. The dependent variable is
s k _ { 3 0 , t } - s k _ { 3 6 5 , t }
, the difference between the 30-day and 365-day put-vs-ATM skew on date
t ,
in percentage points. Each point is the mean across trading days in calendar quarter
q   \in   [ - 6 , 8 ]
spanning Q4 2020 through Q2 2024. Coefficients are normalized to the average of all six pre-treatment quarters
q \in [ - 6 , - 1 ]
. The calendar quarter
q = 0
(Q2 2022) is split into q-pre (April 1 to May 15, 2022) and q-post (May 16 to June 30, 2022) to separate pre-and post-treatment observations within the contaminated calendar quarter. The vertical dashed line marks the May 16, 2022 event date. Whiskers are 95% confidence intervals from Newey-West HAC standard errors at 63 trading days (1 quarter) of lags.

29

<!-- page: 31 -->

## Page 31

Figure 3: Date placebo: quarterly event study of the SPX cross-tenor skew differential with placebo treatment quarter Q2 2021

This figure contains a quarterly event study of the SPX cross-tenor skew differential with the placebo treatment quarter set to Q2 2021, one year before the actual May 2022 event The dependent variable is
s k _ { 3 0 , t } - s k _ { 3 6 5 , t }
, the difference between the 30-day and 365-day put-vs-ATM skew, measured in percentage points. Each point is the mean across trading days in the indicated calendar quarter, normalized to
q   =   - 1
(Q1 2021). The sample runs from October 1, 2019 to June 30, 2024. The vertical orange dotted line at
q = - 0 . 5
marks the
\mathrm { Q 1 / Q 2 }
2021 boundary (placebo treatment); the vertical red dashed line at
q   =   3 . 5
marks the
\mathrm { Q 1 / Q 2 }
2022 boundary (actual May 16, 2022 treatment falls within
q = + 4 )
Whiskers are 95% confidence intervals from Newey-West HAC standard errors at 63 trading days (1 quarter) of lags.

30

<!-- page: 32 -->

## Page 32

Figure 4: Asset placebo: cross-tenor difference-in-differences coefficients for SPX and low-correlation control ETFs at the May 16, 2022 event date This figure contains cross-tenor difference-in-differences coefficients for SPX and two lowcorrelation control ETFs at the May 16, 2022 event date. The dependent variable is the 25-delta put implied volatility minus the 50-delta put implied volatility at tenor
T ,
measured in percentage points. Each bar is
\hat { \beta } _ { T }
from equation (2) estimated on the indicated asset's daily skew panel from October 1, 2020 to June 30, 2024, with a binary post-indicator at May 16, 2022 and the 365-day tenor as the omitted base SPX is the directly treated asset; TLT (long-duration Treasuries) and LQD (investmentgrade corporate bonds) are essentially uncorrelated with SPX skew innovations, with
| \rho ( \Delta s k _ { X } ^ { 3 0 } , \Delta s k _ { \mathrm { S P X } } ^ { 3 0 } ) | \; < \; 0 . 0 5
in first differences over January 2, 2018 to June 30, 2024. Whiskers are 95% confidence intervals from Newey-West HAC standard errors at 63 trading days (1 quarter) of lags (matching the daily-panel specification of Table 2)

31

<!-- page: 33 -->

## Page 33

Figure 5: Cross-tenor differential profile of typical aggregate shocks and the May 2022 break

This figure contains the cross-tenor differential profile
\beta _ { T } = \Delta s k _ { T } - \Delta s k _ { 3 6 5 }
across tenors. comparing typical aggregate pre-period shocks to the May 2022 break.
\beta _ { T }
is the difference in the change in the put-vs-ATM skew at tenor
T
and at the 365-day base, measured in percentage points and then rescaled so that
\beta _ { 3 0 } = 1
for each object. The blue line plots the median
\beta _ { T }
across the top five percent pre-period absolute daily
\Delta s k _ { \mathrm { 3 0 } }
moves on the SPX panel from October 1, 2020 to May 13, 2022; the shaded band is the corresponding interquartile range. The red line plots
\beta _ { T }
for the May 2022 cumulative break, computed as the difference in tenor-specific mean skew between the 63 calendar days before and after May 16, 2022.

32

<!-- page: 34 -->

## Page 34

## Figure 6: Random Forest counterfactual for the 30-day SPX put-vs-ATM skew

This figure contains a Random Forest counterfactual model fit on the 30-day SPX put-vs ATM skew. The dependent variable is the 25-delta put implied volatility minus the 50- delta put implied volatility at the 30-day tenor, measured in percentage points. Panel A plots the actual series in blue against the Random Forest prediction in red (dashed) Panel B plots the residual (actual minus predicted), evaluated out-of-sample from May 16. 2022 onwards. The model (500 trees, default depth) is fit on the pre-treatment sample from October 1, 2020 to May 15, 2022 on 19 non-option-derived predictors: 5-, 10-21-, 63-, and 126-day realized volatility of SPX returns; 21- and 63-day realized return skewness; 5-, 21-, and 63-day cumulative returns; 21- and 63-day downside realized semi variance; log(SP500), 21-day deviation from moving average, and 252-day drawdown; FOMC and CPI announcement-day dummies; and days-since-last-FOMC and days-to-next-FOMC counters. The pre-period in-sample
R ^ { 2 }
is 0.98 (Random Forest with default depth fits the training data near-perfectly by construction); honest out-of-sample fit within the pre-period is mean
R ^ { 2 } = 0 . 3 0
from K = 5 expanding-window cross-validation. The mean post-period residual is —2.22 pp. The vertical dotted line marks May 16, 2022

Panel A: Actual versus Random Forest predicted 30-day skew

Panel B: Residual (actual minus predicted)

33

<!-- page: 35 -->

## Page 35

## Tables

## Table 1: Summary statistics

Summary statistics for the variables used in the empirical analysis. The pre-treatment sample runs from October 1, 2020 to May 15, 2022, and the post-treatment sample runs from May 16, 2022 to June 30, 2024. Skew measures are in percentage points. Volume shares are in percent of total SPX option volume. Net put flow variables are signed daily customer net buying volume in contracts per day (positive = net buying). The seven days-to-expiration buckets are mutually exclusive and exhaustive and sum to total customer net put flow on each date. Flow variables come from the CBOE Open-Close Volume Summary file and use the same pre- and post-treatment window; the 0DTE row includes zeros on dates without a same-day expiration.

**[table]**

<table><tr><td rowspan="2">Variable</td><td colspan="3">Pre-treatment</td><td colspan="3">Post-treatment</td></tr><tr><td>N</td><td>Mean</td><td>Std</td><td>N</td><td>Mean</td><td>Std</td></tr><tr><td>SPX 30d put-vs-ATM skew (%)</td><td>408</td><td>4.80</td><td>0.82</td><td>533</td><td>2.37</td><td>0.82</td></tr><tr><td>SPX 30d 25∆ risk-rev (%)</td><td>408</td><td>7.59</td><td>1.67</td><td>526</td><td>4.13</td><td>1.49</td></tr><tr><td>SPX 30d ATM IV (%)</td><td>408</td><td>17.3</td><td>4.88</td><td>533</td><td>16.4</td><td>5.44</td></tr><tr><td>SPX 0DTE volume share (%)</td><td>408</td><td>19.5</td><td>15.1</td><td>533</td><td>45.1</td><td>4.99</td></tr><tr><td>Customer net 0DTE put flow (contracts/day)</td><td>408</td><td>+3,525</td><td>4,480</td><td>533</td><td>+14,799</td><td>7,779</td></tr><tr><td>(contracts/day) Customer net 1–2d put flow</td><td>408</td><td>-1,487</td><td>6,045</td><td>533</td><td>+5,620</td><td>13,302</td></tr><tr><td>Customer net 3–7d put flow (contracts/day)</td><td>408</td><td>-310.4</td><td>11,167</td><td>533</td><td>+3,120</td><td>11,515</td></tr><tr><td>Customer net 8–30d put flow (contracts/day)</td><td>408</td><td>+2,713</td><td>12,882</td><td>533</td><td>965.4</td><td>8,222</td></tr><tr><td>Customer net 31–91d put flow (contracts/day)</td><td>408</td><td>922.1</td><td>10,222</td><td>533</td><td>-88.2</td><td>8,438</td></tr><tr><td>Customer net 92–365d put flow (contracts/day)</td><td>408</td><td>178.5</td><td>5,104</td><td>533</td><td>+1,402</td><td>6,367</td></tr><tr><td>(contracts/day) Customer net 366+d put flow</td><td>408</td><td>362.1</td><td>1,615</td><td>533</td><td>576.0</td><td>1,507</td></tr></table>

34

<!-- page: 36 -->

## Page 36

**[table]**

Table 2: Cross-tenor difference-in-differences estimates of SPX put skew compression
This table reports estimates from cross-tenor difference-in-differences regressions of equation (2) on SPX. The dependent variable is the 25-delta put implied volatility minus the 50-delta put implied volatility at tenor T (the 25-delta put is the out-of-the-money put with Black-Scholes delta -0.25), measured in percentage points. Columns (1) and (2) use a binary post-indicator at May 16, 2022 Columns (3) and (4) replace it with the daily 0DTE share of total SPX option volume (continuous, averaging approximately 0.20 before treatment and 0.45 after treatment). Controls in columns (2) and (4) are
\log ( \mathrm { r v _ { 2 1 } } )
(log of 21-day realized volatility of SPX log-returns) and
r s _ { 2 1 }
(21-day realized return skewness). Option-derived controls are deliberately excluded because the treatment moves the option surface. The omitted tenor is 365 days. The sample runs from October 1, 2020 to June 30, 2024. Date and tenor fixed effects are absorbed. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.
<table><tr><td>Tenor</td><td>(1) Baseline</td><td>(2) Controls 十</td><td>(3) Dose-response</td><td>(4) Dose-resp + Controls</td></tr><tr><td>7d</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td>-0.10</td><td>-0.02</td><td>-0.34</td><td>-0.18</td></tr><tr><td>(−0.63)</td><td>(−0.14)</td><td>(−0.79)</td><td>(−0.43)</td></tr><tr><td rowspan="2">14d</td><td>-0.50</td><td>-0.42</td><td>-1.11</td><td>-0.90</td></tr><tr><td>(-3.54)</td><td>(-2.89)</td><td>(−3.11)</td><td>(-2.59)</td></tr><tr><td rowspan="2">30d</td><td>-0.72</td><td>-0.66</td><td>-1.66</td><td>-1.45</td></tr><tr><td>(−6.08)</td><td>(-5.80)</td><td>(−5.44)</td><td>(−5.12)</td></tr><tr><td rowspan="2">60d</td><td>-0.66</td><td>-0.62</td><td>-1.52</td><td>-1.34</td></tr><tr><td>(−5.84)</td><td>(-6.38)</td><td>(−5.32)</td><td>(−5.43)</td></tr><tr><td rowspan="2">91d 182d</td><td>-0.64</td><td>-0.63</td><td>-1.51</td><td>-1.37</td></tr><tr><td>(−6.24)</td><td>(−7.51)</td><td>(−5.73)</td><td>(−6.20)</td></tr><tr><td rowspan="2"></td><td>-0.51</td><td>-0.51</td><td>-1.24</td><td>-1.16</td></tr><tr><td>(-7.49)</td><td>(−10.55)</td><td>(−6.68)</td><td>(-7.68)</td></tr><tr><td>Treatment</td><td>Post</td><td>Post</td><td>0DTE share</td><td>0DTE share</td></tr><tr><td>Controls</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Date FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Tenor FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>6,587</td><td>6,587</td><td>6,587</td><td>6,587</td></tr><tr><td><eq>R ^ { 2 }</eq></td><td>0.252</td><td>0.276</td><td>0.162</td><td>0.193</td></tr></table>

35

<!-- page: 37 -->

## Page 37

## Table 3: Falsification: asset placebo and date placebo

This table reports falsification tests of the headline cross-tenor difference-in-differences specification. The dependent variable is the 25-delta put implied volatility minus the 50- delta put implied volatility at tenor T, measured in percentage points. Panel A reports
\hat { \beta } _ { T }
from equation (2) at the May 16, 2022 event date for SPX (the treated asset), TLT and LQD on the headline window from October 1, 2020 to June 30, 2024; first-differenced 30-day skew correlations with SPX are
\rho _ { \mathrm { T L T } } = - 0 . 0 3
and
\rho _ { \mathrm { L Q D } } = 0 . 0 4
. The 7-day tenor is omitted because LQD's 7-day coverage is incomplete on the estimation window; estimating SPX on the same 6-tenor panel makes the SPX coefficients and t-statistics in Panel A identical to Table 2 Column (1). Panel B gives the SPX cross-tenor coefficient at the actual May 2022 event date (column 1), the mean and standard deviation of the placebo coefficient distribution (column 2), and the percentile rank of the actual coefficient in that distribution (column 3); the placebo distribution comprises 82 pseudo-dates between January 2015 and October 2021 (one per month), with each placebo coefficient estimated on a ±6-month window centered on the pseudo-date. Panel B's column 1 uses the same ±6-month window for comparison with the placebos, while the headline-window SPX coefficient appears in Panel A and in Table 2. Date and tenor fixed effects are absorbed. The reported
R ^ { 2 }
is the
within-  R^{2}
of the panel fixed-effects fit, which can be slightly negative when the post-indicator and tenor dummies explain less variation than the demeaning baseline (as for TLT in Panel A). Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.

**[table]**

Panel A: Asset placebo at May 16, 2022
<table><tr><td>Panel A: Asset placebo at May 16, 2022 (3) (2) (1) Tenor</td></tr><tr><td>SPX (treated) TLT LQD</td></tr><tr><td>-0.50 0.12 -0.11 14d</td></tr><tr><td>(1.08) (-3.54) (−0.79) 30d 0.07 -0.72 -0.05</td></tr><tr><td>(0.74) (−6.08) (−0.43)</td></tr><tr><td>60d 0.09 -0.66 0.09</td></tr><tr><td>(−5.84) (0.93) (0.94) 91d 0.01 0.08 -0.64</td></tr><tr><td>(0.17) (−6.24) (0.90)</td></tr><tr><td>-0.01 182d -0.51 -0.11</td></tr><tr><td>(−0.23) (-7.49) (−1.64)</td></tr><tr><td>Yes Yes Yes Date FE</td></tr><tr><td>Yes Yes Yes Tenor FE</td></tr><tr><td>5,421 N 5,323 5,646</td></tr><tr><td>0.281 <eq>R ^ { 2 }</eq> -0.004 0.003</td></tr></table>

36

<!-- page: 38 -->

## Page 38

**[table]**

Table 3: Falsification (continued): Panel B.
<table><tr><td colspan="3">Panel B: Date placebo on SPX panel</td><td rowspan="2">(3)</td></tr><tr><td>Tenor</td><td>(1) Actual May 2022</td><td>(2) Placebo mean (std)</td></tr><tr><td>14d</td><td>-0.71</td><td>−0.06 (0.73)</td><td>Percentile rank 12%</td></tr><tr><td>30d</td><td>(-4.88) -0.81</td><td>–0.03 (0.59)</td><td>6%</td></tr><tr><td>60d</td><td>(−6.02) -0.69</td><td>−0.02 (0.49)</td><td>6%</td></tr><tr><td>91d</td><td>(−4.85) -0.70</td><td>–0.01 (0.40)</td><td>4%</td></tr><tr><td>182d</td><td>(-5.79) -0.54</td><td>0.00 (0.25)</td><td>4%</td></tr><tr><td></td><td>(-7.27)</td><td></td><td></td></tr><tr><td>Date FE Tenor FE</td><td>Yes Yes</td><td>Yes Yes</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>N R2</td><td>1,494 0.397</td><td>82 placebos</td><td>82 placebos</td></tr></table>

37

<!-- page: 39 -->

## Page 39

# Table 4: Holiday-window heterogeneity in the cross-tenor difference-in-differences estimate

This table reports the triple-DiD coefficient
\hat { \gamma } _ { T }
on
\mathrm { P o s t } _ { t } \mathrm { \times H o l C o u n t } _ { t , T } \mathrm { \times } \mathbf { 1 } [ T ]
in the pooled-panel regression

\begin{aligned} { s k _ { t , T } } & { { } = \alpha _ { T } + \delta _ { t } + \sum _ { T ^ { \prime } \neq 3 6 5 } \phi _ { T ^ { \prime } } \operatorname { H o l C o u n t } _ { t , T ^ { \prime } } \mathbf { 1 } [ T = T ^ { \prime } ] } \\ { } & { { } \quad + \sum _ { T ^ { \prime } \neq 3 6 5 } \beta _ { T ^ { \prime } } \operatorname { P o s t } _ { t } \mathbf { 1 } [ T = T ^ { \prime } ] } \\ { } & { { } \quad + \sum _ { T ^ { \prime } \neq 3 6 5 } \gamma _ { T ^ { \prime } } \operatorname { P o s t } _ { t } \operatorname { H o l C o u n t } _ { t , T ^ { \prime } } \mathbf { 1 } [ T = T ^ { \prime } ] } \\ { } & { { } \quad + \operatorname { c o n t r o l s } + \varepsilon _ { t , T } . } \\ \end{aligned}

where
s k _ { t , T }
is the put-vs-ATM skew at tenor
T
in percentage points and
\operatorname { H o l C o u n t } _ { t , T }
counts NYSE market holidays in
( t , t + T ]
calendar days. The panel stacks tenors
T \in \{ 7 , 1 4 , 3 0 , 6 0 , \dot { 9 } 1 , 1 8 2 , 3 6 5 \}
; the 365-day tenor is the omitted reference for all interaction terms.
\alpha _ { T }
and
\delta _ { t }
are tenor and date fixed effects. Column (1) is the baseline with no controls beyond fixed effects. Column (2) adds tenor-specific linear trends. Column (3) adds non-option realized controls-
\mathrm { - l o g ( r v _ { 2 1 } ) }
, log(rv63), rs21, rs63, cum21, and FOMC and CPI release-day indicators—each interacted with log T. The post period begins on May 16, 2022. The sample runs from October 1, 2020 to June 30, 2024. Coefficients are in percentage points. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.

**[table]**

<table><tr><td>Tenor</td><td>(1) (2)</td><td>(3)</td></tr><tr><td>7d</td><td>+0.29 +0.27 (+2.74)</td><td>+0.28 (+2.76)</td></tr><tr><td>14d</td><td>(+2.87) +0.05</td><td>+0.05 +0.04</td></tr><tr><td>30d</td><td>(+0.48) -0.01</td><td>(+0.35) (+0.56) -0.00 -0.00</td></tr><tr><td>60d</td><td>(−0.15) (−0.05) -0.02</td><td>(−0.00) +0.00 -0.02</td></tr><tr><td>91d</td><td>(+0.07) (−0.43) -0.05</td><td>(−0.39) -0.02 -0.04</td></tr><tr><td>182d</td><td>(−1.11) +0.01 (+0.17)</td><td>(−1.00) (−0.35) +0.01 +0.01 (+0.11) (+0.17)</td></tr><tr><td>Date FE</td><td>Yes</td><td>Yes Yes</td></tr><tr><td>Tenor FE</td><td>Yes Yes</td><td>Yes</td></tr><tr><td>Tenor-specific trends</td><td>No Yes</td><td>No</td></tr><tr><td>Controls</td><td>No No</td><td>Yes</td></tr><tr><td>N</td><td>6,587 6,587</td><td>6,587</td></tr><tr><td><eq>R ^ { 2 }</eq></td><td>0.249 0.258</td><td>0.066</td></tr></table>

38

<!-- page: 40 -->

## Page 40

## Appendix: Robustness Figures

## Figure A.1: Quarterly event study of the SPX cross-tenor skew differential under a multi-period reference

This figure contains the quarterly event study of the SPX cross-tenor skew differential
s k _ { 3 0 , q } - s k _ { 3 6 5 , q }
on the headline window (October 1, 2020 to June 30, 2024), in percentage points, with the entire calendar quarter
q = 0
(Q2 2022) excluded from the regression. The specification matches main-paper Figure 2 except for the treatment of the contaminated calendar quarter that contains the May 16, 2022 event date. Coefficients are normalized to the average of all six pre-treatment quarters
q \in [ - 6 , - 1 ]
. Whiskers are 95% confidence intervals from Newey-West HAC standard errors at 63 trading days (1 quarter) of lags.

39

<!-- page: 41 -->

## Page 41

Figure A.2: Cross-tenor differential profile on the long pre-period from January 2018

This figure contains the SPX cross-tenor differential profile
\beta _ { T }   =   \Delta s k _ { T }   -   \Delta s k _ { 3 6 5 }
on a longer pre-period beginning January 2018 instead of October 2020, and is the counterpart to main-paper Figure 5.
\beta _ { T }
is the difference in the change in the put-vs-ATM skew at tenor
T
and at the 365-day base, measured in percentage points and then rescaled so that
\beta _ { 3 0 }   =   1
for each object. The blue line plots the median
\beta _ { T }
across the top five percent pre-period absolute daily
\Delta s k _ { \mathrm { 3 0 } }
moves; the shaded band is the corresponding interquartile range. The red line plots
\beta _ { T }
for the May 2022 cumulative break, computed as the difference in tenor-specific mean skew between the 63 calendar days before and after May 16, 2022.

40

<!-- page: 42 -->

## Page 42

## Figure A.3: Random Forest counterfactual on the long pre-period from January 2018

This figure contains the Random Forest counterfactual for the 30-day SPX put-vs-ATM skew on a longer pre-period from January 2, 2018 to May 13, 2022, and is the counterpart to main-paper Figure 6. The predictor set is identical to that of Figure 6 (19 non-optionderived state variables). The dependent variable is the 25-delta put implied volatility minus the 50-delta put implied volatility at the 30-day tenor, measured in percentage points. Panel A plots the actual series against the Random Forest prediction; Panel B plots the residual (actual minus predicted). The mean post-period residual is -2.48 pp. The vertical dotted line marks May 16, 2022.

Panel A: Actual versus Random Forest predicted 30-day skew

Panel B: Residual (actual minus predicted)

41

<!-- page: 43 -->

## Page 43

## Figure A.4: Daily 0DTE option volume by underlying, 2018-2025

This figure contains daily 0DTE option activity by underlying for each of the eight tickers with 0DTE options on every day of the week, listed in Table A.6. Panel A plots 0DTE volume as a share of each ticker's total option volume, in percent, as a 21-trading-day rolling mean. Panel B plots daily 0DTE premium notional (volume × option midpoint price × $100 contract multiplier) on a log scale, also as a 21-trading-day rolling mean; this metric reflects dollar value traded rather than contract count and gives a fairer cross-ticker comparison when index levels differ by an order of magnitude (e.g. the cash SPX index approximately $5,000 vs the SPY ETF approximately $500). In both panels filled markers locate each underlying at its verified 5-day fully-daily 0DTE intro date (Table A.6); colors group by complex (S&P 500 in blues, Nasdaq-100 in reds, Russell 2000 in greens), and line style distinguishes index (solid), ETF (dashed), and mini contracts (dotted). The sample period is 2018 through 2025. Data are from OptionMetrics.

Panel A: 0DTE share of total option volume by underlying

Panel B: Daily 0DTE premium notional $/day by underlying (log scale)

42

<!-- page: 44 -->

## Page 44

## Appendix: Robustness Tables

**[table]**

Table A.1: Put-wing, call-wing, and put-wing-minus-call-wing skew compression
This table reports the cross-tenor difference-in-differences coefficient from equation (2) separately for put-wing skew, call-wing skew, and put-wing minus call-wing skew. Put-wing skew is the 25- delta put implied volatility minus at-the-money implied volatility; call-wing skew is at-the-money implied volatility minus 25-delta call implied volatility. The omitted tenor is 365 days. The sample runs from October 1, 2020 through June 30, 2024. Date and tenor fixed effects are absorbed. Newey-West t-statistics calculated with 63 trading days of lags appear in parentheses.
<table><tr><td>Tenor</td><td>Put wing</td><td>Call wing</td><td>Put wing minus call wing</td></tr><tr><td rowspan="2">7d</td><td>-0.10</td><td>+0.41</td><td>-0.51</td></tr><tr><td>(−0.63)</td><td>(+3.16)</td><td>(-4.69)</td></tr><tr><td rowspan="2">14d</td><td>-0.50</td><td>+0.07</td><td>-0.57</td></tr><tr><td>(-3.54)</td><td>(+0.61)</td><td>(−6.52)</td></tr><tr><td rowspan="2">30d</td><td>-0.72</td><td>-0.15</td><td>-0.57</td></tr><tr><td>(−6.08)</td><td>(-1.39)</td><td>(-8.06)</td></tr><tr><td rowspan="2">60d</td><td>-0.66</td><td>-0.16</td><td>-0.50</td></tr><tr><td>(−5.84)</td><td>(-1.54)</td><td>(-10.19)</td></tr><tr><td rowspan="2">91d</td><td>-0.64</td><td>-0.16</td><td>-0.49</td></tr><tr><td>(-6.24)</td><td>(-1.77)</td><td>(-10.92)</td></tr><tr><td rowspan="2">182d</td><td>-0.51</td><td>-0.10</td><td></td></tr><tr><td>(-7.49)</td><td>(−1.33)</td><td>-0.41 (−8.86)</td></tr></table>

## Table A.2: Historical frequency of persistent two-year SPX skew compression

**[table]**

This table compares the May 2022–June 2024 SPX episode with 86 two-year windows beginning between 2013 and March 2020. Each candidate window uses an 18-month pre-event mean and eight non-overlapping 91-day post-event bins. “Two-year mean" is the average post-minus-pre cross-tenor differential in percentage points. “Negative quarters' counts post-event bins below the pre-event mean. “More negative mean" counts historical windows with a more negative two-year mean than the actual episode. “Placebos all negative" counts historical windows with negative values in all eight bins. The historical windows overlap, so these comparisons describe historical frequency rather than randomization probabilities.
<table><tr><td>Outcome</td><td>Tenor</td><td>Two-year mean</td><td>Negative quarters</td><td>More negative mean</td><td>Placebos all negative</td></tr><tr><td>Put wing</td><td>30d</td><td>-0.70</td><td>8/8</td><td>0/86</td><td>7/86</td></tr><tr><td>Put wing</td><td>60d</td><td>-0.61</td><td>8/8</td><td>0/86</td><td>6/86</td></tr><tr><td>Put wing</td><td>91d</td><td>-0.60</td><td>8/8</td><td>0/86</td><td>2/86</td></tr><tr><td>Put wing minus call wing</td><td>30d</td><td>-0.60</td><td>8/8</td><td>0/86</td><td>5/86</td></tr><tr><td>Put wing minus call wing</td><td>60d</td><td>-0.51</td><td>8/8</td><td>0/86</td><td>2/86</td></tr><tr><td>Put wing minus call wing</td><td>91d</td><td>-0.49</td><td>8/8</td><td>0/86</td><td>1/86</td></tr></table>

43

<!-- page: 45 -->

## Page 45

## Table A.3: Counterfactual 30-day skew gaps through 2024Q2

**[table]**

This table reports realized 30-day SPX put-wing skew minus predictions from models estimated before May 16, 2022. OLS, gradient boosting (GB), and Random Forest (RF) use the 19 non-option-derived predictors described in Section 5.3. The post period runs from May 16, 2022 through June 30, 2024. Negative gaps indicate that realized skew is below the model prediction. Episode amounts apply each model's per-contract counterfactual price difference at 25 delta to observed open interest in 30–90-day SPX puts with deltas between -0.30 and -0.20 over the same period. The turnover convention uses open-interest-weighted maturity; the monthly convention assumes one roll per month These amounts are descriptive roll-cost equivalents over the bounded episode, not permanent annual savings or welfare estimates.
<table><tr><td>Model</td><td>Gap through 2024Q2 (pp)</td><td>Episode, turnover</td><td>Episode, monthly roll</td></tr><tr><td>OLS</td><td>-1.27</td><td>$0.87bn</td><td>$1.64bn</td></tr><tr><td>GB</td><td>-2.12</td><td>$1.45bn</td><td>$2.75bn</td></tr><tr><td>RF</td><td>-2.22</td><td>$1.52bn</td><td>$2.87bn</td></tr></table>

44

<!-- page: 46 -->

## Page 46

## Table A.4: Cross-tenor difference-in-differences across data sources and skewmeasurement conventions

This table reports estimates from the cross-tenor difference-in-differences specification of equation (2) across two data sources and three skew-measurement conventions. In every column the skew measure is the put-side smile slope
IV( OTM ) - IV( ATM )
at tenor T. in percentage points; columns differ in how the OTM point is identified and in which data source supplies the implied volatilities. The “OTM measure" row identifies the outof-the-money point: columns (1) and (2) use the put at delta -0.25 (the headline deltabased convention); column (3) uses the fixed dollar-moneyness strike K=0.95 S (5% outof-the-money put); column (4) uses the standardized-moneyness strike
K { = } S   e
-σATM√T (one
\sigma _ { \mathrm { A T M } } \sqrt { T }
below at-the-money), where
\sigma _ { \mathrm { A T M } }
is the same-tenor put 50-delta implied volatility. The "Data" row identifies the source: “Raw" denotes implied volatilities reconstructed from OptionMetrics raw daily option prices, interpolated using a monotone (Hermite) cubic spline applied to delta in column (1) (the Section 3 construction, with cross-expiration interpolation in maturity) and to strike in columns (3) and (4) (single nearest expiration); “Surface" denotes implied volatilities read from the OptionMetrics kernel-smoothed implied-volatility surface at its -25 and -50 delta nodes. The 14-day target in the "Raw" columns is mapped to the 10-day node of the "Surface" column the closest available. The post period begins on May 16, 2022 and the omitted tenor is 365 days. The sample runs from October 1, 2020 to June 30, 2024. Date and tenor fixed effects are absorbed. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.

**[table]**

<table><tr><td colspan="3">(1) OTM measure <eq>I V ( - 2 5 \Delta )</eq></td><td colspan="2">(3) (4) <eq>I V ( K / S { = } 0 . 9 5 )</eq> <eq>I V ( - 1 \sigma )</eq></td></tr><tr><td>Data</td><td>Raw</td><td><eq>I V ( - 2 5 \Delta )</eq> Surface</td><td>Raw</td><td>Raw</td></tr><tr><td>14d /  10d</td><td>-0.50</td><td>-0.61</td><td>-2.51</td><td>-0.32</td></tr><tr><td rowspan="3">30d</td><td>(-3.54)</td><td>(-4.35)</td><td>(-5.36)</td><td>(-1.72)</td></tr><tr><td>-0.72</td><td>-0.91</td><td>-1.76</td><td>-0.45</td></tr><tr><td>(−6.08)</td><td>(-8.37)</td><td>(-6.38)</td><td>(−2.63)</td></tr><tr><td>60d</td><td>-0.66</td><td>-0.83</td><td>-0.97</td><td>-0.39</td></tr><tr><td rowspan="3">91d</td><td>(−5.84)</td><td>(-8.50)</td><td>(-6.27)</td><td>(−2.40)</td></tr><tr><td>-0.64</td><td>-0.76</td><td>-0.64</td><td>-0.40</td></tr><tr><td>(-6.24)</td><td>(-9.60)</td><td>(-6.21)</td><td>(-2.70)</td></tr><tr><td rowspan="2">182d</td><td>-0.51</td><td>-0.51</td><td>-0.28</td><td>-0.34</td></tr><tr><td>(-7.49)</td><td>(-12.05)</td><td>(-6.73)</td><td>(-3.70)</td></tr><tr><td>Date FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Tenor FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>5,646</td><td>5,646</td><td>5,646</td><td>5,646</td></tr><tr><td><eq>R ^ { 2 }</eq></td><td>0.281</td><td>0.340</td><td>0.553</td><td>0.168</td></tr></table>

45

<!-- page: 47 -->

## Page 47

## Table A.5: Cross-tenor difference-in-differences estimates under alternative sample windows

This table reports estimates from the cross-tenor difference-in-differences specification of equation (2) under two alternative quarter windows around the Q2 2022 treatment quarter. The dependent variable is the 25-delta put implied volatility minus the 50-delta put implied volatility at tenor T, measured in percentage points. Column (1) uses the [-8,8] window (April 1, 2020 to June 30, 2024); column (2) uses the [-4,8] window (April 1, 2021 to June 30, 2024). The headline specification of Table 2 uses the [-6,8] window. The post period begins on May 16, 2022 and the omitted tenor is 365 days. Date and tenor fixed effects are absorbed. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients.

**[table]**

<table><tr><td colspan="2">(1)</td></tr><tr><td>Tenor</td><td>[−8, +8] window [−4, +8] window</td></tr><tr><td>14d</td><td>-0.54</td></tr><tr><td>30d</td><td>(-2.96) (−2.71) -0.82 -0.65 (-4.85) (−4.86)</td></tr><tr><td>60d</td><td>-0.82 -0.60</td></tr><tr><td>91d</td><td>(−4.56) (−5.04) -0.79 -0.59</td></tr><tr><td>182d</td><td>(-5.59) (-4.78) -0.46</td></tr><tr><td></td><td>-0.62 (−5.74) (−6.71)</td></tr><tr><td></td><td></td></tr><tr><td>Date FE</td><td>Yes</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>Tenor FE</td><td></td></tr><tr><td></td><td>Yes Yes</td></tr><tr><td></td><td>Yes</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>N</td><td>4,896</td></tr><tr><td></td><td>6,408</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>R2</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>0.255</td></tr><tr><td></td><td>0.283</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

46

<!-- page: 48 -->

## Page 48

## Table A.6: 0DTE rollout dates and 2024 total option activity by underlying

This table reports, for each underlying, the first full trading week with 0DTE expirations available on five weekdays, where that coverage persists for four consecutive weeks after accounting for holidays. Coverage is measured using distinct listed expiration dates in OptionMetrics raw daily data. The “0DTE max" column reports the maximum number of weekdays per week with sustained 0DTE coverage. Rows are grouped by underlying complex: S&P 500 (SPX cash index; XSP Mini-SPX cash index; SPY ETF), Russell 2000 (IWM ETF; RUT cash index; MRUT Mini-Russell 2000 cash index), Nasdaq 100 (NDX cash index; QQQ ETF), commodities (SLV silver ETF; GLD gold ETF), and bonds (TLT long-duration Treasury ETF; LQD investment-grade credit ETF). “2024 ADV" is quote-qualified total option volume averaged across the 252 trading days of 2024, in thousands of contracts. “2024 premium $M/day" is contract volume multiplied by the option midpoint price and contract multiplier. MRUT has a $100 contract multiplier and an underlying value equal to one-tenth of RUT. Among underlyings without fully-daily coverage, SLV, GLD, and TLT have sustained Monday, Wednesday, and Friday coverage, while LQD has Friday-only coverage. Bold rows identify SPX, the paper's focal market and the later RUT cash-index rollout; the remaining rows provide neutral institutional context. NDX, XSP, MRUT, QQQ, GLD, and SLV are not used in the empirical analysis; TLT and LQD enter only as low-correlation placebo markets.

**[table]**

<table><tr><td>Ticker</td><td>Type</td><td>secid</td><td>First full-week 0DTE week</td><td>0DTE max (days)</td><td>2024 ADV (k contracts)</td><td>2024 premium ($M/day)</td></tr><tr><td colspan="7">S&amp;P 500</td></tr><tr><td>SPX</td><td>Index</td><td>108105</td><td>2022-05-16</td><td>5</td><td>2,055</td><td>10,098</td></tr><tr><td>XSP</td><td>Index</td><td>189691</td><td>2022-10-10</td><td>5</td><td>55</td><td>19</td></tr><tr><td>SPY</td><td>ETF</td><td>109820</td><td>2022-11-14</td><td>5</td><td>6,413</td><td>1,502</td></tr><tr><td colspan="7">Russell 2000</td></tr><tr><td>IWM</td><td>ETF</td><td>106445</td><td>2024-04-22</td><td>5</td><td>1,234</td><td>318</td></tr><tr><td>RUT</td><td>Index</td><td>102434</td><td>2024-01-15</td><td>5</td><td>58</td><td>160</td></tr><tr><td>MRUT</td><td>Index</td><td>122700</td><td>2024-01-15</td><td>5</td><td>0.34</td><td>&lt;1</td></tr><tr><td colspan="7">Nasdaq 100</td></tr><tr><td>NDX</td><td>Index</td><td>102480</td><td>2022-09-19</td><td>5</td><td>37</td><td>389</td></tr><tr><td>QQQ</td><td>ETF</td><td>107899</td><td>2022-11-14</td><td>5</td><td>3,104</td><td>820</td></tr><tr><td colspan="7">Commodities</td></tr><tr><td>SLV</td><td>ETF</td><td>126776</td><td></td><td>3</td><td>315</td><td>27</td></tr><tr><td>GLD</td><td>ETF</td><td>122392</td><td></td><td>3</td><td>175</td><td>49</td></tr><tr><td colspan="7">Bonds</td></tr><tr><td>TLT</td><td>ETF</td><td>116070</td><td></td><td>3</td><td>401</td><td>58</td></tr><tr><td>LQD</td><td>ETF</td><td>116069</td><td></td><td>1</td><td>55</td><td>4</td></tr></table>

47

<!-- page: 49 -->

## Page 49

## Table A.7: Residual May 2022 cross-tenor break after partialling out a smooth secular trend

This table reports tests of whether the May 2022 cross-tenor break is a discrete event or the continuation of a smooth secular trend of the type documented by Dew-Becker and Giglio (2025). The test specification below is our own and is designed for a known candidate break date. For each tenor
T \in \{ 1 4 , 3 0 , 6 0 , 9 1 , 1 8 2 \}
, the daily SPX cross-tenor differential
s k _ { T } - s k _ { 3 6 5 }
(in percentage points) is fit on the long pre-window (January 2, 2018 to May 13, 2022), the model is projected forward into the post-treatment window (May 16, 2022 to June 30, 2024), and the residual May 2022 break
\hat { \delta }
is the mean of (actual - predicted) over the post period. Each cell is a separate per-tenor time-series OLS regression with its own pre
R ^ { 2 }
. Panel A pre-fits a linear time trend
\left( y _ { t } = \alpha   +   \gamma   t   +   \varepsilon _ { t } \right)
Panel B adds controls: the log of weekly realized SPX volatility, weekly realized return skewness, and the 21-day cumulative SPX return. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients and account for uncertainty in the pre-period trend and control coefficients used to form the post-period projections.

**[table]**

<table><tr><td>Panel A: Linear trend</td><td>(1) 14d</td><td>(2) 30d</td><td>(3) 60d</td><td>(4) 91d</td><td>(5) 182d</td></tr><tr><td>(post break) δ</td><td>-0.29 (−0.91)</td><td>-0.87 (−3.26)</td><td>-0.89 (−3.59)</td><td>-0.84 (−3.92)</td><td>-0.70 (−4.95)</td></tr><tr><td>Linear trend</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Pre N</td><td>1,089</td><td>1,089</td><td>1,089</td><td>1,089</td><td>1,089</td></tr><tr><td>Post N</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td></tr><tr><td><eq>R ^ { 2 }</eq> Pre</td><td>0.030</td><td>0.000</td><td>0.002</td><td>0.004</td><td>0.022</td></tr><tr><td>Panel B: Linear trend + controls</td><td>(1) 14d</td><td>(2) 30d</td><td>(3) 60d</td><td>(4) 91d</td><td>(5) 182d</td></tr><tr><td>δ (post break)</td><td>-0.19 (−0.62)</td><td>-0.76 (−3.18)</td><td>-0.78 (−4.23)</td><td>-0.75 (-5.37)</td><td>-0.65 (−6.94)</td></tr><tr><td>Linear trend</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Pre N</td><td>1,089</td><td>1,089</td><td>1,089</td><td>1,089</td><td>1,089</td></tr><tr><td>Post N</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td></tr><tr><td><eq>R ^ { 2 }</eq> Pre</td><td>0.500</td><td>0.473</td><td>0.518</td><td>0.537</td><td>0.504</td></tr></table>

48

<!-- page: 50 -->

## Page 50

Table A.8: Pre-trend tests, linear-extrapolation bias correction, and persistence diagnostics for the SPX cross-tenor differential

This table consolidates the Section 5.2 diagnostics for the SPX cross-tenor differential
s k _ { T } - s k _ { 3 6 5 }
on the main estimation window (October 1, 2020 to June 30, 2024; treatment May 16, 2022). Panel
\mathrm { A } ;
joint pre-trend F-tests at three pre-window lengths, a Newey-West HAC slope test on the pre-period daily 30-day differential, and the Q1 2022 quarterly deviation under single-reference (raw quarter mean) and multi-period
(q \in [-6, -1]
averaged) normalisations. Panel B: panel-spec bias-corrected difference-in-differences co-efficient
\hat { \beta } _ { T } ^ { \mathrm { B C } } = \hat { \beta } _ { T } - \hat { \gamma } _ { T }   \bar { t } _ { \mathrm { p o s t } }
at each short tenor, computed from a single regression that adds tenor-specific pre-period linear trends
\gamma _ { T } \underset {} { t } { \times } { \operatorname { P r e } } _ { t } { \times } \mathbf { 1 } [ T ]
to equation (2) together with the realized volatility
( \log ( \mathrm { r v _ { 2 1 } } ) )
and realized return skewness
\left( \mathrm { r s } _ { 2 1 } \right)
controls of Table 2 Column (2), each entering with saturated tenor-specific loadings; standard errors are Newey-West HAC at 63 trading days (1 quarter) of lags, with delta-method propagation of
\hat { \gamma } _ { T }
uncertainty. Panel C: persistence diagnostics on the 30-day differential: Augmented Dickey-Fuller test of pre-period stationarity, daily lag-1 autocorrelation
\hat { \rho }
with implied half-life − log 2/ log
\hat { \rho }
days, minimum mean across all 6-month (120 trading-day) rolling windows in the pre period, and post sample mean.

**[table]**

<table><tr><td rowspan="3"></td><td colspan="5">Tenor</td></tr><tr><td>7d</td><td>30d 14d</td><td>60d</td><td>91d</td><td>182d</td></tr><tr><td>Panel A: Pre-trend tests on the cross-tenor differential</td><td></td><td></td><td></td><td></td></tr><tr><td><eq>\left[ -6, +8 \right]</eq> window F(5) joint pre-trend, window F(7) joint pre-trend, <eq>\left[ -8, +8 \right]</eq></td><td colspan="6"><eq>8.04 (p &lt; 0.001)</eq> <eq>11.69 (p &lt; 0.001)</eq></td></tr><tr><td colspan="6"><eq>1 2 . 2 8 ( p &lt; 0 . 0 0 1 )</eq> F(11) joint pre-trend, [−12, +8] window Pre-period slope (daily 30d, NW HAC) −0.00006 pp/day, t = −0.13 <eq>\hat { \gamma } _ { \mathrm { p r e } }</eq></td></tr><tr><td colspan="6">-0.94pp Q1 2022 raw quarterly mean (30d) +0.37 pp Q1 2022 multi-ref dev. from pre-period baseline</td></tr><tr><td colspan="6">Panel B: Linear-extrapolation bias correction; controls included in the bias-corrected specification</td></tr><tr><td colspan="6"><eq>\hat { \beta } _ { T }</eq> -0.10 -0.50 -0.72 -0.66 -0.64 -0.51 Headline <eq>\hat { \beta } _ { T } ^ { \mathrm { B C } }</eq> -0.05-0.53-0.65-0.56-0.61-0.47 Bias-corrected <eq>t ^ { \mathrm { B C } }</eq></td></tr><tr><td colspan="6">-0.1 -1.2 -1.8 -1.6 -2.1 -3.4 Panel C: Persistence diagnostics on the 30d cross-tenor differential</td></tr><tr><td colspan="6">ADF p-value, pre-period (H0: unit root) <eq>p &lt; 0 . 0 0 0 1</eq></td></tr><tr><td colspan="6">0.83 AR(1) pre-period <eq>\hat { \rho } ,</eq></td></tr><tr><td colspan="6">Implied half-life of pre-period shocks (days) 3.8</td></tr><tr><td colspan="6">Pre 6-month rolling-window min mean (pp) -1.57 Post sample mean (pp)</td></tr><tr><td colspan="6">-2.03</td></tr></table>

49

<!-- page: 51 -->

## Page 51

Table A.9: Cross-tenor difference-in-differences conditional on contemporaneous realized volatility

This table reports the headline cross-tenor difference-in-differences with additional pertenor interactions on contemporaneous daily realized volatility. The dependent variable is the 25-delta put implied volatility minus the 50-delta put implied volatility at tenor
T ,
in percentage points. Both columns augment the headline specification (Table 2 Column (1)) with per-tenor interactions
r v _ { t }   \times   \mathbf { 1 } [ T ]
, where
r v _ { t }
is daily SPY annualized realized volatility computed from 15-minute mid-quote returns. Column (1) uses
r v _ { t }
directly; Column (2) uses
\log ( r v _ { t } )
. The post indicator turns on at May 16, 2022; the omitted tenor is 365 days. The sample runs from October 1, 2020 to June 30, 2024. Date and tenor fixed effects are absorbed. Newey-West t-statistics calculated using 63 trading days (1 quarter) of lags are reported in parentheses below the coefficients

**[table]**

<table><tr><td>Tenor</td><td>(1) (2)</td></tr><tr><td>7d</td><td>-0.11 -0.13 (−0.69)</td></tr><tr><td>14d</td><td>(−0.60) -0.50 -0.52</td></tr><tr><td>30d</td><td>(-3.47) (-3.39) -0.72 -0.74</td></tr><tr><td>60d</td><td>(-6.27) (−6.43) -0.66 -0.68</td></tr><tr><td>91d</td><td>(−6.84) (-7.13) -0.65 -0.66</td></tr><tr><td>182d</td><td>(-7.76) (-8.20) -0.52 -0.53 (-9.86) (-10.90)</td></tr><tr><td>Date FE</td><td>Yes Yes</td></tr><tr><td>Tenor FE</td><td>Yes Yes</td></tr><tr><td>Realized volatility interactions</td><td>Log Linear</td></tr><tr><td>N <eq>R ^ { 2 }</eq></td><td>6,587 6,587 0.306 0.316</td></tr></table>

50
