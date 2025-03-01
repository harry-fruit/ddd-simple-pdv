class Price:
    """A Value Object representing a price amount in a given currency."""
    
    def __init__(self, amount: float, currency: str = "USD"):
        if amount < 0:
            raise ValueError("Price cannot be negative")
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    # def __eq__(self, other):
    #     return isinstance(other, Price) and self.amount == other.amount and self.currency == other.currency
