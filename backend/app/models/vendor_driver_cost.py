from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, UniqueConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorDriverCost(Base):
    __tablename__ = "vendor_driver_costs"
    __table_args__ = (
        UniqueConstraint("vendorId", "vehicleTypeId", name="uq_vendor_driver_cost"),
        Index("ix_vendor_driver_cost_vendor", "vendorId"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    driverBhatta: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    foodCost: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    accomodationCost: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    extraCost: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    morningPerHour: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    eveningPerHour: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
