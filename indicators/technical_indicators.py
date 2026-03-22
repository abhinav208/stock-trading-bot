import numpy as np
import pandas as pd

class TechnicalIndicators:
    def __init__(self, data):
        self.data = data

    def calculate_rsi(self, period=14):
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, short_period=12, long_period=26, signal_period=9):
        short_ema = self.data['Close'].ewm(span=short_period, adjust=False).mean()
        long_ema = self.data['Close'].ewm(span=long_period, adjust=False).mean()
        macd = short_ema - long_ema
        signal = macd.ewm(span=signal_period, adjust=False).mean()
        return macd, signal

    def calculate_bollinger_bands(self, window=20, num_sd=2):
        rolling_mean = self.data['Close'].rolling(window).mean()
        rolling_std = self.data['Close'].rolling(window).std()
        upper_band = rolling_mean + (rolling_std * num_sd)
        lower_band = rolling_mean - (rolling_std * num_sd)
        return upper_band, lower_band

    def calculate_moving_average(self, window=30):
        return self.data['Close'].rolling(window).mean()

    def calculate_stochastic_oscillator(self, k_period=14, d_period=3):
        low_min = self.data['Low'].rolling(window=k_period).min()
        high_max = self.data['High'].rolling(window=k_period).max()
        stoch_k = 100 * ((self.data['Close'] - low_min) / (high_max - low_min))
        stoch_d = stoch_k.rolling(window=d_period).mean()
        return stoch_k, stoch_d
