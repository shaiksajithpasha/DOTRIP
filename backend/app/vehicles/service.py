
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.vehicles.schemas import VehicleCreate, VehicleUpdate


def get_vehicles(db: Session):
    return db.query(Vehicle).all()


def get_vehicle(db: Session, vehicle_id: int):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found",
        )

    return vehicle


def create_vehicle(db: Session, data: VehicleCreate):
    existing_vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.registrationNumber == data.registrationNumber)
        .first()
    )

    if existing_vehicle:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Vehicle with this registration number already exists",
        )

    vehicle = Vehicle(
        image=data.image,
        additional_images=data.additional_images,
        registrationNumber=data.registrationNumber,
        chassisNumber=data.chassisNumber,
        status=data.status,
        createdBy=data.createdBy,
        vehicleTypeId=data.vehicleTypeId,
        lastServicedDate=data.lastServicedDate,
        vehicleExpiryDate=data.vehicleExpiryDate,
        extraKmCharge=data.extraKmCharge,
        earlyMorningCharges=data.earlyMorningCharges,
        eveningCharges=data.eveningCharges,
        videoUrl=data.videoUrl,
        insurancePolicyNumber=data.insurancePolicyNumber,
        insuranceStartDate=data.insuranceStartDate,
        insuranceEndDate=data.insuranceEndDate,
        insuranceContactNumber=data.insuranceContactNumber,
        rtoCode=data.rtoCode,
        vendorId=data.vendorId,
        driverOwnerId=data.driverOwnerId,
    )

    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)

    return vehicle


def update_vehicle(
    db: Session,
    vehicle_id: int,
    data: VehicleUpdate,
):
    vehicle = get_vehicle(db, vehicle_id)

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(vehicle, field, value)

    db.commit()
    db.refresh(vehicle)

    return vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    vehicle = get_vehicle(db, vehicle_id)

    db.delete(vehicle)
    db.commit()

    return {
        "message": "Vehicle deleted successfully"
    }