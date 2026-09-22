from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VendorBranch(Base):
    __tablename__ = "vendor_branches"
    __table_args__ = (
        UniqueConstraint("vendorId", "name", name="uq_vendor_branch_name"),
        Index("ix_vendor_branches_vendorId", "vendorId"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str | None] = mapped_column(String(255))
    primaryMobile: Mapped[str | None] = mapped_column(String(50))
    altMobile: Mapped[str | None] = mapped_column(String(50))
    country: Mapped[str | None] = mapped_column(String(100), default="India")
    state: Mapped[str | None] = mapped_column(String(100))
    city: Mapped[str | None] = mapped_column(String(100))
    pincode: Mapped[str | None] = mapped_column(String(20))
    gstType: Mapped[str | None] = mapped_column(String(50))
    gstPercent: Mapped[int | None] = mapped_column(Integer)
    address: Mapped[str | None] = mapped_column(String(500))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
