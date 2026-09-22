from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint, Enum, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from .enums import AddressType

class AddressBook(Base):
    __tablename__ = "address_books"
    __table_args__ = (
        UniqueConstraint("userId", "type", "address", name="uq_address_book_user_type_address"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    type: Mapped[AddressType] = mapped_column(Enum(AddressType, name="address_type_enum"), nullable=False)
    address: Mapped[str | None] = mapped_column(String(500))
    city: Mapped[str | None] = mapped_column(String(255))
    pinCode: Mapped[str | None] = mapped_column(String(20))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
