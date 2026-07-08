# Statement of the theory
The efficient market hypothesis states that at any point in time, the price of a security is *fully reflected* by available information.

This means two things:
* Changes in information are reflected **instantaneously** (within the same time period) in the price
* Changes in information are reflected **in their entirety** in the price

As a result, there is no more information left to exploit to get **excess** returns beyond the expected returns. Based on current information, the expected value of any excess returns is **0**.

# Expected return / "Fair Game" models
Based on the statement that current prices fully reflect all available information, we can make the following claim about the future market equilibrium, i.e. future prices: **The expected price and expected return, one time period into the future, is some function of the current price and current set of 'all information'**

Let:
* Price of security $j$ at time $t$ be $p_{j,t}$
* Set of information at time $t$ be $\Phi_t$
* Return over one time period be $r_{j,t} = \frac{p_{j,t+1} - p_{j, t}}{p_{j,t}}$

Then, given current information, the expected value of future price is given by:
$$E(p_{j, t+1} | \Phi_t) = [1 + E(r_{j, t} | \Phi_t)] \cdot p_{j,t}$$
(This isn't the claim of the theory, its just an identity - Expected future price given some condition is current price times expected return given the same condition)

Now, if the equilibrium expected returns $(p_{j, t+1})$ are formed **entirely** on the basis of current information $\Phi_t$, it follows that there **should not** be any excess price increase beyond the expected future price. In other words, if

$$x_{j, t+1} = p_{j, t+1} - E(p_{j, t+1} | \Phi_t)$$

Then:
$$E(x_{j, t+1} | \Phi_t) = 0$$

In other words, the excess returns are truly random, or 'fair game', with respect to the information $\Phi_t$

# Factors which may influence market efficiency
In accordance with the efficient market hypothesis, the 'efficiency' of a market is the ability of the market to respond immediately to new information, and price it in.

Factors such as:
* Transaction costs
* Information not freely available to all investors
* Disagreement among investors on the implications of given information on the price

Can serve to diminish the ability of the price to immediately adjust to information.

# What is the actual current state of the market?
The strong EMH would imply that even fundamental analysis is a useless strategy, as it prices in immediately into the security price. As a result, people argue that that the stock market, in reality, lies somewhere between the weak and semi-strong EMH, allowing for fundamental analysis to still grant some excess gains.

# Side-topic: Cross-Sectional Dispersion
Rather than looking at the change over time of just *one* security, what if we compare multiple share over a fixed time? That is cross-sectional analysis
