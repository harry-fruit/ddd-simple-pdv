import uuid
from domain.entities.product_entity import Product

class OrderItem:

    def __init__(self, id: uuid.UUID, product: Product, quantity: int, price: float):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price

    def change_quantity(self, new_quantity: int):
        """Business rule to update quantity."""
        self.quantity = new_quantity

    def __repr__(self):
        return f"OrderItem(id={self.id}, product={self.product}, quantity={self.quantity})"