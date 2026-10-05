from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import bcrypt

from app.models.driver import Driver
from app.models.user import User
from app.models.enums import Role
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
    # Check duplicate license number
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

    # Check duplicate User email
    existing_email = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    # Check duplicate User phone
    existing_phone = (
        db.query(User)
        .filter(User.phone == data.phone) 
        .first()
    )

    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone already exists",
        )

    try:
        # --------------------------------
        # 1. Create User account
        # --------------------------------

        hashed_password = bcrypt.hashpw(
            data.password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")

        user = User(
            name=data.fullName,
            email=data.email,
            password=hashed_password,
            phone=data.phone,
            gender=data.gender,
            role=Role.DRIVER,
        )

        db.add(user)
        db.flush()

        # --------------------------------
        # 2. Create Driver profile
        # --------------------------------

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
            userId=user.id,
        )

        db.add(driver)

        # --------------------------------
        # 3. Save both records
        # --------------------------------

        db.commit()

        db.refresh(driver)

        return driver

    except Exception:
        db.rollback()
        raise


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