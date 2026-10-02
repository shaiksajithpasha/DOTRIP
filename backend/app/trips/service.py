
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.trips.schemas import TripCreate, TripUpdate


def get_trips(db: Session):
    return db.query(Trip).all()


def get_trip(db: Session, trip_id: int):
    trip = (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )

    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    return trip


def create_trip(db: Session, data: TripCreate):
    trip = Trip(
        bookingId=data.bookingId,
        riderId=data.riderId,
        driverId=data.driverId,
        vehicleId=data.vehicleId,
        vendorId=data.vendorId,
        corporateBookingId=data.corporateBookingId,
        startTime=data.startTime,
        endTime=data.endTime,
        status=data.status,
        distance=data.distance,
        fare=data.fare,
        breakdownReported=data.breakdownReported,
        breakdownNotes=data.breakdownNotes,
    )

    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip


def update_trip(
    db: Session,
    trip_id: int,
    data: TripUpdate,
):
    trip = get_trip(db, trip_id)

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(trip, field, value)

    db.commit()
    db.refresh(trip)

    return trip


def delete_trip(db: Session, trip_id: int):
    trip = get_trip(db, trip_id)

    db.delete(trip)
    db.commit()

    return {
        "message": "Trip deleted successfully"
    }