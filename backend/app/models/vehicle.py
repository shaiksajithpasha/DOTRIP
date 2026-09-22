from datetime import date
from sqlalchemy import Date, Float, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from .enums import Role

class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String(500), nullable=False)
    additional_images: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    registrationNumber: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    chassisNumber: Mapped[str | None] = mapped_column(String(100), unique=True)
    status: Mapped[str] = mapped_column(String(50), default="available", nullable=False)
    createdBy: Mapped[Role] = mapped_column(default=Role.VENDOR, nullable=False)
    vehicleTypeId: Mapped[int] = mapped_column(ForeignKey("vehicle_types.id"), nullable=False)

    lastServicedDate: Mapped[date | None] = mapped_column(Date)
    vehicleExpiryDate: Mapped[date | None] = mapped_column(Date)
    extraKmCharge: Mapped[float | None] = mapped_column(Float, default=0)
    earlyMorningCharges: Mapped[float | None] = mapped_column(Float, default=0)
    eveningCharges: Mapped[float | None] = mapped_column(Float, default=0)
    videoUrl: Mapped[str | None] = mapped_column(String(500))

    insurancePolicyNumber: Mapped[str | None] = mapped_column(String(255))
    insuranceStartDate: Mapped[date | None] = mapped_column(Date)
    insuranceEndDate: Mapped[date | None] = mapped_column(Date)
    insuranceContactNumber: Mapped[str | None] = mapped_column(String(50))
    rtoCode: Mapped[str | None] = mapped_column(String(50))

    vendorId: Mapped[int | None] = mapped_column(ForeignKey("vendors.id"))
    driverOwnerId: Mapped[int | None] = mapped_column(ForeignKey("drivers.id"))

    __table_args__ = ()
