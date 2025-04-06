from sqlalchemy import Float, ForeignKey, Integer
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID

class OrderItemAlchemyModel(Base):
    __tablename__ = "order_item"

    order_item_id: Mapped[UUID] = mapped_column(primary_key=True)
    order_id: Mapped[UUID] = mapped_column(ForeignKey("order.order_id"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("product.product_id"))
    quantity: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    price: Mapped[float] = mapped_column(type_=Float, nullable=False)

    def __repr__(self) -> str:
        return f"OrderItem(id={self.id!r}, order_id={self.order_id!r}, product_id={self.product_id!r}, quantity={self.quantity!r}, price={self.price!r})"
    