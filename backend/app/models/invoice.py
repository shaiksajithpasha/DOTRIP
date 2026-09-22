from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    invoiceNumber: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    vendorCommission: Mapped[float] = mapped_column(Float, nullable=False)
    adminCommission: Mapped[float] = mapped_column(Float, nullable=False)
    totalAmount: Mapped[float] = mapped_column(Float, nullable=False)
    pdfUrl: Mapped[str | None] = mapped_column(String(500))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    tripId: Mapped[int] = mapped_column(ForeignKey("trips.id"), unique=True, nullable=False)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
