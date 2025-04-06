from sqlalchemy import Float, ForeignKey, Integer
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID

class OrderItemAlchemyModel(Base):
    __tablename__ = "order_item"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    order_id: Mapped[UUID] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    price: Mapped[float] = mapped_column(type_=Float, nullable=False)
    