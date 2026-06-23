# Simple Returns
Simple returns refers to the basic way of calculating the growth in a stock price, comparing between times $t_1$ and $t_2$. Simple returns divides the change in price by original price:

$$\frac{P_{t_2} - P_{t_1}}{P_{t_1}}$$

# Log Returns
Log returns formula is given by:

$$\ln(\frac{P_{t_2}}{P_{t_1}})$$

# The difference
Log returns treats the change in stock price differently to Simple returns:

* Simple returns calculates the *relative change* in price
* Log returns calculates the *continuously compunded rate of return* that would result in the observed growth in stock price

Explanation: We know that if the rate of return of a certain value is $x\%$, and this return is compunded continuously, then after time $t$, the value grows to $Pe^{xt}$. Then, the log return formula would give us:

$$ln(\frac{Pe^{xt}}{P}) = xt$$

Here, $xt$ is the *continuously compounded rate of return* that will grow the stock price from $P_0$ to $P_1$. 

# Conversion between the two
If $r$ is our simple rate of return, then 

$$r = \frac{P_{t_2} - P_{t_1}}{P_{t_1}} \Rightarrow \frac{P_{t_2}}{P_{t_1}} = 1+r \Rightarrow  \ln(\frac{P_{t_2}}{P_{t_1}}) = ln(1+r)$$ 

# Benefits / Disadvantages
## Addition
Because of the following property:

$$\frac{P_2}{P_0} = \frac{P_1}{P_0} \cdot \frac{P_2}{P_1}$$

To stitch together the growth over two consecutive time periods, you just need to multiply the fractions. By a property of logarithms, this means that you can simply add log returns over two periods to get the overall log returns over both periods

## Log-normal distribution
In Asset pricing, stock prices are assumed to follow a log-normal distribtion. Since a log return can also be expressed as the difference of the logs of two stock prices, log returns are also assumed to be normally distributed.

## Log doesn't allow aggregating across multiple assets in a portfolio
If we have multiple assets, each with their own growth rates, we can use a weighted sum of all the simple returns.