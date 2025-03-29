from shared.domain.repository import Repository
from entities.product_entity import Product
from uuid import UUID

class ProductRepository(Repository[Product, UUID]):
    """A Repository interface for Product Entities."""
    pass