from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import bcrypt
from jose import jwt
import os

from app.models.user import User
from app.auth.schemas import LoginRequest


def login_user(db: Session, data: LoginRequest):
    user = (
        db.query(User)
        .filter(
            (User.email == data.identifier)
            | (User.phone == data.identifier)
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email/phone or password",
        )

    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password login is not available for this account",
        )

    password_valid = bcrypt.checkpw(
        data.password.encode("utf-8"),
        user.password.encode("utf-8"),
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email/phone or password",
        )

    return user


def create_access_token(user: User):
    secret_key = os.getenv("SECRET_KEY")
    expire_minutes = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )

    if not secret_key:
        raise RuntimeError("SECRET_KEY is not configured")

    payload = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role,
    }

    from datetime import datetime, timedelta, timezone

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expire_minutes
    )

    payload["exp"] = expire

    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256",
    )

    return token