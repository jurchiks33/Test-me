# Backtesting.py
import pandas as pd

def backtest(df):
    initial_balance = 10000
    balance = initial_balance
    for index, row in df.iterrows():
        # Trading logic is coming here
        pass
    return balance

if __name__ == '__main__':
    df = pd.read_csv('AAPL_data_with_signals.csv')
    final_balance = backtest(df)
    print(f"Final balance: ${final_balance}")