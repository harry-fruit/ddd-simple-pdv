from domain.entities.order_item_entity import OrderItem
from shared.either import Either, Success, Failure
from shared.errors.unexpected_error import UnexpectedError

Response = Either[None, BaseException]

class Order:
    """A Domain Entity representing an Order in the system."""

    def __init__(
            self, 
            order_id: int, 
            customer_id: int, 
            product_id: int, 
            quantity: int, 
            price: float,
            order_items: list[OrderItem]
        ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.order_items = order_items

    def add_order_item(self, order_item: OrderItem) -> Response:
        """Business rule to add an order item to the order."""
        try:
            self.order_items.append(order_item)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def remove_order_item(self, order_item: OrderItem) -> Response:
        """Business rule to remove an order item from the order."""
        try:
            self.order_items.remove(order_item)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def __repr__(self):
        return f"Order(id={self.order_id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity}, price={self.price})"