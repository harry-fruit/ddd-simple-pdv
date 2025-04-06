from uuid import UUID
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String
from typing import List
from sqlalchemy.orm import relationship
from models.alchemy.customer_address_model import CustomerAddressAlchemyModel


class CustomerAlchemyModel(Base):
    __tablename__ = "customer"

    customer_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.user_id"))
    customer_address: Mapped[List[CustomerAddressAlchemyModel]] = relationship(
        back_populates="product_category", cascade="all"
    )

    def __repr__(self) -> str:
        return f"Customer(id={self.customer_id!r}, name={self.name!r})"