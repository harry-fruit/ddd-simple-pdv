from domain.entities.product_entity import Product
from uuid import UUID

class OrderItem:
    def __init__(self, order_item_id: UUID, order_id: UUID, product: Product, quantity: int, price: float):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.price = price

    def change_quantity(self, new_quantity: int):
        """Business rule to update quantity."""
        self.quantity = new_quantity

    def __repr__(self):
        return f"OrderItem(order_item_id={self.order_item_id}, product={self.product}, quantity={self.quantity})"