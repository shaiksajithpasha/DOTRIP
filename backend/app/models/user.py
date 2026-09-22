from datetime import datetime

from sqlalchemy import DateTime, Enum, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from .enums import Role


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True
    )

    age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    gender: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role, name="role_enum"),
        default=Role.RIDER,
        nullable=False
    )

    token: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )