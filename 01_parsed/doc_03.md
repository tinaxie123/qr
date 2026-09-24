# doc_03 分数阶导数识别市场效率状态与粗糙波动

- source_path: `/Users/xiehaotong/Desktop/literature_pipeline/00_raw/期货日内因子_精选文献15篇/01_英文论文_微观结构与方法/03_分数阶导数识别市场效率状态与粗糙波动(GL).pdf`
- parser: `MinerU`
- mineru_version: `4.0.7`
- mineru_tier: `basic`
- ocr_mode: `auto`
- lang: en
- type: paper
- page_count: 36

<!-- page: 1 -->

## Page 1

arXiv:2606.27932v1 [q-fin.ST] 26 Jun 2026

# (In)Efficient Market States and Rough Volatility Detected via Grünwald-Letnikov Fractional Derivative

Daniele Angelini MEMOTEF, Sapienza University of Rome (Italy) daniele.angelini@uniroma1.it

## Abstract

Testing self-similarity in fractional processes from a single observed trajectory is difficult under long-range dependence, because the associated Kolmogorov–Smirnov (KS) statistic undergoes a phase transition when
H   >   1 / 2 .
In this regime, the classical limit collapses to a non-functional absolute Gaussian law and finite-sample convergence becomes severely distorted. This paper introduces a regime-adaptive KS/GL–KS framework based on the discrete Grünwald–Letnikov (GL) fractional derivative. The GL filter removes the low-frequency long-memory singularity while pre-serving the finite-dimensional H-self-similarity needed for distributional identification. We derive the filtered empirical-process limit, prove consistency and local asymptotic behavior of the resulting Hurst estimator, and validate the method through Monte Carlo simulations. Financial applications to realized volatility and equity index prices show how the procedure detects rough volatility and persistent, anti-persistent, or efficient market states.

Keywords:
Hurst exponent; Fractional processes; Kolmogorov–Smirnov test; Grünwald-Letnikov derivative

## 1 Introduction

Fractional Brownian motion (fBm), pioneered by Kolmogorov [18] and formalized by Mandelbrot and Van Ness [19], stands as a cornerstone stochastic framework for modeling complex systems that exhibit self-similarity, non-stationarity, and scaling behaviors. Fully characterized by its Hurst parameter
H \in ( 0 , 1 ]
, fBm has become indispensable across a multitude of quantitative disciplines, most notably in financial economics, where asset prices, exchange rates, and volatility dynamics frequently display persistent scaling laws. The increment process of fBm, known as fractional Gaussian noise (fGn), inherits this scaling behavior and exhibits a distinctive memory structure governed entirely by H. When
H   =   1 / 2
, fGn reduces to standard independent white noise; for
H   <   1 / 2
, it features anti-persistence or short-range dependence (SRD). Conversely, when
H   >   1 / 2
the process enters the long-range dependence (LRD) regime, where its autocovariance function decays non-integrably and its spectral density diverges at the origin.

In empirical applications, precisely identifying and validating the true self-similarity parameter H is a critical inferential task. Traditional estimation approaches for the Hurst exponent and long-range dependence are often based on moment or second-order scaling relations, including variance plots, rescaled-range methods, absolute-moment scaling, DFA-type procedures, and periodogram regression [24, 27]. Although these methods are widely used, their finite-sample behavior can be strongly affected by short records, trends, shifts in the mean, and scaling crossovers [25, 17]. Such effects may generate spurious evidence of persistence or distort the estimated scaling exponent, especially in financial series where structural breaks and heavy-tailed fluctuations are common. To mitigate these vulnerabilities,

1

<!-- page: 2 -->

## Page 2

recent advancements have introduced non-parametric, distribution-based approaches to evaluate self-similarity. By exploiting the strict invariance of rescaled increment distributions across varying time scales, one can define the diameter of a family of distributions, which theoretically achieves a global minimum of zero at the true parameter H. When applied to empirical data, this framework constructs a two-sample Kolmogorov–Smirnov (KS) type statistic from lagged increments extracted from a single observed trajectory [3].

However, applying this framework to time series encounters significant theoretical obstacles. Specifically, extracting rescaled processes from a single sample trajectory introduces a complex dependence structure that violates the core independence assumptions underlying the classical KS test. This issue manifests on two distinct fronts: the intradependence problem, which stems from the internal autocorrelation of the process governed by the self-similarity parameter H, and the interdependence problem, which arises from the statistical overlap among the extracted rescaled series [1]. Consequently, the standard KS distribution proves inadequate, necessitating an alternative asymptotic distribution that explicitly accounts for the H-induced dependence structure. While [1] partially mitigated these hurdles using a random permutation approach, this method remains computationally intensive and, crucially, introduces an additional source of estimation variance, thereby highlighting the need for an accelerated, robust analytical framework.

However, this transition is not merely computational; it is fundamentally dictated by the underlying stochastic properties of the process. As established in Propositions 2.2 and 2.3, the asymptotic behavior of this
\mathrm { K S - t y p e }
statistic undergoes a sharp, structurally disruptive phase transition at the critical threshold of
H = 0 . 1 / 2
. In the SRD and independent regimes
( H \leq 1 / 2 )
, the statistic converges swiftly to a theoretical limit defined by the supremum of a centered Gaussian process with an explicit covariance structure. Conversely, when
H > 1 / 2
the LRD regime necessitates a distinct normalization, as the limit collapses to a scaled absolute Gaussian random variable. As shown in Remark 2.4, the persistent, heavy correlation structures inherent to the LRD regime generate severe finite-sample distortions, leading to a slow rate of empirical convergence. This slow convergence fundamentally devalues the standard asymptotic distribution for
H   >   1 / 2 ,
, rendering the classical framework practically ineffective for robust hypothesis testing and goodness-of-fit verification in longmemory environments.

To overcome this issue, this paper presents a novel mathematical architecture designed to accelerate convergence by separating the long-range memory of the process from its self-similar scaling properties. We achieve this by filtering the fGn process through a discrete fractional transformation based on the Grünwald-Letnikov (GL) derivative. By applying a discrete GL derivative of order α, where α is strategically chosen such that
H - \alpha < 1 / 2
, we fundamentally re-engineer the low-frequency behavior of the stochastic process. In the frequency domain, while the spectral density of the original fGn blows up at the origin due to long memory, the spectral density of the GL-filtered process behaves asymptotically as
\tilde { f } ( \lambda ) \; \sim \; | \lambda | ^ { 1 - 2 ( \tilde { H } - \alpha ) }
as
\lambda \rightarrow 0
Because
H   -   \alpha   <   1 / 2
, the exponent becomes positive, effectively shifting the filtered process out of the LRD domain and into a short-memory, anti-persistent regime. Crucially, we prove that this fractional transformation decouples memory from scaling without disrupting the underlying self-similarity relation required for distributional self-similarity testing; the discrete GL derivative preserves the strict H-self-similarity in the sense of finite-dimensional distributions across distinct scales.

Building upon this theoretical mechanism, this paper pursues two main aims:

Derivation of the Asymptotic Distribution: Our first objective is to find and formalize the limiting distribution of the newly proposed Grünwald–Letnikov–Kolmogorov-Smirnov (GL-KS) test statistic for this transformed short-memory process. By successfully neutralizing the LRD via the GL filter, we bypass the correlation-induced slow convergence rates that plague the

2

<!-- page: 3 -->

## Page 3

classical test. We demonstrate that the empirical process of the GL-derivative adheres to shortrange dependence functional central limit theorems, enabling the GL-KS statistic to converge rapidly to the supremum of a well-defined, centered Gaussian process. This provides a robust, computationally viable diagnostic tool with stable critical values, even when the underlying original process exhibits extreme long memory.

Application to Finance: Our second objective is to showcase the practical utility of this accelerated framework within financial mathematics. Specifically, our methodology serves as a robust diagnostic tool to address key open questions in empirical finance, beginning with the validation of the rough volatility paradigm. By precisely testing the roughness parameter H, this approach enhances the modeling of asset price fluctuations, which is crucial for modern option pricing and risk management. More importantly, we contextualize the verification of the weak-form Efficient Market Hypothesis (EMH). In this context,
H = 1 / 2
represents the Brownian benchmark associated with the absence of statistically detectable persistence or anti-persistence in price increments. Confidence intervals lying entirely above or below
1 / 2
are interpreted as evidence of positive or negative inefficiency [4, 8], respectively, while intervals containing
1 / 2
are classified as statistically neutral.

The remainder of this paper is structured as follows. Section 2 reviews the mathematical preliminaries of fractional Brownian motion and details the convergence problem inherent to the long-memory KS test. Section 3 formalizes the discrete Grünwald-Letnikov derivative filter, detailing its action in both direct and spectral spaces and proving how it successfully splits memory from self-similarity. Section 3.2 presents our main theoretical contribution, deriving the limiting distribution of the accelerated GL-KS test statistic. Section 4 provides extensive numerical simulations validating the rapid convergence rates and finite-sample properties of the test. Section 5 presents the empirical application to financial time series, demonstrating the framework’s performance on real-world asset data. Finally, Section 6 concludes.

## 2 Preliminaries and problem statement

A fractional Brownian motion (fBm) with Hurst exponent
H   \in   ( 0 , 1 ]
is a centered Gaussian, non-stationary and self-similar process Bⁿ
B _ { t } ^ { H }
fully characterized by its covariance function

\mathbb { E } \left[ B _ { t } ^ { H } B _ { s } ^ { H } \right] = \frac { 1 } { 2 } \left( t ^ { 2 H } + s ^ { 2 H } - | t - s | ^ { 2 H } \right) .

By definition, fBm is an H-self-similar process
\scriptstyle { \left( H - \mathrm { s s } \right) }
, which implies the following scaling invariance in the sense of finite-dimensional distributions

\left\{ B _ { a t } ^ { H } \right\} _ { t \geq 0 } \overset { f . d . d . } { = } a ^ { H } \left\{ B _ { t } ^ { H } \right\} _ { t \geq 0 } , \qquad \forall a > 0 .

A core feature of fBm is that it is the unique mean-zero Gaussian process with stationary and self-similar increments. Its discrete-time increment process, known as fractional Gaussian noise (fGn)
Z _ { t , a }   =   B _ { t + a } ^ { H }   -   B _ { t } ^ { H }
, inherits this underlying scaling structure and serves as the standard statistical foundation for inference on fractional time series. Its covariance function is

\begin{array} { l } { K _ { H } ( k ) = K _ { Z _ { \cdot , a } ^ { H } } ( t - s ) = \frac { 1 } { 2 } \left[ | k + a | ^ { 2 H } + | k - a | ^ { 2 H } - 2 | k | ^ { 2 H } \right] , \quad t , s \geq 0 . } \\ \end{array}

3

<!-- page: 4 -->

## Page 4

From a spectral point of view, the covariance function can be represented as
\begin{array} { r } { K _ { H } ( k ) = \int _ { - \pi } ^ { \pi } e ^ { i k \lambda } f _ { H } ( \lambda ) d \lambda } \end{array}
where the spectral density is

\begin{array} { l l l } { f _ { H } ( \lambda ) } & { = } & { \frac { 1 } { 2 \pi } \displaystyle \sum _ { k \in \mathbb { Z } } K _ { H } ( k ) e ^ { - i k \lambda } } \\ { } & { = } & { \frac { \operatorname { s i n } ( \pi H ) \Gamma ( 2 H + 1 ) } { \pi } \left( 1 - \operatorname { c o s } ( \lambda ) \right) \displaystyle \sum _ { m \in \mathbb { Z } } | \lambda + 2 \pi m | ^ { - 2 H - 1 } , \quad \lambda \in [ - \pi , \pi ] . } \\ \end{array}\tag{1}

Writing
\begin{array} { r } { C _ { H } = \frac { \sin ( \pi H ) \Gamma ( 2 H + 1 ) } { \pi } } \end{array}
, near zero the spectral density boils down to

f _ { H } ( \lambda ) \sim C _ { H } | \lambda | ^ { 1 - 2 H } , \quad \lambda \to 0 .\tag{2}

The fGn inherits the property of self-similarity from the fBm. In particular, a fGn is
H - s s
in the sense of the finite-dimensional distributions

\left\{ { Z } _ { a t , a } ^ { H } \right\} _ { t \geq 0 } : = \left\{ { B } _ { a \left( t + 1 \right) } ^ { H } - { B } _ { a t } ^ { H } \right\} _ { t \geq 0 } \overset { f . d . d . } { = } { a } ^ { H } \left\{ { B } _ { t + 1 } ^ { H } - { B } _ { t } ^ { H } \right\} _ { t \geq 0 } = : { a } ^ { H } \left\{ { Z } _ { t , 1 } ^ { H } \right\} _ { t \geq 0 } .

From an empirical point of view, testing the previous self-similarity property of a finite fGn process is expensive in terms of the number of elements. In fact, simulating a fGn process of length N, the scaled fGn
Z _ { a t , a } ^ { H }
has only
N / a
elements. To overcome this issue, we give the following definition.

Definition 2.1.
Let
\left\{ Z _ { t , a } ^ { H } \right\} _ { t \geq 0 }
be a fGn with Hurst exponent
H \in ( 0 , 1 ]
and integer scaling parameter
a \geq 1
. A crossed fGn is defined as

G _ { a , r } ^ { H } ( t ) : = Z _ { r + a t , a } ^ { H } = B _ { r + a ( t + 1 ) } ^ { H } - B _ { r + a t } ^ { H } , \quad r = 0 , \ldots , a - 1 .

The union
\mathcal { B } _ { a } ^ { H } ( t ) = \bigcup _ { r = 0 } ^ { a - 1 } G _ { a , r } ^ { H } ( t )
represents the set of all fBm increments with lag a.

Clearly, fixing a branch
r ,
a crossed fGn
G _ { a , r } ^ { H } ( t )
is an H-ss process:

\left\{ G _ { a , r } ^ { H } ( t ) \right\} _ { t \geq 0 } \overset { { f . d . d . } } { = } \left\{ B _ { a ( t + 1 ) } ^ { H } - B _ { a t } ^ { H } \right\} _ { t \geq 0 } \overset { { f . d . d . } } { = } a ^ { H } \left\{ B _ { t + 1 } ^ { H } - B _ { t } ^ { H } \right\} _ { t \geq 0 } = : a ^ { H } \left\{ G _ { 1 , 0 } ^ { H } ( t ) \right\} _ { t \geq 0 } .

By the previous self-similarity property, the covariance function can be written as

K _ { G _ { a , r } ^ { H } } ( t - s ) = \mathbb { E } \left[ Z _ { r + a t , a } ^ { H } Z _ { r + a s , a } ^ { H } \right] = \mathbb { E } \left[ Z _ { a t , a } Z _ { a s , a } \right] = a ^ { 2 H } \mathbb { E } \left[ Z _ { t , 1 } ^ { H } Z _ { s , 1 } ^ { H } \right] = a ^ { 2 H } K _ { G _ { 1 , 0 } ^ { H } } ( t - s ) .

Therefore, the relation between the spectral density of an fGn
Z _ { t , a } ^ { H }
and a r-th crossed fGn
G _ { a , r } ^ { H } ( t )

f _ { G _ { a , r } ^ { H } } ( \lambda ) = a ^ { 2 H } f _ { H } ( \lambda ) .

## 2.1 Problem Statement and the Long-Memory Issue

Let
B ^ { H _ { 0 } } = \{ B _ { t } ^ { H _ { 0 } } \} _ { t \geq 0 }
be a fractional Brownian motion with unknown Hurst parameter
H _ { 0 } \in ( 0 , 1 )
defined on a probability space
( \Omega , \mathcal { F } , \mathbb { P } )
. Since
B ^ { H _ { 0 } }
has stationary and
H _ { 0 } \mathrm { - s e l f } \mathrm { - s i m i l a r }
increments, its increment process satisfies, for every integer scale
a \geq 1

\begin{aligned} { \big \{ B _ { a ( t + 1 ) } ^ { H _ { 0 } } - B _ { a t } ^ { H _ { 0 } } \big \} _ { t \geq 0 } \overset { f . d . d . } { = } a ^ { H _ { 0 } } \big \{ B _ { t + 1 } ^ { H _ { 0 } } - B _ { t } ^ { H _ { 0 } } \big \} _ { t \geq 0 } . } \\ \end{aligned}

To exploit this property without losing observations at large scales, we work with the crossed fractional Gaussian noises

G _ { a , r } ^ { H _ { 0 } } ( t ) : = B _ { r + a ( t + 1 ) } ^ { H _ { 0 } } - B _ { r + a t } ^ { H _ { 0 } } , \qquad r = 0 , \ldots , a - 1 ,

4

<!-- page: 5 -->

## Page 5

where t ranges over all indices such that the increment is contained in the observed path. For each fixed branch
r ,

\{ G _ { a , r } ^ { H _ { 0 } } ( t ) \} _ { t \geq 0 } \overset { f . d . d . } { = } a ^ { H _ { 0 } } \{ G _ { 1 , 0 } ^ { H _ { 0 } } ( t ) \} _ { t \geq 0 } .

Thus the unit-scale reference sample is

X _ { i } : = G _ { 1 , 0 } ^ { H _ { 0 } } ( i ) = B _ { i + 1 } ^ { H _ { 0 } } - B _ { i } ^ { H _ { 0 } } , \qquad i = 0 , \ldots , n ,\tag{3}

where
n = N - 1
, while, for a candidate value
\theta \in ( 0 , 1 )
, the rescaled crossed sample at scale
a > 1
is

Y _ { t , r } ^ { ( \theta ) } : = a ^ { - \theta } G _ { a , r } ^ { H _ { 0 } } ( t ) = a ^ { - \theta } \big ( B _ { r + a ( t + 1 ) } ^ { H _ { 0 } } - B _ { r + a t } ^ { H _ { 0 } } \big ) .\tag{4}

Pooling all branches gives
\textstyle \mathcal { { G } } _ { a } ^ { ( \theta ) } = \{ Y _ { t , r } ^ { ( \theta ) } : r = 0 , \ldots , a - 1 , t = 0 , \ldots , m _ { r } - 1 \} , \thinspace m = \sum _ { r = 0 } ^ { a - 1 } m _ { r } \simeq n

At the theoretical level, if
\theta \; = \; H _ { \mathrm { 0 , } }
then every rescaled crossed branch has the same finitedimensional distributions as the unit-scale fGn:

\{ Y _ { t , r } ^ { ( H _ { 0 } ) } \} _ { t \geq 0 } \overset { f . d . d . } { = } \{ X _ { i } \} _ { i \geq 0 } .

Equivalently, denoting by Φ the distribution function of
X _ { i } .
, one has

Y _ { t , r } ^ { ( \theta ) } \stackrel { d } { = } a ^ { H _ { 0 } - \theta } X _ { i } , \qquad \Phi _ { a , \theta } ( x ) : = \mathbb { P } ( Y _ { t , r } ^ { ( \theta ) } \leq x ) = \Phi \big ( a ^ { \theta - H _ { 0 } } x \big ) .

For a set of scales
\mathcal { A } = [ \underline { { a } } , \overline { { a } } ] \subset \mathbb { R } _ { + }
, define the family of rescaled distribution functions

\Psi _ { \theta } : = \{ \Phi _ { a , \theta } ( x ) : a \in \mathcal { A } , x \in \mathbb { R } \}

and its Kolmogorov-type diameter
\delta ( \theta ) : = \operatorname* { s u p } _ { x \in \mathbb { R } } \operatorname* { s u p } _ { a , b \in \mathcal { A } } \left| \Phi \big ( a ^ { \theta - H _ { 0 } } x \big ) - \Phi \big ( b ^ { \theta - H _ { 0 } } x \big ) \right| .

By Propositions 1-3 proved in [3], the diameter is minimized at the true self-similarity exponent: it is non-increasing for
\theta \leq H _ { 0 }
, non-decreasing for
\theta \geq H _ { 0 }
, and it increases away from zero as the scale interval is enlarged. Hence, in the population case,

H _ { 0 } = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { \theta \in ( 0 , 1 ) } \delta ( \theta ) .

Empirically, fixing
\underline { { a } } = 1
and
{ \overline { { a } } } = a
for simplicity, the unknown distribution functions are replaced by the empirical distribution functions

F _ { n } ( x ) : = \frac { 1 } { n } \sum _ { i = 0 } ^ { n - 1 } \mathbb { 1 } _ { \{ X _ { i } \leq x \} } , \qquad G _ { m } ^ { ( \theta ) } ( x ) : = \frac { 1 } { m } \sum _ { r = 0 } ^ { a - 1 } \sum _ { t = 0 } ^ { m _ { r } - 1 } \mathbb { 1 } _ { \{ Y _ { t , r } ^ { ( \theta ) } \leq x \} } .

Therefore, the empirical diameter becomes the two-sample Kolmogorov–Smirnov statistic

\widehat { \delta } _ { a } ( \theta ) : = D _ { n , m } ( \theta ) = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| F _ { n } ( x ) - G _ { m } ^ { ( \theta ) } ( x ) \right| ,

and the Hurst exponent is estimated by

\widehat { H } = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { \theta \in ( 0 , 1 ) } \widehat { \delta } _ { a } ( \theta ) .\tag{5}

More generally, when several scales are used, one may minimize

\widehat { \delta } _ { \mathcal { A } } ( \theta ) : = \operatorname* { s u p } _ { x \in \mathbb { R } } \operatorname* { s u p } _ { a , b \in \mathcal { A } } \left| \widehat { \Phi } _ { a } ^ { ( \theta ) } ( x ) - \widehat { \Phi } _ { b } ^ { ( \theta ) } ( x ) \right| , \qquad \widehat { H } = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { \theta \in ( 0 , 1 ) } \widehat { \delta } _ { \mathcal { A } } ( \theta ) .

5

<!-- page: 6 -->

## Page 6

The main difficulty is that the two empirical samples are not independent. They are extracted from the same sample path
B ^ { H _ { 0 } }
and therefore combine two sources of dependence: the cross-dependence induced by overlapping or nearby branches, and the internal temporal dependence governed by H. This affects both the asymptotic distribution of
D _ { n , m }
and the speed at which its finite-sample law approaches the limit.

