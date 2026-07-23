# Factors affecting option prices
## Underlying stock price
The payoff is directly related to the stock price. 
* For call options, increased stock price --> higher payoff --> more valuable. 
* For put options, lower stock price --> more valuable.

## Time to expiry
Comparing two options: one with a shorter expiry and one with a longer expiry, the latter has *more* choices, and more flexibility than the former, as such the latter must be atleast as valuable as the former, if not more. So generally, a later expiry date adds more value to the option.

However, in the case of European options, which only allow exercising the option at expiry, an expiry date further on exposes the underlying stock to more risk. For example, if the company issues dividends after the first date of expiry, which changes the price of the stock, holding the longer expiry option may put you at a disadvantage.

## Underlying stock volatility
In the case of stocks, price volatility, which refers to the chances of price fluctuation in either direction, the large downside risk makes the stock less appetising. However, for option holders, the downside risk is capped at the price of the option (since you could opt to cancel the contract). As a result, the value of the option increases with underlying stock volatility.

## Risk-Free rate
Two main effects:
1. The increase in risk free rates causes investors to expect larger price increase from the underlying stock. As a result, the stock price is expected to move upwards --> making call options more valuable & put options less valuable
2. Risk-free rates also refer to interest rates - they dictate the baseline rate at which stuff will grow in value. 
    * The strike price **K** of the option is a future cash-flow - we'll be receiving it in the future, in terms of future money, which, in comparison to current money, has grown by the risk-free rate. 
    * So the present value of the strike price is a lower quantity, something that would grow to become **K** in the future. As a result, we can calculate the present value of the cash-flow by starting out at **K** and discounting it by the risk-free rate.
    * When risk-free rate increases, K is discounted by a larger percentage, leading to a *lower* current value, i.e. effectively a lower strike price
    * For call options, lower strike price --> buy lower, sell at the same price --> increased value
    * For put options, lower strike price --> sell lower, buy at the same price --> decreased value

# Upper & Lower limits for option prices
Let $C$ be the call option price, and $P$ be the put option price. We discuss how these are bounded above and below
## Upper Limits
### Call options
The price of a call option $C$ must not exceed the current stock price $S_0$. If $C > S_0$:
* I could buy the stock for $S_0$, then sell (write) a call option for $C$
* I make profit $C - S_0$. This is *riskless* profit
* In case the buyer of the call option decides to exercise it, I simply sell him the stock which I already had. I am not exposed to any more losses.

As such, $C$ is always bounded by $C \le S_0$, if not, it would allow arbitrageurs to enjoy riskless profit. This holds for both American and European options

### Put options
A put option involves selling stocks for price $K$. Since the stock price cannot be below $0$, the maximum payoff is $K$. As such, we must have $$P \le Present\ Value(K)$$ If not, even at maximum profit, the put holder would still make a loss. Arbitrageurs will also be able to take advantage of this. 
**American-style**: Since they can be exercised at any time, the present value of the strike price *is* $K$. Thus, $P \le K$

**European-style**: Since these can only be exercised at expiry, we discount the strike price to arrive at: $P \le K\cdot e^{-rt}$, $r$ is the risk free rate & $t$ is time to expiry

## Lower Limits
### Call options (We look at European)
A lot more complicated. We claim that the lower bound for a call option is given by $C \ge S_0 - Ke^{-rt}$.

We consider a portfolio containing 1) A european call option for one stock & 2) A bond that provides payoff $K$ at expiry of the option. By the expiry date:
* If $S_t > K$, we exercise the option, use payoff $K$ from the bond. Our portfolio is now worth $S_t$
* If $S_t < K$, we don't exercise, and our portfolio is worth $K$

In both cases, portfolio value is $max(S_t, K)$. Furthermore, the portfolio is worth atleast $S_t$. While we've shown this holds at expiry, this same relation should also hold *at all times leading up to expiry*. Discounting both sides to the present day, we would have:

$$
\begin{aligned}
Portfolio\ Value &\ge S_0\\
Call\ value + Bond\ Value &\ge S_0\\
C + Ke^{-rt} &\ge S_0\\
C &\ge S_0 - Ke^{-rt}
\end{aligned}
$$

This strategy with the portfolio vs the stock price leads us to an important equation relating the call option price to the current stock price, thus giving us a lower bound

#### Note: Why must a relationship which holds at expiry also hold at all other times
Consider any 2 portfolios A & B, such that at time T, $Value_{T}(A) = Value_{T}(B)$. *We argue that at all other times, Value(A) = Value(B)*.

Assume to the contrary that at time $t < T$, $Value_{t}(A) < Value_{t}(B)$. 
* An arbitrageur could **buy A & sell B**, instantly making profit in the price differences. 
* Since their value is identical at time T, he can use the value of A to pay off the value of B once time = T

As such, if the two portfolios have identical value at time T, they must have identical value today.

# Put-Call Parity
We consider another situation with 2 portfolios which will give us an equation relating call prices:

Portfolio A: 1x European call option strike price K & time T, 1x zero-coupon bond giving us payoff K at time T 

Portfolio B: 1x European put option strike price K & time T, 1x share of the stock

Once time = T:
* If $S_T > K$
    * For **A**: Call option is exercised, with a value of $S_T - K$. The bond has a value of $K$. Total value = $(S_T - K) + K = S_T$
    * For **B**: Put option is not exercised, becomes worthless. The stock has a value of $S_T$. Total value = $S_T$
* If $S_T < K$
    * For **A**: Call option is not exercised, becomes worthless. The bond has a value of $K$. Total value = $K$
    * For **B**: Put option is exercised, value is $K - S_T$. The stock has a value of $S_T$. Total value = $(K - S_T) + S_T = K$

<u>Price of both portfolios @ time T</u>
||Portfolio A| Portfolio B|
|---|-----------|------------|
|$S_t > K$|$S_T$|$S_T$|
|$S_t < K$|$K$|$K$|

In all possible cases, both portfolios have identical value at time T. So, they must have identical value right now:
$$
\begin{aligned}
PV(A) &= PV(B)\\
C + Ke^{-rT} &= P + S_0\\
\end{aligned}
$$
This equation, relating the value of a call option to that of a put option, is called **put-call parity**


