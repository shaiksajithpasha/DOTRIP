from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Trip(Base):
    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bookingId: Mapped[int] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    riderId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    driverId: Mapped[int] = mapped_column(ForeignKey("drivers.id"), nullable=False)
    vehicleId: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    corporateBookingId: Mapped[int | None] = mapped_column(Integer)
    startTime: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    endTime: Mapped[datetime | None] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(50), default="ONGOING", nullable=False)
    distance: Mapped[float | None] = mapped_column(Float)
    fare: Mapped[float | None] = mapped_column(Float)
    breakdownReported: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    breakdownNotes: Mapped[str | None] = mapped_column(String(1000))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
