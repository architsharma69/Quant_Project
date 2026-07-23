# Call & Put Options
Options are traded forward contracts with the right, but not the obligation, to fulfil the contract. 

## Call options
A call option is the option to buy an asset for a certain price at a certain time. The price of the option is an initial payment which grants you the right to purchase that asset at the strike date. For example:

Imagine there is a call option for 100 stocks of a company:
* Current stock price is $98 per share
* Strike price is $100 per share
* Option price is $5 per share

By the date of maturity, 
* if **stock price < strike price**, you are buying something for a higher price than on the market --> Making a *Loss*
* if **stock price > strike price**, you are buying stocks at strike price which is lower than market price --> Making a *Profit*
* However, your net profit comes after deducting the price of the options: **$500**

## Put options
A put option is the option to sell an asset for a certain price at a certain time. If the asset were stocks, and you held till expiry, you could either 1) Short Sell the stocks, or 2) If you own that many stocks, simply sell them

Imagine a put option for 100 stocks:
* Current stock price is $65 per share
* Strike price is $70 per share
* Option price is $7 per share

By the date of maturity,
* **stock price < strike price** $\rightarrow$ you sell at higher price, buy at the mkt price $\rightarrow$ make *profit*
* **strike price < stock price** $\rightarrow$ sell lower, buy higher $\rightarrow$ make *loss* $\rightarrow$ so you should exercise the option to stop the contract

# Short positions on options
The last 2 examples discussed were for long positions on call and put options. But where did the option, i.e the contract, even come from? 

Someone had to have generated it, since once you are the owner of the option, you're simply in a contract with someone. But who is that someone?

## Writing options
Going short on a call / put option is called *writing an option*. To clarify, this means selling an option when you aren't holding any options yourself. In other words, you are generating the contract yourself. 

While someone going long on a call option must pay the option premium, you, as the creator of the contract, will receive the option premium. You have two choices to close your position (i.e. to buy back the call option)
1) Close your position early (before maturity), buy a call option at its current premiumm, and receive the price difference in the premia.
2) Wait till maturity, reap the results of the conditional contract. This is why the payoff for an option writer is always the **opposite** as that of the option buyer

Exact same principle applies to writers of put options.
# Payoffs from the different kinds of positions
Let the final underlying stock price be **S** and the strike price be **K**. We examine the *payoff*, which is simply the money earned from fulfilling the contract stated in the option.
* Long position in a call option: $max(S - K, 0)$ (Buy at K, sell at S)
* Long position in a put option: $max(K - S, 0)$ (Buy at S, sell at K)
* Short position in a call option: $-min(K - S, 0)$
* Short position in a put option: $-min(S - K, 0)$

The minimum value of 0 represents the safety net given by the option to prevent the contract from executing.

# Terminology
## In / At / Out of the money
In the money simply refers to whether the underlying asset is at a price such that the option will still yield a positive payoff. I.e. a call option is in the money when S > K, while a put is in the money when S < K.

At the money is when the asset price equals the strike price, and out is when the theoretical payoff is negative.

## Intrinsic Value
At any point in time, the intrinsic value of an option is the value it would have if the exercise time *right now*, i.e. there is no time to maturity. In other words, you calculate the payoff of the option as if the underlying stock price is given by the current price.

Since it is typically beneficial to hold the option for longer if possible, the additional time to expiry of the option gives it more value, called the **time value** of the option.

Total value can be thought of as intrinsic value + time value.

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

# Naked vs Covered options
The terms *naked* and *covered* only apply to writers of options. Buyers of put and call options always have a safety net - that is the price of the option. But writers do not:
* For writers of call options, the higher stock price is above strike price, the greater their loss (theoretically, infinitely high)
* For writers of put options, the lower stock price is below strike price, the greater their loss (capped at the strike price K)

As such, writers have a way to cap their losses, by already holding either long / short positions in the underlying stocks. This is called a *covered option*
## Covered Calls
By expiry, the writer of a call option will have to sell stocks at price $K$. If stock mkt price at time of expiry, $S_t < K$, then his profit is the option price. However, if $S_t > K$:

In a *naked* call, the writer doesn't own the stocks beforehand, so he will have to short them - sell at $K$, then immediately buy at $S_t$. Theoretical loss = $K - S_t$, which is unbounded below.

In a *covered* call, the writer buys the stocks beforehand, at price $S_0$, and sells at $K$ --> Maximum possible loss = $K - S_0$.

## Covered Puts
The idea is the same, a *naked* put exposes the writer to maximum potential loss of $K$ (buy stock at $K$ but sell at $0$).

For *covered* puts, the writer either
1) Keeps aside enough cash to pay the maximum potential loss of $K$ (so that he does not have to take on any debt)
2) Has a short position in the stocks from before, where he sold them at price $S_0$. As such, when he buys the stocks at $K$, his loss is capped at $K - S_0$

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
