# gui.py
import tkinter as tk
from tkinter import ttk
from data_fetching import fetch_stock_data
from strategy import calculate_signals, apply_stop_loss_take_profit
from backtesting import backtest
from ml_optimization import optimize_strategy

class TradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trading Strategy Tester")

        # Ticker input
        tk.Label(root, text="Ticker"). grid(row=0, column=0)
        self.ticker_entry = tk.Entry(root)
        self.ticker_entry.grid(row=0, column=1)

        # Strategy Selection
        tk.Label(root, text="Strategy").grid(row=1, column=0)
        self.strategy_combobox = ttk.Combobox(root, values=["Strategy 1", "Strategy 2"])
        self.strategy_combobox.grid(row=1, column=1)

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.grid(row=2, column=1)

    def start(self):
        ticker = self.ticker_entry.get()
        strategy = self.strategy_combobox.get()

        # Data fetching
        df = fetch_stock_data(ticker, '2022-01-01', '2023-01-01')
        df = calculate_signals(df)
        df = apply_stop_loss_take_profit(df, 0.10, 0.30)

        # Backtesting and optimization.
        final_balance = backtest(df)
        best_params = optimize_strategy(df)

        print(f"Final Balance: ${final_balance}")
        print(f"Best parameters: {best_params}")