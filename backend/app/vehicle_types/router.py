
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.vehicle_types.schemas import (
    VehicleTypeCreate,
    VehicleTypeResponse,
    VehicleTypeUpdate,
)

from app.vehicle_types.service import (
    create_vehicle_type,
    delete_vehicle_type,
    get_all_vehicle_types,
    get_vehicle_type_by_id,
    update_vehicle_type,
)


router = APIRouter(
    prefix="/vehicle-types",
    tags=["Vehicle Types"],
    dependencies=[Depends(require_admin)],
)


@router.get(
    "/",
    response_model=list[VehicleTypeResponse]
)
def get_vehicle_types(
    db: Session = Depends(get_db)
):
    return get_all_vehicle_types(db)


@router.get(
    "/{vehicle_type_id}",
    response_model=VehicleTypeResponse
)
def get_vehicle_type(
    vehicle_type_id: int,
    db: Session = Depends(get_db)
):
    return get_vehicle_type_by_id(
        db,
        vehicle_type_id
    )


@router.post(
    "/",
    response_model=VehicleTypeResponse,
    status_code=201
)
def create_new_vehicle_type(
    data: VehicleTypeCreate,
    db: Session = Depends(get_db)
):
    return create_vehicle_type(db, data)


@router.put(
    "/{vehicle_type_id}",
    response_model=VehicleTypeResponse
)
def update_existing_vehicle_type(
    vehicle_type_id: int,
    data: VehicleTypeUpdate,
    db: Session = Depends(get_db)
):
    return update_vehicle_type(
        db,
        vehicle_type_id,
        data
    )


@router.delete(
    "/{vehicle_type_id}"
)
def delete_existing_vehicle_type(
    vehicle_type_id: int,
    db: Session = Depends(get_db)
):
    return delete_vehicle_type(
        db,
        vehicle_type_id
    )