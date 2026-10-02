from pydantic import BaseModel
from typing import Optional


class VehicleTypeCreate(BaseModel):
    name: str
    estimatedRatePerKm: float
    baseFare: float
    seatingCapacity: int
    image: Optional[str] = None


class VehicleTypeUpdate(BaseModel):
    name: Optional[str] = None
    estimatedRatePerKm: Optional[float] = None
    baseFare: Optional[float] = None
    seatingCapacity: Optional[int] = None
    image: Optional[str] = None


class VehicleTypeResponse(BaseModel):
    id: int
    name: str
    estimatedRatePerKm: float
    baseFare: float
    seatingCapacity: int
    image: Optional[str] = None

    class Config:
        from_attributes = True