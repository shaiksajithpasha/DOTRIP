from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Earnings(Base):
    __tablename__ = "earnings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendorId: Mapped[int] = mapped_column(ForeignKey("vendors.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    note: Mapped[str | None] = mapped_column(String(1000))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
