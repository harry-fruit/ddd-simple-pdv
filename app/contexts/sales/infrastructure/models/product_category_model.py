from uuid import UUID
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from typing import List
from sqlalchemy.orm import relationship
from models.product_type_model import ProductType

class ProductCategory(Base):
    __tablename__ = "product_category"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    unique_key: Mapped[str] = mapped_column(
        type_=String(50), 
        nullable=False, 
        unique=True
    )

    product_type: Mapped[List[ProductType]] = relationship(
        back_populates="product_category", cascade="all"
    )

    def __repr__(self) -> str:
        return f"ProductCategory(id={self.id!r}, name={self.name!r}, fullname={self.unique_key!r})"