from abc import ABC, abstractmethod
from domain.entities.product_entity import Product
from shared.either import Either

class IProductRepository(ABC):
    """Interface for ProductRepository"""

    @abstractmethod
    def add(self, product: Product) -> Either[Product, Exception]:
        """Add a new product"""
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Either[Product | None, Exception]:
        """Retrieve a product by ID"""
        pass

    @abstractmethod
    def get_all(self) -> Either[list[Product], Exception]:
        """Retrieve all products"""
        pass

    @abstractmethod
    def update(self, product: Product) -> Either[Product, Exception]:
        """Update a product"""
        pass

    @abstractmethod
    def delete(self, product_id: int) -> Either[bool, Exception]:
        """Delete a product"""
        pass