The asymptotic behavior of the statistic splits into two regimes. In the present paper, these two regimes are used as a benchmark: they identify the obstruction that the Grünwald–Letnikov derivative is designed to remove in Section 3.

Throughout this section we consider only the balanced asymptotic regime
\textstyle n , m \to \infty , { \frac { n } { m } } \to 1
, or, equivalently,
\textstyle { \frac { n } { n + m } } \; \to \; { \frac { 1 } { 2 } }
. This is the regime corresponding to the empirical construction used in the applications, where the two samples have the same asymptotic size.

Proposition 2.2
(Short-memory benchmark). Assume that the auto-covariance and cross-covariance sequences associated with the two standardized increment samples are absolutely summable. Assume also that
\textstyle n , m \to \infty , { \frac { n } { m } } \to 1
. Then

D _ { n , m } ^ { \star } : = \sqrt { \frac { n m } { n + m } } D _ { n , m } \Rightarrow \operatorname* { s u p } _ { x \in \mathbb { R } } | U ( x ) | ,\tag{6}

where
U
is a centered Gaussian process with covariance kernel

\operatorname { C o v } ( U ( x ) , U ( y ) ) = \frac { 1 } { 2 } \Gamma _ { X } ( x , y ) + \frac { 1 } { 2 } \Gamma _ { Y } ( x , y ) - \frac { 1 } { 2 } \left[ \Gamma _ { X Y } ( x , y ) + \Gamma _ { Y X } ( x , y ) \right] .\tag{7}

Here
\Gamma _ { X }
and
\Gamma _ { Y }
are the long-run covariance kernels of the two marginal empirical processes, while Γ
XY
and
\Gamma _ { Y X }
are the corresponding cross-covariance kernels. In particular,
D _ { n , m } = O _ { P } \left( ( n \wedge m ) ^ { - 1 / 2 } \right)

Proof. See Appendix A.

In the short-memory regime, the KS statistic therefore retains the usual two-sample order. The limiting distribution is not the classical KS law, because the two samples are extracted from the same trajectory and are therefore cross-dependent, but the normalization remains the standard one.

Proposition 2.3
(Long-memory benchmark). Assume
H > 1 / 2
. Assume also that
\textstyle n , m \to \infty , { \frac { n } { m } } \to 1
Then

D _ { n , m } ^ { \diamond } : = \frac { n ^ { 1 - H } m ^ { 1 - H } } { n ^ { 1 - H } + m ^ { 1 - H } } D _ { n , m } \Rightarrow \frac { 1 } { \sqrt { 2 \pi } } | Z _ { 0 } | ,\tag{8}

where
\begin{array} { r } { Z _ { 0 } = \frac { 1 } { 2 } \left( Z _ { X } - Z _ { Y } \right) } \end{array}

Here
( Z _ { X } , Z _ { Y } )
is the centered Gaussian limit of the normalized linear partial sums

n ^ { - H } \sum _ { i = 1 } ^ { n } X _ { i } , \qquad m ^ { - H } \sum _ { j = 1 } ^ { m } Y _ { j } .

Consequently,
Z _ { 0 }
is centered Gaussian with variance
\begin{array} { r } { \sigma _ { 0 } ^ { 2 } = \frac { 1 } { 4 } \left( \sigma _ { X } ^ { 2 } + \sigma _ { Y } ^ { 2 } - 2 \sigma _ { X Y } \right) } \end{array}
, where

\sigma _ { X } ^ { 2 } = \operatorname* { l i m } _ { n \to \infty } n ^ { - 2 H } \operatorname { V a r } \left( \sum _ { i = 1 } ^ { n } X _ { i } \right) , \qquad \sigma _ { Y } ^ { 2 } = \operatorname* { l i m } _ { m \to \infty } m ^ { - 2 H } \operatorname { V a r } \left( \sum _ { j = 1 } ^ { m } Y _ { j } \right)

{ a n d } \quad \sigma _ { X Y } = \operatorname* { l i m } _ { n , m \to \infty } ( n m ) ^ { - H } \operatorname { C o v } \left( \sum _ { i = 1 } ^ { n } X _ { i } , \sum _ { j = 1 } ^ { m } Y _ { j } \right) .

6

<!-- page: 7 -->

## Page 7

Proof. See Appendix B.

Remark 2.4.
The long-memory case is substantially more delicate from a statistical point of view. Although the limiting statistic is simpler, since the functional limit collapses to the deterministic profile ϕ(x) multiplied by a single Gaussian random variable, the convergence to this limit may be slow.

The reason is that the centered indicator admits the Gaussian projection decomposition

\mathbb { 1 } _ { \{ Z \leq x \} } - \Phi ( x ) = - \phi ( x ) Z + r _ { x } ( Z ) , \qquad \mathbb { E } [ r _ { x } ( Z ) Z ] = 0 ,

where
Z \sim \mathcal { N } ( 0 , 1 )
The first term produces the limiting profile
\phi ( x )
, while the residual term
r _ { x } ( Z )
is asymptotically negligible only at a rate depending on the strength of the long-range dependence.

More precisely, after removing the leading linear projection, the residual empirical process
R _ { n , m }
satisfies, for
n \asymp m ,

\left\| \operatorname* { s u p } _ { x \in \mathbb { R } } | R _ { n , m } ( x ) | \right\| _ { L ^ { 2 } } =  \begin{cases} { \mathcal { O } \left( ( n \wedge m ) ^ { 1 / 2 - H } \right) , } & { 1 / 2 < H < 3 / 4 , } \\ { \mathcal { O } \left( ( n \wedge m ) ^ { - 1 / 4 } \sqrt { \operatorname { l o g } ( n \wedge m ) } \right) , } & { H = 3 / 4 , } \\ { \mathcal { O } \left( ( n \wedge m ) ^ { H - 1 } \right) , } & { 3 / 4 < H < 1 . } \\ \end{cases}

Thus, the closer H is to one, the slower the residual component vanishes. This explains why the KS statistic becomes progressively less stable in the long-memory regime: finite-sample deviations from the asymptotic law persist for much longer samples.

The Grünwald–Letnikov transformation introduced below is designed precisely to remove this longmemory obstruction before applying the Kolmogorov–Smirnov comparison. By weakening the lowfrequency persistence of the increment process, the filtered statistic is brought back to a short-memory empirical-process regime, where the convergence to the limiting law is substantially more stable.

Remark 2.5.
At first sight, since fBm is Gaussian, the study of its first two moments would be sufficient to characterize its finite-dimensional distributions. In this sense, for a purely Gaussian
f B m ,
a covariance-based approach would already contain the full probabilistic information.

**[table]**

Table 1: Long-lag dependence in representative fractional processes.
<table><tbody><tr><td>Process</td><td>Asymptotic behavior</td><td>Key parameter</td></tr><tr><td>fGn</td><td>E[Z<sub>t</sub>Z<sub>t+τ</sub>] ∼ |τ|2H<sup>-2</sup></td><td>H ∈ (0,1)</td></tr><tr><td>fPP</td><td>E[N(t)N(t + τ)] ∼ |τ|-<sup>α</sup></td><td>α ∈ (0,1)</td></tr><tr><td>fLm</td><td>E[L<sub>H</sub>(t)L<sub>H</sub>(t + τ)] ∼ |τ|2H<sup>-2</sup></td><td>H ∈ (0,1)</td></tr><tr><td>ARFIMA</td><td>ρ(τ) ∼ |τ|2d<sup>-1</sup></td><td>d ∈ (0,1/2)</td></tr><tr><td>fOU, Langevin type</td><td>γ(τ) ∼ C<sub>H</sub>,λ|τ|2H<sup>-2</sup></td><td>H ∈ (0,1)</td></tr><tr><td>fOU, Lamperti type</td><td>γ(τ) ∼ Ce-λτ</td><td>H ∈ (0,1)</td></tr></tbody></table>

Notes. fGn denotes fractional Gaussian noise; fPP fractional Poisson process; fLm fractional Lévy motion; ARFIMA autoregressive fractionally integrated moving average; fOU fractional Ornstein–Uhlenbeck process. The table is intended only as a qualitative benchmark: the listed processes are not assumed to be distributionally equivalent to fGn. In infinite-variance Lévy-type settings, covariance-based expressions must be replaced by appropriate dependence notions such as codifference or covariation.

The reason for adopting a distributional KS criterion is different. The aim is not only to recover the covariance structure of Gaussian fBm, but to build a non-parametric self-similarity diagnostic that can be transported, at least in principle, to broader classes of fractional processes. In such settings, the first two moments may be insufficient, unstable, or even undefined. A distributional comparison

7

<!-- page: 8 -->

## Page 8

of rescaled increments is therefore more flexible: it tests the scaling relation directly at the level of empirical distributions rather than only through moment scaling.

The fGn is used here as the canonical benchmark because it is the stationary increment process of fBm, it has an explicit covariance and spectral structure, and it exhibits the standard powerlaw memory pattern governed by the Hurst exponent. Moreover, many fractional models used in applications display analogous hyperbolic memory, or can be compared with fGn at the level of their long-lag dependence. Table 1 summarizes the relevant asymptotic regimes. The purpose of the table is not to claim that all these models are identical to fGn, but to justify why fGn provides the natural reference model for deriving the asymptotic theory developed below.

## 3 Grünwald-Letnikov-Kolmogorov–Smirnov test

To overcome the slow empirical convergence rates caused by LRD inside the classical KS test framework, we introduce in Section 3.1 a mathematical architecture designed to accelerate convergence by decoupling the long-memory properties of the process from its underlying self-similar scaling behavior. This is achieved by filtering the fGn through a discrete fractional transformation based on the Grünwald-Letnikov (GL) derivative. In Section 3.2 we will introduce the KS asymptotic distribution for LRD after a GL filtration.

## 3.1 Grünwald-Letnikov filter

Definition 3.1
(Discrete Grünwald-Letnikov derivative [21]). The discrete Grünwald-Letnikov derivative of order
\alpha \in \mathbb { R } ^ { + }
with step size
h > 0
for a real-valued function
f ( x ) \in \mathbb { R }
is defined as:

\Delta _ { h } ^ { { G L } , \alpha } f ( x ) = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } ( - 1 ) ^ { k } \binom { \alpha } { k } f ( x - k h ) = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) f ( x - k h ) ,\tag{9}

where the GL binomial coefficients
\begin{array} { r } { \omega _ { k } ( \alpha ) = \frac { \Gamma ( k - \alpha ) } { \Gamma ( - \alpha ) \Gamma ( k + 1 ) } } \end{array}

In terms of the lag operator
L _ { h } f ( x ) : = f ( x   -   h )
, and the repeated lag operator
L _ { h } ^ { k } f ( x ) : = f ( x   -   h k )
the discrete GL derivative operator can be compactly expressed as a fractional power of the differencing operator:

\Delta _ { h } ^ { G L , \alpha } f ( x ) = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) L _ { h } ^ { k } f ( x ) = h ^ { - \alpha } ( 1 - L _ { h } ) ^ { \alpha } f ( x ) .\tag{10}

## 3.1.1 Filter application at the direct space

We now explore how the GL filter acts upon fractional Brownian motion and its increments in the time domain, focusing specifically on how it modifies the self-similarity index depending on the choice of the scaling operator definition.

Proposition 3.2.
Let
B _ { t } ^ { H }
be a fBm with Hurst exponent
H   \in   ( 0 , 1 )
, and let
a   \in   \mathbb { R } ^ { + }
be a scale parameter. Then, the discrete GL derivative applied to the fBm process is
H - s s .

\Delta _ { h } ^ { G L , \alpha } B _ { a t } ^ { H } \stackrel { f . d . d . } { = } a ^ { H } \cdot \Delta _ { h } ^ { G L , \alpha } B _ { t } ^ { H } .\tag{11}

8

<!-- page: 9 -->

## Page 9

Proof. To establish (11), we expand the definition of the derivative operator
\Delta _ { h } ^ { G L , \alpha }
and utilize the intrinsic H-self-similarity of the underlying fBm process
( B _ { a t } ^ { H } \stackrel { f . d . d . } { = } a ^ { H } B _ { t } ^ { H } )
:

\Delta _ { h } ^ { { G L } , \alpha } B _ { a t } ^ { H } = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) B _ { a ( t - k h ) } ^ { H } \overset { f . d . d . } { = } a ^ { H } \left( \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) B _ { t - k h } ^ { H } \right) = a ^ { H } \cdot \Delta _ { h } ^ { { G L } , \alpha } B _ { t } ^ { H } .

The core operational breakthrough of this paper relies on applying this filtering technique to the crossed fGn framework defined in Section 2. The next proposition guarantees that filtering the multi-scale branches preserves the exact distributional scaling law required for our test statistic in the finite-dimensional sense.

Proposition 3.3.
The discrete Grünwald-Letnikov derivative
\Delta _ { h } ^ { G L , \alpha }
of a crossed fGn process
G _ { a , r } ^ { H } ( t )
remains strictly H-self-similar for any scale
a \geq 1
and branch
r = 0 , \ldots , a - 1

\Delta _ { h } ^ { G L , \alpha } G _ { a , r } ^ { H } ( t ) \stackrel { f . d . d . } { = } a ^ { H } \cdot \Delta _ { h } ^ { G L , \alpha } G _ { 1 , 0 } ^ { H } ( t ) .

Proof. By mapping the definition of the crossed fGn
G _ { a , r } ^ { H } ( t ) = B _ { r + a ( t + 1 ) } ^ { H }   -   B _ { r + a t } ^ { H }
into the GL operator, we obtain:

\Delta _ { h } ^ { G L , \alpha } G _ { a , r } ^ { H } ( t ) = \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) \left( B _ { r + a ( t - k h + 1 ) } ^ { H } - B _ { r + a ( t - k h ) } ^ { H } \right) .

Since fBm features strictly stationary increments, the deterministic time shift r can be dropped without modifying the joint finite-dimensional distributions of the process:

\Delta _ { h } ^ { { G L } , \alpha } G _ { a , r } ^ { H } ( t ) \stackrel { { f . d . d . } } { = } \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) \left( B _ { a ( t - k h + 1 ) } ^ { H } - B _ { a ( t - k h ) } ^ { H } \right) .

Finally, factoring out the scale parameter a using the H-self-similarity of fBm yields the targeted relation:

\begin{array} { l l l } { \Delta _ { h } ^ { G L , \alpha } G _ { a , r } ^ { H } ( t ) } & { \overset { f . d . d . } { = } } & { a ^ { H } \left[ \frac { 1 } { h ^ { \alpha } } \sum _ { k = 0 } ^ { \infty } \omega _ { k } ( \alpha ) \left( B _ { t - k h + 1 } ^ { H } - B _ { t - k h } ^ { H } \right) \right] } \\ { } & { = } & { a ^ { H } \cdot \Delta _ { h } ^ { G L , \alpha } G _ { 1 , 0 } ^ { H } ( t ) . } \\ \end{array}

This completes the proof.

Corollary 3.4 (Identification invariance under GL filtering). Let
B ^ { H _ { 0 } }
be an fBm with
H _ { 0 } \in ( 0 , 1 )
and let
\vec { T _ { \alpha } } = \sigma _ { \alpha , h } ^ { - \vec { 1 } } \Delta _ { h } ^ { G L , \alpha }
be the standardized GL filter, with
\alpha \geq 0
. For a fixed scale
a > 1
, define the population filtered KS criterion

D _ { \alpha } ( \theta ) = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \Phi _ { \alpha } ( x ) - \Phi _ { \alpha } \left( a ^ { \theta - H _ { 0 } } x \right) \right| ,

where
\Phi _ { \alpha }
is the distribution function of
T _ { \alpha } G _ { 1 , 0 } ^ { H _ { 0 } }
. Then

D _ { \alpha } ( \theta ) = 0 \quad \Longleftrightarrow \quad \theta = H _ { 0 } .

Therefore, the GL transformation preserves the population identification of the Hurst exponent. It may change the empirical criterion and its asymptotic covariance structure, but it does not change the self-similarity parameter identified by the minimum-distance problem.

Proof. By Proposition 3.3,

T _ { \alpha } G _ { a , r } ^ { H _ { 0 } } \overset { f . d . d . } { = } a ^ { H _ { 0 } } T _ { \alpha } G _ { 1 , 0 } ^ { H _ { 0 } } .

After rescaling by
a ^ { - \theta }
, the filtered multi-scale sample has distribution
a ^ { H _ { 0 } - \theta } T _ { \alpha } G _ { 1 , 0 } ^ { H _ { 0 } }
Hence, its distribution coincides with that of the unit-scale filtered sample if and only if
a ^ { H _ { 0 } - \theta } = \dot { 1 }
. Since
a > 1
, this is equivalent to
\theta = H _ { 0 }
. Therefore, the population KS diameter is uniquely minimized at
H _ { 0 }
□

9

<!-- page: 10 -->

## Page 10

## 3.1.2 Filter application at the spectral space

While Proposition 3.3 establishes that the GL filter leaves the structural scaling multiplier
a ^ { H }
perfectly intact across scales, we now demonstrate its effect in the frequency domain, proving that it simultaneously eliminates the long-memory singularity at the origin.

Let
Y _ { a , r } ^ { H , \alpha } ( t ) : = \Delta _ { h } ^ { G L , \alpha } G _ { a , r } ^ { H } ( t )
denote the GL-filtered crossed fGn process. Its spectral characterization is formalized below.

Proposition 3.5.
The spectral density of the discrete GL-filtered crossed fGn process
Y _ { a , r } ^ { H , \alpha } ( t )
is given by:

f _ { Y } ^ { ( h ) } ( \lambda ) = a ^ { 2 H } h ^ { - 2 \alpha } \left| 1 - e ^ { - i h \lambda } \right| ^ { 2 \alpha } f _ { H } ( \lambda ) , \quad \lambda \in [ - \pi , \pi ] ,\tag{12}

where
f _ { H } ( \lambda )
represents the spectral density of the unscaled fGn process (Equation (1)).

Proof. The discrete GL derivative operator
\Delta _ { h } ^ { G L , \alpha }   =   h ^ { - \alpha } ( 1 - L _ { h } ) ^ { \alpha }
represents a linear filter whose characteristic transfer function in the frequency domain is given by
A _ { \alpha , h } ( \lambda ) = h ^ { - \alpha } ( 1   -   e ^ { - i h \lambda } ) ^ { \alpha }
. Under linear filtering theory, the spectral density of the output process is equal to the spectral density of the input process multiplied by the squared modulus of the transfer function:

f _ { Y } ^ { ( h ) } ( \lambda ) = \left| A _ { \alpha , h } ( \lambda ) \right| ^ { 2 } f _ { G _ { a , r } ^ { H } } ( \lambda ) = \frac { 1 } { h ^ { 2 \alpha } } \left| 1 - e ^ { - i h \lambda } \right| ^ { 2 \alpha } f _ { G _ { a , r } ^ { H } } ( \lambda ) .

Substituting the crossed fGn spectral relation
f _ { G _ { a , r } ^ { H } } ( \lambda )   =   a ^ { 2 H } f _ { H } ( \lambda )
into the filter formula directly yields (12), completing the proof. □

Proposition 3.6.
In the low-frequency limit
\lambda \to 0
, the spectral density of the filtered process
Y _ { a , r } ^ { H , \alpha } ( t )
behaves as:

f _ { Y } ^ { ( h ) } ( \lambda ) \sim a ^ { 2 H } C _ { H } | \lambda | ^ { 1 - 2 ( H - \alpha ) } , \quad \mathit { a s } \lambda \to 0 ,\tag{13}

where
\begin{array} { r } { C _ { H } = \frac { \sin ( \pi H ) \Gamma ( 2 H + 1 ) } { \pi } } \end{array}

Proof. We examine the asymptotic behavior of the individual terms in Equation (12) as
\lambda \to 0
. First, applying a first-order Taylor expansion to the exponential component of the transfer function yields:

\left| 1 - e ^ { - i h \lambda } \right| ^ { 2 \alpha } = \left| 1 - \left( 1 - i h \lambda + \mathcal { O } ( \lambda ^ { 2 } ) \right) \right| ^ { 2 \alpha } \sim | i h \lambda | ^ { 2 \alpha } = h ^ { 2 \alpha } | \lambda | ^ { 2 \alpha } .

Second, from Equation (2), we know that the unscaled fGn spectral density scales near the origin as
f _ { H } ( \lambda ) \sim C _ { H } | \lambda | ^ { 1 - 2 H }
. Combining these limits inside the expression for
f _ { Y } ^ { ( h ) } ( \lambda )
leads to:

f _ { Y } ^ { ( h ) } ( \lambda ) \sim \left( \frac { 1 } { h ^ { 2 \alpha } } \right) \left( h ^ { 2 \alpha } | \lambda | ^ { 2 \alpha } \right) \left( a ^ { 2 H } C _ { H } | \lambda | ^ { 1 - 2 H } \right) = a ^ { 2 H } C _ { H } | \lambda | ^ { 2 \alpha + 1 - 2 H } .

Gathering the exponents of
| \lambda |
simplifies the expression directly to
a ^ { 2 H } C _ { H } | \lambda | ^ { 1 - 2 ( H - \alpha ) }
, completing the proof. □

By choosing a fractional filter order α such that
H   -   \alpha \; < \; 1 / 2
, the exponent
1   -   2 ( H   -   \alpha )
in Equation (13) becomes strictly positive. Consequently, the spectral density no longer diverges at the origin lim
\operatorname { h } _ { \lambda \to 0 } f _ { Y } ^ { ( h ) } ( \lambda ) = 0
, meaning the long-memory singularity is successfully removed. The filtering operation shifts the process out of the LRD domain and into a short-memory or anti-persistent domain while preserving the scaling constant
a ^ { 2 H }
intact. This dual feature provides the mathematical framework required to derive stable, fast-converging non-parametric test statistics under short-range dependence functional limit theorems, as formalized in Section 3.2.

10

<!-- page: 11 -->

## Page 11

## 3.2 KS asymptotic distribution for LRD

Having established that the discrete Grünwald-Letnikov filter maps a long-memory fractional Gaussian noise into a SRD regime while preserving its exact finite-dimensional scaling laws, we are now positioned to derive the asymptotic distribution of the accelerated test statistic.

