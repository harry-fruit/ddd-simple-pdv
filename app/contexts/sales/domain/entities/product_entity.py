from domain.value_objects.price import Price
from domain.entities.product_category_entity import ProductCategory
from domain.entities.product_type_entity import ProductType
from domain.entities.brand_entity import Brand
from shared.domain.entity import Entity
import uuid

class Product(Entity):
    """A Domain Entity representing a Product in the system."""

    def __init__(
            self, 
            id: uuid.UUID,
            name: str, 
            description: str,
            price: Price,
            product_category: ProductCategory,
            product_type: ProductType,
            brand: Brand,
        ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.product_category = product_category
        self.product_type = product_type
        self.brand = brand

    def change_price(self, new_price: Price):
        """Business rule to update price."""
        self.price = new_price

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"