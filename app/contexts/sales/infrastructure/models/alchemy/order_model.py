from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID
from db.database import Base


class OrderAlchemyModel(Base):
    __tablename__ = "order"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customer.id"))
    price: Mapped[float] = mapped_column(type_=Float, nullable=False)