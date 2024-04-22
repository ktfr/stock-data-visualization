import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

#Ask the user to input the ticker symbol they wish to view
ticker_symbol = str(input("Which stock would you like to view? (Please enter the ticker symbol): "))

# Download stock data
yf.pdr_override() 

# Define the start and end dates for the data
start_date = str(input("Please enter a start date in YYYY-MM-DD format: ")) # ex. 2023-01-01
end_date = str(input("Please enter an end date in YYYY-MM-DD format: "))

# Fetch the data
stock_data = pdr.get_data_yahoo(ticker_symbol, start=start_date, end=end_date)

# Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')

# Add title and labels
plt.title(ticker_symbol + "Data Visualization - {}".format(ticker_symbol))
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()

# Show plot
plt.grid(True)
plt.show()
