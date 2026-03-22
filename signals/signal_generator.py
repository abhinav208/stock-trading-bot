import numpy as np
import pandas as pd
import talib

class SignalGenerator:
    def __init__(self, data):
        self.data = data

    def compute_indicators(self):
        self.data['SMA20'] = talib.SMA(self.data['Close'], timeperiod=20)
        self.data['SMA50'] = talib.SMA(self.data['Close'], timeperiod=50)
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)
        self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    def generate_signals(self):
        signals = []
        for i in range(len(self.data)):
            if (self.data['SMA20'].iloc[i] > self.data['SMA50'].iloc[i]) and (self.data['RSI'].iloc[i] < 30):
                signals.append('Buy')
            elif (self.data['SMA20'].iloc[i] < self.data['SMA50'].iloc[i]) and (self.data['RSI'].iloc[i] > 70):
                signals.append('Sell')
            else:
                signals.append('Hold')
        self.data['Signal'] = signals
        return self.data

# Example usage:
# df = pd.read_csv('your_data.csv')  # Replace with your data source
# generator = SignalGenerator(df)
# generator.compute_indicators()
# signals_df = generator.generate_signals()