from shared.domain.repository import Repository
from entities.product_type_entity import ProductType
from uuid import UUID

class ProductTypeRepository(Repository[ProductType, UUID]):
    """A Repository interface for ProductType Entities."""
    pass