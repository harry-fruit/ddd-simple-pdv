from domain.entities.product_category_entity import ProductCategory
from shared.domain.entity import Entity
from uuid import UUID


class ProductType(Entity):
    """A Domain Entity representing a Product Type in the system."""

    def __init__(
            self, 
            product_type_id: UUID,
            unique_key: str, 
            name: str, 
            product_category: ProductCategory, 
        ):
        self.product_type_id = product_type_id
        self.product_category = product_category
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"ProductType(product_type_id={self.product_type_id}, name={self.name}, unique_key={self.unique_key}, product_category={self.product_category})"