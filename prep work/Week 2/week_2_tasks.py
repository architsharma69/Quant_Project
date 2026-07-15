import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math
from datetime import datetime

today_date = datetime.now()

securities = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "AVGO", "GOOG", "META", "TSLA", "MU", "JPM", "LLY", "AMD", "XOM", "WMT", "INTC", "JNJ", "V", "COST", "GE"]
sec_names = " ".join([security for security in securities])
stocks = yf.Tickers(sec_names).tickers

def cross_sectional_returns():
    """
    Over a period of one year, compare 20 different S&P 500 securities by their monthly returns
    For each security, we graph its average monthly return, and separately, its return volatility (stdev) 
    """
    avg_log_ret = lambda ser: (np.log(ser / ser.shift(1)).dropna()).mean()
    ret_stdev = lambda ser: (np.log(ser / ser.shift(1)).dropna()).std(ddof = 0)

    # Modify the {tickername: tickerobj} dict to hold series of close prices as values instead
    for security in securities:
        ticker = stocks[security]
        stocks[security] = ticker.history(period = f"1y", end = "2026-06-01", interval = "1mo")["Close"]
    
    # Create list of avg monthly log returns, following the same sequence as `securities`
    returns, volatility = [avg_log_ret(stocks[security]) for security in securities], [ret_stdev(stocks[security]) for security in securities]

    # Plot bar graphs for all securities in parallel (use `securities` as the category list)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10,5))
    ax1.bar(securities, returns, color = 'skyblue')
    ax1.set_title('Average Log Returns')
    ax1.set_ylabel('Value')
    ax1.tick_params(axis='x', labelsize=4) 
    ax1.set_ylim(-0.02, 0.2) 
    ax1.yaxis.set_major_locator(MultipleLocator(0.015)) 

    ax2.bar(securities, volatility, color = 'salmon')
    ax2.set_title('Stdev of Log Returns')
    ax2.set_ylabel('Value')
    ax2.tick_params(axis='x', labelsize=4)

    plt.tight_layout()
    plt.show()

def long_short_portfolio(signal_rank, returns):
    """
    `signal_rank` is a dict which maps security name --> ranking, `returns` is a dict which maps security name --> next month return, in % return
    """
    num = len(signal_rank.keys())           # Just the number of securities

    # Scaling Factor: The weight for each stock tells us how much of our capital we are putting in that stock.
    # In a portfolio with $1 long and $1 short, the weights on both sides must add up to one respectively, since the total capital on each side is $1
    # Now, the raw weight comes from the difference of the security's ranking from the mean ranking, then,
    # Final weight is raw weight normalised, i.e. divided by sum of all raw weights
    raw_weights = [rank - ((num + 1) / 2) for rank in range(math.ceil(num / 2) + 1, num + 1, 1)]

    scaling_factor = 1 / sum(raw_weights)

    weight = lambda sec: (signal_rank[sec] - (num + 1) / 2) * scaling_factor # Negative weight means sell, positive means buy

    print("\n################# Simulate a Long-Short Portfolio, with $2 capital injection ######################")
    for sec in securities:
        print(f'{sec}: Weight = {weight(sec)}, % Return = {round(returns[sec], 4)}, Absolute return = {round(returns[sec] * weight(sec), 4)}        {'PROFIT' if returns[sec] * weight(sec) > 0 else 'LOSS'}')
    abs_returns = sum([(returns[sec] / 100) * weight(sec) for sec in securities]) # return * weight gives us the absolute return to the portfolio due to that security
    rel_returns = (abs_returns / 2) * 100

    return (2 + abs_returns, rel_returns)


def momentum_ranking():
    """
    An introduction to factor investing using momentum: 
    Rank the 20 stocks from the previous task based on their 12-2 Momentum values, visualise with bar graph
    """
    # Momentum equation for a single ticker, given 1y series of close prices (12 close prices)
    mom = lambda ser: ((ser.iloc[-2] - ser.iloc[0]) / ser.iloc[0]) * 100
    m1_ret = lambda ser: ((ser.iloc[-1] - ser.iloc[-2]) / ser.iloc[-2]) * 100

    # Modify the {tickername: tickerobj} dict to hold series of close prices as values instead
    for security in securities:
        ticker = stocks[security]
        stocks[security] = ticker.history(period = f"1y", end = today_date, interval = "1mo")["Close"]

    momentums = [mom(stocks[security]) for security in securities]
    next_month_returns = [m1_ret(stocks[security]) for security in securities]

    mom_pairs = sorted(zip(momentums, securities), key=lambda x: x[0], reverse=False)
    momentum_sorted = [pair[0] for pair in mom_pairs]
    momentum_labels = [pair[1] for pair in mom_pairs]

    return_pairs = sorted(zip(next_month_returns, securities), key=lambda x: x[0], reverse=False)
    return_sorted = [pair[0] for pair in return_pairs]
    return_labels = [pair[1] for pair in return_pairs]

    momentum_rank = {security: rank + 1 for rank, (_, security) in enumerate(mom_pairs)}
    return_rank = {security: rank + 1 for rank, (_, security) in enumerate(return_pairs)}
    return_values = {security: m1_ret(stocks[security]) for security in securities}
    for security in securities:
        print(f'{security}: Momentum ranking: {momentum_rank[security]}, Return Ranking: {return_rank[security]}')
    
    # Simulate performance of momentum factor using
    abs_ret, rel_ret = long_short_portfolio(momentum_rank, return_values)
    print(f"Portfolio value in the next month is: {abs_ret}.\nReturns are: {round(rel_ret, 3)}%")

    # Plot
    fig, (plot, plot2) = plt.subplots(2, 1, figsize = (12,10))

    bars = plot.bar(momentum_labels, momentum_sorted, color='salmon')
    plot.set_title(f'12-2 Momentum upto {today_date.strftime('%d/%m/%y')}')
    plot.set_ylabel('Percentage Momentum')
    plot.bar_label(bars, padding=3)
    plot.set_ylim(min(momentums) - 50, max(momentums) * 1.1)

    bars2 = plot2.bar(return_labels, return_sorted, color='skyblue')
    plot2.set_title(f'Final month return')
    plot2.set_ylabel('Percentage 1-month returns')
    plot2.bar_label(bars2, padding=3)
    plot2.set_ylim(min(next_month_returns) - 10, max(next_month_returns) * 1.1)


    plt.tight_layout()
    plt.show()

def value_quality_factors():
    """
    Building on the Long-Short portfolio work from the last task, this task uses both value and quality as factors deciding which positions to take for my 20-stock portfolio.
    Both factors are constructed with more information this time:
    The P/B and P/E ratios of the company combine to form a composite value factor
    The ROE and Gross Margin of the company combine to form a composite quality factor

    Factor construction:
    * Standardise ratios such that `higher` indicates `stronger signal for returns` --> Invert P/E and P/B

    Weighting of stocks:
    * Same as before, using ranking system
    * As each factor uses 2 statistics, factor weight = mean(statistic 1 weight, statistic 2 weight)
    """
    # Modify the {tickername: tickerobj} dict: `stocks`
    for security in securities:
        ticker = stocks[security]
        stocks[security] = {"P/E": 1, "P/B": 1, "ROE": 1, "Gross Margin": 1}

if __name__ == '__main__':
    momentum_ranking()
