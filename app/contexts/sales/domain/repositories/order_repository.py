from shared.domain.repository import Repository
from entities.order_entity import Order
from uuid import UUID


class OrderRepository(Repository[Order, UUID]):
    """A Repository interface for Order Entities."""
    pass