from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.vehicle_type import VehicleType
from app.vehicle_types.schemas import (
    VehicleTypeCreate,
    VehicleTypeUpdate,
)


def get_all_vehicle_types(db: Session):
    return db.query(VehicleType).all()


def get_vehicle_type_by_id(
    db: Session,
    vehicle_type_id: int,
):
    vehicle_type = (
        db.query(VehicleType)
        .filter(VehicleType.id == vehicle_type_id)
        .first()
    )

    if not vehicle_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle type not found",
        )

    return vehicle_type


def create_vehicle_type(
    db: Session,
    data: VehicleTypeCreate,
):
    existing = (
        db.query(VehicleType)
        .filter(VehicleType.name == data.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Vehicle type already exists",
        )

    vehicle_type = VehicleType(
        name=data.name,
        estimatedRatePerKm=data.estimatedRatePerKm,
        baseFare=data.baseFare,
        seatingCapacity=data.seatingCapacity,
        image=data.image,
    )

    db.add(vehicle_type)
    db.commit()
    db.refresh(vehicle_type)

    return vehicle_type


def update_vehicle_type(
    db: Session,
    vehicle_type_id: int,
    data: VehicleTypeUpdate,
):
    vehicle_type = get_vehicle_type_by_id(
        db,
        vehicle_type_id,
    )

    update_data = data.model_dump(exclude_unset=True)

    if "name" in update_data:
        existing = (
            db.query(VehicleType)
            .filter(
                VehicleType.name == update_data["name"],
                VehicleType.id != vehicle_type_id,
            )
            .first()
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Vehicle type already exists",
            )

    for field, value in update_data.items():
        setattr(vehicle_type, field, value)

    db.commit()
    db.refresh(vehicle_type)

    return vehicle_type


def delete_vehicle_type(
    db: Session,
    vehicle_type_id: int,
):
    vehicle_type = get_vehicle_type_by_id(
        db,
        vehicle_type_id,
    )

    db.delete(vehicle_type)
    db.commit()

    return {
        "message": "Vehicle type deleted successfully"
    }