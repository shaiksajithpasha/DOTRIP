from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class DriverUpdate(Base):
    __tablename__ = "driver_updates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    driverId: Mapped[int] = mapped_column(ForeignKey("drivers.id"), nullable=False)
    tripId: Mapped[int] = mapped_column(ForeignKey("trips.id"), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    statusMessage: Mapped[str] = mapped_column(String(500), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
