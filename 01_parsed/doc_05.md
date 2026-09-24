# doc_05 股票因子分散的层次聚类 JPMorgan HRP

- source_path: `/Users/xiehaotong/Desktop/literature_pipeline/00_raw/期货日内因子_精选文献15篇/01_英文论文_微观结构与方法/05_股票因子分散的层次聚类(JPMorgan HRP).pdf`
- parser: `MinerU`
- mineru_version: `4.0.7`
- mineru_tier: `basic`
- ocr_mode: `auto`
- lang: en
- type: paper
- page_count: 57

<!-- page: 1 -->

## Page 1

J.P.Morgan

Global Quantitative & Derivatives Strategy 13 September 2018

## Diversification of Equity Factors

## Hierarchical Clustering for better risk allocation

Diversifying equity exposure when building quantitative factor models can be done in many ways – from a simple equal weighting, or with volatility adjustments, right through to a full mean-variance optimization (we test 10 different weighting schemes in all). No matter the scheme we show that they all seem to benefit by first incorporating the hierarchical cluster relationships between the factors.

Some of the more modern risk allocation techniques like Hierarchical Risk Parity (Lopez de Prado, 2016) and Hierarchical Cluster Parity (Raffinot, 2016) already have this cluster information built in and our tests confirm they tend to do better. But we find that the hierarchical relationship between factors can be included as a preprocessing step with any allocation scheme and it almost always improves the model performance (especially for the more naïve ones like equal weighting).

We can introduce this cluster information by applying the risk allocation scheme onto the hierarchical dendrogram at different distance thresholds (as shown below). First we test the scheme on the full set of 70 factors, and then as we increase the distance threshold the number of clusters will reduce and we can apply the allocation across the clusters instead. Doing so can remove collinear asset returns and redundant factors and in some scenarios greatly increase the risk adjusted returns (but only up to a point after which the reduced cluster number becomes too coarse to fully represent the exposures present in the original returns set).

## Big Data & AI Strategies (Asia Pac)

Robert Smith, PhD
AC (852) 2800 8569 robert.z.smith@jpmorgan.com
Bloomberg
JPMA RSMITH <GO> J.P. Morgan Securities (Asia Pacific) Limited

Berowne Hlavaty
(61-2) 9003-8602 berowne.d.hlavaty@jpmorgan.com J.P. Morgan Securities Australia Limited

Ada Lau
(852) 2800-7618 ada.lau@jpmorgan.com J.P. Morgan Securities (Asia Pacific) Limited/ J.P. Morgan Broking (Hong Kong) Limited

Evan Hu
(852) 2800-8508 evan.hu@jpmorgan.com J.P. Morgan Securities (Asia Pacific) Limited

## Global Head Quant & Derivative Strategy

Marko Kolanovic, PhD
(1-212) 272-1438 marko.kolanovic@jpmorgan.com J.P. Morgan Securities LLC

**[image_text]**

