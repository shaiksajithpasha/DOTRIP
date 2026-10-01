from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.users.schemas import (
    UserCreate,
    UserResponse,
    UserUpdate,
)

from app.users.service import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_id,
    update_user,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return get_all_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_by_id(db, user_id)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_new_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, data)


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_existing_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user(db, user_id, data)


@router.delete("/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db, user_id)