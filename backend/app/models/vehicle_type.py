from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VehicleType(Base):

    __tablename__ = "vehicle_types"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    estimatedRatePerKm: Mapped[float] = mapped_column(
        Float,
        default=10.0,
        nullable=False
    )

    baseFare: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    seatingCapacity: Mapped[int] = mapped_column(
        Integer,
        default=4,
        nullable=False
    )

    image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )