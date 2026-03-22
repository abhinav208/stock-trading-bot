import datetime

class PortfolioTracker:
    def __init__(self):
        self.positions = {}
        self.trades = []
        self.performance = []

    def add_position(self, symbol, quantity, price):
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity
        self.trades.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'date': datetime.datetime.now()
        })

    def remove_position(self, symbol, quantity):
        if symbol in self.positions:
            self.positions[symbol] -= quantity
            if self.positions[symbol] <= 0:
                del self.positions[symbol]

    def calculate_performance(self):
        # This is just a placeholder for actual performance calculation logic
        total_value = sum([quant * 100 for quant in self.positions.values()])  # Assuming a fixed price of 100 for simplification
        self.performance.append((datetime.datetime.now(), total_value))
        return total_value

    def get_positions(self):
        return self.positions

    def get_trades(self):
        return self.trades

    def get_performance(self):
        return self.performance


# Example usage
# tracker = PortfolioTracker()
# tracker.add_position('AAPL', 10, 150)
# tracker.remove_position('AAPL', 5)
# print(tracker.get_positions())
# print(tracker.calculate_performance())