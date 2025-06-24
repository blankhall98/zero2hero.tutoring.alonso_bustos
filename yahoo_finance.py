#yahoo_finance.py

#import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data = yf.download(
    tickers=['AAPL','MSFT'],           # Single ticker or list
    start='2020-01-01',       # Start date (YYYY-MM-DD)
    end='2025-01-01',         # End date (exclusive)
    progress=True             # Show progress bar
)

tesla = yf.Ticker("TSLA").history(period="max")
ford = yf.Ticker("F").history(period="max")

#graph Open
plt.figure()
plt.title("Stock Comparison")
tesla['Open'].plot(label="Tesla")
ford['Open'].plot(label="Ford")
plt.legend()
plt.show()

#Class: Stock Analysis

class Analysis:
    
    def __init__(self):
        print('app is active!')
        self.stocks = {}
        
    def load_stock(self,tick):
        self.stocks[tick] = yf.Ticker(tick).history(period='1y')
        
    def calculate_returns(self):
        for tick in self.stocks.keys():
            self.stocks[tick]['Returns'] = self.stocks[tick]['Close'].pct_change()
        
    def graph(self,value):
        plt.figure()
        plt.title("Stock Comparison")
        for tick in self.stocks.keys():
            self.stocks[tick][value].plot(label=tick)
        plt.legend()
        plt.show()
        

        
    