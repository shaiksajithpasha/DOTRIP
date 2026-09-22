from sqlalchemy import Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class CityDistance(Base):
    __tablename__ = "city_distances"
    __table_args__ = (
        UniqueConstraint("fromCityId", "toCityId", name="uq_city_distance_direction"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fromCityId: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    toCityId: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    distanceKm: Mapped[float] = mapped_column(Float, nullable=False)
    fromCityName: Mapped[str] = mapped_column(String(255), nullable=False)
    toCityName: Mapped[str] = mapped_column(String(255), nullable=False)
