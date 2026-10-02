
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.bookings.schemas import (
    BookingCreate,
    BookingUpdate,
    BookingResponse,
)

from app.bookings.service import (
    get_bookings,
    get_booking,
    create_booking,
    update_booking,
    delete_booking,
)


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[BookingResponse])
def list_bookings(db: Session = Depends(get_db)):
    return get_bookings(db)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_single_booking(
    booking_id: int,
    db: Session = Depends(get_db),
):
    return get_booking(db, booking_id)


@router.post("/", response_model=BookingResponse)
def add_booking(
    data: BookingCreate,
    db: Session = Depends(get_db),
):
    return create_booking(db, data)


@router.put("/{booking_id}", response_model=BookingResponse)
def edit_booking(
    booking_id: int,
    data: BookingUpdate,
    db: Session = Depends(get_db),
):
    return update_booking(db, booking_id, data)


@router.delete("/{booking_id}")
def remove_booking(
    booking_id: int,
    db: Session = Depends(get_db),
):
    return delete_booking(db, booking_id)