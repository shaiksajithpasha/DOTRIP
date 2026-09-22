from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    companyReg: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    userId: Mapped[int | None] = mapped_column(Integer, unique=True, nullable=True)
    email: Mapped[str | None] = mapped_column(String(255))
    primaryMobile: Mapped[str | None] = mapped_column(String(50))
    altMobile: Mapped[str | None] = mapped_column(String(50))
    otherNumber: Mapped[str | None] = mapped_column(String(50))
    country: Mapped[str | None] = mapped_column(String(100), default="India")
    state: Mapped[str | None] = mapped_column(String(100))
    city: Mapped[str | None] = mapped_column(String(100))
    pincode: Mapped[str | None] = mapped_column(String(20))
    address: Mapped[str | None] = mapped_column(String(500))

    logoUrl: Mapped[str | None] = mapped_column(String(500))
    invoiceCompanyName: Mapped[str | None] = mapped_column(String(255))
    invoiceAddress: Mapped[str | None] = mapped_column(String(500))
    invoicePincode: Mapped[str | None] = mapped_column(String(20))
    invoiceGstin: Mapped[str | None] = mapped_column(String(100))
    invoicePan: Mapped[str | None] = mapped_column(String(100))
    invoiceContactNo: Mapped[str | None] = mapped_column(String(50))
    invoiceEmail: Mapped[str | None] = mapped_column(String(255))

    vendorMarginPercent: Mapped[float | None] = mapped_column(Float)
    vendorMarginGstType: Mapped[str | None] = mapped_column(String(50))
    vendorMarginGstPct: Mapped[int | None] = mapped_column(Integer)
