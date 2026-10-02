
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.drivers.schemas import (
    DriverCreate,
    DriverResponse,
    DriverUpdate,
)

from app.drivers.service import (
    create_driver,
    delete_driver,
    get_all_drivers,
    get_driver_by_id,
    update_driver,
)


router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
    dependencies=[Depends(require_admin)],
)


@router.get(
    "/",
    response_model=list[DriverResponse]
)
def get_drivers(
    db: Session = Depends(get_db)
):
    return get_all_drivers(db)


@router.get(
    "/{driver_id}",
    response_model=DriverResponse
)
def get_driver(
    driver_id: int,
    db: Session = Depends(get_db)
):
    return get_driver_by_id(db, driver_id)


@router.post(
    "/",
    response_model=DriverResponse,
    status_code=201
)
def create_new_driver(
    data: DriverCreate,
    db: Session = Depends(get_db)
):
    return create_driver(db, data)


@router.put(
    "/{driver_id}",
    response_model=DriverResponse
)
def update_existing_driver(
    driver_id: int,
    data: DriverUpdate,
    db: Session = Depends(get_db)
):
    return update_driver(db, driver_id, data)


@router.delete("/{driver_id}")
def delete_existing_driver(
    driver_id: int,
    db: Session = Depends(get_db)
):
    return delete_driver(db, driver_id)