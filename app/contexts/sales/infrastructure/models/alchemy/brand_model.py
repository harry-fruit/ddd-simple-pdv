from sqlalchemy import String
from db.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID

class BrandAlchemyModel(Base):
    __tablename__ = "brand"

    brand_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=String(30), nullable=True)
    unique_key: Mapped[str] = mapped_column(
        type_=String(50), 
        nullable=False, 
        unique=True
    )

    def __repr__(self) -> str:
        return f"Brand(id={self.brand_id!r}, name={self.name!r}, fullname={self.unique_key!r})"