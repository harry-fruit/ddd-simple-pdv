from domain.value_objects.price import Price

class Product:
    """A Domain Entity representing a Product in the system."""

    def __init__(self, product_id: int, name: str, price: Price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def change_price(self, new_price: Price):
        """Business rule to update price."""
        self.price = new_price

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price})"