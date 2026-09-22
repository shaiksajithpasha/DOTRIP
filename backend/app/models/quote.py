from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bookingId: Mapped[int] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    approved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
