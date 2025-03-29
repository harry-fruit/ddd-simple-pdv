from domain.entities.product_category_entity import ProductCategory
from shared.domain.entity import Entity
import uuid


class ProductType(Entity):
    """A Domain Entity representing a Product Type in the system."""

    def __init__(
            self, 
            id: uuid.UUID,
            unique_key: str, 
            name: str, 
            product_category: ProductCategory, 
        ):
        self.id = id
        self.product_category = product_category
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"ProductType(id={self.id}, name={self.name}, unique_key={self.unique_key}, product_category={self.product_category})"