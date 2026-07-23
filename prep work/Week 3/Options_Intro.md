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