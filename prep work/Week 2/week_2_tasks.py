import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math

def cross_sectional_returns():
    """
    Over a period of one year, compare 20 different S&P 500 securities by their monthly returns
    For each security, we graph its average monthly return, and separately, its return volatility (stdev) 
    """
    securities = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "AVGO", "GOOG", "META", "TSLA", "MU", "JPM", "LLY", "AMD", "XOM", "WMT", "INTC", "JNJ", "V", "COST"]
    sec_names = " ".join([security for security in securities])

    avg_log_ret = lambda ser: (np.log(ser / ser.shift(1)).dropna()).mean()
    ret_stdev = lambda ser: (np.log(ser / ser.shift(1)).dropna()).std(ddof = 0)

    stocks = yf.Tickers(sec_names).tickers
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

def momentum_ranking():
    """
    An introduction to factor investing using momentum: 
    Rank the 20 stocks from the previous task based on their 12-2 Momentum values, visualise with bar graph
    """
    pass

if __name__ == '__main__':
    cross_sectional_returns()
