import yfinance as yf
import matplotlib.pyplot as plt
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
            print("Couldn't retrive eenough info")


if __name__ == "__main__":
    spread_and_liquidity()