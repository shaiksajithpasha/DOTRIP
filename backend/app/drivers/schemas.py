from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class DriverCreate(BaseModel):
    fullName: str
    phone: str
    email: EmailStr
    password: str

    licenseNumber: str
    licenseExpiry: datetime

    isPartTime: bool = False
    isAvailable: bool = True

    licenseImage: Optional[str] = None
    rcImage: Optional[str] = None
    profileImage: Optional[str] = None

    whatsappPhone: Optional[str] = None
    altPhone: Optional[str] = None

    licenseIssueDate: Optional[datetime] = None
    dob: Optional[datetime] = None

    gender: Optional[str] = None
    bloodGroup: Optional[str] = None

    aadhaarNumber: Optional[str] = None
    panNumber: Optional[str] = None
    voterId: Optional[str] = None

    address: Optional[str] = None

    assignedVehicleId: Optional[int] = None
    vendorId: Optional[int] = None


class DriverUpdate(BaseModel):
    fullName: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

    licenseNumber: Optional[str] = None
    licenseExpiry: Optional[datetime] = None

    isPartTime: Optional[bool] = None
    isAvailable: Optional[bool] = None

    licenseImage: Optional[str] = None
    rcImage: Optional[str] = None
    profileImage: Optional[str] = None

    whatsappPhone: Optional[str] = None
    altPhone: Optional[str] = None

    licenseIssueDate: Optional[datetime] = None
    dob: Optional[datetime] = None

    gender: Optional[str] = None
    bloodGroup: Optional[str] = None

    aadhaarNumber: Optional[str] = None
    panNumber: Optional[str] = None
    voterId: Optional[str] = None

    address: Optional[str] = None

    assignedVehicleId: Optional[int] = None
    vendorId: Optional[int] = None


class DriverResponse(BaseModel):
    id: int

    fullName: str
    phone: str
    email: Optional[str] = None

    licenseNumber: str
    licenseExpiry: datetime

    isPartTime: bool
    isAvailable: bool

    licenseImage: Optional[str] = None
    rcImage: Optional[str] = None
    profileImage: Optional[str] = None

    whatsappPhone: Optional[str] = None
    altPhone: Optional[str] = None

    licenseIssueDate: Optional[datetime] = None
    dob: Optional[datetime] = None

    gender: Optional[str] = None
    bloodGroup: Optional[str] = None

    aadhaarNumber: Optional[str] = None
    panNumber: Optional[str] = None
    voterId: Optional[str] = None

    address: Optional[str] = None

    assignedVehicleId: Optional[int] = None
    vendorId: Optional[int] = None
    userId: Optional[int] = None

    class Config:
        from_attributes = True