Increasing the cluster distance threshold on 70 long only equity factors (we see the cluster count go from 17 down to 2
Source: J.P. Morgan Quantitative and Derivatives Strategy (QDS)
See page 54 for analyst certification and important disclosures, including non-US analyst disclosures.
J.P. Morgan does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

www.jpmorganmarkets.com

<!-- page: 2 -->

## Page 2

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Table of Contents

Diversification of Factors .3
Static is really Dynamic 4
Our approach.. 5
Weighting schemes.
Equal Weight (EW) 6
Inverse Vol (IV). 6
Hierarchal Risk Parity (HRP)
Hierarchical Cluster Parity (HCP)
Cluster Risk Parity (CRP).
Minimum Variance (MVP)
Maximally Diversified Portfolio (MDP 8
Mean-Variance Optimization (MVO) .8
Equal Contribution to Risk (ECR) 8
Term Weighting (TW) .8
Assumptions.
Backtests 10
Equal weight. .12
Long Only. 14
Inverse Volatility .15
HCP and HRP . .17
Long Only with Hedges 19
Cluster weights using optimizations .22
Momentum Overlays .24
Best in Cluster . ..25
References .. .53
Appendix I: Full Backtesting Results ...30
MSCI GDM, Long Only, 60 months, Average .31
MSCI GEM, Long Only, 60 months, Average. ..32
MSCI GDM, Long Only + HEDGE, 60 months, Averag .33
MSCI GEM, Long Only + HEDGE, 60 months, Averag .34
MSCI GDM, Long-Short, 60 months, Average ..35
MSCI GEM, Long-Short, 60 months, Average. .36
Appendix II: Correlation Matrices ..37
Appendix III: Different Linkage methods ..39
Appendix IV: Iterative Step through ..44

2

<!-- page: 3 -->

## Page 3

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

We iteratively step through different distance cut-offs of a hierarchical dendrogram to test if there is an optimal cluster count to apply the risk allocation schemes.

We find that almost all risk allocation schemes can benefit from first clustering the single factors.

Our favoured approach is to use HCP with cluster weights adjusted for volatility.

## Diversification of Factors

In this report we investigate the effects of various risk allocation techniques on factors attempting to capture different Equity Risk Premia or Smart Beta. These include the typical more traditional approaches such as Equal Weight, Minimum Variance, and Risk Parity, as well as some more recent additions that incorporate the hierarchical clustering i.e. Hierarchical Risk Parity (HRP) and Hierarchical Cluster Parity (HCP).

The return sets are equity factors coming from the usual Equity Risk Premia families – in all we use 70 of our core factors, in long-only and long-short forms, plus some market hedges (either short the market or the short the beta of Value, Earnings, Momentum and Quality).

The main focus is how the different allocation schemes perform not just across all the single factors, but also across clusters formed at different hierarchical distance thresholds. We make a stepped scan of the hierarchical structure of the clusters with the allocation schemes applied to the clusters at every step (see the front cover diagram).

In general we note that as we reduce the asset count by allocating grouping more factors into clusters and THEN applying the risk allocation scheme, we get better risk/return profiles up to a point. The added benefit is a simplified portfolio construction as there are fewer assets to consider and manage.

Clustering is already embedded in the HRP and HCP approaches, but we show how it can also be added to any other weighting schemes as a preprocessing step to improve performance and it almost always does to some degree. We explore the pros and cons of the different approaches applied before and after clustering.

In both MSCI GEM and GDM we conclude that clustering before applying most risk allocation techniques can improve risk adjusted returns. We see it removes redundant exposures that can unfairly bias the allocation when applied across all the single assets. This is especially the case for some of the simpler allocation schemes like Equal Weight and Inverse Vol.

Our preferred approach is to use inverse vol but at the cluster level by taking into account hierarchical distance as well. We call this Cluster Risk Parity (CRP) and it is essentially the HCP approach but adjusted for cluster variance. HRP adjusts for variance but does not take into account cluster size or distance between clusters.

We also explore alternative ways to implement each clusters return i.e. not just the average of the returns across the cluster membership. For example we could choose the best performing factor in each cluster, or perhaps the most liquid or best Value spread. In general doing this also boosts performance.

Lastly we test an expected return momentum overlay on the cluster selection and see that it significantly improves risk adjusted returns. This can be done through Mean Variance Optimization, and we also test the Term Structure weighting scheme as described in our report
“Mitigating Equity Index Risk Using Term Structure of Price Momentum
”

3

<!-- page: 4 -->

## Page 4

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Static is really Dynamic

Allocating across equity factors to extract risk premia is a key part of quantitative investing in equities. Static weighting is often proposed as a simpler and diversified approach however it does not take into account concentrations of exposures can build up as some factors ‘change their spots’ through time.

Probably the most effected factors are those in the momentum family. At some points in the cycle they are more like high beta factors (such as Value) and at other points more like low beta factors (like Quality).

Ironically, an equal weight to Momentum, Quality and Value in fact will give us a dynamic loading between Quality and Value depending on the market cycle.

Pairwise correlations between factors can vary greatly through time.

Price Momentum is probably one of the worst affected because of its dynamic (trending) nature. Not only that but it’s a popular factor simply due to its potency.

Figure 1: Pairwise correlations between 12-month Price Momentum and Beta through time
Source: MSCI, Factset, J.P. Morgan QDS
We would like to dynamically adjust both traditional and modern weighting schemes to allow for these correlation changes.

Figure 2: Pairwise correlations between ROE and Beta through time
Source: MSCI, Factset, J.P. Morgan QDS

In this report we take a look at the pairwise correlation between 70 or so quantitative equity factors in MSCI GDM and MSCI GEM. We use a hierarchical clustering approach to explore ways to make risk allocation and diversification across these factors more robust.

4

<!-- page: 5 -->

## Page 5

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Instead of allocating to each and every single asset (~70 in this example) we allocate to the clusters at a certain distance threshold (7 in this example).

The cluster returns can be implemented through a simple average or for better performance and easier implementation a single asset selection strategy within each cluster could also be used (i.e. performance, volatility, liquidity or value driven).

## Our approach

We will take a look at ten different weighting schemes and demonstrate how in general they can all be improved by first finding the hierarchical clusters, and then weighting the clusters. The approach is fairly robust to the parameters used in the pair-wise correlations or the clustering technique.

The clusters can be formed aggressively or mildly by changing the threshold for dendrogram cutoff and we will explore the sensitivity of the results to this parameter in particular.

**[image_text]**

Figure 3: Example hierarchical cluster and correlation matrix(70 assets reduced to 7 clusters)
1.6 1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0

Source: J.P. Morgan QDS

Our main measure of the success of the technique is risk-adjusted returns. But the approach also benefits from:

Better handles collinearity as it removes the effects of redundant assets that are effectively the same as others. This can also help remove pre-selection bias for a universe of assets in more naïve weighting schemes;

Includes more information about the hierarchical structure which can be used to make more informed asset substitution decisions;

 Flexible in implementation so we can get performance boosts on asset selection within each cluster;

Can make implementation simpler (less assets to manage); and

 Fewer assets make any optimization process much faster to run.

5

<!-- page: 6 -->

## Page 6

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Weighting schemes

The goal of risk-based allocations lies in the concept of diversification: Since we do not have an idea of expected returns, we would rather focus our attention to either minimize and/or diversify risk. As highlighted in Jean-Charles et al (2015), one can define different measures of diversification, and each measure could lead to a particular risk-based portfolios. For instance, an equal-weighted portfolio diversifies in terms of asset weights; a portfolio built to have equal risk contributions diversifies in terms of risk budgets, etc.

These are the different weighting schemes we tested both on the individual factors as wells as the cluster groups. None of them require any forward return estimation except for the Mean Variance optimization and the Term Weighting approach.

## Equal Weight (EW)

All assets have the same weighting which is 1 / N (number of assets). This is the simplest allocation but a useful benchmark no less.

## Inverse Vol (IV)

This strategy allocates weights inversely proportional to asset volatility (we use the variance). It is a “naïve” form of risk parity which does not take into account correlations. This aligns with the approach used in Hierarchical Risk Parity by Lopez de Prado (2016).

## Hierarchal Risk Parity (HRP)

Lopez de Prado (2016) introduced a new and interesting idea of allocation called Hierarchical Risk Parity. It is termed “Hierarchical” because it makes use of the hierarchical clustering algorithm to assign assets into similar groups, and then apply the (naïve) Risk Parity allocations recursively across asset groups. As such, HRP also considers correlations among assets instead of simply looking at asset volatilities. Actually, rather than trying to improve upon the naïve Risk Parity approach, Lopez de Prado (2016) comes up with the idea of HRP so as to improve upon the Minimum Variance strategy.

The rationale behind HRP is to avoid the instability and concentration in Minimum Variance (MV) portfolios that rely on the inversion of covariance matrix, which is problematic when there are highly correlated assets that render the covariance matrix close to singular.

The rationale behind HRP is to avoid the instability and concentration in Minimum Variance (MVP) portfolios that rely on the inversion of covariance matrix, which is problematic when the matrix is close to singular – this happens when there are highly correlated assets. Furthermore, estimations of full covariance matrices could be noisy or spurious, especially when the number of assets is large and the number of observations is relatively small6. HRP comes as a solution to get around the above issues by allocating to clusters of similar assets. For a full overview of the algorithm please refer to our report
“Hierarchical Risk Parity: Enhancing Returns at Target Volatility”
.

6

<!-- page: 7 -->

## Page 7

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

In the dendrogram are five assets and three clusters. The first cluster is made up of assets 1 and 2, asset 3 constitutes the second cluster and the third cluster consists of assets 4 and 5. Based on the hierarchical clustering, making a split at vertical distance measure of 1.5 (say), the weights for cluster number one is 0.5 (simply a 1/2 = 0.5) and weights for clusters 2 and 3 are 0.25 (0.5/2 = 0.25) each. Since there are two assets in the cluster number one, the final weights for assets 1 and 2 are 25%. Asset 3 has been assigned a weight of 25% while, assets 4 and 5 would get a weight of 0.25 divided equally between them (12.5%).

## Hierarchical Cluster Parity (HCP)

Another method to create a diversified weighting is to distribute the capital across each cluster hierarchy such that many correlated assets receive the same total allocation as a single uncorrelated one. This idea was recently published by Thomas Raffinot in his paper
"Hierarchical Clustering based Asset Allocation"

Figure 4: Hierarchical Clustering Parity (HCP) example
Source: J.P. Morgan QDS, Thomas Raffinot "Hierarchical Clustering based Asset Allocation"

In his paper, Raffinot highlights that complex systems, such as financial markets, have a structure and are usually organized in a hierarchical manner, with separate and separable sub-structures (Simon 1962). The hierarchical structure of interactions among elements strongly affects the dynamics of complex systems.

Raffinot (and Lopez de Prado) notes that correlation matrices lack the notion of hierarchy, which allows weights to vary freely in unintended ways. A correlation matrix makes no difference between assets yet, some assets seem closer substitutes of one another, while others seem complementary to one another.

## Cluster Risk Parity (CRP)

This is our preferred approach, in which the cluster weight is determined by the cluster distances AND the variance of the averaged asset returns inside each cluster. This hybrid approach then accounts for cluster size, distance between clusters AND is volatility adjusted.

## Minimum Variance (MVP)

Minimum Variance portfolios have a very simple objective, which is to minimize the expected portfolio variance. Such portfolios have been documented to have high out-of-sample returns, especially in equities (Clarke et al 2011). Together with the low volatility (provided that one does not leverage), Minimum Variance portfolios tend to have high information ratios. However, if we look at a very large universe (e.g. hundreds of stocks), the performance of Minimum Variance usually deteriorates. This is largely due to two issues in Minimum Variance portfolios

7

<!-- page: 8 -->

## Page 8

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Sensitivity to inputs: To obtain the optimal weights in an MV portfolio, one has to invert the covariance matrix. Such inversion makes it very sensitive to the noises in the covariance estimates, especially when there are highly correlated assets that render the covariance matrix close to singular.

Concentrated positions: MV tends to assign concentrated weights to only a few assets, and as such, even within a large universe, the actual uncorrelated number of exposures is low. Concentrated portfolios tend to be more prone to sudden drawdowns and have higher realized volatilities.

## Maximally Diversified Portfolio (MDP)

Maximum Diversification (MD): Maximize the diversification ratio (Choueifaty and Coignard 2008), defined as the ratio of weighted volatility to portfolio volatility. An interesting property of the Maximum Diversification portfolio is that all assets have the same positive correlation with the portfolio. This is intuitive, because if one asset has a higher correlation with the portfolio, that asset is deemed to be “overrepresented”. We will then increase the diversification ratio by decreasing the weight of that asset, hence its correlation with the portfolio will decrease – see Choueifaty et al (2011) which provides more insightful analysis on the properties of this Most Diversified portfolio.

## Mean-Variance Optimization (MVO)

The Markowitz's Mean-Variance Optimization (MVO) also requires expected returns so it is not quite the same as the pure risk allocation methods but we wanted to examine it regardless. Mean-Variance analysis trades off risk against expected return and we aimed to maximize the Sharpe ratio in the portfolio.

## Equal Contribution to Risk (ECR)

This strategy assigns weights so that all assets have the same contribution to total portfolio risk (Maillard et al 2010). If Total Risk Contribution (TRC) is the proportion of risk of an asset contributed to the final portfolio volatility, then a strategy with Equal Risk Contribution means that risk budgets (i.e. TRC) are equal for all assets.

## Term Weighting (TW)

This is a momentum overlay using the differing look back periods for momentum. The term weightings we use are 25% allocation per 4 different lookback periods – 1, 3, 6 and 12 months. The way it works is that if all 4 lookback periods have positive returns, then the weight is 100%. If no lookback period had a positive return then the allocation weight to that asset is 0%. Partial allocations of 25%, 50% and 75% are then possible too.

Please see our report
“Mitigating Equity Index Risk Using Term Structure of Price Momentum
” for a full overview of this approach.

8

<!-- page: 9 -->

## Page 9

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Assumptions

We tested various parameters for the pairwise correlations and clustering process.

## Look back period

We tested 12, 36 and 60 month look back periods for the pairwise correlations. The longer periods were naturally more stable and tended to have better risk-adjusted returns.

## Distance metric

We always transformed the correlation matrix into distances before clustering using the following:

d _ { i , j } = \sqrt { ( 1 - \rho _ { i , j } ) / 2 }

## Correlation type

Pearson correlations are the most popular and this is what we used.

All our clustering was done using Python’s Sci-Kit Learn package.

## Cluster linkages

We are only looking at Hierarchical Agglomerative Clustering (HCA) methods (see our report
“Dynamic Cluster Neutralisation in Global Equity Markets
”) so that we can scan the dendrogram and examine clusters at different thresholds. This is a "bottom up" approach: each observation starts in its own cluster and pairs of clusters are merged as we move up the hierarchy.

Cluster linkage methods for the HAC tested were:

Single (minimum distance between members of the clusters) – a drawback of this method is that it tends to produce long thin clusters in which nearby elements of the same cluster have small distances. Clusters do not merge readily at lower distance thresholds.

Complete (maximum distance) – looking for the largest difference between all members of joined clusters.

 Average (unweighted pair group simple average distance across all members) – typically we had the best results with this method.

Ward (finds the next pair of clusters to merge that leads to minimum increase in total within-cluster variance after merging) – this techniques produces clusters with small distances between them nearer the leaves, but large distances further up the branches. Equal step sizes up the hierarchy tend to reduce the cluster numbers too quickly.

See Appendix III for examples of their structures.

## Cluster Returns

To start we simply average the returns of all factors in each cluster. Later in this report we demonstrate the effects of using other criteria to form the returns – see the section ‘Best in Cluster’.

9

<!-- page: 10 -->

## Page 10

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

The test period runs monthly from January 2000 to May 2018.

## Backtests

Our test assets are equity factors representing various equity risk premia. We look at MSCI GDM and MSCI GEM separately. Below are performances of the last ~20 years of a sample selection from the full suite of 67 factors we tracked.

Figure 5: MSCI GDM, Long Only Factor performance – the market beta effect can be clear see on each factor
The pairwise correlations of these LO factors look like this – with hierarchical clustering shown on the side.
Note these are Long Only and so have a significant market beta exposure. Hence the correlations are broadly 75% or more.

**[image_text]**

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (Clusters on 36 months correlations, Average method)

10

<!-- page: 11 -->

## Page 11

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

We also want to look at the long-short space which is commonly used with equity factors – see the chart below.

Figure 6: MSCI GDM, Long Short Factor performance – we have neutralized the market beta somewhat by being long-short
The pairwise correlations of these LS factors look like this – with hierarchical clustering shown on the side.
Note how with the Long-Short factors the distance between clusters is on average 3x that of the Long-Only.
Much more diversification is possible when available asset return correlations are negative.

**[image_text]**

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (Clusters on 36 months correlations, Average method)

A final test we run will be again looking at the Long-Only factors but with some smart beta hedges. This will help demonstrate the benefits of the approach even more in a scenario where some correlations are negative.

11

<!-- page: 12 -->

## Page 12

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Equal weight

If we were to equal weight the risk premia shown above, it would look something like this below. Of course this is probably the simplest and most naïve approach and it is prone to survivorship bias as we have pre-selected these factors over many years of working with them, but it serves as a handy benchmark.

Figure 7: Equal weight exposure to all Long Only factors, MSCI GDM
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

If we cluster the factors before applying the weighting, then we can allocate the equal weighting to each cluster. We can run the sensitivities to the cluster distances by gradually increasing the distance threshold as shown below.

**[image_text]**

Figure 8: Correlation clusters on the 67 Long Only factors in MSCI GDM – increasing the distance threshold: starting in this example from 17 clusters down to just 2 clusters on the right.
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (Clusters on 60 months correlations, Average method)

12

<!-- page: 13 -->

## Page 13

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

A subtle effect occurs as we increase the distance thresholds: collinear factor returns are averaged which effectively removes them from the returns set. This allows more even weight to be given to the actual factor exposures present and not just across whatever factor selection happens to be thrown into the pot. This works up until a point of course, after which the number of clusters are too few to capture the set of factor representations present in the returns.

Figure 9: Risk Adjusted returns when using EW on the cluster (distance threshold increases from 0.0 (67 clusters with 1 factor per cluster) to 1.0 (just 1 cluster that contains all 67 factors)

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>EW</td><td>AVG</td><td>0</td><td>67.0</td><td>0.57</td><td>9.7%</td><td>17.0%</td><td>(82.3%)</td><td>63.0%</td><td>2.10</td></tr><tr><td>EW</td><td>AVG</td><td>0.1</td><td>59.6</td><td>0.57</td><td>9.6%</td><td>16.8%</td><td>(81.9%)</td><td>61.7%</td><td>2.11</td></tr><tr><td>EW</td><td>AVG</td><td>0.2</td><td>30.0</td><td>0.59</td><td>9.7%</td><td>16.4%</td><td>(80.7%)</td><td>62.3%</td><td>2.18</td></tr><tr><td>EW</td><td>AVG</td><td>0.3</td><td>11.4</td><td>0.60</td><td>9.5%</td><td>15.9%</td><td>(79.1%)</td><td>62.3%</td><td>2.20</td></tr><tr><td>EW</td><td>AVG</td><td>0.4</td><td>5.7</td><td>0.60</td><td>9.2%</td><td>15.4%</td><td>(75.0%)</td><td>63.0%</td><td>2.21</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td><td>3.4</td><td>0.62</td><td>9.7%</td><td>15.6%</td><td>(75.7%)</td><td>63.0%</td><td>2.30</td></tr><tr><td>EW</td><td>AVG</td><td>0.6</td><td>2.3</td><td>0.61</td><td>9.8%</td><td>16.1%</td><td>(78.8%)</td><td>62.3%</td><td>2.25</td></tr><tr><td>EW</td><td>AVG</td><td>0.7</td><td>1.9</td><td>0.59</td><td>9.6%</td><td>16.4%</td><td>(81.7%)</td><td>61.1%</td><td>2.16</td></tr><tr><td>EW</td><td>AVG</td><td>0.8</td><td>1.3</td><td>0.57</td><td>9.5%</td><td>16.8%</td><td>(82.1%)</td><td>61.7%</td><td>2.09</td></tr><tr><td>EW</td><td>AVG</td><td>0.9</td><td>1.2</td><td>0.56</td><td>9.6%</td><td>17.0%</td><td>(82.3%)</td><td>61.7%</td><td>2.08</td></tr><tr><td>EW</td><td>AVG</td><td>1.1</td><td>1.0</td><td>0.57</td><td>9.7%</td><td>17.0%</td><td>(82.3%)</td><td>63.0%</td><td>2.10</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

The real benefit is that we can use this approach across all the many and varied risk allocation schemes from Equal Weight to Mean Variance Portfolios – as we show in the next section.

13

<!-- page: 14 -->

## Page 14

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Long Only

We next test all the LO factors, under all the different weighting schemes, and then introduce different cluster distances on the weighting schemes to show the improvements. The distance is increased for each step giving us fewer clusters with larger memberships.

Figure 10: Risk adjusted returns of Long-Only factors under different weighting schemes (no clustering), MSCI GDM

CRP Cluster Risk Parity ERC Equal Contribution to Risk EW Equal Weight HCP Hierarchical Cluster Parity HRP Hierarchical Risk Parity IV Inverse Volatility

CRP does the best because it takes into account both the volatility and the hierarchy. HRP does this too but does not consider the cluster sizes or distances between them.

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (67 factors in each test)
Figure 11: Risk adjusted returns of Long-Only factors under different weighting schemes (now with clustering), MSCI GDM – in every case clustering helps up until a point
The benefit is clear: clustering before weighting helps every scheme (up to a point) even when these are highly correlated return sets.
The benefits are even more apparent when the correlations are lower or negative as we will see in the next sections.

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix (0.0 to 1.1 distance thresholds with 1 factor to 67 factor member counts respectively)

14

<!-- page: 15 -->

## Page 15

14 0.6 0.5 0.4 0.3 0.2 0.1 0.0

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Inverse Volatility

The hedges are much further away in distance and so will remain in their distinct cluster for longer. This allows even the more naïve weighting algorithms (such as Inverse Volatility) to better access their hedging properties after clustering.

We can add some hedges to better demonstrate the effects of clustering on the weighting schemes.

In this section we use GEM long only factors with some smart-beta hedges (with negative correlations). We cluster the factors before applying the inverse volatility weighting and test the performance gained by gradually increasing the distance threshold.

**[image_text]**

Figure 12: Correlation matrix and dendrogram for GEM long onlyfactors

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

15

<!-- page: 16 -->

## Page 16

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Clearly the performance improves if we use the clusters instead of the single factors as shown in the performance charts.

Figure 13: Risk adjusted and cumulative returns using the Inverse Volatility weighted exposure to various clusters combinations in MSCI GEM

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

The benefit of using IV weighted clusters improves as the Hedge cluster becomes more dominant (i.e. when the cluster count comes down and only up to a point). We are introducing the cluster information explicitly into the IV weighting. Compare this with HCP and HRP in the next section which have the cluster structure built into their weighting schemes and so do better at the outset before any clustering.

16

<!-- page: 17 -->

## Page 17

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

HCP has the highest weight of 50% to cluster 4 because it is furthest away from the other LO factors, with only one branch split to the top. The other branch shares 50% between clusters 1, 2 and 3 according to the number of branch splits (12.5%, 12.5% and 25% respectively).

HRP uses recursive bisection to allocate weights according to the cluster volatility. The four clusters are firstly split 1 & 2 vs 3 & 4. Because 3 & 4 includes the Hedge cluster its combined volatility will be very small giving it the bigger weight. Then each component cluster is allocated a volatility adjusted weight and because cluster 3 has less standard deviation than cluster 4 it will have a higher weight. Similarly clusters 1 and 2 divide their share and cluster 1 has lower vol and so a higher weight than cluster 2.

## HCP and HRP

This time we apply the HCP and HRP to the GEM long only factors with hedges. These two techniques are special as they directly involve the cluster hierarchy in the weighting scheme. What we observe is they start already strong and don't benefit as much by subsequent clustering – although there is still an improvement.

**[image_text]**

Figure 14: HRP and HCP weighting example

**[table]**

<table><tbody><tr><td>Cluster</td><td>Count</td><td>EW</td><td>HCP</td><td>HRP</td><td>Std Dev</td></tr><tr><td>1</td><td>11</td><td>25%</td><td>12.5%</td><td>3.8%</td><td>3.7%</td></tr><tr><td>2</td><td>6</td><td>25%</td><td>12.5%</td><td>2.5%</td><td>3.9%</td></tr><tr><td>3</td><td>49</td><td>25%</td><td>25%</td><td>56.7%</td><td>4.7%</td></tr><tr><td>4</td><td>4</td><td>25%</td><td>50%</td><td>37.0%</td><td>5.0%</td></tr></tbody></table>
Source: J.P. Morgan, MSCI, Factset, Bloomberg

17

<!-- page: 18 -->

## Page 18

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Figure 15: HCP and HRP weighted exposure to various cluster formations in MSCI GEM

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

In summary, HCP and HRP have the cluster structure built into their weighting schemes which puts them in a better position right away to exploit the pairwise distances between the LO factors and the hedges (due to the negative correlations). However they also still benefit from factor grouping via increased clusters sizes.

18

<!-- page: 19 -->

## Page 19

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

The correlations between the LO factors and Hedges are negative so the distance measure has them very far apart.

The correlations are extreme with the LO vs Hedges at near -1.0

## Long Only with Hedges

Again we take the GEM LO factors and with the smart beta hedges under different weighting schemes. The hedges are the short legs of the Momentum, Value, Quality and Earnings smart-beta composites.

Figure 16: Clustering LO factors with four smart-beta hedges

**[image_text]**

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (67 factors in each test); Correlations are on 60mnths, Average method clusters

19

<!-- page: 20 -->

## Page 20

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

The best result is with the CRP allocation scheme which is volatility adjusted HCP. It has the advantage of using both the hierarchical cluster distances AND adjusts for volatility.

CRP Cluster Risk Parity ERC Equal Contribution to Risk EW Equal Weight HCP Hierarchical Cluster Parity HRP Hierarchical Risk Parity IV Inverse Volatility

Cluster Risk Parity can use both the hierarchical distance AND the volatility.

HCP does not use any volatility adjustment.

Figure 17: Risk adjusted returns of Long-Only factors under different weighting schemes (no clustering) when there are available hedges, MSCI GEM

HRP does adjust for volatility, but the distance information is more coarsely applied using recursive bisection after ordering by distance between assets, and not directly on the clusters (i.e. it ignores cluster sizes).

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (67 factors in each test); Correlations are on 60mnths, Average method
Figure 18: Cumulative returns of Long-Only factors under different weighting schemes (no clustering) when there are available hedges, MSCI GEM
The CRP and HCP are able to allocate 50% to the Hedges because of how far they are from the LO returns. HRP can also to a lesser degree because the hedge distances are only applied through recursive bisection.

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS (67 factors in each test)

20

<!-- page: 21 -->

## Page 21

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

In every allocation scheme, forming clusters beforehand can improve the risk adjusted returns as shown in the chart below. Beyond a point however, the clusters become unable to adequately reflect the risk premia contained in the factors.

Figure 19: Risk adjusted returns of Long-Only factors and Four Hedges under different weighting schemes (now with clustering), MSCI GEM – in every case clustering helps

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td>70.0</td><td>1.79</td><td>5.2%</td><td>2.9%</td><td>(6.7%)</td><td>73.8%</td><td>6.54</td></tr><tr><td>CRP</td><td>AVG</td><td>0.25</td><td>21.7</td><td>1.51</td><td>4.8%</td><td>3.2%</td><td>(9.2%)</td><td>71.9%</td><td>5.54</td></tr><tr><td>CRP</td><td>AVG</td><td>0.4</td><td>5.5</td><td>1.70</td><td>5.3%</td><td>3.1%</td><td>(6.9%)</td><td>73.8%</td><td>6.23</td></tr><tr><td>CRP</td><td>AVG</td><td>0.5</td><td>3.2</td><td>1.75</td><td>5.3%</td><td>3.0%</td><td>(6.8%)</td><td>73.8%</td><td>6.42</td></tr><tr><td>ERC</td><td>AVG</td><td>0</td><td>70.0</td><td>0.61</td><td>14.1%</td><td>22.9%</td><td>(82.4%)</td><td>61.3%</td><td>2.25</td></tr><tr><td>ERC</td><td>AVG</td><td>0.25</td><td>21.7</td><td>0.63</td><td>13.7%</td><td>21.5%</td><td>(81.0%)</td><td>61.3%</td><td>2.33</td></tr><tr><td>ERC</td><td>AVG</td><td>0.4</td><td>5.5</td><td>0.63</td><td>13.3%</td><td>21.2%</td><td>(84.0%)</td><td>62.5%</td><td>2.30</td></tr><tr><td>ERC</td><td>AVG</td><td>0.5</td><td>3.2</td><td>0.99</td><td>17.0%</td><td>17.2%</td><td>(28.0%)</td><td>64.4%</td><td>3.62</td></tr><tr><td>EW</td><td>AVG</td><td>0</td><td>70.0</td><td>0.63</td><td>12.9%</td><td>20.6%</td><td>(73.1%)</td><td>61.3%</td><td>2.29</td></tr><tr><td>EW</td><td>AVG</td><td>0.25</td><td>21.7</td><td>0.66</td><td>12.3%</td><td>18.6%</td><td>(69.6%)</td><td>61.9%</td><td>2.42</td></tr><tr><td>EW</td><td>AVG</td><td>0.4</td><td>5.5</td><td>0.95</td><td>10.9%</td><td>11.5%</td><td>(31.3%)</td><td>63.8%</td><td>3.49</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td><td>3.2</td><td>1.44</td><td>9.3%</td><td>6.4%</td><td>(8.3%)</td><td>71.3%</td><td>5.29</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td><td>70.0</td><td>1.03</td><td>3.2%</td><td>3.1%</td><td>(9.9%)</td><td>69.4%</td><td>3.76</td></tr><tr><td>HCP</td><td>AVG</td><td>0.25</td><td>21.7</td><td>1.06</td><td>3.3%</td><td>3.1%</td><td>(9.7%)</td><td>67.5%</td><td>3.90</td></tr><tr><td>HCP</td><td>AVG</td><td>0.4</td><td>5.5</td><td>1.23</td><td>3.4%</td><td>2.8%</td><td>(6.5%)</td><td>73.1%</td><td>4.50</td></tr><tr><td>HCP</td><td>AVG</td><td>0.5</td><td>3.2</td><td>1.36</td><td>3.9%</td><td>2.9%</td><td>(7.1%)</td><td>70.6%</td><td>4.99</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td><td>70.0</td><td>0.86</td><td>10.4%</td><td>12.0%</td><td>(37.4%)</td><td>63.8%</td><td>3.16</td></tr><tr><td>HRP</td><td>AVG</td><td>0.25</td><td>21.7</td><td>0.81</td><td>9.0%</td><td>11.0%</td><td>(33.2%)</td><td>63.1%</td><td>2.97</td></tr><tr><td>HRP</td><td>AVG</td><td>0.4</td><td>5.5</td><td>1.48</td><td>7.0%</td><td>4.8%</td><td>(5.4%)</td><td>68.1%</td><td>5.42</td></tr><tr><td>HRP</td><td>AVG</td><td>0.5</td><td>3.2</td><td>1.81</td><td>5.6%</td><td>3.1%</td><td>(6.3%)</td><td>73.8%</td><td>6.61</td></tr><tr><td>IV</td><td>AVG</td><td>0</td><td>70.0</td><td>0.65</td><td>13.1%</td><td>20.1%</td><td>(71.4%)</td><td>61.3%</td><td>2.39</td></tr><tr><td>IV</td><td>AVG</td><td>0.25</td><td>21.7</td><td>0.68</td><td>12.5%</td><td>18.4%</td><td>(68.5%)</td><td>61.9%</td><td>2.49</td></tr><tr><td>IV</td><td>AVG</td><td>0.4</td><td>5.5</td><td>0.96</td><td>11.6%</td><td>12.1%</td><td>(29.8%)</td><td>64.4%</td><td>3.51</td></tr><tr><td>IV</td><td>AVG</td><td>0.5</td><td>3.2</td><td>1.36</td><td>10.3%</td><td>7.6%</td><td>(11.9%)</td><td>70.6%</td><td>4.99</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix (0.0 to 1.1 distance thresholds with 1 factor to 67 factor member counts respectively)

21

<!-- page: 22 -->

## Page 22

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Cluster weights using optimizations

We can also improve the performance of the usual optimized portfolios approaches by using clusters. We tested the following optimization schemes against Equal Weight (EW) again for comparison:

Equal Risk Contribution (ERC)

 Minimum Variance (MV),

 Mean Variance Optimization (MVO), and

Maximally Diversified Portfolio (MDP).

We only allowed positive weights in the optimizations and they must sum to one. Additionally we limited the single asset holdings to be a maximum of 3x the equal weight benchmark or else it has a tendency to allocate heavily into single assets.

**[table]**

Figure 20: MSCI GEM risk adjusted returns of Long-Only factors and Hedges under different weighting schemes
<table><tbody><tr><td></td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>ERC</td><td>0.61</td><td>14.1%</td><td>22.9%</td><td>(82.4%)</td><td>61.3%</td><td>2.25</td></tr><tr><td>EW</td><td>0.63</td><td>12.9%</td><td>20.6%</td><td>(73.1%)</td><td>61.3%</td><td>2.29</td></tr><tr><td>MDP</td><td>0.98</td><td>1.3%</td><td>1.3%</td><td>(3.4%)</td><td>60.0%</td><td>3.60</td></tr><tr><td>MVO</td><td>0.84</td><td>11.7%</td><td>14.0%</td><td>(52.4%)</td><td>65.0%</td><td>3.07</td></tr><tr><td>MVP</td><td>0.73</td><td>11.8%</td><td>16.1%</td><td>(57.9%)</td><td>62.5%</td><td>2.68</td></tr></tbody></table>

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

22

<!-- page: 23 -->

## Page 23

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Figure 21: MSCI GEM risk adjusted returns of Long-Only factors + HEDGEs under different weighting schemes AND distance thresholds – pre-clustering helps traditional optimization
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

Figure 22: MSCI GDM risk adjusted returns of Long-Only factors (NO Hedge) under different weighting schemes AND distance thresholds – pre-clustering again can help
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

23

<!-- page: 24 -->

## Page 24

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Another more direct way to look at the effects of Momentum is to use what we call a Term Weighted (TW) approach, using the momentum of different lookback periods.

Term weighting uses a 25% allocation on 4 different lookback periods – 1, 3, 6 and 12 months. If all 4 lookback periods have positive returns, then the weight is 100%.

We also apply the TW to HCP and CRP for a momentum overlay on both.

See our full report on TW:
“Mitigating Equity Index Risk Using Term Structure of Price Momentum
”

## Momentum Overlays

Next we investigate the use of a returns estimate (in addition to the volatility and correlations estimate). We already included the Mean-Variance Optimization (MVO) in optimizations comparison previously and it tended to do better as in some ways it is using factor momentum in its allocations.

Figure 23: Optimization first with no clustering, then using different cluster distances thresholds (MSCI GDM Long Only)

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

24

<!-- page: 25 -->

## Page 25

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Best in Cluster

Lastly we look at how alternative implementation of the cluster exposure can affect the strategy returns. So far we have been only using the simple average return of all assets in each cluster. However we could choose to implement the cluster by selecting the asset or factor with the best:

 12-month risk adjusted return (Sharpe)

 Prior 1 month return

 Prior year (12 month) return

 Most Volume/Liquidity

 Cheapest Value spreads (in the case of factors)

 Market cap (if applicable)

Figure 24: GDM, Equal Weighted LO with cluster average (AVG) vs 12mth ‘Best in Cluster’ (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Average linkage on 60 month distance matrix

Figure 25: GEM, Inverse Vol Weighted LO factors with cluster average (AVG) vs 12mth (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Average linkage on 60 month distance matrix

25

<!-- page: 26 -->

## Page 26

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Figure 26: GDM, LO factors with returns as the cluster average (AVG) vs 1m Best in Cluster (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Average linkage on 60 month distance matrix

Figure 27: GEM, LO factors with returns as the cluster average (AVG) vs 1m Best in Cluster (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Average linkage on 60 month distance matrix

26

<!-- page: 27 -->

## Page 27

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Figure 28: GEM, LO + HEDGE cluster average (AVG) vs 1 month Best in Cluster (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan; Average linkage on 60 month distance matrix; BIC is the best past 1 month return

Figure 29: GDM, Long Short cluster average (AVG) vs 1 month Best in Cluster (BIC)
Source: MSCI, Bloomberg, Factset, J.P. Morgan; Average linkage on 60 month distance matrix; BIC is the best past 1 month return

27

<!-- page: 28 -->

## Page 28

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

**[image_text]**

Blue factors are the current months selection and red are the prior month (if there is no red factor in a cluster then the selection did not change month on month).
Figure 30: GDM, LO 1 month Best in Cluster (BIC) at different example thresholds

Source: MSCI, Bloomberg, Factset, J.P. Morgan; Average linkage on 60 month distance matrix; BIC is the best past 1 month return

28

<!-- page: 29 -->

## Page 29

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Figure 31: GEM, LO 1 month Best in Cluster (BIC) at different example thresholds

Source: MSCI, Bloomberg, Factset, J.P. Morgan; Average linkage on 60 month distance matrix; BIC is the best past 1 month return

29

<!-- page: 30 -->

## Page 30

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Appendix I: Full Backtesting Results

In this appendix we have all the results for the following backtests:

 MSCI GEM equity factors

 MSCI GDM equity factors

 Long Only

 Long + HEDGE

 Long Short

 60 month pairwise correlations

 Average method for cluster dendrogram

 Allocation methods

 Cluster Risk Parity (CRP)

 Equal Weight (EW)

 Hierarchal Cluster Parity (HCP)

 Hierarchal Risk Parity (HRP)

 Inverse Vol (IV)

 Maximally Diversified Portfolio (MDP)

 Mean Variance Optimized (MVO)

 Minimum Variance Portfolio (MVP)

 Term Weighted (TW)

We step the cluster cut-off thresholds from 0.0 (all assets) up to a point where there is just a single cluster (this threshold varies depending on the parameters used).

Cluster returns are formed by average the returns of all the single assets inside each cluster.

30

<!-- page: 31 -->

## Page 31

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GDM, Long Only, 60 months, Average

**[table]**

<table><tbody><tr><td>Wght</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="27" colspan="7">67 0.67 9.3% 13.9% (68.7%) 63.6% 2.473.4 0.67 9.8% 14.7% (70.7%) 61.7% 2.461.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0967.0 0.57 9.7% 17.0% (82.3%) 63.0% 2.103.4 0.62 9.7% 15.6% (75.7%) 63.0% 2.301.0 0.57 9.7% 17.0% (82.3%) 62.3% 2.0967.0 0.63 9.5% 15.1% (73.0%) 62.3% 2.333.4 0.64 9.8% 15.2% (73.2%) 61.7% 2.371.0 0.57 9.7% 17.0% (82.3%) 62.3% 2.0967.0 0.60 9.7% 16.3% (79.8%) 61.7% 2.203.4 0.67 9.9% 14.7% (71.9%) 62.3% 2.481.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0967.0 0.59 9.7% 16.3% (79.9%) 62.3% 2.193.4 0.65 9.8% 15.0% (73.0%) 61.7% 2.401.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0967.0 0.60 9.6% 16.1% (81.1%) 59.9% 2.193.4 0.63 9.6% 15.2% (74.0%) 61.1% 2.331.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0967.0 0.64 9.8% 15.5% (76.9%) 64.2% 2.353.4 0.64 9.0% 14.0% (64.8%) 63.0% 2.371.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0967.0 0.65 10.0% 15.2% (75.3%) 63.0% 2.413.4 0.68 9.5% 14.0% (69.5%) 61.1% 2.521.0 0.57 9.6% 17.0% (82.3%) 62.3% 2.0867.0 0.84 12.1% 14.5% (46.3%) 63.7% 3.083.4 0.99 13.0% 13.1% (30.0%) 64.5% 3.651.0 0.88 12.5% 14.2% (32.6%) 63.7% 3.23</td></tr><tr><td>CRP</td><td>AVG</td><td>0.5</td></tr><tr><td>CRP</td><td>AVG</td><td>1</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td></tr><tr><td>EW</td><td>AVG</td><td>1</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>0.5</td></tr><tr><td>HCP</td><td>AVG</td><td>1</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>0.5</td></tr><tr><td>HRP</td><td>AVG</td><td>1</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>0.5</td></tr><tr><td>IV</td><td>AVG</td><td>1</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>0.5</td></tr><tr><td>MDP</td><td>AVG</td><td>1</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>0.5</td></tr><tr><td>MVO</td><td>AVG</td><td>1</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>0.5</td></tr><tr><td>MVP</td><td>AVG</td><td>1</td></tr><tr><td>TW</td><td>AVG</td><td>0</td></tr><tr><td>TW</td><td>AVG</td><td>0.5</td></tr><tr><td>TW</td><td>AVG</td><td>1</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

31

<!-- page: 32 -->

## Page 32

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GEM, Long Only, 60 months, Average

**[table]**

<table><tbody><tr><td>Wght</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="27" colspan="7">66.0 0.65 13.1% 20.3% (76.9%) 62.5% 2.372.2 0.65 14.5% 22.2% (83.0%) 61.3% 2.391.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.222.2 0.65 14.5% 22.4% (83.0%) 60.6% 2.371.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2366.0 0.64 13.4% 21.0% (78.7%) 61.3% 2.332.2 0.65 14.5% 22.4% (83.0%) 60.6% 2.381.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2366.0 0.62 14.1% 22.6% (81.6%) 61.3% 2.282.2 0.65 14.4% 22.2% (83.0%) 61.3% 2.391.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.62 14.1% 22.6% (81.6%) 61.3% 2.282.2 0.65 14.5% 22.2% (83.0%) 61.3% 2.391.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.63 13.3% 21.3% (76.8%) 61.3% 2.292.2 0.65 14.6% 22.3% (83.0%) 60.6% 2.401.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.71 15.6% 22.0% (82.1%) 62.5% 2.602.2 0.61 13.3% 21.9% (83.0%) 61.9% 2.241.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.67 14.3% 21.4% (77.5%) 63.1% 2.452.2 0.66 14.1% 21.3% (83.0%) 64.4% 2.421.0 0.61 14.1% 23.3% (83.1%) 61.3% 2.2266.0 0.77 16.6% 21.6% (61.1%) 61.9% 2.822.2 0.97 18.9% 19.5% (34.4%) 63.3% 3.561.0 0.90 18.2% 20.3% (37.8%) 63.7% 3.29</td></tr><tr><td>CRP</td><td>AVG</td><td>0.5</td></tr><tr><td>CRP</td><td>AVG</td><td>0.9</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td></tr><tr><td>EW</td><td>AVG</td><td>0.9</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>0.5</td></tr><tr><td>HCP</td><td>AVG</td><td>0.9</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>0.5</td></tr><tr><td>HRP</td><td>AVG</td><td>0.9</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>0.5</td></tr><tr><td>IV</td><td>AVG</td><td>0.9</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>0.5</td></tr><tr><td>MDP</td><td>AVG</td><td>0.9</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>0.5</td></tr><tr><td>MVO</td><td>AVG</td><td>0.9</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>0.5</td></tr><tr><td>MVP</td><td>AVG</td><td>0.9</td></tr><tr><td>TW</td><td>AVG</td><td>0</td></tr><tr><td>TW</td><td>AVG</td><td>0.5</td></tr><tr><td>TW</td><td>AVG</td><td>0.9</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

32

<!-- page: 33 -->

## Page 33

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GDM, Long Only + HEDGE, 60 months, Average

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="27" colspan="7">68.0 0.38 0.7% 1.9% (4.9%) 54.9% 1.394.4 0.35 0.8% 2.3% (8.1%) 54.9% 1.302.3 0.05 0.1% 2.1% (12.5%) 51.9% 0.1768.0 0.57 9.4% 16.6% (80.1%) 63.0% 2.104.4 0.66 5.4% 8.2% (38.3%) 61.7% 2.442.3 0.72 2.3% 3.2% (8.7%) 59.9% 2.6468.0 0.40 0.6% 1.5% (3.5%) 54.9% 1.464.4 0.44 0.7% 1.7% (3.8%) 54.3% 1.612.3 0.32 0.6% 1.9% (7.3%) 57.4% 1.1868.0 0.63 8.3% 13.2% (63.3%) 62.3% 2.324.4 0.74 2.0% 2.7% (6.6%) 58.6% 2.742.3 0.11 0.2% 2.1% (11.6%) 51.9% 0.4068.0 0.60 9.4% 15.6% (76.4%) 62.3% 2.204.4 0.78 5.4% 6.9% (28.2%) 61.1% 2.892.3 0.63 1.8% 2.8% (8.2%) 55.6% 2.3268.0 0.30 0.4% 1.2% (2.4%) 54.3% 1.124.4 0.36 0.6% 1.6% (4.0%) 54.3% 1.322.3 0.13 0.2% 1.6% (5.9%) 50.6% 0.4768.0 0.64 9.1% 14.1% (70.0%) 64.2% 2.374.4 0.79 3.0% 3.8% (15.8%) 63.6% 2.912.3 0.26 2.1% 8.0% (34.3%) 61.7% 0.9868.0 0.66 9.4% 14.3% (70.8%) 63.0% 2.424.4 0.73 1.8% 2.5% (5.1%) 57.4% 2.702.3 0.18 0.3% 1.6% (5.8%) 52.5% 0.6768.0 0.96 13.9% 14.5% (24.9%) 64.8% 3.534.4 0.95 11.3% 11.9% (19.6%) 62.3% 3.502.3 0.80 9.5% 11.9% (22.2%) 62.3% 2.95</td></tr><tr><td>CRP</td><td>AVG</td><td>0.5</td></tr><tr><td>CRP</td><td>AVG</td><td>0.8</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td></tr><tr><td>EW</td><td>AVG</td><td>0.8</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>0.5</td></tr><tr><td>HCP</td><td>AVG</td><td>0.8</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>0.5</td></tr><tr><td>HRP</td><td>AVG</td><td>0.8</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>0.5</td></tr><tr><td>IV</td><td>AVG</td><td>0.8</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>0.5</td></tr><tr><td>MDP</td><td>AVG</td><td>0.8</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>0.5</td></tr><tr><td>MVO</td><td>AVG</td><td>0.8</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>0.5</td></tr><tr><td>MVP</td><td>AVG</td><td>0.8</td></tr><tr><td>TW</td><td>AVG</td><td>0</td></tr><tr><td>TW</td><td>AVG</td><td>0.5</td></tr><tr><td>TW</td><td>AVG</td><td>0.8</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

33

<!-- page: 34 -->

## Page 34

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GEM, Long Only + HEDGE, 60 months, Average

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="24" colspan="7">70.0 1.79 5.2% 2.9% (6.7%) 73.8% 6.543.2 1.75 5.3% 3.0% (6.8%) 73.8% 6.421.4 0.61 8.2% 13.4% (44.8%) 67.5% 2.2570.0 0.63 12.9% 20.6% (73.1%) 61.3% 2.293.2 1.44 9.3% 6.4% (8.3%) 71.3% 5.291.4 0.62 8.2% 13.3% (44.2%) 66.9% 2.2670.0 1.03 3.2% 3.1% (9.9%) 69.4% 3.763.2 1.36 3.9% 2.9% (7.1%) 70.6% 4.991.4 0.62 8.2% 13.3% (44.2%) 66.9% 2.2670.0 0.86 10.4% 12.0% (37.4%) 63.8% 3.163.2 1.81 5.6% 3.1% (6.3%) 73.8% 6.611.4 0.61 8.2% 13.4% (44.8%) 67.5% 2.2570.0 0.65 13.1% 20.1% (71.4%) 61.3% 2.393.2 1.36 10.3% 7.6% (11.9%) 70.6% 4.991.4 0.61 8.2% 13.4% (44.8%) 67.5% 2.2570.0 0.98 1.3% 1.3% (3.4%) 60.0% 3.603.2 2.01 3.9% 1.9% (3.5%) 74.4% 7.351.4 0.62 8.2% 13.3% (44.5%) 67.5% 2.2670.0 0.84 11.7% 14.0% (52.4%) 65.0% 3.073.2 1.95 4.1% 2.1% (4.3%) 76.3% 7.151.4 0.62 8.3% 13.3% (44.6%) 69.4% 2.2770.0 0.73 11.8% 16.1% (57.9%) 62.5% 2.683.2 2.02 4.1% 2.0% (3.5%) 75.0% 7.381.4 0.62 8.2% 13.3% (44.5%) 67.5% 2.26</td></tr><tr><td>CRP</td><td>AVG</td><td>0.5</td></tr><tr><td>CRP</td><td>AVG</td><td>7</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>0.5</td></tr><tr><td>EW</td><td>AVG</td><td>7</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>0.5</td></tr><tr><td>HCP</td><td>AVG</td><td>7</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>0.5</td></tr><tr><td>HRP</td><td>AVG</td><td>7</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>0.5</td></tr><tr><td>IV</td><td>AVG</td><td>7</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>0.5</td></tr><tr><td>MDP</td><td>AVG</td><td>7</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>0.5</td></tr><tr><td>MVO</td><td>AVG</td><td>7</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>0.5</td></tr><tr><td>MVP</td><td>AVG</td><td>7</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

34

<!-- page: 35 -->

## Page 35

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GDM, Long-Short, 60 months, Average

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="27" colspan="7">67.0 0.10 0.2% 2.1% (9.8%) 53.7% 0.3516.7 0.33 0.6% 1.8% (7.5%) 56.8% 1.211.4 0.50 1.3% 2.5% (10.6%) 59.3% 1.8467.0 0.50 1.2% 2.5% (12.0%) 60.5% 1.8516.7 0.34 0.7% 2.1% (7.7%) 62.3% 1.251.4 0.49 1.2% 2.5% (11.4%) 61.1% 1.8167.0 0.12 0.3% 2.3% (10.2%) 58.0% 0.4516.7 0.40 0.8% 1.9% (6.0%) 54.9% 1.481.4 0.49 1.2% 2.5% (11.4%) 61.1% 1.8167.0 0.46 0.8% 1.8% (8.3%) 60.5% 1.7016.7 0.38 0.7% 1.8% (6.1%) 58.6% 1.411.4 0.50 1.3% 2.5% (10.6%) 59.3% 1.8467.0 0.51 1.1% 2.1% (8.8%) 61.1% 1.8616.7 0.35 0.7% 2.0% (6.6%) 60.5% 1.301.4 0.50 1.3% 2.5% (10.6%) 59.3% 1.8467.0 1.16 1.2% 1.0% (1.0%) 69.8% 4.2816.7 0.86 1.1% 1.3% (2.5%) 68.5% 3.161.4 0.50 1.2% 2.4% (10.0%) 59.9% 1.8667.0 1.24 1.5% 1.2% (2.3%) 69.1% 4.5616.7 0.62 1.1% 1.8% (4.3%) 64.8% 2.281.4 0.49 1.6% 3.3% (10.4%) 56.8% 1.8067.0 1.10 1.3% 1.2% (2.2%) 67.9% 4.0716.7 0.75 0.9% 1.2% (2.1%) 64.2% 2.761.4 0.50 1.2% 2.5% (10.0%) 59.9% 1.8667.0 0.81 3.1% 3.8% (6.1%) 64.8% 2.9816.7 0.69 1.9% 2.8% (4.5%) 59.9% 2.551.4 0.94 2.4% 2.5% (4.4%) 63.5% 3.46</td></tr><tr><td>CRP</td><td>AVG</td><td>1</td></tr><tr><td>CRP</td><td>AVG</td><td>3</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>1</td></tr><tr><td>EW</td><td>AVG</td><td>3</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>1</td></tr><tr><td>HCP</td><td>AVG</td><td>3</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>1</td></tr><tr><td>HRP</td><td>AVG</td><td>3</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>1</td></tr><tr><td>IV</td><td>AVG</td><td>3</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>1</td></tr><tr><td>MDP</td><td>AVG</td><td>3</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>1</td></tr><tr><td>MVO</td><td>AVG</td><td>3</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>1</td></tr><tr><td>MVP</td><td>AVG</td><td>3</td></tr><tr><td>TW</td><td>AVG</td><td>0</td></tr><tr><td>TW</td><td>AVG</td><td>1</td></tr><tr><td>TW</td><td>AVG</td><td>3</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

35

<!-- page: 36 -->

## Page 36

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

MSCI GEM, Long-Short, 60 months, Average

**[table]**

<table><tbody><tr><td>Weight</td><td>Return</td><td>Distance</td><td>AvgN</td><td>Sharpe</td><td>Ret</td><td>Vol</td><td>MDD</td><td>Hitrate</td><td>tStat</td></tr><tr><td>CRP</td><td>AVG</td><td>0</td><td rowspan="31" colspan="7">65.9 1.18 3.2% 2.7% (8.8%) 69.4% 4.333.2 1.93 4.1% 2.1% (3.1%) 72.5% 7.051.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 2.21 5.2% 2.3% (3.7%) 76.9% 8.093.2 2.04 4.6% 2.3% (4.4%) 74.4% 7.461.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 2.22 5.6% 2.5% (6.4%) 78.8% 8.123.2 1.80 4.6% 2.6% (7.0%) 73.1% 6.581.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 0.92 2.9% 3.2% (13.4%) 69.4% 3.373.2 1.78 4.3% 2.4% (3.7%) 72.5% 6.521.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 2.09 4.0% 1.9% (2.3%) 71.9% 7.653.2 1.84 4.0% 2.2% (3.5%) 71.3% 6.731.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 2.49 5.4% 2.2% (3.1%) 82.5% 9.143.2 1.85 4.0% 2.2% (4.1%) 73.1% 6.781.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 1.21 1.8% 1.5% (2.2%) 63.8% 4.453.2 2.16 4.5% 2.1% (4.4%) 75.0% 7.901.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 1.77 3.4% 1.9% (3.5%) 73.1% 6.483.2 1.99 4.2% 2.1% (6.0%) 75.6% 7.291.0 2.22 5.6% 2.5% (6.4%) 78.8% 8.1265.9 1.88 2.6% 1.4% (2.2%) 73.8% 6.883.2 2.13 4.2% 2.0% (3.6%) 74.4% 7.7965.9 2.25 7.9% 3.5% (3.8%) 78.1% 8.263.2 2.11 6.2% 2.9% (3.2%) 78.8% 7.721.0 2.30 5.7% 2.5% (4.9%) 79.1% 8.4465.9 1.52 5.4% 3.6% (4.2%) 74.4% 5.563.2 2.04 5.9% 2.9% (3.6%) 75.6% 7.46</td></tr><tr><td>CRP</td><td>AVG</td><td>1.5</td></tr><tr><td>CRP</td><td>AVG</td><td>3</td></tr><tr><td>ERC</td><td>AVG</td><td>0</td></tr><tr><td>ERC</td><td>AVG</td><td>1.5</td></tr><tr><td>ERC</td><td>AVG</td><td>3</td></tr><tr><td>EW</td><td>AVG</td><td>0</td></tr><tr><td>EW</td><td>AVG</td><td>1.5</td></tr><tr><td>EW</td><td>AVG</td><td>3</td></tr><tr><td>HCP</td><td>AVG</td><td>0</td></tr><tr><td>HCP</td><td>AVG</td><td>1.5</td></tr><tr><td>HCP</td><td>AVG</td><td>3</td></tr><tr><td>HRP</td><td>AVG</td><td>0</td></tr><tr><td>HRP</td><td>AVG</td><td>1.5</td></tr><tr><td>HRP</td><td>AVG</td><td>3</td></tr><tr><td>IV</td><td>AVG</td><td>0</td></tr><tr><td>IV</td><td>AVG</td><td>1.5</td></tr><tr><td>IV</td><td>AVG</td><td>3</td></tr><tr><td>MDP</td><td>AVG</td><td>0</td></tr><tr><td>MDP</td><td>AVG</td><td>1.5</td></tr><tr><td>MDP</td><td>AVG</td><td>3</td></tr><tr><td>MVO</td><td>AVG</td><td>0</td></tr><tr><td>MVO</td><td>AVG</td><td>1.5</td></tr><tr><td>MVO</td><td>AVG</td><td>3</td></tr><tr><td>MVP</td><td>AVG</td><td>0</td></tr><tr><td>MVP</td><td>AVG</td><td>1.5</td></tr><tr><td>TW</td><td>AVG</td><td>0</td></tr><tr><td>TW</td><td>AVG</td><td>1.5</td></tr><tr><td>TW</td><td>AVG</td><td>3</td></tr><tr><td>TW on HCP</td><td>AVG</td><td>0</td></tr><tr><td>TW on HCP</td><td>AVG</td><td>1.5</td></tr></tbody></table>
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

36

<!-- page: 37 -->

## Page 37

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

# Appendix II: Correlation Matrices

**[image_text]**

GDM Long Only, 60 months, average method

**[image_text]**

GEM Long Only, 60 months, average method

37

<!-- page: 38 -->

## Page 38

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

**[image_text]**

GDM Long Short, 60 months, average method

**[image_text]**

GEM Long Short, 60 months, average method
Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS; Cluster scheme: Average method on 60 month distance matrix

38

<!-- page: 39 -->

## Page 39

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

# Appendix III: Different Linkage methods

Universe: MSCI GDM long only factors (67)

We use a 60 month lookback for pairwise correlations and distance matrix.

Four different linkage methods on the above are shown in this order:

 Single

 Complete

 Average

 Ward

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

39

<!-- page: 40 -->

## Page 40

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

40

<!-- page: 41 -->

## Page 41

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Net Revisions to FY1 [Up-Down]/[Up+Down] Forward Earnings Momentum (1Mth Change) Net Revisions to FY2 [Up-Down]/[Up+Down] Composite Momentum Sentiment Composite Price Acceleration 6M Price Acceleration 3M 3 Mth Price Momentum Percent Off 52 Week High Interest Cover Historical Returns Volatility Over Last Year in LOCAL Currency Forward Earnings Momentum (3Mth Change) Composite Forward Earnings Momentum (1Mth + 3 Mth) Forward Earnings Momentum (3Mth Change) / Coefficient Of Variat Liquidity Composite Quality Asset Turnover (Historical) ALTMAN Z-score Q-Score Composite Composite Value Momentum Quality Price Model PIOTROSKI F-score (Fundamental Scorecard) Change In ROE Between Current and 12 Mths Prior Consensus Recommendation Historical Sales Growth Asset Turnover Growth (Historical) Internal Growth Historical Return On Equity Composite Recommendation 3 Mth Change in Consensus Recommendation 1 Mth Change in Consensus Recommendation Composite Price with 1 Month Reversion 12 Mth Price Momentum 12 Month Price Momentum adjusted for volatility (sharpe style) 6M change in Target Price 6 Mth Price Momentum Composite Price Historical BETA RSI 30 Days (Reversion) 1 Mth Price Reversion 1 year forward forecast PE Relative To History Historical Dividend Yield Number of Consensus Estimates (FY1) Gearing Free Cash Flow to Enterprise Value (Historical) Value To Growth RSI 10 Days (Reversion) Payout Ratio Forecast Earnings Growth FY1 to FY2 EBIT Margin Growth 5 years Historical Earnings Growth Composite Value Momentum Mode Composite Value Growth Momentum Model Composite Value Momentum Quality Price Model (Value Biased) 1 year forward forecast PE Relative To Sector 1 year forward forecast PE Composite Value and Growth Historical Earnings Yield Value To Risk Historical P/Sales Ratio EBITDA to Enterprise Value Historical P/Cash Earnings Ratio Cash Flow Yield Mean of FY1 and FY2 Cash Flow Yield FY2 Cash Flow Yield FY1

41

<!-- page: 42 -->

## Page 42

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

42

<!-- page: 43 -->

## Page 43

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

43

<!-- page: 44 -->

## Page 44

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Appendix IV: Iterative Step through

MSCI GEM long only factors (66)

We use a 60 month lookback for pairwise correlations.

We use the AVERAGE linkage method.

We show the one month 'Best in Cluster' as of 31 May 2018 in blue (and the month before that is in red which will not be present if it was the same as the current month).

We iterate through the distance thresholds to demonstrate the convergence of the cluster hierarchy and how the factor selection would look under the past 12 month returns for the Best in Cluster approach:

[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

Source: MSCI, Bloomberg, Factset, J.P. Morgan QDS

44

<!-- page: 45 -->

## Page 45

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

45

<!-- page: 46 -->

## Page 46

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

46

<!-- page: 47 -->

## Page 47

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

47

<!-- page: 48 -->

## Page 48

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

48

<!-- page: 49 -->

## Page 49

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

49

<!-- page: 50 -->

## Page 50

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

50

<!-- page: 51 -->

## Page 51

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

51

<!-- page: 52 -->

## Page 52

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

52

<!-- page: 53 -->

## Page 53

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## References

Choueifaty, Yves, and Coignard , Yves (2008). Toward Maximum Diversification. Journal of Portfolio Management 35 (1): 40-51. Available at
http://www.tobam.fr/wp-content/uploads/2014/12/TOBAM-JoPM-Maximum-Div-2008.pdf

Choueifaty, Yves and Froidure, Tristan and Reynier, Julien (2011) Properties of the Most Diversified Portfolio. Journal of Investment Strategies, Vol.2(2), Spring 2013, pp.49-70. . Available at SSRN:
https://ssrn.com/abstract=1895459

Clarke, Roger G and de Silva, Harindra and Thorley, Steven, Minimum Variance Portfolio Composition (2011). Journal of Portfolio Management, 37(2), 31-45. Available at SSRN:
https://ssrn.com/abstract=1549949

Jean-Charles, Richard and Thierry, Roncalli (2015) Smart Beta: Managing Diversification of Minimum Variance Portfolios. Available at SSRN:
https://ssrn.com/abstract=2595051

Lopez de Prado, Marcos (2016) Building Diversified Portfolios that Outperform Outof-Sample. Journal of Portfolio Management, Forthcoming. Available at SSRN:
https://ssrn.com/abstract=2708678

Lopez de Prado, Marcos (2016) Building Diversified Portfolios that Outperform Outof-Sample (Presentation Slides). Available at
http://ssrn.com/abstract=2713516

Maillard, Sebastien and Roncalli, Thierry and Teiletche, Jerome (2010) The Properties of Equally-Weighted Risk Contributions Portfolios. The Journal of Portfolio Management, 36(4), 60-70. Available at SSRN:
https://ssrn.com/abstract=1271972

Meucci, Attilio (2009) Managing Diversification. Risk, pp. 74-79, Bloomberg Education & Quantitative Research and Education Paper. Available at SSRN:
https://ssrn.com/abstract=1358533

Raffinot, Thomas (2016) "Hierarchical Clustering based Asset Allocation".
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2840729

53

<!-- page: 54 -->

## Page 54

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

## Disclosures

This report is a product of the research department's Global Quantitative and Derivatives Strategy group. Views expressed may differ from the views of the research analysts covering stocks or sectors mentioned in this report. Structured securities, options, futures and other derivatives are complex instruments, may involve a high degree of risk, and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. Because of the importance of tax considerations to many option transactions, the investor considering options should consult with his/her tax advisor as to how taxes affect the outcome of contemplated option transactions.

Analyst Certification:
The research analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple research analysts are primarily responsible for this report, the research analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the research analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect his or her personal views about any and all of the subject securities or issuers; and (2) no part of any of the research analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the research analyst(s) in this report. For all Korea-based research analysts listed on the front cover, they also certify, as per KOFIA requirements, that their analysis was made in good faith and that the views reflect their own opinion, without undue influence or intervention.

## Important Disclosures

 MSCI: The MSCI sourced information is the exclusive property of MSCI. Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an 'as is' basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI and the MSCI indexes are services marks of MSCI and its affiliates.

Company-Specific Disclosures:
Important disclosures, including price charts and credit opinion history tables, are available for compendium reports and all J.P. Morgan–covered companies by visiting
https://www.jpmm.com/research/disclosures,
calling 1-800-477-0406, or e-mailing
research.disclosure.inquiries@jpmorgan.com
with your request. J.P. Morgan’s Strategy, Technical, and Quantitative Research teams may screen companies not covered by J.P. Morgan. For important disclosures for these companies, please call 1-800-477-0406 or e-mail
research.disclosure.inquiries@jpmorgan.com.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

J.P. Morgan uses the following rating system: Overweight [Over the next six to twelve months, we expect this stock will outperform the average total return of the stocks in the analyst’s (or the analyst’s team’s) coverage universe.] Neutral [Over the next six to twelve months, we expect this stock will perform in line with the average total return of the stocks in the analyst’s (or the analyst’s team’s) coverage universe.] Underweight [Over the next six to twelve months, we expect this stock will underperform the average total return of the stocks in the analyst’s (or the analyst’s team’s) coverage universe.] Not Rated (NR): J.P. Morgan has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap equity research, each stock’s expected total return is compared to the expected total return of a benchmark country market index, not to those analysts’ coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying analyst’s coverage universe can be found on J.P. Morgan’s research website, www.jpmorganmarkets.com.

## J.P. Morgan Equity Research Ratings Distribution, as of July 02, 2018

**[table]**

<table><tbody><tr><td rowspan="2"></td><td rowspan="2">Overweight (buy)</td><td rowspan="2">Neutral (hold)</td><td rowspan="2">Underweight (sell)</td></tr><tr></tr><tr><td>J.P. Morgan Global Equity Research Coverage</td><td>47%</td><td>41%</td><td>13%</td></tr><tr><td>IB clients*</td><td>54%</td><td>48%</td><td>40%</td></tr><tr><td>JPMS Equity Research Coverage</td><td>45%</td><td>42%</td><td>13%</td></tr><tr><td>IB clients*</td><td>74%</td><td>66%</td><td>58%</td></tr></tbody></table>
*Percentage of investment banking clients in each rating category.

For purposes only of FINRA/NYSE ratings distribution rules, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above.

54

<!-- page: 55 -->

## Page 55

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Equity Valuation and Risks:
For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at
http://www.jpmorganmarkets.com,
contact the primary analys or your J.P. Morgan representative, or email
research.disclosure.inquiries@jpmorgan.com.
For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website,
http://www.jpmorganmarkets.com.
This report also sets out within it the material underlying assumptions used.

Equity Analysts' Compensation:
The equity research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts:
Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPMS, are not registered/qualified as research analysts under NASD/NYSE rules, may not be associated persons of JPMS, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

J.P. Morgan ("JPM") is the global brand name for J.P. Morgan Securities LLC ("JPMS") and its affiliates worldwide. J.P. Morgan Cazenove is a marketing name for the U.K. investment banking businesses and EMEA cash equities and equity research businesses of JPMorgan Chase & Co. and its subsidiaries.

All research reports made available to clients are simultaneously available on our client website, J.P. Morgan Markets. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research reports available on a particular stock, please contact your sales representative.

Options related research:
If the information contained herein regards options related research, such information is available only to persons who have received the proper option risk disclosure documents. For a copy of the Option Clearing Corporation's Characteristics and Risks of Standardized Options please contact your J.P. Morgan Representative or visit the OCC's website at
https://www.theocc.com/components/docs/riskstoc.pdf

Private Bank Clients:
Where you are a client of the private banking businesses offered by JPMorgan Chase & Co. and its subsidiaries (“J.P. Morgan Private Bank”), research is issued to you by J.P. Morgan Private Bank and not by any other division of J.P. Morgan, including but not limited to the J.P. Morgan corporate and investment bank and its research division.

## Legal Entities Disclosures

U.S
.: JPMS is a member of NYSE, FINRA, SIPC and the NFA. JPMorgan Chase Bank, N.A. is a member of FDIC.
U.K
.: JPMorgan Chase N.A., London Branch, is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and to limited regulation by the Prudential Regulation Authority. Details about the extent of our regulation by the Prudential Regulation Authority are available from J.P. Morgan on request. J.P. Morgan Securities plc (JPMS plc) is a member of the London Stock Exchange and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority. Registered in England & Wales No. 2711006. Registered Office 25 Bank Street, London, E14 5JP.
South Africa
: J.P. Morgan Equities South Africa Proprietary Limited is a member of the Johannesburg Securities Exchange and is regulated by the Financial Services Board.
Hong Kong
: J.P. Morgan Securities (Asia Pacific) Limited (CE number AAJ321) is regulated by the Hong Kong Monetary Authority and the Securities and Futures Commission in Hong Kong and/or J.P. Morgan Broking (Hong Kong) Limited (CE number AAB027) is regulated by the Securities and Futures Commission in Hong Kong.
Korea
: This material is issued and distributed in Korea by or through J.P. Morgan Securities (Far East) Limited, Seoul Branch, which is a member of the Korea Exchange(KRX) and is regulated by the Financial Services Commission (FSC) and the Financial Supervisory Service (FSS).
Australia
: J.P. Morgan Securities Australia Limited (JPMSAL) (ABN 61 003 245 234/AFS Licence No: 238066) is regulated by ASIC and is a Market, Clearing and Settlement Participant of ASX Limited and CHI-X.
Taiwan
: J.P. Morgan Securities (Taiwan) Limited is a participant of the Taiwan Stock Exchange (company-type) and regulated by the Taiwan Securities and Futures Bureau.
India:
J.P. Morgan India Private Limited (Corporate Identity Number - U67120MH1992FTC068724), having its registered office at J.P. Morgan Tower, Off. C.S.T. Road, Kalina, Santacruz - East, Mumbai – 400098, is registered with Securities and Exchange Board of India (SEBI) as a ‘Research Analyst’ having registration number INH000001873. J.P. Morgan India Private Limited is also registered with SEBI as a member of the National Stock Exchange of India Limited (SEBI Registration Number - INB 230675231/INF 230675231/INE 230675231), the Bombay Stock Exchange Limited (SEBI Registration Number - INB 010675237/INF 010675237) and as a Merchant Banker (SEBI Registration Number - MB/INM000002970). Telephone: 91-22-6157 3000, Facsimile: 91-22-6157 3990 and Website:
www.jpmipl.com.
For non local research reports, this material is not distributed in India by J.P. Morgan India Private Limited.
Thailand
: This material is issued and distributed in Thailand by JPMorgan Securities (Thailand) Ltd., which is a member of the Stock Exchange of Thailand and is regulated by the Ministry of Finance and the Securities and Exchange Commission and its registered address is 3rd Floor, 20 North Sathorn Road, Silom, Bangrak, Bangkok 10500.
Indonesia
: PT J.P. Morgan Securities Indonesia is a member of the Indonesia Stock Exchange and is regulated by the OJK a.k.a. BAPEPAM LK.
Philippines
: J.P. Morgan Securities Philippines Inc. is a Trading Participant of the Philippine Stock Exchange and a member of the Securities Clearing Corporation of the Philippines and the Securities Investor Protection Fund. It is regulated by the Securities and Exchange Commission.
Brazil
: Banco J.P. Morgan S.A. is regulated by the Comissao de Valores Mobiliarios (CVM) and by the Central Bank of Brazil.
Mexico
: J.P. Morgan Casa de Bolsa, S.A. de C.V., J.P. Morgan Grupo Financiero is a member of the Mexican Stock Exchange and authorized to act as a broker dealer by the National Banking and Securities Exchange Commission.
Singapore:
This material is issued and distributed in Singapore by or through J.P. Morgan Securities Singapore Private Limited (JPMSS) [MCI (P) 099/04/2018 and Co. Reg. No.: 199405335R], which is a member of the Singapore Exchange Securities Trading Limited and/or JPMorgan Chase Bank, N.A., Singapore branch (JPMCB Singapore) [MCI (P) 046/09/2018], both of which are regulated by the Monetary Authority of Singapore. This material is issued and distributed in Singapore only to accredited investors, expert investors and institutional investors, as defined in Section 4A of the Securities and Futures Act, Cap. 289 (SFA). This material is not intended to be issued or distributed to any retail investors or any other investors that do not fall into the classes of “accredited investors,” “expert investors” or “institutional investors,” as defined under Section 4A of the SFA. Recipients of this document are to contact JPMSS or JPMCB Singapore in respect of any matters arising from, or in connection with, the document.
Japan
: JPMorgan Securities Japan Co., Ltd. and JPMorgan Chase Bank, N.A., Tokyo

55

<!-- page: 56 -->

## Page 56

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

Branch are regulated by the Financial Services Agency in Japan.
Malaysia
: This material is issued and distributed in Malaysia by JPMorgan Securities (Malaysia) Sdn Bhd (18146-X) which is a Participating Organization of Bursa Malaysia Berhad and a holder of Capital Markets Services License issued by the Securities Commission in Malaysia.
Pakistan
: J. P. Morgan Pakistan Broking (Pvt.) Ltd is a member of the Karachi Stock Exchange and regulated by the Securities and Exchange Commission of Pakistan.
Saudi Arabia
: J.P. Morgan Saudi Arabia Ltd. is authorized by the Capital Market Authority of the Kingdom of Saudi Arabia (CMA) to carry out dealing as an agent, arranging, advising and custody, with respect to securities business under licence number 35-07079 and its registered address is at 8th Floor, Al-Faisaliyah Tower, King Fahad Road, P.O. Box 51907, Riyadh 11553, Kingdom of Saudi Arabia.
Dubai
: JPMorgan Chase Bank, N.A., Dubai Branch is regulated by the Dubai Financial Services Authority (DFSA) and its registered address is Dubai International Financial Centre - Building 3, Level 7, PO Box 506551, Dubai, UAE.

## Country and Region Specific Disclosures

U.K. and European Economic Area (EEA):
Unless specified to the contrary, issued and approved for distribution in the U.K. and the EEA by JPMS plc. Investment research issued by JPMS plc has been prepared in accordance with JPMS plc's policies for managing conflicts of interest arising as a result of publication and distribution of investment research. Many European regulators require a firm to establish, implement and maintain such a policy. Further information about J.P. Morgan's conflict of interest policy and a description of the effective internal organisations and administrative arrangements set up for the prevention and avoidance of conflicts of interest is set out at the following link
https://www.jpmorgan.com/jpmpdf/1320742677360.pdf.
This report has been issued in the U.K. only to persons of a kind described in Article 19 (5), 38, 47 and 49 of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (all such persons being referred to as "relevant persons"). This document must not be acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this document relates is only available to relevant persons and will be engaged in only with relevant persons. In other EEA countries, the report has been issued to persons regarded as professional investors (or equivalent) in their home jurisdiction.
Australia:
This material is issued and distributed by JPMSAL in Australia to "wholesale clients" only. This material does not take into account the specific investment objectives, financial situation or particular needs of the recipient. The recipient of this material must not distribute it to any third party or outside Australia without the prior written consent of JPMSAL. For the purposes of this paragraph the term "wholesale client" has the meaning given in section 761G of the Corporations Act 2001. J.P. Morgan’s research coverage universe spans listed securities across the ASX All Ordinaries index, securities listed on offshore markets, unlisted issuers and investment products which Research management deem to be relevant to the investor base from time to time. J.P. Morgan seeks to cover companies of relevance to the domestic and international investor base across all GIC sectors, as well as across a range of market capitalisation sizes.
Germany:
This material is distributed in Germany by J.P. Morgan Securities plc, Frankfurt Branch which is regulated by the Bundesanstalt für Finanzdienstleistungsaufsicht.
Hong Kong:
The 1% ownership disclosure as of the previous month end satisfies the requirements under Paragraph 16.5(a) of the Hong Kong Code of Conduct for Persons Licensed by or Registered with the Securities and Futures Commission. (For research published within the first ten days of the month, the disclosure may be based on the month end data from two months prior.) J.P. Morgan Broking (Hong Kong) Limited is the liquidity provider/market maker for derivative warrants, callable bull bear contracts and stock options listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.
Korea:
This report may have been edited or contributed to from time to time by affiliates of J.P. Morgan Securities (Far East) Limited, Seoul Branch.
Singapore:
As at the date of this report, JPMSS is a designated market maker for certain structured warrants listed on the Singapore Exchange where the underlying securities may be the securities discussed in this report. Arising from its role as designated market maker for such structured warrants, JPMSS may conduct hedging activities in respect of such underlying securities and hold or have an interest in such underlying securities as a result. The updated list of structured warrants for which JPMSS acts as designated market maker may be found on the website of the Singapore Exchange Limited:
http://www.sgx.com.
In addition, JPMSS and/or its affiliates may also have an interest or holding in any of the securities discussed in this report – please see the Important Disclosures section above. For securities where the holding is 1% or greater, the holding may be found in the Important Disclosures section above. For all other securities mentioned in this report, JPMSS and/or its affiliates may have a holding of less than 1% in such securities and may trade them in ways different from those discussed in this report. Employees of JPMSS and/or its affiliates not involved in the preparation of this report may have investments in the securities (or derivatives of such securities) mentioned in this report and may trade them in ways different from those discussed in this report.
Taiwan
: Research relating to equity securities is issued and distributed in Taiwan by J.P. Morgan Securities (Taiwan) Limited, subject to the license scope and the applicable laws and the regulations in Taiwan. According to Paragraph 2, Article 7-1 of Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers (as amended or supplemented) and/or other applicable laws or regulations, please note that the recipient of this material is not permitted to engage in any activities in connection with the material which may give rise to conflicts of interests, unless otherwise disclosed in the “Important Disclosures” in this material.
India:
For private circulation only, not for sale.
Pakistan:
For private circulation only, not for sale.
New Zealand:
This material is issued and distributed by JPMSAL in New Zealand only to persons whose principal business is the investment of money or who, in the course of and for the purposes of their business, habitually invest money. JPMSAL does not issue or distribute this material to members of "the public" as determined in accordance with section 3 of the Securities Act 1978. The recipient of this material must not distribute it to any third party or outside New Zealand without the prior written consent of JPMSAL.
Canada:
The information contained herein is not, and under no circumstances is to be construed as, a prospectus, an advertisement, a public offering, an offer to sell securities described herein, or solicitation of an offer to buy securities described herein, in Canada or any province or territory thereof. Any offer or sale of the securities described herein in Canada will be made only under an exemption from the requirements to file a prospectus with the relevant Canadian securities regulators and only by a dealer properly registered under applicable securities laws or, alternatively, pursuant to an exemption from the dealer registration requirement in the relevant province or territory of Canada in which such offer or sale is made. The information contained herein is under no circumstances to be construed as investment advice in any province or territory of Canada and is not tailored to the needs of the recipient. To the extent that the information contained herein references securities of an issuer incorporated, formed or created under the laws of Canada or a province or territory of Canada, any trades in such securities must be conducted through a dealer registered in Canada. No securities commission or similar regulatory authority in Canada has reviewed or in any way passed judgment upon these materials, the information contained herein or the merits of the securities described herein, and any representation to the contrary is an offence.
Dubai:
This report has been issued to persons regarded as professional clients as defined under the DFSA rules.
Brazil
: Ombudsman J.P. Morgan: 0800-7700847 / ouvidoria.jp.morgan@jpmorgan.com.

General:
Additional information is available upon request. Information has been obtained from sources believed to be reliable but JPMorgan Chase & Co. or its affiliates and/or subsidiaries (collectively J.P. Morgan) do not warrant its completeness or accuracy except with respect to any disclosures relative to JPMS and/or its affiliates and the analyst's involvement with the issuer that is the subject of the research. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Opinions and estimates constitute our judgment as of the date of this material and are subject to change without notice. Past performance is not indicative of future results. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not

56

<!-- page: 57 -->

## Page 57

Robert Smith, PhD (852) 2800 8569 robert.z.smith@jpmorgan.com

Global Quantitative & Derivatives Strategy 13 September 2018

J.P.Morgan

intended as recommendations of particular securities, financial instruments or strategies to particular clients. The recipient of this report must make its own independent decisions regarding any securities or financial instruments mentioned herein. JPMS distributes in the U.S. research published by non-U.S. affiliates and accepts responsibility for its contents. Periodic updates may be provided on companies/industries based on company specific developments or announcements, market conditions or any other publicly available information. Clients should contact analysts and execute transactions through a J.P. Morgan subsidiary or affiliate in their home jurisdiction unless governing law permits otherwise.

"Other Disclosures" last revised August 18, 2018.

Copyright 2018 JPMorgan Chase & Co. All rights reserved. This report or any portion hereof may not be reprinted, sold or redistributed without the written consent of J.P. Morgan.

Disseminated 13 Sep 2018 04:34 PM HKT

57

Completed 13 Sep 2018 02:38 PM HKT
