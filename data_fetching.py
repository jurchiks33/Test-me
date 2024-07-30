# data_fetching.py
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end = end_date)
    stock_data.reset_index(inplace=True)
    return stock_data

if __name__ == "__main__":
    df = fetch_stock_data('AAPL', '2022-01-01', '2023-01-01')
    print(df.head())