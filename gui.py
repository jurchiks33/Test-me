# gui.py
import tkinter as tk
from tkinter import ttk
from data_fetching import fetch_stock_data
from strategy import calculate_signals, apply_stop_loss_take_profit
from backtesting import backtest
from ml_optimization import optimize_strategy
