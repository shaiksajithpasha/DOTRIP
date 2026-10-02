
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VehicleCreate(BaseModel):
    image: Optional[str] = None
    additional_images: Optional[str] = None

    registrationNumber: str
    chassisNumber: Optional[str] = None
    status: Optional[str] = None

    createdBy: Optional[int] = None
    vehicleTypeId: Optional[int] = None

    lastServicedDate: Optional[datetime] = None
    vehicleExpiryDate: Optional[datetime] = None

    extraKmCharge: Optional[float] = None
    earlyMorningCharges: Optional[float] = None
    eveningCharges: Optional[float] = None

    videoUrl: Optional[str] = None

    insurancePolicyNumber: Optional[str] = None
    insuranceStartDate: Optional[datetime] = None
    insuranceEndDate: Optional[datetime] = None
    insuranceContactNumber: Optional[str] = None

    rtoCode: Optional[str] = None

    vendorId: Optional[int] = None
    driverOwnerId: Optional[int] = None


class VehicleUpdate(BaseModel):
    image: Optional[str] = None
    additional_images: Optional[str] = None

    registrationNumber: Optional[str] = None
    chassisNumber: Optional[str] = None
    status: Optional[str] = None

    createdBy: Optional[int] = None
    vehicleTypeId: Optional[int] = None

    lastServicedDate: Optional[datetime] = None
    vehicleExpiryDate: Optional[datetime] = None

    extraKmCharge: Optional[float] = None
    earlyMorningCharges: Optional[float] = None
    eveningCharges: Optional[float] = None

    videoUrl: Optional[str] = None

    insurancePolicyNumber: Optional[str] = None
    insuranceStartDate: Optional[datetime] = None
    insuranceEndDate: Optional[datetime] = None
    insuranceContactNumber: Optional[str] = None

    rtoCode: Optional[str] = None

    vendorId: Optional[int] = None
    driverOwnerId: Optional[int] = None


class VehicleResponse(BaseModel):
    id: int

    image: Optional[str] = None
    additional_images: Optional[str] = None

    registrationNumber: str
    chassisNumber: Optional[str] = None
    status: Optional[str] = None

    createdBy: Optional[int] = None
    vehicleTypeId: Optional[int] = None

    lastServicedDate: Optional[datetime] = None
    vehicleExpiryDate: Optional[datetime] = None

    extraKmCharge: Optional[float] = None
    earlyMorningCharges: Optional[float] = None
    eveningCharges: Optional[float] = None

    videoUrl: Optional[str] = None

    insurancePolicyNumber: Optional[str] = None
    insuranceStartDate: Optional[datetime] = None
    insuranceEndDate: Optional[datetime] = None
    insuranceContactNumber: Optional[str] = None

    rtoCode: Optional[str] = None

    vendorId: Optional[int] = None
    driverOwnerId: Optional[int] = None

    class Config:
        from_attributes = True