import uuid
from domain.entities.product_entity import Product
from shared.either import Either, Success, Failure
from shared.errors.unexpected_error import UnexpectedError

Response = Either[None, BaseException]

class Cart:
    """A Domain Entity representing a Cart in the system."""

    def __init__(self, id: uuid.UUID, customer_id: uuid.UUID, products: list[Product] = []):
        self.id = id
        self.customer_id = customer_id
        self.products = products

    def add_product(self, product: Product) -> Response:
        """Business rule to add a product to the cart."""
        try:
            self.products.append(product)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def remove_product(self, product: Product) -> Response:
        """Business rule to remove a product from the cart."""
        try:
            self.products.remove(product)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def __repr__(self):
        return f"Cart(id={self.id}, customer_id={self.customer_id}, products={self.products})"