Before introducing the filtered samples, we specify the null hypothesis considered in this subsection. For a fixed
H _ { 0 } \in ( 1 / 2 , 1 )
, the null hypothesis is the correctly specified self-similarity relation

\mathcal { H } _ { 0 } ( H _ { 0 } ) : \qquad \left\{ a ^ { - H _ { 0 } } G _ { a , r } ^ { H _ { 0 } } ( t ) \right\} _ { t \geq 0 } \overset { { f . d . d . } } { = } \left\{ G _ { 1 , 0 } ^ { H _ { 0 } } ( t ) \right\} _ { t \geq 0 } , \qquad r = 0 , \ldots , a - 1 .

This is not the classical independence null of the two-sample KS test, since both samples are extracted from the same trajectory. The aim is to derive the limiting law of the KS distance under this dependent self-similarity null.

Let
\{ X _ { i } \} _ { i = 1 } ^ { n }
and
\{ Y _ { t , r } \} ( t = 0 , \ldots , m _ { r } - 1 ; \thinspace r = 0 , \ldots , a - 1 )
be the unit-lag and pooled multi-scale samples defined in Equations (3) and (4) with
\theta = H _ { 0 }
, respectively. We apply the pre-scaled discrete GL derivative operator
\Delta _ { h } ^ { G L , \alpha }
of order
\alpha > H _ { 0 } - 1 / 2
to both samples. Under
\mathcal { H } _ { 0 } ( H _ { 0 } )
, we normalize the filtered increments by their common theoretical standard deviation
\sigma _ { \alpha , h } : = \left( \mathbb { E } \left[ ( \Delta _ { h } ^ { G L , \alpha } X _ { 1 } ) ^ { 2 } \right] \right) ^ { 1 / 2 }
This yields the standardized, GL-filtered stochastically equivalent sequences:

\tilde { X } _ { i } = \frac { 1 } { \sigma _ { \alpha , h } } \Delta _ { h } ^ { G L , \alpha } X _ { i } , \quad \tilde { Y } _ { t , r } = \frac { 1 } { \sigma _ { \alpha , h } } \Delta _ { h } ^ { G L , \alpha } Y _ { t , r } .

The pooled multi-scale filtered sample
\{ \tilde { Y } _ { j } \} _ { j = 1 } ^ { m }
is constructed by aggregating all branches
\tilde { Y } _ { t , r } ,
maintaining a total sample size of
\begin{array} { r } { m   =   \sum _ { r = 0 } ^ { a - 1 } \dot { m _ { r } }   \approx   n } \end{array}
. Under
\mathcal { H } _ { 0 } ( H _ { 0 } )
, Proposition 3.3 guarantees that
\tilde { X } _ { i } \stackrel { d } { = } \tilde { Y } _ { j } \sim \mathcal { N } ( 0 , 1 )
marginally, and their joint finite-dimensional distributions satisfy
\{ \tilde { Y } _ { t , r } \} _ { t \geq 0 } \stackrel { f . d . d . } { = }
\{ \tilde { X } _ { i } \} _ { i \geq 1 }

We define the corresponding ECDFs of the filtered samples as:

