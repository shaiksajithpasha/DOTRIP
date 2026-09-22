from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tripId: Mapped[int] = mapped_column(ForeignKey("trips.id"), unique=True, nullable=False)
    riderId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    driverId: Mapped[int | None] = mapped_column(ForeignKey("drivers.id"))
    driverRating: Mapped[int] = mapped_column(Integer, nullable=False)
    vehicleRating: Mapped[int] = mapped_column(Integer, nullable=False)
    serviceRating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(String(2000), nullable=False)
    feedbackTime: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.now())
