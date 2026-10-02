
from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime


class BookingCreate(BaseModel):
    userId: int
    vehicleTypeId: int
    pickupAddressId: int
    dropAddressId: int

    pickupDate: Optional[date] = None
    pickupTime: Optional[time] = None
    returnDate: Optional[date] = None
    returnTime: Optional[time] = None

    fromCityId: int
    toCityId: int
    tripTypeId: int

    fare: float

    numPersons: int = 1
    numVehicles: int = 1

    bookingType: str = "individual"
    status: str = "PENDING"

    vendorId: Optional[int] = None


class BookingUpdate(BaseModel):
    userId: Optional[int] = None
    vehicleTypeId: Optional[int] = None
    pickupAddressId: Optional[int] = None
    dropAddressId: Optional[int] = None

    pickupDate: Optional[date] = None
    pickupTime: Optional[time] = None
    returnDate: Optional[date] = None
    returnTime: Optional[time] = None

    fromCityId: Optional[int] = None
    toCityId: Optional[int] = None
    tripTypeId: Optional[int] = None

    fare: Optional[float] = None

    numPersons: Optional[int] = None
    numVehicles: Optional[int] = None

    bookingType: Optional[str] = None
    status: Optional[str] = None

    vendorId: Optional[int] = None


class BookingResponse(BaseModel):
    id: int

    userId: int
    vehicleTypeId: int
    pickupAddressId: int
    dropAddressId: int

    pickupDate: Optional[date] = None
    pickupTime: Optional[time] = None
    returnDate: Optional[date] = None
    returnTime: Optional[time] = None

    fromCityId: int
    toCityId: int
    tripTypeId: int

    fare: float

    numPersons: int
    numVehicles: int

    bookingType: str
    status: str

    createdAt: datetime

    vendorId: Optional[int] = None

    class Config:
        from_attributes = True