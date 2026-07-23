# Binary / Digital Options
A binary option promises a *fixed payoff* based on whether or not the stock price is higher / lower than the strike price at time of expiry.
* Binary Call: Receive payout if $S_T > K$
* Binary Put: Receive payout if $S_T < K$

If the condition for payout is not met, you simply lose your initial investment in the option price. Since binaries don't include transferring actual stocks, it is hard to hedge against the risks the way one would in normal options. This makes binaries more so like betting.

## Quick note on put-call parity of binaries
Say we have a put and call binary option, with the same strike prices, at the same expiry, with an identical payoff of $M$. Then, if I held a portfolio of 1x binary call & 1x binary put, at expiry exactly one of the options will pay out, giving our portfolio a value $M$. Present value will thus be $Me^{-rt}$, leading to the equation:$$P + C = Me^{-rt}$$ 

# Bull & Bear Spreads
## Bull Spread
Consider a portfolio consisting of:
1. A long call option with strike price 100
2. A short (written) call option with strike price 120

With both expiring on the same day. We have a few cases:
1. **$S_T < 100$**: Long call @ 100 is not exercised, Short call @ 120 is not exercised. Total payoff = 0
2. **$120 < S_T$**: Long call @ 100 is exercised --> Payoff = $S_T - 100$. Short call @ 120 is exercised --> Payoff = $120 - S_T$. Total payoff = $120 - 100 = 20$
3. **$100 < S_T < 120$**: Long call @ 100 is exercised --> Payoff = $S_T - 100$. Short call @ 120 is not exercised. Total payoff = $S_T - 100$ (linear with $S_T$) between 0 and 20

We benefit from a bull spread in a bull market, so we implement this strategy if we think the direction is bullish

## Bear Spread
This time, we have:
1. Long Put @ 120
2. Short (Written) put @ 100

The cases are very similar. This time, $S_T < 100$ gives us the payoff of $120 - 100 = 20, $S_T > 120$ gives us nothing, and payoff is linear in between. We implement this strategy if we think the market is bearish.

# Straddle
In the straddle, we simultaneously take a long position in a call option and a put option, both identical. As a result, the initial loss is already $P + C$. We hope that a large fluctuation in the underlying stock in either direction will help offset these losses and bring us profit. The cases where this is favourable are shown below:
1. **$S_T - K > (P + C)$**: Here, the call is exercised yielding a payoff of $S_T - K$. The put is not exercised, yielding payoff 0. Total profit = $S_T - K - (P+C)$, a profit
2. **$K - S_T > (P+C)$**: Now, call is not exercised so payoff = 0. Put is exercised with payoff $K - S_T$. Total profit = $S_T - K - (P+C)$, a profit

In other words, this strategy succeeds if the price moves in either direction by a large enough amount, so that the payoff from one of the options offsets the combined premia of purchasing both options.