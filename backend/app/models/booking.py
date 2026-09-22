from datetime import date, time, datetime
from sqlalchemy import Boolean, Date, DateTime, Float, ForeignKey, Integer, String, Time, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    pickupAddressId: Mapped[int] = mapped_column(ForeignKey("address_books.id"), nullable=False)
    dropAddressId: Mapped[int] = mapped_column(ForeignKey("address_books.id"), nullable=False)

    pickupDate: Mapped[date | None] = mapped_column(Date)
    pickupTime: Mapped[time | None] = mapped_column(Time(0))
    returnDate: Mapped[date | None] = mapped_column(Date)
    returnTime: Mapped[time | None] = mapped_column(Time(0))

    fromCityId: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    toCityId: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    tripTypeId: Mapped[int] = mapped_column(ForeignKey("trip_types.id"), nullable=False)
    fare: Mapped[float] = mapped_column(Float, nullable=False)
    numPersons: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    numVehicles: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    bookingType: Mapped[str] = mapped_column(String(50), default="individual", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="PENDING", nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    vendorId: Mapped[int | None] = mapped_column(ForeignKey("vendors.id"))
