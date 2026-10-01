
import bcrypt

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.users.schemas import UserCreate, UserUpdate


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


def create_user(db: Session, data: UserCreate):
    existing_email = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    if data.phone:
        existing_phone = (
            db.query(User)
            .filter(User.phone == data.phone)
            .first()
        )

        if existing_phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already exists"
            )

    hashed_password = bcrypt.hashpw(
        data.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        name=data.name,
        email=data.email,
        password=hashed_password,
        phone=data.phone,
        age=data.age,
        gender=data.gender,
        role=data.role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(
    db: Session,
    user_id: int,
    data: UserUpdate
):
    user = get_user_by_id(db, user_id)

    if data.email is not None and data.email != user.email:
        existing_email = (
            db.query(User)
            .filter(
                User.email == data.email,
                User.id != user_id
            )
            .first()
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        user.email = data.email

    if data.name is not None:
        user.name = data.name

    if data.phone is not None:
        existing_phone = (
            db.query(User)
            .filter(
                User.phone == data.phone,
                User.id != user_id
            )
            .first()
        )

        if existing_phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already exists"
            )

        user.phone = data.phone

    if data.age is not None:
        user.age = data.age

    if data.gender is not None:
        user.gender = data.gender

    if data.role is not None:
        user.role = data.role

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }