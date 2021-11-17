class Portfolio:
    def __init__(self):
        self._stocks = []
    
    def buy(self, name, shares, price):
        if shares <= 0:
            raise ValueError("Shares cannot be negative!")
        self._stocks.append((name, shares, price))

    def cost(self):
        return sum(
            shares * price for name, shares, price in self._stocks
        )
