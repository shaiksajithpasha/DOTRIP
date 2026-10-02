
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.trips.schemas import (
    TripCreate,
    TripUpdate,
    TripResponse,
)

from app.trips.service import (
    get_trips,
    get_trip,
    create_trip,
    update_trip,
    delete_trip,
)


router = APIRouter(
    prefix="/trips",
    tags=["Trips"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[TripResponse])
def list_trips(db: Session = Depends(get_db)):
    return get_trips(db)


@router.get("/{trip_id}", response_model=TripResponse)
def get_single_trip(
    trip_id: int,
    db: Session = Depends(get_db),
):
    return get_trip(db, trip_id)


@router.post("/", response_model=TripResponse)
def add_trip(
    data: TripCreate,
    db: Session = Depends(get_db),
):
    return create_trip(db, data)


@router.put("/{trip_id}", response_model=TripResponse)
def edit_trip(
    trip_id: int,
    data: TripUpdate,
    db: Session = Depends(get_db),
):
    return update_trip(db, trip_id, data)


@router.delete("/{trip_id}")
def remove_trip(
    trip_id: int,
    db: Session = Depends(get_db),
):
    return delete_trip(db, trip_id)