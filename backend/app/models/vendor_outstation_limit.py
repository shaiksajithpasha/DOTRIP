from sqlalchemy import ForeignKey, Integer, String, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorOutstationLimit(Base):
    __tablename__ = "vendor_outstation_limits"
    __table_args__ = (Index("ix_vendor_outstation_limit_vendor_vehicle", "vendorId", "vehicleTypeId"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    km: Mapped[int] = mapped_column(Integer, nullable=False)
