from datetime import datetime
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from .enums import MessageStatus

class TripAssistance(Base):
    __tablename__ = "trip_assistances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tripId: Mapped[int] = mapped_column(ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    driverId: Mapped[int | None] = mapped_column(ForeignKey("drivers.id"))
    location: Mapped[str] = mapped_column(String(500), nullable=False)
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    reply: Mapped[str | None] = mapped_column(String(2000))
    messageStatus: Mapped[MessageStatus | None] = mapped_column(
        Enum(MessageStatus, name="message_status_enum"), default=MessageStatus.UNREAD
    )
    createdAt: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
