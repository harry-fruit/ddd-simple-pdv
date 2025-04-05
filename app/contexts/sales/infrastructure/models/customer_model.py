from uuid import UUID
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped

class CustomerAlchemyModel(Base):
    __tablename__ = "customer"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    address