\tilde { F } _ { n } ( x ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbb { 1 } _ { \{ \tilde { X } _ { i } \leq x \} } , \quad \tilde { G } _ { m } ( x ) = \frac { 1 } { m } \sum _ { r = 0 } ^ { a - 1 } \sum _ { t = 0 } ^ { m _ { r } - 1 } \mathbb { 1 } _ { \{ \tilde { Y } _ { t , r } \leq x \} } .

The Grünwald-Letnikov-Kolmogorov–Smirnov (GL-KS) test statistic is then formalized as:

\tilde { D } _ { n , m } = \operatorname* { s u p } _ { x \in \mathbb { R } } | \tilde { F } _ { n } ( x ) - \tilde { G } _ { m } ( x ) | .

The main theoretical contribution of this paper is established in the following theorem, which demonstrates that the GL filter successfully neutralizes the long-memory convergence bottleneck.

Theorem 3.7 (Asymptotic Distribution of the GL-KS Statistic). Let
B _ { t } ^ { H _ { 0 } }
be a fBm with Hurst parameter
H _ { 0 } \in ( 1 / 2 , 1 )
. If the GL filter order α is chosen such that
H _ { 0 }   -   \alpha < 1 / 2 ,
then as
n , m \to \infty
with $\textstyle { \frac { n } { n + m } } \to \lambda \in ( 0 , 1 )$
, the standardized GL-KS statistic satisfies:

D _ { n , m } ^ { \dagger } : = \sqrt { \frac { n m } { n + m } } \tilde { D } _ { n , m } \xrightarrow { d } \operatorname* { s u p } _ { x \in \mathbb { R } } | \tilde { U } ( x ) | ,\tag{14}

where
\tilde { U }
is a centered continuous Gaussian process on R. Its covariance kernel is

\operatorname { C o v } \left( \widetilde { U } ( x ) , \widetilde { U } ( y ) \right) = ( 1 - \lambda ) \Gamma _ { \widetilde { X } \widetilde { X } } ( x , y ) + \lambda \Gamma _ { \widetilde { Y } \widetilde { Y } } ( x , y ) - \sqrt { \lambda ( 1 - \lambda ) } \left[ \Gamma _ { \widetilde { X } \widetilde { Y } } ( x , y ) + \Gamma _ { \widetilde { Y } \widetilde { X } } ( x , y ) \right] ,

11

<!-- page: 12 -->

## Page 12

where, for A,
\begin{array} { r } { B \in \{ \widetilde { X } , \widetilde { Y } \} ,   \Gamma _ { A B } ( x , y ) = \sum _ { k \in \mathbb { Z } } \mathrm { C o v } \left( \mathbb { 1 } _ { \{ A _ { 0 } \leq x \} } , \mathbb { 1 } _ { \{ B _ { k } \leq y \} } \right) } \end{array}

Equivalently, by the Hermite expansion of the centered Gaussian indicator,

\Gamma _ { A B } ( x , y ) = \phi ( x ) \phi ( y ) \sum _ { \ell = 1 } ^ { \infty } \frac { H e _ { \ell - 1 } ( x ) H e _ { \ell - 1 } ( y ) } { \ell ! } \sum _ { k \in \mathbb { Z } } \rho _ { A B } ( k ) ^ { \ell } ,

where
H e _ { \ell } ( \cdot )
denotes the probabilist’s Hermite polynomials of order
\ell , \; \phi ( \cdot )
is the standard Gaussian PDF, and
\rho _ { \tilde { X } } ( k ) , \; \rho _ { \tilde { Y } } ( k ) , \; \rho _ { \tilde { X } \tilde { Y } } ( k )
are the autocorrelation and cross-correlation functions of the GL-filtered Gaussian sequences.

Proof. Let
\widetilde { \beta } _ { n } ( x ) = \sqrt { n } \big ( \widetilde { F } _ { n } ( x ) - \Phi ( x ) \big )
, and
\widetilde { \gamma } _ { m } ( x ) = \sqrt { m } \big ( \widetilde { G } _ { m } ( x ) - \Phi ( x ) \big )
. We first establish the joint weak convergence of
( \widetilde { \beta } _ { n } , \widetilde { \gamma } _ { m } )
in
\ell ^ { \infty } ( \mathbb { R } ) \times \ell ^ { \infty } ( \mathbb { R } )

For any standardized Gaussian random variable ξ, the centered indicator admits the Hermite expansion

\mathbb { 1 } _ { \{ \xi \leq x \} } - \Phi ( x ) = - \phi ( x ) \sum _ { \ell = 1 } ^ { \infty } \frac { H e _ { \ell - 1 } ( x ) } { \ell ! } H e _ { \ell } ( \xi ) .\tag{15}

The Hermite rank is equal to one, because the first coefficient is non-zero.

In the unfiltered long-memory case, the autocorrelation behaves as
\rho ( k )   \sim   C | k | ^ { 2 H _ { 0 } - 2 }
, and for
H _ { 0 } \: > \: 1 / 2
the series
\textstyle \sum _ { k } | \rho ( k ) |
is not summable. The Hermite reduction principle for long-range dependent Gaussian sequences then implies that the first-order Hermite projection dominates the empirical process, producing the non-standard normalization and the collapsed limit described in Proposition 2.3; see [23, 13, 11].

After the GL filtering, Proposition 3.6 gives

f _ { \widetilde { Y } } ^ { ( h ) } ( \lambda ) \sim C | \lambda | ^ { 1 - 2 ( H _ { 0 } - \alpha ) } , \qquad \lambda \to 0 .

Equivalently, the long-lag correlations of the filtered sequences satisfy

\rho _ { \widetilde { X } } ( k ) \sim C _ { \alpha , h } | k | ^ { 2 ( H _ { 0 } - \alpha ) - 2 } , \qquad \rho _ { \widetilde { Y } } ( k ) \sim C _ { \alpha , h } | k | ^ { 2 ( H _ { 0 } - \alpha ) - 2 } .

Since
H _ { 0 } - \alpha < 1 / 2
, we have
2(H_{0}-\alpha)-2<-1
, and therefore

\sum _ { k \in \mathbb { Z } } | \rho _ { \widetilde { X } } ( k ) | < \infty , \qquad \sum _ { k \in \mathbb { Z } } | \rho _ { \widetilde { Y } } ( k ) | < \infty , \qquad \sum _ { k \in \mathbb { Z } } | \rho _ { \widetilde { X } \widetilde { Y } } ( k ) | < \infty .\tag{16}

Moreover, since
| \rho ( k ) | \leq 1
, the same summability holds for every Hermite power
\rho ( k ) ^ { \ell } ,   \ell \geq 1
. Hence, each Hermite component in (15) satisfies a standard central limit theorem of Breuer–Major type, and the Hermite series can be handled by the usual empirical-process central limit theorem for shortmemory Gaussian subordinated sequences; see [6, 2, 11]. Consequently,

\big ( \widetilde { \beta } _ { n } , \widetilde { \gamma } _ { m } \big ) \Rightarrow \big ( U _ { X } , U _ { Y } \big ) \qquad { \operatorname { i n } } \ell ^ { \infty } ( \mathbb { R } ) ^ { 2 } ,

where
( U _ { X } , U _ { Y } )
is a centered bivariate Gaussian process.

For
A , B \in \dot { \{ \widetilde { X } , \widetilde { Y } \} }
, define the long-run covariance kernel

\Gamma _ { A B } ( x , y ) = \sum _ { k \in \mathbb { Z } } \operatorname { C o v } \left( \mathbb { 1 } _ { \{ A _ { 0 } \leq x \} } , \mathbb { 1 } _ { \{ B _ { k } \leq y \} } \right) .

Equivalently, using the Hermite expansion,

\Gamma _ { A B } ( x , y ) = \phi ( x ) \phi ( y ) \sum _ { \ell = 1 } ^ { \infty } \frac { H e _ { \ell - 1 } ( x ) H e _ { \ell - 1 } ( y ) } { \ell ! } \sum _ { k \in \mathbb { Z } } \rho _ { A B } ( k ) ^ { \ell } .

12

<!-- page: 13 -->

## Page 13

The absolute summability in (16) guarantees that these kernels are finite.

Since
n / ( n + m ) \to \lambda \in ( 0 , 1 )
, we have

\sqrt { \frac { n m } { n + m } } ( \widetilde { F } _ { n } ( x ) - \widetilde { G } _ { m } ( x ) ) = \sqrt { \frac { m } { n + m } } \: \widetilde { \beta } _ { n } ( x ) - \sqrt { \frac { n } { n + m } } \: \widetilde { \gamma } _ { m } ( x ) ,

and therefore

\sqrt { \frac { n m } { n + m } } ( \widetilde { F } _ { n } - \widetilde { G } _ { m } ) \Rightarrow \widetilde { U } \qquad \mathrm { i n ~ } \ell ^ { \infty } ( \mathbb { R } ) ,

where
\widetilde { U } ( x ) = \sqrt { 1 - \lambda }   U _ { X } ( x ) - \sqrt { \lambda }   U _ { Y } ( x )
. Its covariance kernel is

\operatorname { C o v } \big ( \widetilde { U } ( x ) , \widetilde { U } ( y ) \big ) = ( 1 - \lambda ) \Gamma _ { \widetilde { X } \widetilde { X } } ( x , y ) + \lambda \Gamma _ { \widetilde { Y } \widetilde { Y } } ( x , y ) - \sqrt { \lambda ( 1 - \lambda ) } \left[ \Gamma _ { \widetilde { X } \widetilde { Y } } ( x , y ) + \Gamma _ { \widetilde { Y } \widetilde { X } } ( x , y ) \right] .

In the balanced case
\lambda   =   1 / 2
, this reduces to the same covariance structure as in Proposition 2.2, with the unfiltered kernels replaced by their GL-filtered counterparts.

Finally, since the limit process has continuous sample paths and the map
f   \mapsto   \operatorname { s u p } _ { x \in \mathbb { R } } | f ( x ) |
is continuous on the limiting support, the continuous mapping theorem gives

D _ { n , m } ^ { \dagger } = \sqrt { \frac { n m } { n + m } }   \widetilde { D } _ { n , m } \Rightarrow \operatorname* { s u p } _ { x \in \mathbb { R } } | \widetilde { U } ( x ) | .

Remark 3.8.
Theorem 3.7 confirms that the GL-KS statistic bypasses the LRD phase transition. While the classical unfiltered statistic requires a non-standard normalization
n ^ { 1 - H }
and delivers a degenerate absolute Gaussian limit for
H > 1 / 2 ,
, the filtered alternative retains a stable
\sqrt { n }
rate and converges to a rich, functional Gaussian supremum across the entire parameter space. This structural rehabilitation eliminates the inflation of Type I errors and underpins the fast numerical convergence rates analyzed in Section
4 \cdot

## 3.2.1 Finite-Sample Truncation and Burn-in Mechanics

In practical applications, the underlying fGn sequence is observed only over a finite time horizon. Consequently, the infinite summation defining the discrete Grünwald–Letnikov derivative cannot be implemented exactly. This is the standard initialization problem arising in finite-sample implementations of infinite-order linear filters and fractional-difference operators; see [7, 16, 22]. In the present setting, the issue is particularly relevant because the GL coefficients decay only polynomially. We therefore introduce a burn-in deletion rule whose purpose is to remove the finite-sample effect of the unobserved pre-sample history.

Let
X _ { i }
be the unscaled fGn process. For each
i = 1 , \ldots , n
, the theoretical infinite-memory filtered variable
{ \tilde { X } } _ { i }
and its finite-sample truncated counterpart
{ \widehat { X } } _ { i }
are related by

\widehat { X } _ { i } = \frac { 1 } { \sigma _ { \alpha , h } } \sum _ { k = 0 } ^ { i - 1 } \omega _ { k } ( \alpha ) X _ { i - k } = \widetilde { X } _ { i } - E _ { i } ,

where
\begin{array} { r } { E _ { i }   =   \frac { 1 } { \sigma _ { \alpha , h } } \sum _ { k = i } ^ { \infty } \omega _ { k } ( \alpha ) X _ { i - k } } \end{array}
is the omitted pre-sample tail. Since the GL coefficients satisfy
\begin{array} { r } { \omega _ { k } ( \alpha ) \sim \frac { k ^ { - \alpha - 1 } } { \Gamma ( - \alpha ) } ,   k \to \infty } \end{array}
, and the fGn autocovariance satisfies
\gamma _ { X } ( k ) \sim C _ { H } k ^ { 2 H - 2 } ,   k \to \infty
, the variance of the truncation error satisfies

\mathbb { E } [ E _ { i } ^ { 2 } ] \leq C i ^ { 2 H - 2 \alpha - 2 } = C i ^ { - 2 ( 1 + \alpha - H ) } .

13

<!-- page: 14 -->

## Page 14

Therefore, after deleting the first
N _ { 0 } = \lfloor n ^ { \gamma } \rfloor
observations, with

\gamma > \frac { 1 } { 2 ( 1 + \alpha - H ) } ,\tag{17}

we obtain, uniformly for
i \geq N _ { 0 }

\mathbb { E } [ E _ { i } ^ { 2 } ] \leq C n ^ { - 2 \gamma ( 1 + \alpha - H ) } .\tag{18}

Lemma 3.9
(Uniform negligibility of the truncation error). Let
B ^ { H }
be a fBm with
H \in ( 1 / 2 , 1 )
, and let the GL order satisfy
H - \alpha < 1 / 2
. If the burn-in exponent
\gamma
satisfies condition (17), then

\operatorname* { s u p } _ { x \in \mathbb { R } } \sqrt { n } \left| \widehat { F } _ { n } ( x ) - \widetilde { F } _ { n } ( x ) \right| \overset { P } { \longrightarrow } 0 ,

where
\widehat { F } _ { n } ( x )
and
\tilde { F } _ { n } ( x )
denote the empirical distribution functions of the finite-sample truncated filtered sequence and of the theoretical infinite-memory filtered sequence, respectively.

Proof. Set
\kappa = \gamma ( 1 + \alpha - H )
. By assumption,
\kappa > 1 / 2
. From (18),

\operatorname* { s u p } _ { i \geq N _ { 0 } } \mathbb { E } [ E _ { i } ^ { 2 } ] \leq C n ^ { - 2 \kappa } , \qquad \operatorname* { s u p } _ { i \geq N _ { 0 } } \mathbb { E } | E _ { i } | \leq C n ^ { - \kappa } .

For each
x \in \mathbb { R }

\Big | \mathbb { 1 } _ { \{ \widehat { X } _ { i } \leq x \} } - \mathbb { 1 } _ { \{ \widetilde { X } _ { i } \leq x \} } \Big | \leq \mathbb { 1 } _ { \{ | \widetilde { X } _ { i } - x | \leq | E _ { i } | \} } .

Since
( \tilde { X } _ { i } , E _ { i } )
is jointly Gaussian and
\operatorname { V a r } ( E _ { i } ) \to 0
, the conditional density of
{ \widetilde { X } } _ { i }
given
E _ { i }
is uniformly bounded for all sufficiently large
n .
Hence there exists a constant
C > 0
, independent of x and
i ,
such that

\operatorname* { s u p } _ { x \in \mathbb { R } } \mathbb { P } \left( | \widetilde { X } _ { i } - x | \leq | E _ { i } | \right) \leq C \mathbb { E } | E _ { i } | \leq C n ^ { - \kappa } .

Therefore,

\mathbb { E } \left[ \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \widehat { F } _ { n } ( x ) - \widetilde { F } _ { n } ( x ) \right| \right] \leq \frac { 1 } { n - N _ { 0 } } \sum _ { i = N _ { 0 } + 1 } ^ { n } \operatorname* { s u p } _ { x \in \mathbb { R } } \mathbb { P } \left( | \widetilde { X } _ { i } - x | \leq | E _ { i } | \right) \leq C n ^ { - \kappa } .

Multiplying by
\sqrt { n }
gives

\sqrt { n } \mathop { \mathbb { E } } \left[ \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \widehat { F } _ { n } ( x ) - \widetilde { F } _ { n } ( x ) \right| \right] \leq C n ^ { 1 / 2 - \kappa } \longrightarrow 0 ,

because
\kappa > 1 / 2
. Markov’s inequality yields

\operatorname* { s u p } _ { x \in \mathbb { R } } \sqrt { n } \left| \widehat { F } _ { n } ( x ) - \widetilde { F } _ { n } ( x ) \right| \overset { P } { \longrightarrow } 0 .

The argument for the pooled crossed sample is identical after applying the same burn-in deletion inside each branch. This proves the claim. □

By virtue of Lemma 3.9, the difference between the two statistics is negligible at the
{ \sqrt { n } } { \mathrm { - s c a l e } }
Consequently, the asymptotic distribution derived in Theorem 3.7 remains invariant under finitesample truncation.

14

<!-- page: 15 -->

## Page 15

Remark 3.10
(Effective sample sizes in the pooled crossed sample). The notation used above suppresses a minor but important implementation detail. For the unit-scale sample, the burn-in deletion simply removes the first
N _ { 0 } \; = \; \lfloor n ^ { \gamma } \rfloor
filtered observations, so that the effective sample size is
n _ { \mathrm { e f f } }   : =   n   -   N _ { 0 }
. For the multi-scale sample, however, the observations are obtained by pooling the crossed branches
\widehat { Y } _ { t , r }
, with
t = 0 , \ldots , m _ { r } - 1
, and
r = 0 , \ldots , a - 1
. Since the finite-memory approximation of the GL filter is initialized separately along each branch, the burn-in deletion must also be applied branch by branch. Thus, if
M _ { 0 , r } = \lfloor m _ { r } ^ { \gamma } \rfloor
denotes the burn-in length of branch
r ,
the effective size of the pooled multi-scale sample is
\begin{array} { r } { \overleftarrow { m _ { \mathrm { e f f } } } : = \sum _ { r = 0 } ^ { a - 1 } ( m _ { r } - M _ { 0 , r } ) } \end{array}
. Equivalently, the empirical distribution function computed in finite samples is
\begin{array} { r } { \widehat { G } _ { m } ( x ) = \frac { 1 } { m _ { \mathrm { e f f } } } \sum _ { r = 0 } ^ { a - 1 } \sum _ { t = M _ { 0 , r } + 1 } ^ { m _ { r } } \mathbb { 1 } _ { \left\{ \widehat { Y } _ { t , r } \leq x \right\} } } \end{array}
When the branch lengths are asymptotically balanced and the scale a is fixed, one has
m _ { \mathrm { e f f } } \sim m
, because
M _ { 0 , r } / m _ { r } \rightarrow 0
for every branch. Therefore, this branch-wise correction has no first-order effect on the asymptotic distribution derived above, but it is the relevant finite-sample sample size used in the numerical and empirical implementations.

## 3.3 GL-KS estimator

The previous section derived the asymptotic distribution of the GL–KS statistic under a fixed null value of the Hurst parameter. We now invert this testing procedure and define an estimator of the unknown self-similarity exponent. Let
H _ { 0 } \in ( 1 / 2 , 1 )
denote the true Hurst parameter of the underlying fractional Brownian motion. Let
\mathbb { H } \subset ( 0 , 1 )
be a compact parameter set such that
H _ { 0 } \in \mathbb { H }
. In this subsection, we denote by
\theta \in \mathbb { H }
a generic candidate value of the Hurst parameter, in order to avoid confusion with the step size h of the GL operator. For every
\theta   \in   \mathbb { H }
, we construct the GL-filtered unit-scale sample and the GL-filtered multi-scale sample, where the latter is rescaled by
a ^ { - \theta }
. We denote the corresponding empirical distribution functions by
\widetilde { F } _ { n }
and
\tilde { G } _ { m , \theta }
, respectively. The GL–KS criterion is defined as

\widetilde { D } _ { n , m } ( \theta ) = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \widetilde { F } _ { n } ( x ) - \widetilde { G } _ { m , \theta } ( x ) \right| .

The GL–KS estimator of the Hurst parameter is then

\widehat { H } _ { G L K S } = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { \theta \in \mathbb { H } } \widetilde { D } _ { n , m } ( \theta ) .

We now describe the population criterion associated with this estimator. Under the true value
H _ { 0 }
the standardized GL-filtered unit-scale sample has limiting distribution
\mathcal { N } ( 0 , 1 )
. On the other hand, if the multi-scale sample is rescaled by
a ^ { - \theta }
, then its limiting variance is proportional to
a ^ { 2 ( H _ { 0 } - \theta ) }

Therefore, the limiting distribution function of the rescaled multi-scale sample is

x \mapsto \Phi \left( a ^ { \theta - H _ { 0 } } x \right) .

Hence, the deterministic counterpart of the empirical difference is

M ( \theta , x ) = \Phi ( x ) - \Phi \left( a ^ { \theta - H _ { 0 } } x \right) ,

and the corresponding population GL–KS criterion is

D ( \theta ) = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| M ( \theta , x ) \right| .

At the true value
\theta = H _ { 0 }
, we have
M ( H _ { 0 } , x ) = 0
for every
x \in \mathbb { R }
, and therefore
D ( H _ { 0 } ) = 0
. Moreover, if
\theta \neq H _ { 0 }
, then the two Gaussian marginal distributions are different, so that
D ( \theta ) > 0
. Thus
H _ { 0 }
is the unique minimizer of the population criterion. In particular, if

\operatorname* { s u p } _ { \theta \in \mathbb { H } } \left| \widetilde { D } _ { n , m } ( \theta ) - D ( \theta ) \right| \overset { P } { \longrightarrow } 0 ,

15

<!-- page: 16 -->

## Page 16

then the usual arg min consistency argument gives
\widehat { H } _ { G L K S } \overset { P } { \longrightarrow } H _ { 0 }

The next proposition gives the local asymptotic distribution of the GL–KS estimator and the corresponding expression for its asymptotic variance.

Proposition 3.11
(Local distribution and asymptotic variance of the GL–KS estimator). Let
B _ { t } ^ { H _ { 0 } }
be a fractional Brownian motion with
H _ { 0 } \in ( 1 / 2 , 1 )
. Let the GL filter order
\alpha > 0
satisfy
\textstyle H _ { 0 } - \alpha < { \frac { 1 } { 2 } }
Assume that the conditions of Theorem 3.7 and Lemma 3.9 hold. Assume also that the empirical process is locally asymptotically equicontinuous with respect to the parameter θ in a neighbourhood of
H _ { 0 }

Let
$\textstyle r _ { n , m } = \sqrt { \frac { n m } { n + m } } . \; \mathit { I f } \; H _ { 0 } \in \operatorname { i n t } ( \mathbb { H } )$
and the limiting arg min below is almost surely unique, then

r _ { n , m } \left( \widehat { H } _ { { G L K S } } - H _ { 0 } \right) \Rightarrow T _ { { K S } } ,

where T
KS
= arg min
\left\| \widetilde { U } - t \ell _ { a } \right\| _ { \infty }
, with
\ell _ { a } ( x ) = ( \log a ) x \phi ( x )
, and where
\widetilde { U }
is the centered Gaussian t∈R process appearing in Theorem 3.7. Consequently, if the sequence
r _ { n , m } ^ { 2 } ( \widehat { H } _ { G L K S } - H _ { 0 } ) ^ { 2 }
is uniformly integrable, then

r _ { n , m } ^ { 2 } \operatorname { V a r } \left( \widehat { H } _ { G L K S } \right) \longrightarrow \sigma _ { K S } ^ { 2 } ,

where
\sigma _ { K S } ^ { 2 } = \mathrm { V a r } \left( T _ { K S } \right)
. Equivalently,

\mathrm { V a r } \left( \widehat { H } _ { G L K S } \right) = \frac { n + m } { n m } \sigma _ { K S } ^ { 2 } + o \left( \frac { n + m } { n m } \right) .

In the balanced case
m \simeq n _ { \mathrm { l } }
, this becomes Var
\begin{array} { r } { \left( \widehat { H } _ { G L K S } \right) = \frac { 2 } { n } \sigma _ { K S } ^ { 2 } + o \left( \frac { 1 } { n } \right) } \end{array}

Proof. We study the local behavior of the criterion in a shrinking neighbourhood of
H _ { 0 }
. The deterministic component of the difference between the two limiting distribution functions is

M ( \theta , x ) = \Phi ( x ) - \Phi \left( a ^ { \theta - H _ { 0 } } x \right) .

Differentiating with respect to
\theta ,
we obtain

\frac { \partial } { \partial \theta } M ( \theta , x ) = - ( \operatorname { l o g } a ) a ^ { \theta - H _ { 0 } } x \phi \left( a ^ { \theta - H _ { 0 } } x \right) .

Therefore, at
\theta = H _ { 0 }

\dot { M } _ { H _ { 0 } } ( x ) = \left. \frac { \partial } { \partial \theta } M ( \theta , x ) \right| _ { \theta = H _ { 0 } } = - ( \operatorname { l o g } a ) x \phi ( x ) .

Set
\ell _ { a } ( x ) = ( \log a ) x \phi ( x )
. Then
\dot { M } _ { H _ { 0 } } ( x ) = - \ell _ { a } ( x )
. Hence, uniformly in
x \in \mathbb { R }

M ( \theta , x ) = - ( \theta - H _ { 0 } ) \ell _ { a } ( x ) + o \left( | \theta - H _ { 0 } | \right) , \quad \mathrm { a s } \quad \theta \to H _ { 0 } .

Now take a local perturbation of the form
\begin{array} { r } { \theta = H _ { 0 } + \frac { t } { r _ { n , m } } } \end{array}
. Then

r _ { n , m } M \left( H _ { 0 } + \frac { t } { r _ { n , m } } , x \right) \longrightarrow - t \ell _ { a } ( x ) .

By Theorem 3.7, at the true parameter value,

r _ { n , m } \left[ \widetilde { F } _ { n } ( x ) - \widetilde { G } _ { m , H _ { 0 } } ( x ) \right] \Rightarrow \widetilde { U } ( x ) \qquad \mathrm { i n } \ell ^ { \infty } ( \mathbb { R } ) .

16

<!-- page: 17 -->

## Page 17

Combining this convergence with the previous local expansion and the assumed local stochastic equicontinuity gives, for every compact set
K \subset \mathbb { R }
,

r _ { n , m } \widetilde { D } _ { n , m } \left( H _ { 0 } + \frac { t } { r _ { n , m } } \right) \Rightarrow \left\| \widetilde { U } - t \ell _ { a } \right\| _ { \infty } \qquad \mathrm { i n } \ell ^ { \infty } ( K ) .

Since
H _ { 0 }
is the unique minimizer of the population criterion and the limiting minimizer is assumed to be almost surely unique, the arg min continuous mapping theorem yields

r _ { n , m } \left( \widehat { H } _ { { G L K S } } - H _ { 0 } \right) \Rightarrow \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { t \in \mathbb { R } } \left\| \widetilde { U } - t \ell _ { a } \right\| _ { \infty } .

This proves the claimed weak convergence, with
T _ { K S } = \operatorname { a r g } \operatorname { m i n } _ { t \in \mathbb { R } } \left\| \widetilde { U } - t \ell _ { a } \right\| _ { \infty }
. The variance statement follows from the convergence of second moments.
\mathrm { I f } \; r _ { n , m } ^ { 2 } ( \widehat { H } _ { G L K S } - H _ { 0 } ) ^ { 2 }
is uniformly integrable, then
r _ { n , m } ^ { 2 } \operatorname { V a r } \left( \widehat { H } _ { G L K S } \right) \longrightarrow \operatorname { V a r } \left( T _ { K S } \right)
. Since
\begin{array} { r } { r _ { n , m } ^ { - 2 } = \frac { n + m } { n m } } \end{array}
, we obtain

\operatorname { V a r } \left( \widehat { H } _ { { G L K S } } \right) = \frac { n + m } { n m } \operatorname { V a r } \left( T _ { { K S } } \right) + o \left( \frac { n + m } { n m } \right) .

This concludes the proof.

Remark 3.12
(The short-memory case as the limiting case
( \alpha = 0 ) )
. Theorem 3.7 has been stated for the long-memory case
H _ { 0 }   >   1 / 2
, where the Grünwald–Letnikov derivative is needed in order to bring the empirical process back to the short-memory domain. However, the same local argument also covers the case
H _ { 0 } \leq 1 / 2
by setting the fractional order equal to zero.

Indeed, when
H _ { 0 } < 1 / 2
, the fGn autocovariance sequence is absolutely summable, while for
H _ { 0 } =
1 / 2
the increments are independent. Therefore, the obstruction created by long-range dependence is absent from the outset. In this case one may set

\alpha = 0 , \Delta _ { h } ^ { G L , 0 } = ( 1 - L _ { h } ) ^ { 0 } = I ,

so that the GL-filtered statistic reduces to the unfiltered KS-type statistic. No pre-sample fractionalfilter truncation is introduced, and the burn-in correction can be omitted. Consequently, the local expansion of the population criterion remains unchanged:

M ( \theta , x ) = \Phi ( x ) - \Phi \left( a ^ { \theta - H _ { 0 } } x \right) , \qquad \dot { M } _ { H _ { 0 } } ( x ) = - ( \operatorname { l o g } a ) x \phi ( x ) .

The same argmin argument therefore gives

r _ { n , m } \left( \widehat { H } _ { \operatorname { K S } } - H _ { 0 } \right) \Rightarrow \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { t \in \mathbb { R } } \left\| U - t \ell _ { a } \right\| _ { \infty } , \qquad \ell _ { a } ( x ) = ( \operatorname { l o g } a ) x \phi ( x ) ,

where U denotes the centered Gaussian limit of the unfiltered short-memory empirical process specified in Proposition 2.2. Thus, the variance formula in Proposition 3.11 remains valid in the short-memory and independent regimes after replacing the filtered limiting process by its unfiltered counterpart and taking
\alpha = 0

Remark 3.13.
The scaling factor a plays a direct role in the local identification of the Hurst parameter. Around the true value
H _ { 0 }
, the deterministic component of the criterion satisfies

M ( \theta , x ) = - ( \theta - H _ { 0 } ) ( \operatorname { l o g } a ) x \phi ( x ) + o ( | \theta - H _ { 0 } | ) .

17

<!-- page: 18 -->

## Page 18

Hence the local drift of the criterion is proportional to log a. Larger values of a increase the separation between the unit-scale distribution and the rescaled multi-scale distribution when
\theta   \neq   H _ { 0 }
. In this sense, increasing a steepens the local objective function and tends to improve the precision of the Hurst estimate.

This effect is also visible in the limiting argmin representation

T _ { \operatorname { K S } } ( a ) = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { t \in \mathbb { R } } \left\| \widetilde { U } - t \ell _ { a } \right\| _ { \infty } , \qquad \ell _ { a } ( x ) = ( \operatorname { l o g } a ) x \phi ( x ) .

If the covariance structure of the limiting process were kept fixed as a varies, the deterministic slope would imply an approximate variance reduction of order
( \log a ) ^ { - 2 }
. Therefore, from a purely localidentification perspective, larger scales provide a stronger signal for distinguishing nearby Hurst parameters.

In finite samples, however, this gain is counterbalanced by the structure of the crossed sample. As a increases, each branch
r = 0 , \ldots , a   -   1
contains fewer observations, and the burn-in deletion is applied branch by branch. Thus the effective multi-scale sample size
\begin{array} { r } { m _ { \mathrm { e f f } }   =   \sum _ { r = 0 } ^ { a - 1 } ( m _ { r } - M _ { 0 , r } ) } \end{array}
may decrease relative to the nominal pooled size, especially for large a and moderate N. Very large scales may therefore improve identification through the factor log
a ,
but at the cost of shorter branches, stronger finite-sample effects, and a smaller effective sample after burn-in correction.

The choice of a should consequently be interpreted as a bias–variance and identification–samplesize trade-off. Moderate values of a are expected to improve power and reduce estimator dispersion, whereas excessively large values can deteriorate finite-sample stability because the crossed branches become too short.

Remark 3.14
(Regime-adaptive implementation). The GL filter is not used to redefine the Hurst exponent. It is used only to select a fast-converging limiting distribution when the estimated regime is persistent. In the empirical implementation in Section 5, we first estimate H from the distributional self-similarity criterion. If
\widehat { H }   \leq   1 / 2
, we set
\alpha   =   0
, use the short-memory limit, and no burn-in correction is applied. If
\hat { H }   >   1 / 2
, we choose
\alpha
such that
\hat { H }   -   \alpha   <   1 / 2 ,
, apply the GL filter, and compute the GL-KS statistic with the branch-wise effective sample sizes. This plug-in regime selection is asymptotically valid away from the boundary
H = 1 / 2
, because
\hat { H } \rightarrow H _ { 0 }
in probability.

The theoretical results above are asymptotic. The next section verifies whether the GL-KS statistic retains its predicted stabilization in finite samples, whether the burn-in deletion is sufficient to remove pre-sample truncation effects, and whether the estimator remains reliable across both LRD and SRD regimes.

## 4 Computational Analysis

In this section, we present a comprehensive Monte Carlo simulation study designed with a two-fold objective: first, to empirically validate the asymptotic invariance and phase-transition bypass established in Theorem 3.7; and second, to evaluate the finite-sample performance of the Lemma 3.9 boundary conditions in mitigating pre-history truncation bias. The computational analysis systematically contrasts the standard KS test against our proposed fractional Grünwald-Letnikov filtered alternative GL-KS.

## 4.1 General Monte Carlo Design

To ensure statistical exactness and prevent the structural distortions often induced by Cholesky factorizations or truncated spectral methods, the data generating process employs the circulant embedding

18

<!-- page: 19 -->

## Page 19

technique pioneered by Wood and Chan in [28]. This approach enables the exact synthesis of fBm trajectories by decomposing the associated embedded circulant covariance matrix. It preserves the underlying LRD structure intact while maintaining an optimal computational complexity of O(N log N) via the Fast Fourier Transform. Any fractional Brownian motion was generated using fbmwoodchan() MATLAB function, available in the FracLab Toolbox 2.02 (INRIA package).

The experimental parameter space for the Monte Carlo framework is calibrated as follows:

• Hurst exponent. In the LRD regime we tested the true Hurst exponent
H _ { t r u e } = \{ 0 . 5 1 , 0 . 7 , 0 . 9 \}
while in the SRD regime we tested
H _ { t r u e } = \{ 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 \}
. The candidate Hurst values used in the minimization procedure are evaluated on the grid
\mathbb { H } \; \in \; [ 0 . 0 0 1 , 0 . 9 9 9 ]
with step
\Delta \mathrm { H } = 0 . 0 0 1

• Fractional GL order α. In the LRD regime, the differencing parameter α is chosen to strictly enforce the short memory regime. Specifically, α is selected such that
H - \alpha = 0 . 2 5
to enable a consistent comparison across all simulations. In the SRD regime, we use the unfiltered shortmemory implementation of Remark 3.12.

• Burn-in exponent γ. For the GL-KS statistic, γ is selected above the theoretical threshold of Lemma 3.9 to control the pre-sample truncation error. Unless otherwise stated, its value is fixed within each experiment; in the burn-in sensitivity analysis, γ is varied over a grid. No burn-in correction is applied when
\alpha = 0

• Sample size N. To investigate the rate of asymptotic convergence, fBm trajectories are simulated across five progressive lengths: N ∈ {100, 250, 500, 1000, 5000}.

• Scaling factor a. In alignment with the underlying cross-scaled fGn framework, the scaling factor is varied over
a \in \{ 2 , 3 , 4 , 5 , 1 0 , 2 0 \}

• Monte Carlo replications M. For each parameter configuration, we perform
\mathcal { M } = \mathrm { 1 0 , } 0 0 0
independent Monte Carlo replications. This number of replications provides stable estimates of the empirical distributions, rejection frequencies, and critical quantiles used in the finite-sample analysis.

## 4.2 Convergence Acceleration and Asymptotic Invariance

The first numerical experiment is dedicated to demonstrating the collapse of the LRD-driven phase transition discussed in Theorem 3.7. As documented in the classical literature (e.g., Dehling and Taqqu, 1989), applying non-parametric goodness-of-fit tests directly to long-memory processes compromises the standard convergence rate—slowing it down to
n ^ { 1 - H }
—and causes the limiting distribu tion to become degenerate and structurally dependent on the unknown parameter H.

By introducing the fractional GL filter and scaling the resultant
\tilde { D } _ { n , m }
statistic by the standard
\sqrt { n }
rate, asymptotic invariance is successfully rehabilitated. We monitor this phenomenon by tracking the evolution of the ECDFs as N increases.

Figure 1 illustrates the stabilization effect predicted by Theorem 3.7. In the left panel, the unfiltered classical statistic exhibits ECDF curves that shift systematically to the right as N expands, verifying that the
\sqrt { n }
normalization is mathematically misspecified under LRD. Conversely, the right panel illustrates that the GL-KS test statistics are much more stable across sample sizes, even at a moderate sample size of
N = 2 0 0
. This provides visual evidence that the fractional filter successfully neutralizes the singularity at the origin of the spectral density, effectively relocating the process into the domain of attraction of short-memory functionals.

19

<!-- page: 20 -->

## Page 20

Figure 1: Empirical null distributions of the normalized KS-type statistic for increasing sample sizes. The left panel reports the classical unfiltered statistic under long-range dependence, showing the lack of stabilization under the standard
\sqrt { n }
normalization. The right panel reports the GL-KS statistic after fractional filtering, whose empirical distributions collapse onto a common limiting curve, consistently with the short-memory asymptotic regime restored by the GL derivative.

## 4.3 Finite-Sample Properties: Size and Power

We now investigate the finite-sample inferential performance of the proposed statistic. The analysis focuses on two complementary aspects: empirical size under the null hypothesis and power against misspecified Hurst exponents.

For each Monte Carlo replication, a fractional Brownian motion with parameter
H _ { \mathrm { t r u e } }
is generated, and the corresponding unit-scale and crossed multi-scale increments are constructed as in Section 4.1. The null hypothesis is
\mathcal { H } _ { 0 }   :   H _ { \mathrm { t e s t } }   =   H _ { \mathrm { t r u e } }
, where
H _ { \mathrm { t e s t } }
is the value used to rescale the multi-scale sample. Under the null, the rescaled unit-scale and multi-scale samples should have the same distribution. Rejections are therefore driven by the two-sample KS-type distance between the corresponding empirical distribution functions.

In the persistent case
H _ { \mathrm { t r u e } }   >   1 / 2
, two statistics are compared. The first one is the unfiltered statistic, which is affected by the long-memory phase transition described in Proposition 2.3. The second one is the GL–KS statistic. For the filtered statistic, the GL order is chosen so that the effective memory parameter satisfies
H _ { \mathrm { t r u e } } - \alpha = 0 . 2 5
, and the burn-in exponent is selected above the lower bound of Lemma 3.9. This ensures that the filtered process lies in the short-memory domain while preserving the self-similarity parameter identified by the KS criterion.

Critical values are obtained by Monte Carlo calibration under the corresponding null configuration. This is important because the limiting law is not the classical distribution-free two-sample KS law: the two samples are extracted from the same trajectory and the limiting covariance depends on the auto-covariance and cross-covariance structure of the filtered empirical process. The purpose of the simulation is therefore to compare the finite-sample rejection frequencies of the unfiltered and filtered statistics at the same nominal levels. Table 2 reports empirical rejection frequencies at the 1%, 5%, and 10% nominal levels for
H _ { \mathrm { t r u e } } \: \in \: \{ 0 . 5 1 , 0 . 7 0 , 0 . 9 0 \}
, with scaling factor
a   =   2 0
The unfiltered statistic displays substantial size distortions in the long-memory regime. The distortion is especially severe for large values of H, where the autocorrelation function decays very slowly and the standard
{ \sqrt { n } } \mathrm { - t y p e }
empirical-process approximation is no longer appropriate. For example, when
H   =   0 . 9 0
the unfiltered rejection rates remain far above their nominal levels even for large sample sizes. By contrast, the GL–KS statistic remains well calibrated across all three persistent regimes. Its empirical rejection frequencies stay close to the nominal 1%, 5%, and 10% levels, with only minor finite-sample

20

<!-- page: 21 -->

## Page 21

**[table]**

Table 2: Empirical size in the long-memory regime.
<table><tbody><tr><td rowspan="2">Sign. Level</td><td rowspan="2">αN</td><td colspan="3">Unfiltered KS Test</td><td colspan="3">GL-KS Test</td></tr><tr><td>H = 0.51-</td><td>H = 0.70-</td><td>H = 0.90-</td><td>H = 0.510.26</td><td>H = 0.700.45</td><td>H = 0.900.65</td></tr><tr><td>1%</td><td>10025050010005000</td><td>4.44%5.35%5.84%6.87%6.19%</td><td>7.50%6.07%4.74%3.71%2.40%</td><td>47.12%30.30%19.49%12.31%5.14%</td><td>0.90%1.16%1.17%0.96%0.90%</td><td>1.08%1.21%1.16%1.08%1.06%</td><td>1.06%0.98%1.14%1.04%1.06%</td></tr><tr><td>5%</td><td>10025050010005000</td><td>17.48%19.75%20.54%22.10%21.39%</td><td>24.26%19.30%16.95%14.36%9.45%</td><td>76.95%58.91%43.78%31.33%16.27%</td><td>4.82%4.80%5.36%4.70%4.95%</td><td>5.11%5.04%5.04%5.12%4.94%</td><td>5.09%5.01%4.83%5.14%5.22%</td></tr><tr><td>10%</td><td>10025050010005000</td><td>30.39%34.29%35.26%36.57%35.88%</td><td>39.82%33.30%29.64%25.17%17.51%</td><td>88.51%75.87%61.28%46.74%27.79%</td><td>9.85%9.99%10.43%10.15%10.10%</td><td>9.96%10.23%10.15%10.47%10.12%</td><td>10.17%9.77%10.28%10.22%10.58%</td></tr></tbody></table>
Notes. Rejection frequencies are reported at the 1%, 5%, and 10% nominal levels under
\overline { { \mathcal { H } _ { 0 } \colon H _ { \mathrm { t e s t } } } } = H _ { \mathrm { t r u e } } ,
with
a = 2 0
. The unfiltered statistic is compared with the GL–KS statistic. In the GL–KS columns, α is chosen so that
H _ { \mathrm { t r u e } } - \alpha = 0 . 2 5
, and the burn-in correction is applied branch-wise. The analysis was performed with
\mathcal { M } = 1 0 , 0 0 0
Monte Carlo simulations.

fluctuations. This confirms the main theoretical implication of Theorem 3.7: after fractional filtering, the statistic returns to a short-memory empirical-process regime and the standard
\sqrt { n }
normalization becomes appropriate again.

Figure 2: Empirical power of the GL-KS test against misspecified Hurst exponents. The true value
H _ { \mathrm { t r u e } }
is marked by the vertical dashed line, while the horizontal dashed line denotes the 5% significance level. The left panel shows the effect of the scaling factor a for fixed sample size, whereas the right panel shows the sharpening of the rejection curve as the sample size N increases.

The second experiment evaluates power. We fix the true value at
H _ { \mathrm { t r u e } } = 0 . 7 0
and vary the null value
H _ { \mathrm { t e s t } }
over a grid around the true parameter. For each tested value, the multi-scale sample is rescaled by
a ^ { - H _ { \mathrm { t e s t } } }
. Hence, when
H _ { \operatorname { t e s t } } \neq H _ { \operatorname { t r u e } } ,
, the unit-scale and multi-scale samples no longer have the same distribution, and the test should reject. In the persistent part of the grid, the GL order is selected under the tested null so that
H _ { \mathrm { t e s t } }   -   \alpha = 0 . 2 5
. At the boundary and in the short-memory part of the grid,
\alpha = 0
is used, consistently with Remark 3.12. Figure 2 reports the resulting empirical power curves. The minimum of the rejection curve occurs at
H _ { \mathrm { t e s t } } = H _ { \mathrm { t r u e } }
, where the rejection probability

21

<!-- page: 22 -->

## Page 22

is close to the nominal significance level. As
H _ { \mathrm { t e s t } }
moves away from
H _ { \mathrm { t r u e } } ,
the rejection probability increases, producing the expected V-shaped power profile. The curve becomes steeper as the sample size increases, showing that the test becomes increasingly sensitive to local departures from the null. This behavior is consistent with the local identification argument in Proposition 3.11: the deterministic drift of the criterion separates incorrect Hurst values from the true one, while the stochastic component shrinks at the standard empirical-process rate after GL filtering. The power experiment also highlights the role of the scaling factor a. Larger values of a increase the deterministic separation between the unit-scale distribution and the incorrectly rescaled multi-scale distribution, because the local drift is proportional to log a. At the same time, very large scales reduce branch lengths and may increase finite-sample variability. The numerical evidence therefore supports the bias–variance interpretation discussed in Remark 3.13: moderate-to-large scales improve identification, but excessively large scales can reduce effective sample information.

## 4.4 Sensitivity to Burn-in Initialization

The final component of the computational analysis examines the finite-sample role of the burn-in exponent. Lemma 3.9 requires
\begin{array} { r } { \gamma   >   \gamma _ { \mathrm { m i n } }   : =   \frac { 1 } { 2 ( 1 + \alpha - H ) } } \end{array}
in order for the pre-sample truncation error to be negligible at the empirical-process scale. In this sensitivity experiment we set
H = 0 . 7 0
and
\alpha = 0 . 5 0
, so that
H - \alpha = 0 . 2 0
and
\gamma _ { \mathrm { m i n } } = 5 / 8
. We therefore vary
\gamma
over a grid containing values below and above this threshold and record the empirical rejection frequency under the null hypothesis.

Figure 3 shows the expected finite-sample trade-off. For
\gamma   <   \gamma _ { \mathrm { m i n } } ,
the burn-in deletion is not large enough to absorb the initialization error generated by the finite GL filter. The empirical size is therefore distorted. Once
\gamma
crosses the theoretical lower bound, the rejection frequency stabilizes around the significance level, confirming the practical relevance of Lemma 3.9. For very large values of
\gamma ,
, however, the effective sample size is unnecessarily reduced. This last deterioration is not a contradiction of the lemma: the lemma only gives a lower bound ensuring asymptotic negligibility of the truncation error, while finite samples also require preserving enough observations after the branch-wise deletion.

Figure 3: Sensitivity of the empirical size to the burn-in exponent
\gamma .
The vertical line marks the theoretical lower bound
\dot { \gamma _ { \operatorname* { m i n } } } = 1 / [ 2 ( 1 + \alpha - H ) ]
], while the horizontal dashed line denotes the 5% level. For
\gamma < \gamma _ { \mathrm { m i n } }
, the pre-sample truncation error is not sufficiently absorbed by the burn-in deletion and the test over-rejects. Once γ exceeds the theoretical threshold, the empirical size stabilizes around the nominal level; for very large γ, the effective sample size becomes unnecessarily depleted.

