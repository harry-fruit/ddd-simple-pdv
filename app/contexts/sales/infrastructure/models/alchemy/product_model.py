# # db/models.py
# from sqlalchemy import Column, Integer, String
# from db.database import Base
# from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
# from typing import List

# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship
# from uuid import UUID

# class User(Base):
#     __tablename__ = "product"

#     id: Mapped[UUID] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]

#     addresses: Mapped[list["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )

#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"