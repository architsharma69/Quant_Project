# Price-Earnings (PE) Ratio
PE Ratio is calculated by:
<p style="text-align: center;"><strong>Price Per Share / Earnings Per Share</strong></p>

* Price doesn't need to be explained
* Earnings Per Share: Earnings can be taken from current FY, trailing 4 quarters, or expected

# Max Drawdown
Simply, the largest drop in the price of a stock / value of a portfolio, as a percentage of the peak price. As long as a new peak is not achieved, the stock is still taken to be at a loss. A price becomes a new peak only after it surpasses the original peak. 

# Volume (Annualised)
* Volume of a share over a period is simply the number of shares traded over that period of time
    * Higher volume indicates a more liquid market
    
To annualise something just means that you are calculating that metric over a period of a year, e.g. annualised return, annualised volume, annualised volatility

# Historical Volatility
Simply, the volatility of the price of a stock / return of a portfolio over a period of time, typically measured using *standard deviation*. It can be used to measure **risk**.

# Sharpe Ratio
First, look at the equation for the ratio. For a portfolio, over a period of time, e.g. 10 yrs (120 months), let:
* monthly *rate of return* be $R_p$
* monthly *risk-free rate of return* of the market be $R_f$ 
* *standard deviation of 120 monthly portfolio returns*, as percentage of mean, be $\sigma$, then:

$(R_p - R_f)$ is the monthly return differential against a benchmark. Over 120 months, we simply average it. Then:

$$\frac{Mean(R_p - R_f)}{\sigma}$$

is the **Sharpe Ratio** of the portfolio. This is a metric for **risk-adjusted relative returns** 
* **Relative** because removing the risk-free rate means we eliminate the 'free lunch' returns we would have gotten
* **Risk-adjusted** because: $\uparrow$ risk $\rightarrow$ $\uparrow$ volatility $\rightarrow$ worse Sharpe Ratio, and vice versa

## Std dev assumes normally distributed price movements
Variance or Std Dev simply aggregate all differences in price from the mean. They lose out info about the distribution, i.e. where is it skewed. Since Sharpe uses just std dev to measure volatility, it is like assuming that the price / return changes are normally distributed.

## How to use
While sharpe ratio $>1$ is generally good, you should compare Sharpe Ratios of a fund / security in comparison to its peers.

# Rate of Return
For a security / portfolio - quite obvious:  change in value $\div$ by initial price, as a percentage.