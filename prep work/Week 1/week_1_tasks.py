import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math


# simple vs log returns
def simple_vs_log():
    """
    This script is a quick consolidation of the first two days' work: pulling AAPL stock prices for the past 5 years and comparing daily simple vs log returns
    Note that within the range of Apple's simple returns, which is very close to 0, the simple returns, r, and log returns, ln(1+r), have very similar values
    """
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period = "5y", end = "2026-06-01", interval = "1d") # pandas dataframe

    # Plot the data as a histogram
    close_prices = data["Close"]
    simple_ret = []
    log_ret = []

    # Returns calculated by comparing inter-day closing price:
    for i in range(len(close_prices)-1):
        simple_ret.append((close_prices.iloc[i+1] - close_prices.iloc[i]) / close_prices.iloc[i])
        log_ret.append(math.log(close_prices.iloc[i+1] / close_prices.iloc[i]))

    print(simple_ret[:4], log_ret[:4]) # Print first 5 values

    # Create the histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.hist(simple_ret, bins=20, edgecolor='black', label = "Simple Returns")
    ax1.set_xlabel('Values')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Simple Returns')
    ax1.grid(True)

    ax2.hist(log_ret, bins=20, edgecolor='black', label = "Log Returns")
    ax2.set_xlabel('Values')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Log Returns')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def spread_and_liquidity():
    """
    Here we compare liquidity to spread; it is said that they have an inverse relationship. We quantify liquidity by the volume traded that day, spread is given
    """
    tickers = ['AAPL', 'MGNI', 'SLV']
    for name in tickers:
        ticker = yf.Ticker(name)
        dic = ticker.info
        bid = dic.get("bid", "NA")
        ask = dic.get("ask", "NA")
        price = dic.get("regularMarketPrice", "NA")
        volume = dic.get("volume", "NA")
        print(f"ticker: {name}\n\nbid: {bid}\nask: {ask}\nvolume: {volume}")
        if bid != "NA" and ask != "NA" and price != "NA":
            spread = ask - bid
            rel_spread = spread / price
            print(f"abs spread: {spread}\nspread relative to price: {round(rel_spread * 100, 3)}%")
        else:
            print("Couldn't retrive enough info")

def metrics(period = 12, disp = False):
    """
    If disp, create html view of dashboard, else output in terminal. 
    Sampled in monthly intervals, period is the overall time period, in months
    """
    tickers = ['AAPL']
    for name in tickers:
        ticker = yf.Ticker(name)
        data = ticker.history(period = f"{period}mo", end = "2026-06-01", interval = "1d")
        ANNUALISATION_FACTOR = 252 / (len(data) - 1) # no. of trading days / no. of days measured

        ann_vol = round(data['Volume'].sum() * ANNUALISATION_FACTOR, 2) # sum of daily volumes * annualisation factor
        close = data['Close']
        ann_return = round(((close.iloc[-1] - close.iloc[0]) / close.iloc[0])* 100 * ANNUALISATION_FACTOR, 2) # total return over the period measured * ann factor

        # for max drawdown, we look for the minimum price before a new peak
        max_drawdown = 0
        for price in close:
            peak = close.iloc[0]
            if price >= peak:
                peak = price
            drawdown = ((peak - price) / peak) * 100
            if drawdown > max_drawdown:
                max_drawdown = round(drawdown, 2)

        PE = round(ticker.info.get('currentPrice') / ticker.info.get("trailingEps"), 2) #PE ratio. Trailing EPS uses earnings over the past 12 month period

        ex_returns = np.array([((close.iloc[i] - close.iloc[i-1]) / close.iloc[i])*100 - (5/252) for i in range(1, len(close))])
        sharpe = round((np.mean(ex_returns) / np.std(ex_returns)) * np.sqrt(252), 2) # multiply by sqrt of number of periods in a year

        print(f'ann_vol = {ann_vol}\nann_return = {ann_return}\nmax_drawdown = {max_drawdown}\nPE = {PE}\nsharpe = {sharpe}')



def metrics_dashboard():
    pass

if __name__ == "__main__":
    metrics(period = 12)