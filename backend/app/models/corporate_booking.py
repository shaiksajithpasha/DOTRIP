from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class CorporateBooking(Base):
    __tablename__ = "corporate_bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bookingId: Mapped[int | None] = mapped_column(ForeignKey("bookings.id"), unique=True)
    companyName: Mapped[str] = mapped_column(String(255), nullable=False)
    contactPerson: Mapped[str] = mapped_column(String(255), nullable=False)
    contactEmail: Mapped[str] = mapped_column(String(255), nullable=False)
    contactPhone: Mapped[str] = mapped_column(String(50), nullable=False)
    numberOfVehicles: Mapped[str] = mapped_column(String(50), nullable=False)
    estimatedPassengers: Mapped[str] = mapped_column(String(50), nullable=False)
    specialRequirements: Mapped[str | None] = mapped_column(String(1000))
    budgetRange: Mapped[str | None] = mapped_column(String(255))
    notes: Mapped[str | None] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(String(50), default="PENDING", nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
