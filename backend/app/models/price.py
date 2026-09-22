from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Price(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    priceType: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
