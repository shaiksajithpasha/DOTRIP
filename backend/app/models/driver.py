from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Driver(Base):
    __tablename__ = "drivers"
    __table_args__ = (
        Index("ix_drivers_vendorId", "vendorId"),
        Index("ix_drivers_phone", "phone"),
        Index("ix_drivers_licenseNumber", "licenseNumber"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fullName: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255))
    licenseNumber: Mapped[str] = mapped_column(String(100), nullable=False)
    licenseExpiry: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    isPartTime: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    isAvailable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    licenseImage: Mapped[str | None] = mapped_column(String(500))
    rcImage: Mapped[str | None] = mapped_column(String(500))
    profileImage: Mapped[str | None] = mapped_column(String(500))
    whatsappPhone: Mapped[str | None] = mapped_column(String(50))
    altPhone: Mapped[str | None] = mapped_column(String(50))
    licenseIssueDate: Mapped[datetime | None] = mapped_column(DateTime)
    dob: Mapped[datetime | None] = mapped_column(DateTime)
    gender: Mapped[str | None] = mapped_column(String(50))
    bloodGroup: Mapped[str | None] = mapped_column(String(20))
    aadhaarNumber: Mapped[str | None] = mapped_column(String(50))
    panNumber: Mapped[str | None] = mapped_column(String(50))
    voterId: Mapped[str | None] = mapped_column(String(50))
    address: Mapped[str | None] = mapped_column(String(500))

    assignedVehicleId: Mapped[int | None] = mapped_column(Integer, unique=True)
    vendorId: Mapped[int | None] = mapped_column(ForeignKey("vendors.id"))
    userId: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
