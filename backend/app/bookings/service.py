
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.bookings.schemas import BookingCreate, BookingUpdate


def get_bookings(db: Session):
    return db.query(Booking).all()


def get_booking(db: Session, booking_id: int):
    booking = (
        db.query(Booking)
        .filter(Booking.id == booking_id)
        .first()
    )

    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found",
        )

    return booking


def create_booking(db: Session, data: BookingCreate):
    booking = Booking(
        userId=data.userId,
        vehicleTypeId=data.vehicleTypeId,
        pickupAddressId=data.pickupAddressId,
        dropAddressId=data.dropAddressId,
        pickupDate=data.pickupDate,
        pickupTime=data.pickupTime,
        returnDate=data.returnDate,
        returnTime=data.returnTime,
        fromCityId=data.fromCityId,
        toCityId=data.toCityId,
        tripTypeId=data.tripTypeId,
        fare=data.fare,
        numPersons=data.numPersons,
        numVehicles=data.numVehicles,
        bookingType=data.bookingType,
        status=data.status,
        vendorId=data.vendorId,
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


def update_booking(
    db: Session,
    booking_id: int,
    data: BookingUpdate,
):
    booking = get_booking(db, booking_id)

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(booking, field, value)

    db.commit()
    db.refresh(booking)

    return booking


def delete_booking(db: Session, booking_id: int):
    booking = get_booking(db, booking_id)

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking deleted successfully"
    }