22

<!-- page: 23 -->

## Page 23

## 4.5 Short-Memory Benchmark and Finite-Sample Accuracy of KS/GL-KS test

We finally complete the Monte Carlo analysis by considering the short-memory and independent regimes
H \leq 1 / 2
, and by evaluating the finite-sample accuracy of the Hurst estimator. This serves two purposes: it verifies that the size distortions observed for
H   >   1 / 2
are genuinely caused by long-range dependence, and it validates the regime-adaptive rule of Remark 3.14.

Accordingly, in the short-memory experiment we simulate fBm trajectories with
H _ { \operatorname { t r u e } } \in \{ 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 \}
. For each value of
H _ { \mathrm { t r u e } }
, the null hypothesis is
\mathcal { H } _ { 0 } : H _ { \mathrm { t e s t } } = H _ { \mathrm { t r u e } }
. The empirical statistic is the unfiltered short-memory statistic
\begin{array} { r } { D _ { n , m } ^ { \star } = \sqrt { \frac { n m } { n + m } }   D _ { n , m } , } \end{array}
corresponding to the case
\alpha = 0
and
\Delta _ { h } ^ { G L , 0 } = I .
. Since no fractional filter is applied, there is no pre-sample truncation error and therefore no burn-in deletion. The effective sample sizes coincide with the nominal crossed-sample sizes.

**[table]**

Table 3: Empirical size in the short-memory and independent regimes.
<table><tbody><tr><td>Sign. Level</td><td>N</td><td>H = 0.1</td><td>H = 0.2</td><td>H = 0.3</td><td>H = 0.4</td><td>H = 0.5</td></tr><tr><td>1%</td><td>10025050010005000</td><td>1.13%0.87%0.99%1.08%1.18%</td><td>0.88%1.03%1.02%1.10%1.07%</td><td>1.07%1.05%1.00%1.10%1.01%</td><td>0.91%1.00%0.97%0.97%0.92%</td><td>1.05%1.09%1.06%1.06%1.12%</td></tr><tr><td>5%</td><td>10025050010005000</td><td>5.21%4.91%5.34%5.14%4.99%</td><td>4.94%4.90%5.14%4.98%4.61%</td><td>5.03%4.96%4.87%4.91%5.14%</td><td>5.03%4.91%5.04%5.17%4.84%</td><td>4.94%4.77%5.21%5.10%4.90%</td></tr><tr><td>10%</td><td>10025050010005000</td><td>10.46%9.96%10.28%9.98%10.22%</td><td>9.91%10.56%10.17%10.06%9.89%</td><td>9.78%9.77%9.82%10.08%10.18%</td><td>9.73%10.13%9.84%9.95%9.90%</td><td>9.89%10.29%9.84%10.19%9.81%</td></tr></tbody></table>
Notes. Rejection frequencies are reported at the 1%, 5%, and 10% nominal levels under
\overline { { \mathcal { H } _ { 0 } : H _ { \mathrm { t e s t } } } } = H _ { \mathrm { t r u e } }
. Since
H _ { \mathrm { t r u e } } \leq 1 / 2 ,
, the unfiltered short-memory statistic is used and no burn-in deletion is required. The analysis was performed with
\mathcal { M } = 1 0 , 0 0 0
Monte Carlo simulations.

Table 3 shows that the unfiltered KS-type statistic is already well calibrated throughout the shortmemory region. At all nominal significance levels, the empirical rejection frequencies remain close to their theoretical targets. This holds both in the anti-persistent cases
H < 1 / 2
and in the independent Brownian benchmark
H = 1 / 2

The result is important for the interpretation of the full procedure. In the short-memory regime, the autocorrelation function is summable, so the empirical process converges at the standard
\sqrt { n }
rate. The phase transition observed for
H > 1 / 2
is therefore not a finite-sample artifact of the KS criterion itself, but a consequence of the non-summable dependence structure of the underlying increments. Once the process is already short-memory, the GL correction would be unnecessary and would only introduce an artificial loss of observations.

Table 4 reports Monte Carlo summaries of
\widehat { H }
in both regimes. The estimator is essentially unbiased over the whole parameter range. In the short-memory region, the RMSE remains small; in the persistent region, the GL–KS estimator continues to track the true value accurately despite the effective-sample loss induced by the burn-in correction. These results confirm that the GL transformation changes the empirical fluctuation and the limiting distribution, but not the Hurst parameter identified by the minimum-distance criterion. Taken together, Tables 3 and 4 support the regimeadaptive interpretation of the method: the unfiltered KS implementation is used for
H \leq 1 / 2 ,
, whereas the GL–KS implementation is used in the persistent regime.

23

<!-- page: 24 -->

## Page 24

**[table]**

Table 4: Finite-sample accuracy of the Hurst estimator.
<table><tbody><tr><td>H<sub>0</sub></td><td>N</td><td>a</td><td>α</td><td>γ</td><td>neff</td><td>meff</td><td>Mean</td><td>Bias</td><td>Std</td><td>RMSE</td><td>MAE</td></tr><tr><td>0.10</td><td>1000</td><td>20</td><td>0.000</td><td>-</td><td>999</td><td>980</td><td>0.1000</td><td>-0.0000</td><td>0.0196</td><td>0.0196</td><td>0.0154</td></tr><tr><td>0.20</td><td>1000</td><td>20</td><td>0.000</td><td>-</td><td>999</td><td>980</td><td>0.2006</td><td>0.0006</td><td>0.0248</td><td>0.0248</td><td>0.0193</td></tr><tr><td>0.30</td><td>1000</td><td>20</td><td>0.000</td><td>-</td><td>999</td><td>980</td><td>0.3006</td><td>0.0006</td><td>0.0296</td><td>0.0296</td><td>0.0236</td></tr><tr><td>0.40</td><td>1000</td><td>20</td><td>0.000</td><td>-</td><td>999</td><td>980</td><td>0.4018</td><td>0.0018</td><td>0.0342</td><td>0.0342</td><td>0.0271</td></tr><tr><td>0.50</td><td>1000</td><td>20</td><td>0.000</td><td>-</td><td>999</td><td>980</td><td>0.5018</td><td>0.0018</td><td>0.0389</td><td>0.0389</td><td>0.0304</td></tr><tr><td>0.51</td><td>1000</td><td>20</td><td>0.260</td><td>0.697</td><td>877</td><td>681</td><td>0.5097</td><td>-0.0003</td><td>0.0421</td><td>0.0421</td><td>0.0339</td></tr><tr><td>0.60</td><td>1000</td><td>20</td><td>0.350</td><td>0.697</td><td>877</td><td>681</td><td>0.6006</td><td>0.0006</td><td>0.0451</td><td>0.0451</td><td>0.0356</td></tr><tr><td>0.70</td><td>1000</td><td>20</td><td>0.450</td><td>0.697</td><td>877</td><td>681</td><td>0.6990</td><td>-0.0010</td><td>0.0462</td><td>0.0461</td><td>0.0370</td></tr><tr><td>0.80</td><td>1000</td><td>20</td><td>0.550</td><td>0.697</td><td>877</td><td>681</td><td>0.8044</td><td>0.0044</td><td>0.0492</td><td>0.0494</td><td>0.0395</td></tr><tr><td>0.90</td><td>1000</td><td>20</td><td>0.650</td><td>0.697</td><td>877</td><td>681</td><td>0.9019</td><td>0.0019</td><td>0.0478</td><td>0.0478</td><td>0.0386</td></tr><tr><td>0.10</td><td>5000</td><td>20</td><td>0.000</td><td>-</td><td>4999</td><td>4980</td><td>0.1000</td><td>-0.0000</td><td>0.0087</td><td>0.0087</td><td>0.0069</td></tr><tr><td>0.20</td><td>5000</td><td>20</td><td>0.000</td><td>-</td><td>4999</td><td>4980</td><td>0.1996</td><td>-0.0004</td><td>0.0108</td><td>0.0108</td><td>0.0086</td></tr><tr><td>0.30</td><td>5000</td><td>20</td><td>0.000</td><td>-</td><td>4999</td><td>4980</td><td>0.3001</td><td>0.0001</td><td>0.0127</td><td>0.0127</td><td>0.0100</td></tr><tr><td>0.40</td><td>5000</td><td>20</td><td>0.000</td><td>-</td><td>4999</td><td>4980</td><td>0.4003</td><td>0.0003</td><td>0.0150</td><td>0.0150</td><td>0.0120</td></tr><tr><td>0.50</td><td>5000</td><td>20</td><td>0.000</td><td>-</td><td>4999</td><td>4980</td><td>0.5008</td><td>0.0008</td><td>0.0170</td><td>0.0170</td><td>0.0135</td></tr><tr><td>0.51</td><td>5000</td><td>20</td><td>0.260</td><td>0.697</td><td>4623</td><td>4061</td><td>0.5100</td><td>0.0000</td><td>0.0175</td><td>0.0175</td><td>0.0138</td></tr><tr><td>0.60</td><td>5000</td><td>20</td><td>0.350</td><td>0.697</td><td>4623</td><td>4061</td><td>0.6004</td><td>0.0004</td><td>0.0174</td><td>0.0174</td><td>0.0139</td></tr><tr><td>0.70</td><td>5000</td><td>20</td><td>0.450</td><td>0.697</td><td>4623</td><td>4061</td><td>0.6993</td><td>-0.0007</td><td>0.0192</td><td>0.0192</td><td>0.0152</td></tr><tr><td>0.80</td><td>5000</td><td>20</td><td>0.550</td><td>0.697</td><td>4623</td><td>4061</td><td>0.7990</td><td>-0.0010</td><td>0.0194</td><td>0.0194</td><td>0.0155</td></tr><tr><td>0.90</td><td>5000</td><td>20</td><td>0.650</td><td>0.697</td><td>4623</td><td>4061</td><td>0.8999</td><td>-0.0001</td><td>0.0200</td><td>0.0200</td><td>0.0158</td></tr></tbody></table>
Notes. The table reports Monte Carlo summaries of
\widehat { H } ;
mean, bias, standard deviation, RMSE, and MAE. For
H _ { 0 } \leq 1 / 2
, the estimator is computed with the unfiltered KS criterion. For
H _ { 0 }   >   1 / 2 ,
it is computed with the
\mathrm { G L { - } K S }
criterion, with α chosen so that
H _ { 0 } - \alpha = 0 . 2 5
, and with branch-wise burn-in correction. The analysis uses
\mathcal { M } = 1 0 0 0
Monte Carlo simulations.

## 5 Financial applications

In the present section, we apply the KS/GL–KS methodology to financial time series. The purpose of this section is twofold. First, we use the estimator to investigate the rough volatility hypothesis, namely the empirical evidence that volatility-related processes display Hurst exponents significantly below the Brownian regularity
H = 1 / 2
. Second, we apply the same distribution-based framework to log-price trajectories in order to detect persistent, anti-persistent, and efficient market regimes.

These two applications are conceptually distinct. In the rough volatility setting, the relevant empirical question is whether the volatility process is rough; that is, whether its estimated Hurst exponent is below
1 / 2
. In the log-price setting, instead, the benchmark
H = 1 / 2
is interpreted as the Brownian or weak-form efficiency reference point. Deviations above or below this threshold are used as evidence of persistent or anti-persistent scaling regimes. The aim is not to provide a direct arbitrage test, but rather to construct a non-parametric diagnostic of departures from Brownian scaling across markets and time windows.

A key point of the empirical implementation is that the distributional estimator and the inferential distribution are selected in two distinct steps. First, the Hurst exponent is estimated from the distributional self-similarity criterion following the equation (5). This step identifies the empirical scaling exponent but is not, by itself, a significance statement. Second, conditional on the estimated regime, we select the asymptotic distribution used for inference. If
\widehat { H } \leq 1 / 2
, we use the unfiltered short-memory KS limit described in Proposition 2.2, corresponding to the case
\alpha = 0
. If
\widehat { H } > 1 / 2
, we activate the Grünwald–Letnikov filter and use the GL-KS short-memory limit with the corresponding burn-in correction (see Theorem 3.7 and Lemma 3.9).

24

<!-- page: 25 -->

## Page 25

## 5.1 Empirical Motivation

The Hurst exponent provides a compact way to summarize the scaling behavior of a stochastic process. In financial applications, however, its interpretation depends on the object under study.

The advantage of the distribution-based KS/GL-KS framework is that it estimates H through distributional self-similarity rather than through moment scaling alone. The GL correction is activated only in the persistent regime, where the unfiltered long-memory limit is affected by slow finite-sample convergence. In short-memory and anti-persistent regimes, the same framework reduces to the unfiltered KS statistic with
\alpha = 0
. This is useful in financial data, where heavy tails, regime changes, and structural breaks may affect moment-based estimates. Moreover, the GL correction developed in Section 3 allows the same testing logic to be applied in long-memory regimes without relying on the unstable finite-sample behavior of the unfiltered KS statistic.

## 5.1.1 Rough volatility

The rough-volatility literature provides a natural testing ground for the KS/GL–KS estimator. A standard way to model stochastic volatility with fractional features is to assume that log-volatility follows, or is well approximated by, a fractional Ornstein–Uhlenbeck-type dynamics [10]. This is the case, for instance, in fractional stochastic volatility models, where the volatility factor is driven by fractional noise and mean reversion is introduced through an Ornstein–Uhlenbeck kernel [9]:

\operatorname { l o g } \sigma _ { t } = \mu + \eta \int _ { - \infty } ^ { t } e ^ { - \lambda ( t - s ) } d B _ { s } ^ { H } ,\tag{19}

where
\mu
is the long-mean term,
\lambda > 0
the mean-reverting term,
\eta > 0
the diffusion parameter and
d B ^ { H }
the fractional measure, respectively.

This point requires a clarification. The fractional Ornstein–Uhlenbeck process is stationary and mean-reverting; it is not globally self-similar. Therefore, applying the KS/GL–KS estimator in this setting does not amount to assuming that the fOU process itself is self-similar. Rather, the estimator is used to recover the local roughness parameter governing the small-scale behavior of the process. Indeed, over short time intervals, the mean-reversion component is negligible. If λ denotes the meanreversion speed and a is the scale of the increment used in the multi-scale comparison, then in the regime
a \lambda \ll 1
the exponential OU kernel is locally close to one. In this range, fOU increments behave approximately as fractional Brownian increments, with scaling governed by the same Hurst parameter H. The KS/GL–KS estimator is therefore applied in this local fBm-like regime.

In the rough-volatility application, the empirical question is whether the estimated roughness parameter lies below the Brownian regularity
H   =   1 / 2
Evidence for
H   <   1 / 2
is interpreted as roughness of the volatility path [15]. Since the rough-volatility hypothesis corresponds to
H < 1 / 2 ,
, the relevant empirical regime is already short-memory or anti-persistent. Therefore, no GL correction is required in this application. Accordingly, we use the unfiltered short-memory version of the procedure described in Remark 3.12.

## 5.1.2 Weak-Form Market Efficiency

The second application concerns log-price trajectories. Let
X _ { t }   =   \log P _ { t }
denote the log-price of a financial index. The empirical procedure is applied to multi-scale increments of the form
X _ { t + a } - X _ { t } ,
so that the analysis focuses on the scaling behavior of log-price changes rather than on the marginal distribution of the price level itself.

25

<!-- page: 26 -->

## Page 26

In this setting, the value
H   =   1 / 2
plays the role of a Brownian benchmark and is naturally connected with the weak form of the Efficient Market Hypothesis (EMH).
1
Under this benchmark, log-prices behave locally as a Brownian-type process and past price information should not generate persistent or anti-persistent scaling patterns.

The use of the Hurst exponent as a diagnostic for market efficiency is also consistent with the econophysics literature on scaling and multiscaling in financial markets. Starting from the empirical evidence of scaling laws in financial indices documented by [20], subsequent contributions developed generalized Hurst exponent and multifractal approaches to detect departures from simple Brownian scaling in asset prices [8, 12]. More recently, time-varying Hurst–Hölder exponents have been used to describe local changes in market efficiency and to interpret financial markets as systems alternating between efficient and inefficient states [4]. Related evidence on the interaction between price multiscaling and volatility roughness is discussed in [5].

A market window is therefore classified as persistent when the confidence interval for H lies entirely above
1 / 2 ,
, anti-persistent when it lies entirely below
1 / 2 ,
and neutral when the interval contains
1 / 2 .
Persistent windows indicate trend-like scaling behavior and possible departures from weakform efficiency, while anti-persistent windows indicate mean-reverting or reversal-like scaling behavior. Neutral windows are those for which the data do not provide statistically significant evidence against the Brownian regularity
1 / 2 .
. This classification should be interpreted as a scaling diagnostic rather than as a direct test of arbitrage opportunities. A statistically significant deviation from
1 / 2
indicates a departure from Brownian scaling, but it does not by itself identify an exploitable trading strategy.

