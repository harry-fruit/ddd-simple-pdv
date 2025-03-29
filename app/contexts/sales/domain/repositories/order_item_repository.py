from shared.domain.repository import Repository
from entities.order_item_entity import OrderItem
from uuid import UUID

class OrderItemRepository(Repository[OrderItem, UUID]):
    """A Repository interface for OrderItem Entities."""
    pass