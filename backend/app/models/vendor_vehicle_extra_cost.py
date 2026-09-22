from sqlalchemy import Float, ForeignKey, Integer, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorVehicleExtraCost(Base):
    __tablename__ = "vendor_vehicle_extra_costs"
    __table_args__ = (
        UniqueConstraint("vendorId", "vehicleTypeId", name="uq_vendor_vehicle_extra_cost"),
        Index("ix_vendor_vehicle_extra_cost_vendor", "vendorId"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    extraKm: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    extraHour: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    earlyMorning: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    evening: Mapped[float] = mapped_column(Float, default=0, nullable=False)
