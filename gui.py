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

        