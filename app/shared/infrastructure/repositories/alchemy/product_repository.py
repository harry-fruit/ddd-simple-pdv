from sqlalchemy.orm import Session
from infrastructure.models.alchemy.product_model import ProductModelSQLAlchemy
from infrastructure.mappers.product.product_mapper import ProductMapper
from contexts.catalog.domain.entities.product_entity import Product
from contexts.catalog.domain.repositories.product_repository import IProductRepository
from contexts.catalog.domain.utils.either import Either, Success, Failure
from infrastructure.error.unexpected import UnexpectedError
from infrastructure.error.not_found import NotFoundError


class ProductRepositorySQLAlchemy(IProductRepository):
    """Repository to handle Product data operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product) -> Either[Product, UnexpectedError]:
        """Save a new product."""
        try:
            model = ProductMapper.to_persistence(product)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return Success(ProductMapper.to_domain(model))
        except Exception as e:
            return Failure(UnexpectedError(e))

    def get_by_id(self, product_id: int) -> Either[Product | None, Exception]:
        """Retrieve a product by ID."""
        try:
            model = self.db.query(ProductModelSQLAlchemy).filter(ProductModelSQLAlchemy.id == product_id).first()
            return Success(ProductMapper.to_domain(model) if model else None)
        
        except Exception as e:
            return Failure(UnexpectedError(e))

    def get_all(self) -> Either[list[Product], Exception]:
        """Retrieve all products."""
        try:
            models = self.db.query(ProductModelSQLAlchemy).all()
            return Success([ProductMapper.to_domain(model) for model in models])
        except Exception as e:
            return Failure(UnexpectedError(e))

    def update(self, product: Product) -> Either[Product, Exception]:
        """Update a product's details."""
        try:
            model = self.db.query(ProductModelSQLAlchemy).filter(ProductModelSQLAlchemy.id == product.product_id).first()
            
            if not model:
                return Failure(NotFoundError("Product", str(product.product_id)))
            
            model.name = product.name
            model.price_amount = product.price.amount
            model.price_currency = product.price.currency
            
            self.db.commit()
            self.db.refresh(model)
            return Success(ProductMapper.to_domain(model))
            
        except Exception as e:
            return Failure(UnexpectedError(e))

    def delete(self, product_id: int) -> Either[bool, Exception]:
        """Delete a product."""

        try:
            model = self.db.query(ProductModelSQLAlchemy).filter(ProductModelSQLAlchemy.id == product_id).first()
            
            if not model:
                return Failure(NotFoundError("Product", str(product_id)))
            
            self.db.delete(model)
            self.db.commit()
            return Success(True)
        except Exception as e:
            return Failure(UnexpectedError(e))
