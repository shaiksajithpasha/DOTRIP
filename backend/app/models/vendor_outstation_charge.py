from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorOutstationCharge(Base):
    __tablename__ = "vendor_outstation_charges"
    __table_args__ = (
        UniqueConstraint("vendorId", "vehicleTypeId", "rangeKey", name="uq_vendor_outstation_charge_range"),
        Index("ix_vendor_outstation_charge_vendor_vehicle", "vendorId", "vehicleTypeId"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    rangeKey: Mapped[str] = mapped_column(String(100), default="ALL", nullable=False)
    startDate: Mapped[datetime | None] = mapped_column(DateTime)
    endDate: Mapped[datetime | None] = mapped_column(DateTime)
    amount: Mapped[float] = mapped_column(Float, default=0, nullable=False)
