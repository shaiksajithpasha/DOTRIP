from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class DriverCostDetails(Base):
    __tablename__ = "driver_cost_details"

    driverId: Mapped[int] = mapped_column(ForeignKey("drivers.id", ondelete="CASCADE"), primary_key=True)
    driverSalary: Mapped[float | None] = mapped_column(Float, default=0)
    foodCost: Mapped[float | None] = mapped_column(Float, default=0)
    accommodationCost: Mapped[float | None] = mapped_column(Float, default=0)
    bhattaCost: Mapped[float | None] = mapped_column(Float, default=0)
    earlyMorningCharges: Mapped[float | None] = mapped_column(Float, default=0)
    eveningCharges: Mapped[float | None] = mapped_column(Float, default=0)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
