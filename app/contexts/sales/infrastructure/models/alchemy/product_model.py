from db.database import Base
from models.alchemy.order_item_model import OrderItemAlchemyModel
from sqlalchemy.orm import mapped_column, Mapped
from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Float
from uuid import UUID

class ProductAlchemyModel(Base):
    __tablename__ = "product"

    product_id: Mapped[UUID] = mapped_column(primary_key=True)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customer.customer_id"))
    price: Mapped[float] = mapped_column(type_=Float, nullable=False)
    order_item: Mapped[List[OrderItemAlchemyModel]] = relationship(
        back_populates="product", cascade="all"
    )

    def __repr__(self) -> str:
        return f"Product(id={self.product_id!r}, customer_id={self.customer_id!r}, price={self.price!r})"