**[table]**

Table 5: Description of the log-volatility dataset.
<table><tbody><tr><td>Ticker</td><td>Index</td><td>N</td><td>Start Date</td><td>End Date</td><td>ADF stat.</td><td>ADF p-value</td></tr><tr><td>AEX</td><td>Amsterdam Exchange Index (NLD)</td><td>4, 714</td><td>2000-01-03</td><td>2018-06-27</td><td>-13.850</td><td>&lt; 0.001</td></tr><tr><td>AORD</td><td>All Ordinaries (AUS)</td><td>4, 665</td><td>2000-01-04</td><td>2018-06-27</td><td>-18.861</td><td>&lt; 0.001</td></tr><tr><td>BFX</td><td>Bel 20 (BEL)</td><td>4, 712</td><td>2000-01-03</td><td>2018-06-27</td><td>-14.364</td><td>&lt; 0.001</td></tr><tr><td>BSESN</td><td>Bombay Stock Exchange Sensitive Index (IND)</td><td>4, 591</td><td>2000-01-03</td><td>2018-06-27</td><td>-15.424</td><td>&lt; 0.001</td></tr><tr><td>BVLG</td><td>PSI All Share Gross Return (PRT)</td><td>1, 453</td><td>2012-10-15</td><td>2018-06-27</td><td>-9.362</td><td>&lt; 0.001</td></tr><tr><td>BVSP</td><td>Bovespa Index (BRA)</td><td>4, 556</td><td>2000-01-03</td><td>2018-06-27</td><td>-19.268</td><td>&lt; 0.001</td></tr><tr><td>DJI</td><td>Dow Jones Index (USA)</td><td>4, 635</td><td>2000-01-03</td><td>2018-06-27</td><td>-15.354</td><td>&lt; 0.001</td></tr><tr><td>FCHI</td><td>Cac 40 (FRA)</td><td>4, 713</td><td>2000-01-03</td><td>2018-06-27</td><td>-14.405</td><td>&lt; 0.001</td></tr><tr><td>FTSE</td><td>Footsie 100 Index (GBR)</td><td>4, 660</td><td>2000-01-04</td><td>2018-06-27</td><td>-15.886</td><td>&lt; 0.001</td></tr><tr><td>FTSEMIB</td><td>FTSE Milano Indice di Borsa (ITA)</td><td>2, 307</td><td>2009-06-01</td><td>2018-06-27</td><td>-13.069</td><td>&lt; 0.001</td></tr><tr><td>FTSTI</td><td>FTSE Straits Times Index (SGP)</td><td>2, 696</td><td>2000-01-03</td><td>2018-06-27</td><td>-16.045</td><td>&lt; 0.001</td></tr><tr><td>GDAXI</td><td>Dax 30 (DEU)</td><td>4, 692</td><td>2000-01-03</td><td>2018-06-27</td><td>-14.267</td><td>&lt; 0.001</td></tr><tr><td>GSPTSE</td><td>Toronto Stock Exchange C. I. (CAN)</td><td>4, 043</td><td>2002-05-02</td><td>2018-06-27</td><td>-15.314</td><td>&lt; 0.001</td></tr><tr><td>HSI</td><td>Hang Seng Index (HKG)</td><td>4, 532</td><td>2000-01-04</td><td>2018-06-27</td><td>-15.611</td><td>&lt; 0.001</td></tr><tr><td>IBEX</td><td>Ibex 35 (ESP)</td><td>4, 681</td><td>2000-01-03</td><td>2018-06-27</td><td>-14.458</td><td>&lt; 0.001</td></tr><tr><td>IXIC</td><td>NASDAQ Composite Index (USA)</td><td>4, 637</td><td>2000-01-03</td><td>2018-06-27</td><td>-13.526</td><td>&lt; 0.001</td></tr><tr><td>KS11</td><td>Korea Composite Stock Price Index (KOR)</td><td>4, 550</td><td>2000-01-04</td><td>2018-06-27</td><td>-11.902</td><td>&lt; 0.001</td></tr><tr><td>KSE</td><td>Pakistan Stock Exchange Index (PAK)</td><td>4, 494</td><td>2000-01-04</td><td>2018-06-27</td><td>-18.552</td><td>&lt; 0.001</td></tr><tr><td>MXX</td><td>Mexico Exchange Index (MEX)</td><td>4, 640</td><td>2000-01-03</td><td>2018-06-27</td><td>-19.473</td><td>&lt; 0.001</td></tr><tr><td>NSEI</td><td>Nifty 50 Index (IND)</td><td>4, 586</td><td>2000-01-03</td><td>2018-06-27</td><td>-15.644</td><td>&lt; 0.001</td></tr><tr><td>N225</td><td>Nikkei 225 (JPN)</td><td>4, 501</td><td>2000-02-02</td><td>2018-06-27</td><td>-16.238</td><td>&lt; 0.001</td></tr><tr><td>OMXC20</td><td>Omx Copenhagen 20 Index (DNK)</td><td>3, 167</td><td>2005-10-03</td><td>2018-06-27</td><td>-15.023</td><td>&lt; 0.001</td></tr><tr><td>OMXHPI</td><td>Omx Helsinki All-Share Index (FIN)</td><td>3, 197</td><td>2005-10-03</td><td>2018-06-27</td><td>-12.885</td><td>&lt; 0.001</td></tr><tr><td>OMXSPI</td><td>Omx Stockholm All-Share Index (SWE)</td><td>3, 196</td><td>2005-10-03</td><td>2018-06-27</td><td>-11.685</td><td>&lt; 0.001</td></tr><tr><td>OSEAX</td><td>Oslo Bors All-Share Index (NOR)</td><td>4, 192</td><td>2001-09-03</td><td>2018-06-27</td><td>-16.314</td><td>&lt; 0.001</td></tr><tr><td>RUT</td><td>Russell 2000 (USA)</td><td>4, 636</td><td>2000-01-03</td><td>2018-06-27</td><td>-18.909</td><td>&lt; 0.001</td></tr><tr><td>SPX</td><td>S&amp;P 500 Index (USA)</td><td>4, 641</td><td>2000-01-03</td><td>2018-06-27</td><td>-14.390</td><td>&lt; 0.001</td></tr><tr><td>SSE</td><td>Shanghai Stock Exchange Composite Index (CHN)</td><td>4, 461</td><td>2000-01-04</td><td>2018-06-27</td><td>-14.730</td><td>&lt; 0.001</td></tr><tr><td>SSMI</td><td>Swiss Market Index (CHE)</td><td>4, 636</td><td>2000-01-04</td><td>2018-06-27</td><td>-13.219</td><td>&lt; 0.001</td></tr><tr><td>STOXX50E</td><td>Euro Stock 50 (EUR)</td><td>4, 713</td><td>2000-01-03</td><td>2018-06-27</td><td>-17.973</td><td>&lt; 0.001</td></tr></tbody></table>
Notes. The table reports the volatility-related series used in the rough-volatility application. N denotes the number of available observations after preprocessing. The start and end dates indicate the calendar coverage of each series. The ADF column reports the Augmented Dickey–Fuller statistic, with the corresponding p-value reported in the last column.

[ ], [...]

1According to 14 “ a market in which prices always fully reflect available information is called efficient.” Depending on the information set, different forms of market efficiency can be considered: weak-form efficiency, when current prices reflect all information contained in past prices; semi-strong-form efficiency, when prices also reflect all publicly available information, such as earnings announcements, stock splits, or macroeconomic news; and strong-form efficiency, when prices also reflect private information available only to some investors. Since the present analysis is based only on historical price trajectories, it is related to weak-form efficiency.

26

<!-- page: 27 -->

## Page 27

## 5.2 Data

The empirical analysis is based on two datasets, corresponding to the two applications described above. The first dataset is used for the rough-volatility exercise and contains volatility-related series for a set of major equity indices. The second dataset contains daily closing prices for a broader panel of international stock-market indices and is used to study persistence, anti-persistence, and neutral regimes in log-price dynamics.

For the rough-volatility application, we use daily log-realized volatility series computed from
5 -
minute intraday returns. The sample composition, reported in Table 5, is taken from the Oxford-Man Institute Realized Library. Since the objective is to estimate the local roughness parameter, the GL– KS estimator is applied to volatility increments at short scales, consistently with the local fBm-like approximation discussed in the previous Subsection.

For the market-efficiency application, we consider the log-price process
X _ { t } \: = \:
log
P _ { t } ,
where
P _ { t }
denotes the daily closing price of the corresponding index. The analysis is performed on multi-scale log-price increments
X _ { t + a } - X _ { t }
. Table 6 reports the list of indices, sample lengths, calendar coverage, and preliminary stationarity diagnostics for the associated return series.

**[table]**

Table 6: Description of the log-price dataset
<table><tbody><tr><td>Ticker</td><td>Index</td><td>N</td><td>Start Date</td><td>End Date</td><td>ADF stat.</td><td>ADF p-value</td></tr><tr><td>AEX</td><td>Amsterdam Exchange Index (NLD)</td><td>10,922</td><td>1983-01-04</td><td>2025-10-16</td><td>-73.991</td><td>&lt;0.001</td></tr><tr><td>AORD</td><td>All Ordinaries (AUS)</td><td>6,294</td><td>2001-04-19</td><td>2025-10-16</td><td>-55.765</td><td>&lt;0.001</td></tr><tr><td>ATG</td><td>Athens General Composite Index (GRC)</td><td>5,857</td><td>1997-07-01</td><td>2021-09-30</td><td>-92.268</td><td>&lt;0.001</td></tr><tr><td>AXJO</td><td>Asx 200 (AUS)</td><td>8,278</td><td>1992-11-23</td><td>2025-08-22</td><td>-64.972</td><td>&lt;0.001</td></tr><tr><td>BFX</td><td>Bel 20 (BEL)</td><td>8,726</td><td>1991-04-09</td><td>2025-08-22</td><td>-63.957</td><td>&lt;0.001</td></tr><tr><td>BSESN</td><td>Bombay Stock Exchange Sensitive Index (IND)</td><td>6,934</td><td>1997-07-01</td><td>2025-08-22</td><td>-59.095</td><td>&lt;0.001</td></tr><tr><td>BUX</td><td>Budapest Stock Exchange Index (HUN)</td><td>5,908</td><td>1997-07-01</td><td>2021-09-30</td><td>-54.778</td><td>&lt;0.001</td></tr><tr><td>BVSP</td><td>Bovespa Index (BRA)</td><td>8,005</td><td>1993-04-27</td><td>2025-08-22</td><td>-62.106</td><td>&lt;0.001</td></tr><tr><td>DJI</td><td>Dow Jones Index (USA)</td><td>13,516</td><td>1979-12-25</td><td>2025-10-15</td><td>-83.831</td><td>&lt;0.001</td></tr><tr><td>FCHI</td><td>Cac 40 (FRA)</td><td>9,717</td><td>1987-07-10</td><td>2025-10-16</td><td>-70.736</td><td>&lt;0.001</td></tr><tr><td>FTSE</td><td>Footsie 100 Index (GBR)</td><td>10,519</td><td>1984-01-03</td><td>2025-08-22</td><td>-74.554</td><td>&lt;0.001</td></tr><tr><td>FTSEMIB</td><td>FTSE Milano Indice di Borsa (ITA)</td><td>7,097</td><td>1998-01-02</td><td>2025-10-16</td><td>-71.837</td><td>&lt;0.001</td></tr><tr><td>FTSTI</td><td>FTSE Straits Times Index (SGP)</td><td>9,408</td><td>1987-12-28</td><td>2025-08-22</td><td>-63.742</td><td>&lt;0.001</td></tr><tr><td>GDAXI</td><td>Dax 30 (DEU)</td><td>9,520</td><td>1987-12-30</td><td>2025-08-22</td><td>-70.405</td><td>&lt;0.001</td></tr><tr><td>GSPTSE</td><td>Toronto Stock Exchange C. I. (CAN)</td><td>11,588</td><td>1979-06-29</td><td>2025-08-13</td><td>-74.465</td><td>&lt;0.001</td></tr><tr><td>HSI</td><td>Hang Seng Index (HKG)</td><td>11,367</td><td>1979-12-25</td><td>2025-10-16</td><td>-75.867</td><td>&lt;0.001</td></tr><tr><td>IBEX</td><td>Ibex 35 (ESP)</td><td>8,639</td><td>1991-09-09</td><td>2025-10-16</td><td>-65.978</td><td>&lt;0.001</td></tr><tr><td>IMOEX</td><td>Moscow Exchange Index (RUS)</td><td>2,795</td><td>2013-03-05</td><td>2024-06-14</td><td>-37.995</td><td>&lt;0.001</td></tr><tr><td>IXIC</td><td>NASDAQ Composite Index (USA)</td><td>13,753</td><td>1971-02-05</td><td>2025-08-22</td><td>-82.574</td><td>&lt;0.001</td></tr><tr><td>JKSE</td><td>Jakarta Composite Index (IDN)</td><td>8,615</td><td>1990-04-06</td><td>2025-08-22</td><td>-61.003</td><td>&lt;0.001</td></tr><tr><td>KLCI</td><td>Kuala Lumpur Composite Index (MYS)</td><td>7,795</td><td>1993-12-03</td><td>2025-08-22</td><td>-58.853</td><td>&lt;0.001</td></tr><tr><td>KS11</td><td>Korea Composite Stock Price Index (KOR)</td><td>7,067</td><td>1996-12-11</td><td>2025-08-22</td><td>-59.636</td><td>&lt;0.001</td></tr><tr><td>MXX</td><td>Mexico Exchange Index (MEX)</td><td>9,742</td><td>1987-01-05</td><td>2025-10-15</td><td>-69.476</td><td>&lt;0.001</td></tr><tr><td>NSEI</td><td>Nifty 50 Index (IND)</td><td>7,451</td><td>1995-11-06</td><td>2025-10-16</td><td>-61.212</td><td>&lt;0.001</td></tr><tr><td>N225</td><td>Nikkei 225 (JPN)</td><td>14,909</td><td>1965-01-05</td><td>2025-08-22</td><td>-88.298</td><td>&lt;0.001</td></tr><tr><td>OMX</td><td>Omx Stockholm 30 (SWE)</td><td>4,202</td><td>2008-11-20</td><td>2025-08-22</td><td>-47.975</td><td>&lt;0.001</td></tr><tr><td>RUT</td><td>Russell 2000 (USA)</td><td>9,561</td><td>1987-09-10</td><td>2025-08-22</td><td>-68.595</td><td>&lt;0.001</td></tr><tr><td>SET</td><td>Stock Exchange of Thailand Index</td><td>7,000</td><td>1996-12-11</td><td>2025-08-22</td><td>-54.773</td><td>&lt;0.001</td></tr><tr><td>SPX</td><td>S&amp;P 500 Index (USA)</td><td>24,527</td><td>1927-12-30</td><td>2025-08-13</td><td>-113.176</td><td>&lt;0.001</td></tr><tr><td>SSE</td><td>Shanghai Stock Exchange Composite Index (CHN)</td><td>6,819</td><td>1997-07-02</td><td>2025-08-22</td><td>-58.947</td><td>&lt;0.001</td></tr><tr><td>SZSE</td><td>Shenzhen Stock Exchange Component Index (CHN)</td><td>6,786</td><td>1997-08-22</td><td>2025-08-22</td><td>-57.928</td><td>&lt;0.001</td></tr><tr><td>SSMI</td><td>Swiss Market Index (CHE)</td><td>9,500</td><td>1988-01-05</td><td>2025-10-16</td><td>-69.683</td><td>&lt;0.001</td></tr><tr><td>STOXX50E</td><td>Euro Stock 50 (EUR)</td><td>4,612</td><td>2007-03-30</td><td>2025-08-22</td><td>-49.450</td><td>&lt;0.001</td></tr><tr><td>TA-125</td><td>Tel Aviv 125 (ISR)</td><td>6,989</td><td>1992-10-08</td><td>2025-08-21</td><td>-57.929</td><td>&lt;0.001</td></tr><tr><td>TWII</td><td>Taiwan Weighted Index (TWN)</td><td>6,900</td><td>1997-07-02</td><td>2025-08-22</td><td>-56.339</td><td>&lt;0.001</td></tr></tbody></table>
Notes. The table reports the international stock-market indices used in the log-price application. N denotes the number of daily observations. The empirical analysis is performed on
X _ { t } = \log P _ { t }
, where
P _ { t }
is the daily closing price. The ADF column reports the Augmented Dickey–Fuller statistic computed on the corresponding log-return series, with the associated p-value reported in the last column.

The Augmented Dickey–Fuller (ADF) statistics reported in the data tables are used only as pre-liminary diagnostics. They confirm that the transformed series entering the empirical analysis are compatible with the standard stationarity requirements for increment-based scaling analysis. The subsequent inference on H is entirely based on the GL–KS procedure described in the next subsection.

27

<!-- page: 28 -->

## Page 28

## 5.3 Regime-Adaptive Empirical KS/GL-KS Methodology

The empirical implementation follows the distribution-based estimation procedure introduced in Section 3.1. For each time series, we construct multi-scale increments and estimate the Hurst exponent by minimizing the Kolmogorov–Smirnov distance between the empirical distribution of the unit-scale increments and the rescaled empirical distribution of the crossed increments.

The empirical procedure is regime-adaptive. For each series, we first compute the Hurst estimate

\widehat { H } = \mathop { \operatorname { a r g } \operatorname* { m i n } } _ { \theta \in \mathbb { H } } D _ { n , m } ( \theta ) ,

where
D _ { n , m } ( \theta )
denotes the distributional KS criterion computed from unit-scale increments and rescaled crossed increments. This first step is used only to estimate the self-similarity exponent. Inference is performed conditionally on the estimated regime. If
\widehat { H } \leq 1 / 2
, the process is treated as short-memory or anti-persistent. We set
\alpha = 0
, so that
\widetilde { \Delta _ { h } ^ { G L , 0 } } = I
, and use the short-memory limit of Proposition 2.2. No burn-in correction is applied, and the effective sample sizes coincide with the nominal crossed-sample sizes. If
\widehat { H } > 1 / 2
, the process is treated as persistent. In this case, the unfiltered long-memory limit is not used for empirical inference because of its slow finite-sample convergence. We instead apply the GL filter with an order α such that
\hat { H } - \alpha < 1 / 2
, and use the GL-KS limit of Theorem 3.7. The statistic is then computed after the branch-wise burn-in correction, with effective sample sizes
n _ { \mathrm { e f f } }
and
m _ { \mathrm { e f f } }
. The GL filter is therefore an inferential device, not a different definition of the Hurst exponent. By Corollary 3.4, the population minimizer of the distributional criterion is invariant under GL filtering; the filter changes the stochastic fluctuation and the limiting distribution, but not the target parameter
H _ { 0 }

The interpretation of the estimator depends on the application. In the rough-volatility exercise, the object of interest is the local roughness of log-realized volatility. Since the rough-volatility hypoth esis corresponds to
H   <   1 / 2
, the process is already in the short-memory or anti-persistent regime. Therefore, consistently with Remark 3.12, we set
\alpha = 0
and no burn-in correction is applied. In the log-price application, instead, the procedure is used to detect persistent, anti-persistent, and neutral market regimes relative to the Brownian benchmark
H = 1 / 2

For the rough-volatility application, we also fit an auxiliary stationary fractional Ornstein–Uhlenbeck specification, as described in equation (19). The fOU model provides a natural stationary framework for realized volatility with rough sample paths, as in [26]. In our implementation, however, the Hurst exponent is not estimated from the fOU model. It is first obtained from the KS criterion. Then, conditionally on
H = \widehat { H } _ { \mathrm { K S } }
, the mean-reversion speed λ is estimated using the moment-based estimator of [26, Eq. (3.4)]:

\widehat { \lambda } = \left( \frac { N \sum _ { i = 1 } ^ { N } \operatorname { l o g } \sigma _ { i } ^ { 2 } - \left( \sum _ { i = 1 } ^ { N } \operatorname { l o g } \sigma _ { i } \right) ^ { 2 } } { N ^ { 2 } \widehat { \eta } ^ { 2 } \widehat { H } _ { K S } \Gamma ( 2 \widehat { H } _ { K S } ) } \right) ^ { - 1 / ( 2 \widehat { H } _ { K S } ) } \; \operatorname { w i t h } \widehat { \eta } = \sqrt { \frac { \sum _ { i = 1 } ^ { N - 2 } ( \operatorname { l o g } \sigma _ { i + 2 } - 2 \operatorname { l o g } \sigma _ { i + 1 } + \operatorname { l o g } \sigma _ { i } ) ^ { 2 } } { N ( 4 - 2 ^ { 2 \widehat { H } _ { K S } } ) } } .

This auxiliary step is used only to assess the scale at which the local fBm approximation is applied. Specifically, the reported quantity
a \Delta \widehat { \lambda }
measures the selected scale
a \Delta
relative to the estimated meanreversion horizon, where
\Delta
represents the daily frequency
( \Delta = 1 )
. Small values of
a \Delta \widehat { \lambda }
indicate that mean reversion is negligible over the scale used in the GL–KS comparison, supporting the local fBmlike interpretation.

For each estimate, we report the point estimator
\widehat { H }
, its asymptotic standard error, the corresponding 95% confidence interval, and the value of the normalized KS statistic evaluated at
\widehat { H }
. The associated
p _ { \delta }
-value is used as a goodness-of-fit diagnostic for the distributional self-similarity relation at the estimated exponent.

28

<!-- page: 29 -->

## Page 29

## 5.3.1 Application I: Rough volatility

Table 7 reports the GL–KS estimates obtained from the daily log-realized volatility series. The estimation is performed at the fixed scale
a   =   1 0
. The last column reports
a \Delta \widehat { \lambda }
, computed from the auxiliary fOU fit described above. Since these values are close to zero, the selected scale is short relative to the estimated mean-reversion horizon, consistently with the local fBm-like approximation.

