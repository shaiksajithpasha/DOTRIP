
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TripCreate(BaseModel):
    bookingId: int
    riderId: int
    driverId: int
    vehicleId: int
    vendorId: int

    corporateBookingId: Optional[int] = None

    startTime: datetime
    endTime: Optional[datetime] = None

    status: str = "ONGOING"

    distance: Optional[float] = None
    fare: Optional[float] = None

    breakdownReported: bool = False
    breakdownNotes: Optional[str] = None


class TripUpdate(BaseModel):
    bookingId: Optional[int] = None
    riderId: Optional[int] = None
    driverId: Optional[int] = None
    vehicleId: Optional[int] = None
    vendorId: Optional[int] = None

    corporateBookingId: Optional[int] = None

    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

    status: Optional[str] = None

    distance: Optional[float] = None
    fare: Optional[float] = None

    breakdownReported: Optional[bool] = None
    breakdownNotes: Optional[str] = None


class TripResponse(BaseModel):
    id: int

    bookingId: int
    riderId: int
    driverId: int
    vehicleId: int
    vendorId: int

    corporateBookingId: Optional[int] = None

    startTime: datetime
    endTime: Optional[datetime] = None

    status: str

    distance: Optional[float] = None
    fare: Optional[float] = None

    breakdownReported: bool
    breakdownNotes: Optional[str] = None

    createdAt: datetime

    class Config:
        from_attributes = True