
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.vehicles.schemas import (
    VehicleCreate,
    VehicleUpdate,
    VehicleResponse,
)

from app.vehicles.service import (
    get_vehicles,
    get_vehicle,
    create_vehicle,
    update_vehicle,
    delete_vehicle,
)


router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[VehicleResponse])
def list_vehicles(db: Session = Depends(get_db)):
    return get_vehicles(db)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_single_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    return get_vehicle(db, vehicle_id)


@router.post("/", response_model=VehicleResponse)
def add_vehicle(
    data: VehicleCreate,
    db: Session = Depends(get_db),
):
    return create_vehicle(db, data)


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def edit_vehicle(
    vehicle_id: int,
    data: VehicleUpdate,
    db: Session = Depends(get_db),
):
    return update_vehicle(db, vehicle_id, data)


@router.delete("/{vehicle_id}")
def remove_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    return delete_vehicle(db, vehicle_id)