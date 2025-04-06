from shared.domain.repository import Repository
from entities.product_category_entity import ProductCategory
from uuid import UUID

class ProductCategoryRepository(Repository[ProductCategory, UUID]):
    """A Repository interface for ProductCategory Entities."""
    pass