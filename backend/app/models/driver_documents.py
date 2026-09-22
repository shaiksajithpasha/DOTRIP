from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class DriverDocuments(Base):
    __tablename__ = "driver_documents"

    driverId: Mapped[int] = mapped_column(ForeignKey("drivers.id", ondelete="CASCADE"), primary_key=True)
    aadharUrl: Mapped[str | None] = mapped_column(String(500))
    panUrl: Mapped[str | None] = mapped_column(String(500))
    voterUrl: Mapped[str | None] = mapped_column(String(500))
    licenseUrl: Mapped[str | None] = mapped_column(String(500))
    profileUrl: Mapped[str | None] = mapped_column(String(500))
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
