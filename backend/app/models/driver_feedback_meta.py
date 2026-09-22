from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, JSON, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class DriverFeedbackMeta(Base):
    __tablename__ = "driver_feedback_meta"

    driverId: Mapped[int] = mapped_column(ForeignKey("drivers.id", ondelete="CASCADE"), primary_key=True)
    ratingAvg: Mapped[float | None] = mapped_column(Float)
    remarks: Mapped[str | None] = mapped_column(String(1000))
    reviews: Mapped[dict | list | None] = mapped_column(JSON)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
