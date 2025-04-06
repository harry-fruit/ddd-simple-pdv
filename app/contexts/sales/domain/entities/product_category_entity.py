from shared.domain.entity import Entity
from uuid import UUID


class ProductCategory(Entity):
    """A Domain Entity representing a Product Category in the system."""

    def __init__(self, product_category_id: UUID, unique_key: str, name: str):
        self.product_category_id = product_category_id
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"ProductCategory(product_category_id={self.product_category_id}, name={self.name}, unique_key={self.unique_key})"