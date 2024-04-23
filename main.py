import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

# Fetching stock data from Yahoo Finance
def fetch_stock_data(ticker, start_date, end_date):
    stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    return stock

# Ask the user to input the ticker symbol they wish to view
ticker_symbol = str(input("Which stock would you like to view? (Please enter the ticker symbol): "))

# Download stock data
yf.pdr_override() 

# Define the start and end dates for the data
start_date = input("Please enter a start date in YYYY-MM-DD format: ") # ex. 2023-01-01
end_date = input("Please enter an end date in YYYY-MM-DD format: ")

# Fetch the data
stock_data = fetch_stock_data(ticker_symbol, start_date, end_date)

# Creating the plot
plt.figure(figsize=(12, 8))
plt.title("Data Visualization - {}".format(ticker_symbol))

# Plotting Closing Prices
plt.subplot(2, 1, 1)
plt.plot(stock_data['Close'], label='Closing Data', color='blue')
plt.title("Closing Price for {}".format(ticker_symbol))
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()

# Plotting Volume
plt.subplot(2, 1, 2)
plt.bar(stock_data.index, stock_data['Volume'], label='Volume Data', color='green', alpha=0.7)
plt.title("Volume of {} shares traded".format(ticker_symbol))
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid(True)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