The results provide strong evidence in favour of rough volatility. Across all indices, the estimated Hurst exponents are well below the Brownian threshold
1 / 2 ,
and the corresponding confidence intervals lie entirely in the rough region. The estimates are concentrated around very low values of
H .
, typically between approximately 0.05 and 0.15, confirming that the local dynamics of log-realized volatility are substantially rougher than Brownian motion.

**[table]**

Table 7: GL–KS estimates of the Hurst exponent for log-volatility series.
<table><tr><td>Ticker</td><td>N</td><td><eq>\widehat { H }</eq> (95% CI)</td><td><eq>S E \times 1 0 ^ { 2 }</eq></td><td><eq>D _ { n , m } ^ { \star } ( \hat { H } )</eq></td><td>pδ-value</td><td><eq>a \Delta \widehat { \lambda }</eq></td></tr><tr><td>AEX</td><td>4,714</td><td>0.1255 (0.1057, 0.1454)</td><td>1.0142</td><td>0.9750</td><td>0.0500</td><td><eq>1 . 1 6 6 4 \times { { 1 0 } ^ { - 2 } }</eq></td></tr><tr><td>AORD</td><td>4,665</td><td>0.0545 (0.0358, 0.0732)</td><td>0.9529</td><td>0.3703</td><td>0.9946</td><td><eq>2 . 1 4 3 6 \times 1 0 ^ { - 6 }</eq></td></tr><tr><td>BFX</td><td>4,712</td><td>0.1220 (0.1021, 0.1419)</td><td>1.0174</td><td>0.9732</td><td>0.0491</td><td><eq>1 . 0 5 8 1 \times { { 1 0 } ^ { - 2 } }</eq></td></tr><tr><td>BSESN</td><td>4,591</td><td>0.1350 (0.1134, 0.1565)</td><td>1.0994</td><td>0.6509</td><td>0.5427</td><td><eq>1 . 1 3 1 0 \times 1 0 ^ { - 2 }</eq></td></tr><tr><td>BVLG</td><td>1,453</td><td>0.1480 (0.1088, 0.1872)</td><td>2.0023</td><td>0.6867</td><td>0.4547</td><td>-6 6.8824 × 10</td></tr><tr><td>BVSP</td><td>4,556</td><td>0.1148 (0.0946, 0.1351)</td><td>1.0327</td><td>0.8148</td><td>0.1900</td><td><eq>3 . 7 5 4 9 \times 1 0 ^ { - 2 }</eq></td></tr><tr><td>DJI</td><td>4,635</td><td>0.1220 (0.1024, 0.1416)</td><td>1.0013</td><td>0.9766</td><td>0.0474</td><td><eq>6 . 0 3 0 3 \times 1 0 _ { - 2 } ^ { - 3 }</eq></td></tr><tr><td>FCHI</td><td>4,713</td><td>0.1268 (0.1074, 0.1462)</td><td>0.9902</td><td>1.1398</td><td>0.0084</td><td><eq>1 . 0 5 2 9 \times 1 0 ^ { - 2 }</eq></td></tr><tr><td>FTSE</td><td>4,660</td><td>0.1058 (0.0858, 0.1258)</td><td>1.0202</td><td>0.6342</td><td>0.5485</td><td>-6 2.1491 × 10</td></tr><tr><td>FTSEMIB</td><td>2,307</td><td>0.1200 (0.0913, 0.1467)</td><td>1.4668</td><td>1.0516</td><td>0.0226</td><td>-3 3.3940 × 10</td></tr><tr><td>FTSTI</td><td>2,696</td><td>0.0702 (0.0454, 0.0950)</td><td>1.2645</td><td>0.5352</td><td>0.7905</td><td>6 3.7107 × 10</td></tr><tr><td>GDAXI</td><td>4,692</td><td>0.1260 (0.1062, 0.1458)</td><td>1.0094</td><td>0.7528</td><td>0.2966</td><td>4.8259 × 10 -3</td></tr><tr><td>GSPTSE</td><td>4,043</td><td>0.0915 (0.0712, 0.1119)</td><td>1.0384</td><td>0.6067</td><td>0.6157</td><td>-6 2.4734 × 10</td></tr><tr><td>HSI</td><td>4,532</td><td>0.0665 (0.0476, 0.0853)</td><td>0.0962</td><td>0.5443</td><td>0.7662</td><td>-6 2.2066 × 10</td></tr><tr><td>IBEX</td><td>4,681</td><td>0.1160 (0.0959, 0.1361)</td><td>1.0273</td><td>1.1226</td><td>0.0090</td><td>2.1369 × 10−6</td></tr><tr><td>IXIC</td><td>4,637</td><td>0.1531 (0.1318, 0.1743)</td><td>1.0856</td><td>0.5069</td><td>0.8833</td><td>-2 1.0789 × 10</td></tr><tr><td>KS11</td><td>4,550</td><td>0.1100 (0.0893, 0.1307)</td><td>1.0583</td><td>0.8133</td><td>0.1838</td><td>6 2.1978 × 10</td></tr><tr><td>KSE</td><td>4,494</td><td>0.1165 (0.0964, 0.1365)</td><td>1.0224</td><td>0.4980</td><td>0.8844</td><td>3.9042 × 10−2</td></tr><tr><td>MXX</td><td>4,640</td><td>0.0900 (0.0714, 0.1086)</td><td>0.9496</td><td>0.4340</td><td>0.9662</td><td>2.1560 × 10−6</td></tr><tr><td>NSEI</td><td>4,586</td><td>0.1250 (0.1046, 0.1453)</td><td>1.0361</td><td>0.7928</td><td>0.2318</td><td>6 2.1806 × 10</td></tr><tr><td>N225</td><td>4,501</td><td>0.1267 (0.1054, 0.1479)</td><td>1.0839</td><td>0.4790</td><td>0.9172</td><td>2.2171 × 10</td></tr><tr><td>OMXC20</td><td>3,167</td><td>0.1020 (0.0785, 0.1255)</td><td>1.1966</td><td>1.0092</td><td>0.0273</td><td>6 3.1581 × 10</td></tr><tr><td>OMXHPI</td><td>3,197</td><td>0.1430 (0.1174, 0.1685)</td><td>1.3045</td><td>0.5894</td><td>0.6907</td><td>-6 3.1280 × 10</td></tr><tr><td>OMXSPI</td><td>3,196</td><td>0.1363 (0.1115, 0.1612)</td><td>1.2675</td><td>0.7102</td><td>0.3981</td><td>6 3.1289 × 10</td></tr><tr><td>OSEAX</td><td>4,192</td><td>0.0864 (0.0660, 0.1069)</td><td>1.0413</td><td>0.8073</td><td>0.1726</td><td>2.3856 × 10 6</td></tr><tr><td>RUT</td><td>4,636</td><td>0.1231 (0.1027, 0.1434)</td><td>1.0372</td><td>0.4067</td><td>0.9851</td><td>-3 9.0486 × 10</td></tr><tr><td>SPX</td><td>4,641</td><td>0.1463 (0.1256, 0.1671)</td><td>1.0592</td><td>0.6828</td><td>0.4713</td><td>-2 1.1308 × 10</td></tr><tr><td>SSE</td><td>4,461</td><td>0.1461 (0.1238, 0.1685)</td><td>1.1395</td><td>0.4786</td><td>0.9199</td><td>2 1.2123 × 10 -2</td></tr><tr><td>SSMI</td><td>4,636</td><td>0.1240 (0.1034, 0.1446)</td><td>1.0526</td><td>0.8995</td><td>0.0965</td><td>1.2161 × 10 -3</td></tr><tr><td>STOXX50E</td><td>4,713</td><td>0.1235 (0.1041, 0.1430)</td><td>0.9910</td><td>0.7214</td><td>0.3578</td><td>8.1816 × 10</td></tr></table>
Notes. The table reports GL–KS estimates of the local Hurst exponent for daily log-realized volatility series. N denotes the number of observations. The column
\widehat { H }
reports the point estimate, with the corresponding 95% confidence interval in parentheses. The standard error is reported as
S E \times 1 0 ^ { 2 } . D _ { n , m } ^ { \star } ( \widehat { H } )
is the normalized KS statistic evaluated at the estimated Hurst exponent. The
p _ { \delta }
-value measures the empirical compatibility between the observed increments and the distributional self-similarity relation evaluated at
\widehat { H } .
The last column reports
a \Delta \widehat { \lambda } ,
where
\widehat { \lambda }
is the mean-reversion speed estimated from an auxiliary fOU model conditional on
H = \widehat { H } _ { \mathrm { G L K S } }
. Since all estimated Hurst exponents lie below
1 / 2 ,
the rough-volatility application is implemented with
\alpha = 0 ,
and no burn-in correction is applied.

The
p _ { \delta ^ { - } } \mathrm { v a l u e s }
quantify the empirical compatibility between the observed log-realized volatility increments and the distributional self-similarity relation evaluated at
\widehat { H }
. High values indicate that the estimated exponent provides a satisfactory GL–KS fit, whereas lower values point to a weaker agreement with the local fBm approximation. Some series display smaller
p _ { \delta ^ { - } } \mathrm { { v a l u e s } , }
suggesting that additional market-specific features may affect the local scaling structure. Nevertheless, this does not alter the main conclusion: the estimated confidence intervals remain far below
1 / 2 ,
providing robust evidence of rough volatility across the panel.

29

<!-- page: 30 -->

## Page 30

## 5.3.2 Application II: log-prices and weak-form efficiency

We now apply the GL–KS estimator to log-price trajectories. Differently from the rough-volatility application, the objective is not to test for roughness, but to assess whether the scaling behavior of log-prices is compatible with the Brownian benchmark
H = 1 / 2 .
. Values significantly above this threshold are interpreted as evidence of persistent scaling, values significantly below it as evidence of anti-persistent scaling, and confidence intervals containing
1 / 2
as neutral regimes.

Table 8 reports the full-window estimates. The estimates are generally close to the Brownian benchmark, but several indices display confidence intervals entirely above
1 / 2
, indicating persistent scaling over the full sample. A smaller number of markets are classified as neutral, since their confidence intervals contain
1 / 2 .
Isolated cases may display anti-persistent full-window behavior when the entire confidence interval lies below
1 / 2 .

**[table]**

Table 8: Full-window GL–KS estimates of the Hurst exponent for log-price trajectories.
<table><tbody><tr><td>Ticker</td><td>N</td><td>Method</td><td>neff</td><td>meff</td><td>γ</td><td>Hb (95% CI)</td><td>SE × 10<sup>2</sup></td><td>Dn⋆/<sub>eff</sub>† ,m<sub>eff</sub>(Hˆ)</td><td>p<sub>δ</sub>-value</td><td>p0.5-value</td></tr><tr><td>AEX</td><td>10,922</td><td>GL-KS</td><td>10,767</td><td>10,302</td><td>0.5421</td><td>0.5235 (0.5023,0.5447)</td><td>1.0812</td><td>0.8378</td><td>0.6773</td><td>0.0295</td></tr><tr><td>AORD</td><td>6,294</td><td>GL-KS</td><td>6,185</td><td>5,854</td><td>0.5353</td><td>0.5105 (0.4827,0.5384)</td><td>1.4198</td><td>0.7430</td><td>0.7947</td><td>0.4579</td></tr><tr><td>ATG</td><td>5,857</td><td>GL-KS</td><td>5,724</td><td>5,357</td><td>0.5633</td><td>0.5625 (0.5318,0.5932)</td><td>1.5653</td><td>0.8000</td><td>0.7733</td><td>&lt;0.001</td></tr><tr><td>AXJO</td><td>8,278</td><td>KS</td><td>8,277</td><td>8,257</td><td>-</td><td>0.4921 (0.4684,0.5159)</td><td>1.2123</td><td>0.6396</td><td>0.8957</td><td>0.5150</td></tr><tr><td>BFX</td><td>8,726</td><td>GL-KS</td><td>8,593</td><td>8,186</td><td>0.5385</td><td>0.5167 (0.4934,0.5401)</td><td>1.1907</td><td>1.8381</td><td>0.0117</td><td>0.1603</td></tr><tr><td>BSESN</td><td>6,934</td><td>GL-KS</td><td>6,795</td><td>6,400</td><td>0.5574</td><td>0.5520 (0.5248,0.5792)</td><td>1.3873</td><td>1.0865</td><td>0.3906</td><td>&lt;0.001</td></tr><tr><td>BUX</td><td>5,908</td><td>GL-KS</td><td>5,804</td><td>5,488</td><td>0.5347</td><td>0.5093 (0.4814,0.5371)</td><td>1.4208</td><td>0.9039</td><td>0.5915</td><td>0.5133</td></tr><tr><td>BVSP</td><td>8,005</td><td>KS</td><td>8,004</td><td>7,984</td><td>-</td><td>0.4875 (0.4631,0.5120)</td><td>1.2456</td><td>0.5517</td><td>0.9593</td><td>0.3168</td></tr><tr><td>DJI</td><td>13,516</td><td>GL-KS</td><td>13,342</td><td>12,816</td><td>0.5424</td><td>0.5221 (0.5036,0.5407)</td><td>0.9480</td><td>1.3736</td><td>0.1209</td><td>0.0196</td></tr><tr><td>FCHI</td><td>9,717</td><td>KS</td><td>9,716</td><td>9,696</td><td>-</td><td>0.4964 (0.4747,0.5181)</td><td>1.1068</td><td>0.5783</td><td>0.9414</td><td>0.7425</td></tr><tr><td>FTSE</td><td>10,519</td><td>GL-KS</td><td>10,383</td><td>9,959</td><td>0.5302</td><td>0.5005 (0.4800,0.5210)</td><td>1.0453</td><td>0.6489</td><td>0.8908</td><td>0.9635</td></tr><tr><td>FTSEMIB</td><td>7,097</td><td>GL-KS</td><td>6,986</td><td>6,637</td><td>0.5308</td><td>0.5015 (0.4760,0.5271)</td><td>1.3056</td><td>1.3519</td><td>0.1321</td><td>0.9065</td></tr><tr><td>FTSTI</td><td>9,048</td><td>GL-KS</td><td>9,241</td><td>8,768</td><td>0.5591</td><td>0.5550 (0.5314,0.5786)</td><td>1.2043</td><td>0.8309</td><td>0.7092</td><td>&lt;0.001</td></tr><tr><td>GDAXI</td><td>9,520</td><td>KS</td><td>9,519</td><td>9,499</td><td>-</td><td>0.4955 (0.4739,0.5172)</td><td>1.1032</td><td>0.6557</td><td>0.8828</td><td>0.6856</td></tr><tr><td>GSPTSE</td><td>11,588</td><td>GL-KS</td><td>11,397</td><td>10,868</td><td>0.5612</td><td>0.5588 (0.5377,0.5799)</td><td>1.0781</td><td>1.0730</td><td>0.4005</td><td>&lt;0.001</td></tr><tr><td>HSI</td><td>11,367</td><td>GL-KS</td><td>11,186</td><td>10,667</td><td>0.5565</td><td>0.5504 (0.5286,0.5723)</td><td>1.1139</td><td>1.3451</td><td>0.1534</td><td>&lt;0.001</td></tr><tr><td>IBEX</td><td>8,639</td><td>GL-KS</td><td>8,495</td><td>8,079</td><td>0.5482</td><td>0.5359 (0.5124,0.5594)</td><td>1.1986</td><td>1.1398</td><td>0.3183</td><td>0.0028</td></tr><tr><td>IMOEX</td><td>2,795</td><td>GL-KS</td><td>2,720</td><td>2,495</td><td>0.5433</td><td>0.5260 (0.4809,0.5711)</td><td>2.3012</td><td>0.9519</td><td>0.5604</td><td>0.2586</td></tr><tr><td>IXIC</td><td>13,753</td><td>GL-KS</td><td>13,524</td><td>12,913</td><td>0.5699</td><td>0.5739 (0.5546,0.5931)</td><td>0.9821</td><td>1.4419</td><td>0.1107</td><td>&lt;0.001</td></tr><tr><td>JKSE</td><td>8,615</td><td>GL-KS</td><td>8,448</td><td>7,995</td><td>0.5645</td><td>0.5645 (0.5399,0.5891)</td><td>1.2554</td><td>1.1177</td><td>0.3658</td><td>&lt;0.001</td></tr><tr><td>KLCI</td><td>7,795</td><td>GL-KS</td><td>7,634</td><td>7,195</td><td>0.5668</td><td>0.5685 (0.5419,0.5950)</td><td>1.3550</td><td>0.8348</td><td>0.7228</td><td>&lt;0.001</td></tr><tr><td>KS11</td><td>7,067</td><td>GL-KS</td><td>6,953</td><td>6,607</td><td>0.5341</td><td>0.5082 (0.4822,0.5342)</td><td>1.3276</td><td>0.9838</td><td>0.4747</td><td>0.5386</td></tr><tr><td>MXX</td><td>9,742</td><td>GL-KS</td><td>9,587</td><td>9,142</td><td>0.5489</td><td>0.5365 (0.5139,0.5591)</td><td>1.1514</td><td>1.0235</td><td>0.4484</td><td>0.0015</td></tr><tr><td>NSEI</td><td>7,452</td><td>GL-KS</td><td>7,310</td><td>6,911</td><td>0.5548</td><td>0.5472 (0.5207,0.5737)</td><td>1.3522</td><td>1.1490</td><td>0.3211</td><td>&lt;0.001</td></tr><tr><td>N225</td><td>14,909</td><td>GL-KS</td><td>14,706</td><td>14,129</td><td>0.5528</td><td>0.5435 (0.5255,0.5616)</td><td>0.9227</td><td>1.5890</td><td>0.0515</td><td>&lt;0.001</td></tr><tr><td>OMX</td><td>4,202</td><td>KS</td><td>4,201</td><td>4,181</td><td>-</td><td>0.4628 (0.4267,0.4990)</td><td>1.8440</td><td>0.6105</td><td>0.9196</td><td>0.0439</td></tr><tr><td>RUT</td><td>9,561</td><td>GL-KS</td><td>9,402</td><td>8,941</td><td>0.5530</td><td>0.5439 (0.5214,0.5664)</td><td>1.1471</td><td>1.4036</td><td>0.1179</td><td>&lt;0.001</td></tr><tr><td>SET</td><td>7,000</td><td>GL-KS</td><td>6,859</td><td>6,460</td><td>0.5585</td><td>0.5540 (0.5268,0.5811)</td><td>1.3864</td><td>1.2910</td><td>0.2023</td><td>&lt;0.001</td></tr><tr><td>SPX</td><td>24,527</td><td>GL-KS</td><td>24,260</td><td>23,507</td><td>0.5526</td><td>0.5433 (0.5292,0.5575)</td><td>0.7220</td><td>2.3074</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>SSE</td><td>6,819</td><td>GL-KS</td><td>6,686</td><td>6,299</td><td>0.5533</td><td>0.5445 (0.5174,0.5716)</td><td>1.3831</td><td>0.9087</td><td>0.6078</td><td>0.0013</td></tr><tr><td>SZSE</td><td>6,786</td><td>GL-KS</td><td>6,662</td><td>6,286</td><td>0.5458</td><td>0.5305 (0.5040,0.5569)</td><td>1.3449</td><td>0.6175</td><td>0.9306</td><td>0.0240</td></tr><tr><td>SSMI</td><td>9,500</td><td>GL-KS</td><td>9,362</td><td>8,940</td><td>0.5374</td><td>0.5145 (0.4928,0.5362)</td><td>1.1072</td><td>0.7052</td><td>0.8352</td><td>0.1918</td></tr><tr><td>STOXX50E</td><td>4,612</td><td>GL-KS</td><td>4,519</td><td>4,232</td><td>0.5361</td><td>0.5120 (0.4777,0.5463)</td><td>1.7488</td><td>1.2953</td><td>0.1770</td><td>0.4928</td></tr><tr><td>TA-125</td><td>6,989</td><td>GL-KS</td><td>6,853</td><td>6,469</td><td>0.5547</td><td>0.5471 (0.5202,0.5740)</td><td>1.3727</td><td>2.1247</td><td>0.0027</td><td>&lt;0.001</td></tr><tr><td>TWII</td><td>6,900</td><td>GL-KS</td><td>6,787</td><td>6,440</td><td>0.5340</td><td>0.5075 (0.4816,0.5335)</td><td>1.3256</td><td>1.1628</td><td>0.2752</td><td>0.5698</td></tr></tbody></table>

Notes. The table reports full-window GL–KS estimates of the Hurst exponent obtained from the log-price process
\overline { { X _ { t } = \operatorname { l o g } P _ { t } } } ,
using multi-scale increments
X _ { t + a }   -   X _ { t }
with scaling
a = 2 0
. The columns
n _ { \mathrm { e f f } }
and
m _ { \mathrm { e f f } }
denote the effective sample sizes of the unit-scale and crossed multi-scale samples after the finite-sample burn-in deletion. The column γ reports the burn-in exponent used in the GL implementation. The column
\widehat { H }
reports the point estimate, with the corresponding 95% confidence interval in parentheses. The standard error is reported as
S E \times 1 0 ^ { 2 } . \quad D _ { n _ { \mathrm { e f f } } , m _ { \mathrm { e f f } } } ^ { \dagger } ( \widehat { H } )
is the normalized GL–KS statistic evaluated at the estimated Hurst exponent, while
D _ { n _ { \mathrm { e f f } } , m _ { \mathrm { e f f } } } ^ { \star } ( \widehat { H } )
is the KS-SRD statistic. The
p _ { \delta ^ { * } }
-value measures the goodness of fit of the distributional self-similarity relation at
{ \widehat { H } } .
The
p _ { 0 . 5 }
-value is the two-sided p-value for the Brownian benchmark test
\mathcal { H } _ { 0 } ^ { \mathrm { B M } } = 1 / 2
against
\mathcal { H } _ { 1 } ^ { \mathrm { B M } } \neq 1 / 2 ,
computed from the asymptotic normal statistic
Z _ { 0 . 5 }   =   ( \widehat { H } - 1 / 2 ) / S E ( \widehat { H } )
An index is classified as persistent if the confidence interval lies entirely above
1 / 2 ,
anti-persistent if it lies entirely below
1 / 2 ,
and neutral otherwise. For GL-KS rows, α is chosen so that
\widehat { H }   -   \alpha < 1 / 2
. The burn-in exponent
\gamma
is chosen above the theoretical lower bound
\gamma _ { \operatorname* { m i n } } = 1 / [ 2 ( 1 + \alpha - \widehat { H } ) ]
. For KS rows,
\alpha = 0 ,   \gamma
is not defined, and no burn-in correction is applied.

