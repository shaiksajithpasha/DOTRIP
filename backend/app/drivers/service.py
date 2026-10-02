
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.driver import Driver
from app.drivers.schemas import DriverCreate, DriverUpdate


def get_all_drivers(db: Session):
    return db.query(Driver).all()


def get_driver_by_id(db: Session, driver_id: int):
    driver = (
        db.query(Driver)
        .filter(Driver.id == driver_id)
        .first()
    )

    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Driver not found",
        )

    return driver


def create_driver(db: Session, data: DriverCreate):
    existing_license = (
        db.query(Driver)
        .filter(
            Driver.licenseNumber == data.licenseNumber
        )
        .first()
    )

    if existing_license:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="License number already exists",
        )

    driver = Driver(
        fullName=data.fullName,
        phone=data.phone,
        email=data.email,
        licenseNumber=data.licenseNumber,
        licenseExpiry=data.licenseExpiry,
        isPartTime=data.isPartTime,
        isAvailable=data.isAvailable,
        licenseImage=data.licenseImage,
        rcImage=data.rcImage,
        profileImage=data.profileImage,
        whatsappPhone=data.whatsappPhone,
        altPhone=data.altPhone,
        licenseIssueDate=data.licenseIssueDate,
        dob=data.dob,
        gender=data.gender,
        bloodGroup=data.bloodGroup,
        aadhaarNumber=data.aadhaarNumber,
        panNumber=data.panNumber,
        voterId=data.voterId,
        address=data.address,
        assignedVehicleId=data.assignedVehicleId,
        vendorId=data.vendorId,
        userId=data.userId,
    )

    db.add(driver)
    db.commit()
    db.refresh(driver)

    return driver


def update_driver(
    db: Session,
    driver_id: int,
    data: DriverUpdate,
):
    driver = get_driver_by_id(db, driver_id)

    update_data = data.model_dump(exclude_unset=True)

    if "licenseNumber" in update_data:
        existing_license = (
            db.query(Driver)
            .filter(
                Driver.licenseNumber == update_data["licenseNumber"],
                Driver.id != driver_id,
            )
            .first()
        )

        if existing_license:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="License number already exists",
            )

    for field, value in update_data.items():
        setattr(driver, field, value)

    db.commit()
    db.refresh(driver)

    return driver


def delete_driver(db: Session, driver_id: int):
    driver = get_driver_by_id(db, driver_id)

    db.delete(driver)
    db.commit()

    return {
        "message": "Driver deleted successfully"
    }