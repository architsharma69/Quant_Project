# Definitions of value and momentum
Both value and momentum are **factors** - they are related (or theorized to be related) to returns. These factors' relations to return are explained as two effects:
* The **value effect** - How the ratio of an asset's book (long-run) value to its current market value affects returns
* The **momentum effect** - How an asset's recent relative performance history affects returns

# How these factors are measured for each asset
**Value**: Measured using the book-to-market ratio, *BE/ME*
*Formula: Book Value (Assets - Liabilities) $\div$ Market Cap*

**Momentum**: Past 12-month cumulative raw return (*MOM2-12*), skipping the most recent month
*Formula: [ (Close @ end of 2nd-last month $\div$ Close @ end of 12th-last month) - 1] x 100

## Factor measurement $\rightarrow$ Signal
In the AQR paper, there are **no further calculations** done to the value and momentum values. The raw values are taken as signal values.

# How portfolios are typically constructed in research and real-life applications
The AQR paper constructed its own portfolio to test out the implications of its theory. However, this construction is a general method for constructing portfolios:

* *Long-Short Portfolio*: A portfolio consisting of both long and short positions - some stocks are shorted and some are bought
* *Signal*: A score given to a security - meant to tell the **predicted direction and magnitude** of future returns
    * Positive means buy, Negative means sell
    * We construct the signal based on algorithms / factors (e.g. value or momentum)
* *Weights*: A value given to a security - meant to tell **how much** of the security to keep in the portfolio
    * In a long / short portfolio, negative signal means take a short position, magnitude of the negative signal tells us how much to sell


# How does the AQR paper construct its portfolio
The goal of the paper is to use **value** and **momentum** as factors to predict the future returns of securities, to verify the theory that these factors are strongly correlated with returns.
* Constructs its portfolio with equal capital on both sides (long and short)
    * By doing so, it gives equal weightage to securities that increase and those that decrease in price - as a result, broader market direction has a lower effect on returns, and we observe purely the effect of value / momentum
* Assigns weights based on signal rankings, not raw signal scores
    * Calculation is: $w_{i, t} = Rank(S_{i,t}) - [\frac{\sum_{k = 0}^N Rank(S_{k, t})}{N}]$
    * This way, even if a signal for a security is disproportionally large, it won't be given a disproportionally large weight
    * Since it allows for positive and negative signals, all signals add to 0

# More AQR factors
AQR also discusses two more factors - Quality and Low Risk
## Quality
Quality refers to the fundamentals of a business. Quality looks for companies with **strong** fundamentals, rather than instrinsic valuation compared to market valuation.
* Justification: Companies with high quality tend to be more resilient, and lead in growth. As a result, they can provide *consistent returns* and *minimise risk*
* Metrics to use as quality signals: Profitability ratios, balance sheet health, earnings consistency.

## Low risk
Low risk looks for securities with low price volatility, steady performance
* Justification: These qualities imply that the security will remain stable in the future, maintaining low risk for a portfolio
* Metrics: Returns Volatility (e.g. Std Dev of returns) & Equity Beta

# Reflections from the 12-2 Momentum Ranking Task
In this task, I graph the 12-2 momentum ranking of 20 separate tickers, comparing that with the 1-month return of the subsequent month. Here, since momentum is our signal, the ranking of return should correspond with the ranking of momentum.

**However**, there actually seems to be very little correlation between the signal and the next month's return. If I visually compare the momentum rankings to the rankings of the next month's returns, they do not correlate. In fact, many stocks that ranked *high* in momentum, actually ranked *low* in the subsequent earnings:

![Graph ranking momentum of 20 securities vs next month's earnings](Images/Momentum_Graph.png)

In order to simulate how a long-short portfolio of these 20 stocks would perform, I carried out the same simulation as in the AQR paper - $1 USD Long, \$1 USD short. We then see our portfolio returns the next month:

![List of stock performance](/Users/architsharma/Python/Quant_Project/Images/Portfolio_Sim.png)


**Why?** This could be due to general bear market movements in the past year, such as the memory squeeze and oil shortage, muddying the momentum effect.