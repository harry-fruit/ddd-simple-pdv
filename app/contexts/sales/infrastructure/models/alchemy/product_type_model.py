from uuid import UUID
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String
from models.alchemy.product_category_model import ProductCategoryAlchemyModel

class ProductTypeAlchemyModel(Base): 
    __tablename__ = "product_type"

    product_type_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    unique_key: Mapped[str] = mapped_column(
        type_=String(50), 
        nullable=False, 
        unique=True
    )

    product_category_id: Mapped[int] = mapped_column(ForeignKey("product_category.product_category_id"))
    product_category: Mapped[ProductCategoryAlchemyModel] = relationship(back_populates="product_type")

    def __repr__(self) -> str:
        return f"ProductType(id={self.product_type_id!r}, product_category_id={self.product_category_id!r}, name={self.name!r}, fullname={self.unique_key!r})"