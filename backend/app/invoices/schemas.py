
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InvoiceCreate(BaseModel):
    invoiceNumber: str

    subtotal: float
    vendorCommission: float
    adminCommission: float
    totalAmount: float

    pdfUrl: Optional[str] = None

    tripId: int
    vendorId: int
    userId: int


class InvoiceUpdate(BaseModel):
    invoiceNumber: Optional[str] = None

    subtotal: Optional[float] = None
    vendorCommission: Optional[float] = None
    adminCommission: Optional[float] = None
    totalAmount: Optional[float] = None

    pdfUrl: Optional[str] = None

    tripId: Optional[int] = None
    vendorId: Optional[int] = None
    userId: Optional[int] = None


class InvoiceResponse(BaseModel):
    id: int
    invoiceNumber: str

    subtotal: float
    vendorCommission: float
    adminCommission: float
    totalAmount: float

    pdfUrl: Optional[str] = None

    createdAt: datetime

    tripId: int
    vendorId: int
    userId: int

    class Config:
        from_attributes = True