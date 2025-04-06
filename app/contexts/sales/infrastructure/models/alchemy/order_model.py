from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID
from db.database import Base
from typing import List
from sqlalchemy.orm import relationship
from models.alchemy.order_item_model import OrderItemAlchemyModel


class OrderAlchemyModel(Base):
    __tablename__ = "order"

    order_id: Mapped[UUID] = mapped_column(primary_key=True)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customer.customer_id"))
    price: Mapped[float] = mapped_column(type_=Float, nullable=False)
    order_items: Mapped[List[OrderItemAlchemyModel]] = relationship(
        back_populates="order", cascade="all"
    )

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id!r}, customer_id={self.customer_id!r}, price={self.price!r})"