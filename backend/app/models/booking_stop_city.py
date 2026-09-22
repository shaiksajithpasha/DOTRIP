from sqlalchemy import Column, ForeignKey, Integer, Table
from app.database import Base

booking_stop_cities = Table(
    "booking_stop_cities",
    Base.metadata,
    Column("bookingId", Integer, ForeignKey("bookings.id", ondelete="CASCADE"), primary_key=True),
    Column("cityId", Integer, ForeignKey("cities.id", ondelete="CASCADE"), primary_key=True),
)
