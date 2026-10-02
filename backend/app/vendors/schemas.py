
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VendorCreate(BaseModel):
    name: str
    companyReg: str

    userId: Optional[int] = None

    email: Optional[str] = None
    primaryMobile: Optional[str] = None
    altMobile: Optional[str] = None
    otherNumber: Optional[str] = None

    country: Optional[str] = "India"
    state: Optional[str] = None
    city: Optional[str] = None
    pincode: Optional[str] = None
    address: Optional[str] = None

    logoUrl: Optional[str] = None

    invoiceCompanyName: Optional[str] = None
    invoiceAddress: Optional[str] = None
    invoicePincode: Optional[str] = None
    invoiceGstin: Optional[str] = None
    invoicePan: Optional[str] = None
    invoiceContactNo: Optional[str] = None
    invoiceEmail: Optional[str] = None

    vendorMarginPercent: Optional[float] = None
    vendorMarginGstType: Optional[str] = None
    vendorMarginGstPct: Optional[int] = None


class VendorUpdate(BaseModel):
    name: Optional[str] = None
    companyReg: Optional[str] = None

    userId: Optional[int] = None

    email: Optional[str] = None
    primaryMobile: Optional[str] = None
    altMobile: Optional[str] = None
    otherNumber: Optional[str] = None

    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    pincode: Optional[str] = None
    address: Optional[str] = None

    logoUrl: Optional[str] = None

    invoiceCompanyName: Optional[str] = None
    invoiceAddress: Optional[str] = None
    invoicePincode: Optional[str] = None
    invoiceGstin: Optional[str] = None
    invoicePan: Optional[str] = None
    invoiceContactNo: Optional[str] = None
    invoiceEmail: Optional[str] = None

    vendorMarginPercent: Optional[float] = None
    vendorMarginGstType: Optional[str] = None
    vendorMarginGstPct: Optional[int] = None


class VendorResponse(BaseModel):
    id: int
    name: str
    companyReg: str
    createdAt: datetime

    userId: Optional[int] = None

    email: Optional[str] = None
    primaryMobile: Optional[str] = None
    altMobile: Optional[str] = None
    otherNumber: Optional[str] = None

    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    pincode: Optional[str] = None
    address: Optional[str] = None

    logoUrl: Optional[str] = None

    invoiceCompanyName: Optional[str] = None
    invoiceAddress: Optional[str] = None
    invoicePincode: Optional[str] = None
    invoiceGstin: Optional[str] = None
    invoicePan: Optional[str] = None
    invoiceContactNo: Optional[str] = None
    invoiceEmail: Optional[str] = None

    vendorMarginPercent: Optional[float] = None
    vendorMarginGstType: Optional[str] = None
    vendorMarginGstPct: Optional[int] = None

    class Config:
        from_attributes = True