import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math
from datetime import datetime
import pandas as pd

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

def long_short_portfolio(signals: pd.DataFrame, factor_signal_map: dict, test_returns: pd.DataFrame = None):
    """
    ## Purpose
    Simulates a long-short portfolio taking in raw signal values of each security and a key which maps factors to raw signals

    ## Variables:
    * `signals`: `pd.DataFrame`. 
        * Contains all the security info
        * Securities as columns, ColumnName is the Security Name
        * Raw Signal Values as rows, RowName is the Signal Name

    * `factor_signal_map`: `dict`
        * While raw signals are ratios such as P/E or P/B, a factor is a specific characteristic of the security, such as value, quality, or momentum, that we measure using the raw signals
        * Maps the factor name to its constituent signals, e.g. `quality`: ['ROE']
        * Format of map given by: `str`: `list[str]`
        * In case a factor is a composition of multiple signals, the list must contain all those signals. 
        * Signal names must match exactly to the row names in `signals`
        * For any signal name (one of the rows from `signals`) that is not found in `composite_factor_map`, it is treated as an individual factor
    
    ## Functions
    1. Uses raw signal data to rank stocks by raw signal data
    2. Generates Factor weights for each stock
        * If Factor is composed of multiple signals, takes average signal rank and calculates weight
        * Weight is calculated by distance between Factor rank and Average rank, scaled down so that the long and short sides add up to $1 each
    
    ## Current Assumptions
    * Raw signal data is *standardised*, i.e.
        * All raw signal data points higher for better, lower for worse
    * Magnitude of industry-dependent signals are adjusted by industry.
    * Missing / Invalid raw signal information is substituted for the *industry average signal value*
    """

    securities = signals.columns.tolist()
    signal_names = signals.index.tolist()
    print(f'Columns: {securities} \nRows: {signal_names}')
    n = len(securities)   # Just the number of securities

    print(f'raw signal values: \n{signals}')
    # We rank all securities by each raw signal. Create new df `ranks`
    ranks = signals.transform(
        lambda row: row.rank(),
        axis = 1
    )
    print(f'raw signal ranks: \n{ranks}')

    # Create another df `factors` to rank by factor, switching out raw signal name for factor name and aggregating raw signal ranks for any composite factors
    factors = pd.DataFrame(columns=pd.Series(securities))
    for factor in factor_signal_map.keys():
        constituent_signals = factor_signal_map[factor]
        grouped_signal_ranks = ranks.loc[constituent_signals]
        factor_ranks = grouped_signal_ranks.mean(axis = 0)
        factors.loc[factor] = factor_ranks
    print(f'factors: \n{factors}')
    
    # Construct the map from signal ranking --> weights
        # Scaling Factor: The weight for each stock tells us how much of our capital we are putting in that stock.
        # In a portfolio with $1 long and $1 short, the weights on both sides must add up to one respectively, since the total capital on each side is $1
        # Now, the raw weight comes from the difference of the security's ranking from the mean ranking, then,
        # Final weight is raw weight normalised, i.e. divided by sum of all raw weights
    raw_weights = [rank - ((n + 1) / 2) for rank in range(math.ceil(n / 2) + 1, n + 1, 1)]
    scaling_factor = 1 / sum(raw_weights)
    weight = lambda rank: (rank - (n + 1) / 2) * scaling_factor 

    # Create new df `weights`, to hold the final weights by each factor
    weights = factors.transform(
        lambda row: row.apply(weight),
        axis = 1
        )
    print(f'weights: \n{weights}')
    return weights


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
    signals = pd.DataFrame(
        {'Stock1': [3,6,10],
         'Stock2': [1,5,9],
         'Stock3': [2,8,6],
         'Stock4': [4,7,12]},
         index = ['Sig1', 'Sig2', 'Sig3']
    )
    factormap = {
        'Fac1': ['Sig1'],
        'Fac2': ['Sig2', 'Sig3'],
    }
    long_short_portfolio(signals, factormap)
