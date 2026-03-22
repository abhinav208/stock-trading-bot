import yfinance as yf
import requests
import pandas as pd

class DataCollector:
    def __init__(self, symbol):
        self.symbol = symbol

    def collect_yfinance_data(self):
        # Collect data from Yahoo Finance
        stock_data = yf.download(self.symbol, period='1mo')
        return stock_data

    def collect_alpha_vantage_data(self, api_key):
        # Collect data from Alpha Vantage
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.symbol}&apikey={api_key}&outputsize=compact'
        response = requests.get(url)
        data = response.json()
        return data

# Example usage:
# collector = DataCollector('AAPL')
# yahoo_data = collector.collect_yfinance_data()
# alpha_vantage_data = collector.collect_alpha_vantage_data('YOUR_API_KEY')