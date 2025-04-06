from shared.domain.repository import Repository
from entities.cart_entity import Cart
from uuid import UUID

class CartRepository(Repository[Cart, UUID]):
    """A Repository interface for Cart Entities."""
    pass
