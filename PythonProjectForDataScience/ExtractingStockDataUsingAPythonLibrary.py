import yfinance as yf                        # it allows to download historical market data from "Yahoo! Finance"
import pandas as pd
import matplotlib.pyplot as plt

# Input from user for ticker symbol
ticker_symbol = input("Enter the ticker symbol (e.g., AAPL, MSFT, GOOGL): ").upper()

# Create an instance of the yf.Ticker class and associate it with the given ticker symbol
stock = yf.Ticker(ticker_symbol)

# The info attribute gives a live overview of key financial metrics and company details
stock_info = stock.info

"""
Alternative approach to obtain stock info from a JSON file:
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json
import json
with open('stock_data.json') as json_file:
    stock_info = json.load(json_file)
# This approach downloads the entire web page but loses the live feature
"""

print(f"Stock Info Details: {stock_info}")              # it displays all the stock info as a dictionary

# Get the complete history of the share price as a pandas DataFrame
stock_share_price_data = stock.history(period="max")

print(f"Example of share price history: \n{stock_share_price_data.head()}")

# Reset index to make "Date" a normal column instead of index
# The parameter inplace=True makes this change directly on the current DataFrame
stock_share_price_data.reset_index(inplace=True)

# Plotting the time series
stock_share_price_data.plot(x="Date", y="Open")
plt.title(f"{ticker_symbol} Stock Price History")
plt.xlabel("Date")
plt.ylabel("Opening Price (USD)")
plt.show()