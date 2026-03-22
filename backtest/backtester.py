import pandas as pd
import numpy as np

class Backtester:
    def __init__(self, historical_data):
        self.historical_data = historical_data
        self.results = None

    def run_backtest(self, strategy_func):
        self.results = strategy_func(self.historical_data)

    def get_results(self):
        return self.results

# Example of a simple strategy function
# def simple_moving_average_strategy(historical_data):
#     signals = pd.Series(index=historical_data.index)
#     signals['signal'] = 0
#     signals['signal'][period:] = np.where(historical_data['close'][period:] > historical_data['close'].rolling(window=period).mean(), 1, 0)
#     return signals

# Sample usage:
# historical_data = pd.read_csv('data.csv', index_col='date', parse_dates=True)
# backtester = Backtester(historical_data)
# backtester.run_backtest(simple_moving_average_strategy)
# results = backtester.get_results()