from sqlalchemy import Float, ForeignKey, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorPermitCost(Base):
    __tablename__ = "vendor_permit_costs"
    __table_args__ = (
        UniqueConstraint("vendorId", "vehicleTypeId", "sourceState", "destState", name="uq_vendor_permit_cost"),
        Index("ix_vendor_permit_cost_vendor_vehicle", "vendorId", "vehicleTypeId"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)
    sourceState: Mapped[str] = mapped_column(String(20), nullable=False)
    destState: Mapped[str] = mapped_column(String(20), nullable=False)
    amount: Mapped[float] = mapped_column(Float, default=0, nullable=False)
