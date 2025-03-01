from contexts.catalog.domain.value_objects.price import Price
from infrastructure.models.alchemy.product_model import ProductModelSQLAlchemy
from contexts.catalog.domain.entities.product_entity import Product

class ProductMapper:
    """Converts between SQLAlchemy models and Domain Entities."""
    
    @staticmethod
    def to_domain(model: ProductModelSQLAlchemy) -> Product:
        """Convert DB model to a domain entity."""
        return Product(
            product_id=model.id,
            name=model.name,
            price=Price(model.price_amount, model.price_currency)
        )

    @staticmethod
    def to_persistence(entity: Product) -> ProductModelSQLAlchemy:
        """Convert a domain entity to a DB model."""
        return ProductModelSQLAlchemy(
            id=entity.product_id,
            name=entity.name,
            price_amount=entity.price.amount,
            price_currency=entity.price.currency
        )