The two p-values reported in the table have different meanings. The
p _ { \delta }
-value measures the empirical compatibility between the observed multi-scale increments and the distributional self-similarity relation evaluated at
\widehat { H }
. It is therefore a goodness-of-fit diagnostic for the
\mathrm { G L { - } K S }
scaling relation. The
p _ { 0 . 5 ^ { - } }
value is instead associated with the Brownian benchmark test

30

<!-- page: 31 -->

## Page 31

\mathcal { H } _ { 0 } ^ { \mathrm { B M } } : H = 1 / 2 \qquad \mathrm { a g a i n s t } \qquad \mathcal { H } _ { 1 } ^ { \mathrm { B M } } : H \neq 1 / 2 .

It is computed from the standardized statistic
\begin{array} { r } { Z _ { 0 . 5 } = \frac { \widehat { H } - 1 / 2 } { S E ( \widehat { H } ) } } \end{array}
using the asymptotic normal approximation. Hence, small values of
p _ { 0 . 5 }
indicate statistically significant departures from Brownian scaling. The direction of the departure is determined by the position of the confidence interval: values entirely above
1 / 2
identify persistent regimes, while values entirely below
1 / 2
identify anti-persistent regimes.

## 6 Conclusion

This paper introduced a Grünwald–Letnikov–Kolmogorov–Smirnov framework for testing and estimating the self-similarity parameter of fractional processes under long-range dependence. The main contribution is to show that the discrete Grünwald–Letnikov filter separates memory from scaling: it removes the low-frequency singularity responsible for slow convergence while preserving the self-similar structure needed for the distributional comparison across scales. As a result, the GL–KS statistic recovers a standard short-memory asymptotic regime, with stable finite-sample behavior confirmed by the Monte Carlo experiments.

The empirical analysis illustrates the usefulness of the method in finance. For log-realized volatility, the estimates provide evidence in favour of rough volatility, with Hurst exponents significantly below the Brownian threshold
H   =   1 / 2
. For log-prices, the method is used as a conservative diagnostic of weak-form market efficiency: confidence intervals containing
1 / 2
indicate statistical compatibility with the Brownian benchmark, whereas intervals entirely above or below
1 / 2
suggest persistent or anti-persistent departures from weak-form efficiency.

## References

[1] D. Angelini and S. Bianchi. Kolmogorov–Smirnov estimation of self-similarity in long-range dependent fractional processes. Physica D: Nonlinear Phenomena, 476:134697, 2025.

[2] M.A. Arcones. Limit theorems for nonlinear functionals of a stationary Gaussian sequence of vectors. Annals of Probability, 22(4):2242–2274, 1994.

[3] S. Bianchi. A new distribution-based test of self-similarity. Fractals, 12(03):331–346, 2004.

[4] S. Bianchi and A. Pianese. Time-varying Hurst–Hölder exponents and the dynamics of (in)efficiency in stock markets. Chaos, Solitons & Fractals, 109:64–75, 2018.

[5] G. Brandi and T. Di Matteo. Multiscaling and rough volatility: An empirical investigation. International Review of Financial Analysis, 84:102324, 2022.

[6] P. Breuer and P. Major. Central limit theorems for non-linear functionals of Gaussian fields. Journal of Multivariate Analysis, 13(3):425–441, 1983.

[7] P.J. Brockwell and R.A. Davis. Time series: Theory and methods. Springer science & business media, 2009.

[8] A. Carbone, G. Castelli, and H.E. Stanley. Time-dependent Hurst exponent in financial time series. Physica A: Statistical Mechanics and its Applications, 344(1-2):267–271, 2004.

31

<!-- page: 32 -->

## Page 32

[9] P. Cheridito, H. Kawaguchi, and M. Maejima. Fractional Ornstein-Uhlenbeck processes. Electronic Journal of Probability [electronic only], 8, 2003.

[10] F. Comte and E. Renault. Long memory in continuous-time stochastic volatility models. Mathematical Finance, 8(4):291–323, 1998.

[11] H. Dehling and M.S. Taqqu. The empirical process of some long-range dependent sequences with an application to U-statistics. Annals of Statistics, 17(4):1767–1783, 1989.

[12] T. Di Matteo. Multi-scaling in finance. Quantitative finance, 7(1):21–36, 2007.

[13] R.L. Dobrushin and P. Major. Non-central limit theorems for non-linear functional of Gaussian fields. Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete, 50(1):27–52, 1979.

[14] E.F. Fama. Efficient capital markets: a review of theory and empirical work. The Journal of Finance, 25(2):383–417, 1970.

[15] J. Gatheral, T. Jaisson, and M. Rosenbaum. Volatility is rough. Quantitative Finance, 18(6):933–949, 2018.

[16] L. Giraitis, H.L. Koul, and D. Surgailis. Large sample inference for long memory processes. World Scientific, 2012.

[17] J.W. Kantelhardt, E. Koscielny-Bunde, H.H.A. Rego, S. Havlin, and A. Bunde. Detecting longrange correlations with detrended fluctuation analysis. Physica A: Statistical Mechanics and its Applications, 295:441–454, 2001.

[18] A.N. Kolmogorov. Wienershe spiralen und einige andere interessante kurven im hilbertishen raum. DAS of the URSS (Nat. Sciences), 26:115–118, 1940.

[19] B.B. Mandelbrot and J.W. Van Ness. Fractional Brownian motions, fractional noises and applications. SIAM Review, 10(4):422–437, 1968.

[20] R.N. Mantegna and H.E. Stanley. An Introduction to Econophysics. Correlations and Complexity in Finance. Cambridge University Press, 2004.

[21] A. Ouannas, I.M. Batiha, and V.-T. Pham. Fractional Discrete Chaos. World Scientific, 2023.

[22] I. Podlubny. Fractional Differential Equations, volume 198. Elsevier, 1998.

[23] M.S. Taqqu. Weak convergence to fractional Brownian motion and to the Rosenblatt process. Advances in Applied Probability, 7(2):249–249, 1975.

[24] M.S. Taqqu, V. Teverovsky, and W. Willinger. Estimators for long-range dependence: An empirical study. Fractals, 3(4):785–798, 1995.

[25] V. Teverovsky and M. Taqqu. Testing for long-range dependence in the presence of shifting means or a slowly declining trend, using a variance-type estimator. Journal of Time Series Analysis, 18(3):279–304, 1997.

[26] X. Wang, W. Xiao, and J. Yu. Modeling and forecasting realized volatility with the fractional Ornstein–Uhlenbeck process. Journal of Econometrics, 232(2):389–415, 2023.

[27] R. Weron. Estimating long-range dependence: Finite sample properties and confidence intervals. Physica A: Statistical Mechanics and its Applications, 312(1–2):285–299, 2002.

32

<!-- page: 33 -->

## Page 33

[28] A.T.A. Wood and G. Chan. Simulation of stationary Gaussian processes in
[ 0 , 1 ] ^ { d }
. Journal of Computational and Graphical Statistics, 3(4):409–432, 1994.

## A Proof of the short-memory benchmark

We prove Proposition 2.2 in the balanced regime
\textstyle n , m \to \infty , { \frac { n } { m } } \to 1
. Let

\xi _ { i } ( x ) : = \mathbb { 1 } _ { \{ X _ { i } \leq x \} } - \Phi ( x ) , \qquad \eta _ { j } ( x ) : = \mathbb { 1 } _ { \{ Y _ { j } \leq x \} } - \Phi ( x ) ,

so that

F _ { n } ( x ) - G _ { m } ( x ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \xi _ { i } ( x ) - \frac { 1 } { m } \sum _ { j = 1 } ^ { m } \eta _ { j } ( x ) .

Define the marginal empirical processes

\alpha _ { n } ( x ) : = \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \xi _ { i } ( x ) , \qquad \beta _ { m } ( x ) : = \frac { 1 } { \sqrt { m } } \sum _ { j = 1 } ^ { m } \eta _ { j } ( x ) .

Then

\sqrt { \frac { n m } { n + m } } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) = \sqrt { \frac { m } { n + m } } \: \alpha _ { n } ( x ) - \sqrt { \frac { n } { n + m } } \: \beta _ { m } ( x ) .

Since
n / m \rightarrow 1
, we have
\begin{array} { r } { \sqrt { \frac { m } { n + m } } \rightarrow \frac { 1 } { \sqrt { 2 } } , \; \sqrt { \frac { n } { n + m } } \rightarrow \frac { 1 } { \sqrt { 2 } } } \end{array}
. Therefore,

\sqrt { \frac { n m } { n + m } } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) = \frac { 1 } { \sqrt { 2 } } \left( \alpha _ { n } ( x ) - \beta _ { m } ( x ) \right) + o _ { P } ( 1 ) .

We now identify the covariance structure of the limiting process. If U and V are standard Gaussian random variables with correlation
\rho ,
then

\operatorname { C o v } \left( \mathbb { 1 } _ { \{ U \leq x \} } , \mathbb { 1 } _ { \{ V \leq y \} } \right) = \Phi _ { 2 } ( x , y ; \rho ) - \Phi ( x ) \Phi ( y ) ,

where
\Phi _ { 2 } ( \cdot , \cdot ; \rho )
denotes the distribution function of a centered bivariate normal vector with unit variances and correlation
\rho .
Hence, writing
\rho _ { X } ( k ) = \operatorname { C o r r } ( X _ { 0 } , X _ { k } )
, we define

\Gamma _ { X } ( x , y ) : = \sum _ { k \in \mathbb { Z } } \left[ \Phi _ { 2 } ( x , y ; \rho _ { X } ( k ) ) - \Phi ( x ) \Phi ( y ) \right] \qquad \Gamma _ { Y } ( x , y ) : = \sum _ { k \in \mathbb { Z } } \left[ \Phi _ { 2 } ( x , y ; \rho _ { Y } ( k ) ) - \Phi ( x ) \Phi ( y ) \right] ,

and the cross-covariance kernels are

\Gamma _ { X Y } ( x , y ) : = \sum _ { k \in \mathbb { Z } } \left[ \Phi _ { 2 } ( x , y ; \rho _ { X Y } ( k ) ) - \Phi ( x ) \Phi ( y ) \right] , \qquad \Gamma _ { Y X } ( x , y ) : = \sum _ { k \in \mathbb { Z } } \left[ \Phi _ { 2 } ( x , y ; \rho _ { Y X } ( k ) ) - \Phi ( x ) \Phi ( y ) \right] .

By assumption, the auto-covariance and cross-covariance sequences of the underlying Gaussian increments are absolutely summable. Since the functions
z \mapsto \mathbb { 1 } _ { \{ z \leq x \} } - \Phi ( x )
are bounded and measurable, the corresponding covariance series defining
\Gamma _ { X } , \Gamma _ { Y } , \Gamma _ { X Y } , \dot { \Gamma _ { Y X } }
are finite. Therefore the joint empirical process
( \alpha _ { n } , \beta _ { m } )
satisfies a functional central limit theorem in
\ell ^ { \infty } ( \mathbb { R } ) \times \ell ^ { \infty } ( \mathbb { R } )
. Thus

33

( \alpha _ { n } , \beta _ { m } ) \Rightarrow ( \alpha , \beta ) ,

<!-- page: 34 -->

## Page 34

where
( \alpha , \beta )
is a centered Gaussian pair with covariance kernels

\begin{cases} { \operatorname { C o v } ( \alpha ( x ) , \alpha ( y ) ) = \Gamma _ { X } ( x , y ) , } \\ { \operatorname { C o v } ( \beta ( x ) , \beta ( y ) ) = \Gamma _ { Y } ( x , y ) , } \\ { \operatorname { C o v } ( \alpha ( x ) , \beta ( y ) ) = \Gamma _ { X Y } ( x , y ) , } \\ { \operatorname { C o v } ( \beta ( x ) , \alpha ( y ) ) = \Gamma _ { Y X } ( x , y ) . } \\ \end{cases}

Consequently,

\sqrt { \frac { n m } { n + m } } \left( F _ { n } - G _ { m } \right) \Rightarrow U \qquad \mathrm { i n ~ } \ell ^ { \infty } ( \mathbb { R } ) ,

where
\begin{array} { r } { U ( x ) = \frac { 1 } { \sqrt { 2 } } \left( \alpha ( x ) - \beta ( x ) \right) } \end{array}
. The covariance kernel of U is therefore

\operatorname { C o v } ( U ( x ) , U ( y ) ) = \frac { 1 } { 2 } \Gamma _ { X } ( x , y ) + \frac { 1 } { 2 } \Gamma _ { Y } ( x , y ) - \frac { 1 } { 2 } \left[ \Gamma _ { X Y } ( x , y ) + \Gamma _ { Y X } ( x , y ) \right] .

Finally, by the continuous mapping theorem applied to the supremum norm,

\sqrt { \frac { n m } { n + m } } D _ { n , m } = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \sqrt { \frac { n m } { n + m } } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) \right| \Rightarrow \operatorname* { s u p } _ { x \in \mathbb { R } } | U ( x ) | .

This proves Proposition 2.2.

## B Proof of the long-memory benchmark

We prove Proposition 2.3 in the balanced regime
\textstyle n , m \to \infty , { \frac { n } { m } } \to 1
. Throughout this Appendix we assume
H > 1 / 2
. Let

h _ { x } ( z ) : = \mathbb { 1 } _ { \{ z \leq x \} } - \Phi ( x ) , \qquad x \in \mathbb { R } .

For
Z \sim \mathcal { N } ( 0 , 1 )
, we have

\mathbb { E } [ h _ { x } ( Z ) Z ] = \mathbb { E } \left[ Z \mathbb { 1 } _ { \{ Z \leq x \} } \right] = \int _ { - \infty } ^ { x } z \phi ( z ) \mathop { } \mathopen { } d z = - \phi ( x ) .

Hence
h _ { x } ( Z )
admits the Gaussian projection decomposition

h _ { x } ( Z ) = - \phi ( x ) Z + r _ { x } ( Z ) ,\tag{20}

where
r _ { x } ( Z ) : = h _ { x } ( Z ) + \phi ( x ) Z
satisfies
\mathbb { E } [ r _ { x } ( Z ) ] = 0
, and
\mathbb { E } [ r _ { x } ( Z ) Z ] = 0

Applying the identity (20) to the first sample gives

\sum _ { i = 1 } ^ { n } h _ { x } ( X _ { i } ) = - \phi ( x ) \sum _ { i = 1 } ^ { n } X _ { i } + \sum _ { i = 1 } ^ { n } r _ { x } ( X _ { i } ) .

Therefore,

n ^ { 1 - H } \left( F _ { n } ( x ) - \Phi ( x ) \right) = - \phi ( x ) n ^ { - H } \sum _ { i = 1 } ^ { n } X _ { i } + n ^ { - H } \sum _ { i = 1 } ^ { n } r _ { x } ( X _ { i } ) .

Similarly,

m ^ { 1 - H } \left( G _ { m } ( x ) - \Phi ( x ) \right) = - \phi ( x ) m ^ { - H } \sum _ { j = 1 } ^ { m } Y _ { j } + m ^ { - H } \sum _ { j = 1 } ^ { m } r _ { x } ( Y _ { j } ) .

34

<!-- page: 35 -->

## Page 35

We first consider the leading linear terms. Since the increments are Gaussian and long-range dependent with parameter
H > 1 / 2
, the normalized linear partial sums satisfy

m ^ { - H } \sum _ { i = 1 } ^ { n } X _ { i } \Rightarrow Z _ { X } , \quad \mathrm { ~ a n d ~ } \quad m ^ { - H } \sum _ { j = 1 } ^ { m } Y _ { j } \Rightarrow Z _ { Y } ,

where
( Z _ { X } , Z _ { Y } )
is a centered Gaussian vector with

\operatorname { V a r } ( Z _ { X } ) = \sigma _ { X } ^ { 2 } , \qquad \operatorname { V a r } ( Z _ { Y } ) = \sigma _ { Y } ^ { 2 } , \qquad \operatorname { C o v } ( Z _ { X } , Z _ { Y } ) = \sigma _ { X Y } .

It remains to show that the residual terms are negligible at the normalization used above. Let
U
and
V
be standard Gaussian random variables with correlation
\rho .
Then

\operatorname { C o v } \left( \mathbb { 1 } _ { \{ U \leq x \} } , \mathbb { 1 } _ { \{ V \leq y \} } \right) = \Phi _ { 2 } ( x , y ; \rho ) - \Phi ( x ) \Phi ( y ) .

Using the decomposition in (15) we obtain

\operatorname { C o v } ( r _ { x } ( U ) , r _ { y } ( V ) ) = \Phi _ { 2 } ( x , y ; \rho ) - \Phi ( x ) \Phi ( y ) - \rho \thinspace \phi ( x ) \phi ( y ) .

Moreover,

\left. \frac { \partial } { \partial \rho } \Phi _ { 2 } ( x , y ; \rho ) \right| _ { \rho = 0 } = \phi ( x ) \phi ( y ) .

Thus the first-order term in
\rho
cancels, and for
| \rho |
small,
\operatorname { C o v } ( r _ { x } ( U ) , r _ { y } ( V ) ) = \mathcal { O } ( \rho ^ { 2 } )
. For fGn in the long-memory regime,

\rho _ { X } ( k ) \sim C _ { X } | k | ^ { 2 H - 2 } \quad \mathrm { ~ a n d ~ } \quad \rho _ { Y } ( k ) \sim C _ { Y } | k | ^ { 2 H - 2 } , \qquad | k | \to \infty .

Hence

\operatorname { C o v } ( r _ { x } ( X _ { 0 } ) , r _ { y } ( X _ { k } ) ) = \mathcal { O } \left( | k | ^ { 4 H - 4 } \right) ,

and analogously for the Y -sample. Consequently,

\operatorname { V a r } \left( n ^ { - H } \sum _ { i = 1 } ^ { n } r _ { x } ( X _ { i } ) \right) \leq C n ^ { - 2 H } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | \rho _ { X } ( i - j ) | ^ { 2 } .

The right-hand side converges to zero. More precisely,

\left\| n ^ { - H } \sum _ { i = 1 } ^ { n } r _ { x } ( X _ { i } ) \right\| _ { L ^ { 2 } } =  \begin{cases} { \displaystyle \mathcal { O } \left( n ^ { 1 / 2 - H } \right) , } & { 1 / 2 < H < 3 / 4 , } \\ { \displaystyle \mathcal { O } \left( n ^ { - 1 / 4 } \sqrt { \operatorname { l o g } n } \right) , } & { H = 3 / 4 , } \\ { \displaystyle \mathcal { O } \left( n ^ { H - 1 } \right) , } & { 3 / 4 < H < 1 . } \\ \end{cases}

The same estimates hold for the Y -sample, with m in place of
n .
Using the monotonicity of the empirical distribution functions, together with standard discretization and Gaussian tail bounds, the previous pointwise bounds extend to the supremum over
x \in \mathbb { R }
. Therefore,

\operatorname* { s u p } _ { x \in \mathbb { R } } \left| n ^ { - H } \sum _ { i = 1 } ^ { n } r _ { x } ( X _ { i } ) \right| \to 0 \quad \text { and } \quad \operatorname* { s u p } _ { x \in \mathbb { R } } \left| m ^ { - H } \sum _ { j = 1 } ^ { m } r _ { x } ( Y _ { j } ) \right| \to 0 \qquad \text {in probability. }

It follows that, in
\begin{array} { r } { \ell ^ { \infty } ( \mathbb { R } ) ,   n ^ { 1 - H } \left( F _ { n } - \Phi \right) \Rightarrow - \phi ( \cdot ) Z _ { X } ,   \mathrm { a n d }   m ^ { 1 - H } \left( G _ { m } - \Phi \right) \Rightarrow - \phi ( \cdot ) Z _ { Y } . } \end{array}

35

<!-- page: 36 -->

## Page 36

Now set
\begin{array} { r } { c _ { n , m } : = \frac { n ^ { 1 - H } m ^ { 1 - H } } { n ^ { 1 - H } + m ^ { 1 - H } } } \end{array}
. Then

c _ { n , m } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) = c _ { n , m } n ^ { H - 1 } \left[ n ^ { 1 - H } \left( F _ { n } ( x ) - \Phi ( x ) \right) \right] - c _ { n , m } m ^ { H - 1 } \left[ m ^ { 1 - H } \left( G _ { m } ( x ) - \Phi ( x ) \right) \right] .

Since
n / m \rightarrow 1
, we have

c _ { n , m } n ^ { H - 1 } \to \frac { 1 } { 2 } , \qquad c _ { n , m } m ^ { H - 1 } \to \frac { 1 } { 2 } .

Therefore,

c _ { n , m } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) \Rightarrow - \phi ( x ) Z _ { 0 } ,

where
Z _ { 0 } = { \textstyle { \frac { 1 } { 2 } } } \left( Z _ { X } - Z _ { Y } \right)
. The random variable
Z _ { 0 }
is centered Gaussian with variance

\sigma _ { 0 } ^ { 2 } = \frac { 1 } { 4 } \left( \sigma _ { X } ^ { 2 } + \sigma _ { Y } ^ { 2 } - 2 \sigma _ { X Y } \right) .

Finally, by the continuous mapping theorem,

D _ { n , m } ^ { \diamond } = c _ { n , m } D _ { n , m } = \operatorname* { s u p } _ { x \in \mathbb { R } } \left| c _ { n , m } \left( F _ { n } ( x ) - G _ { m } ( x ) \right) \right| \Rightarrow \operatorname* { s u p } _ { x \in \mathbb { R } } \phi ( x ) | Z _ { 0 } | .

Since sup
\begin{array} { r } { \phi ( x ) = \phi ( 0 ) = \frac { 1 } { \sqrt { 2 \pi } } } \end{array}
, we obtain x∈R

D _ { n , m } ^ { \diamond } : = c _ { n , m } D _ { n , m } \Rightarrow \frac { 1 } { \sqrt { 2 \pi } } | Z _ { 0 } | .

This proves Proposition 2.3.

36
