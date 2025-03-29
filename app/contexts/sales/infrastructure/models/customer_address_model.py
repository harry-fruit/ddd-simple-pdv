from uuid import UUID
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

class CustomerAddress(Base):
    __tablename__ = "customer_address"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    city: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    state: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    zip_code: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    country: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    complement: Mapped[str] = mapped_column(type_=String(30))
    address: Mapped[str] = mapped_column(type_=String(30), nullable=True)

    def __repr__(self) -> str:
        return f"CustomerAddress(id={self.id!r}, number={self.number!r}, city={self.city!r}, state={self.state!r}, zip_code={self.zip_code!r}, country={self.country!r}, complement={self.complement!r}, address={self.address!r})"