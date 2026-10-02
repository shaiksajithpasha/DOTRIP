
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.vendor import Vendor
from app.vendors.schemas import VendorCreate, VendorUpdate


def get_vendors(db: Session):
    return db.query(Vendor).all()


def get_vendor(db: Session, vendor_id: int):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()

    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )

    return vendor


def create_vendor(db: Session, data: VendorCreate):
    existing_vendor = (
        db.query(Vendor)
        .filter(Vendor.companyReg == data.companyReg)
        .first()
    )

    if existing_vendor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Vendor with this company registration already exists",
        )

    vendor = Vendor(
        name=data.name,
        companyReg=data.companyReg,
        userId=data.userId,
        email=data.email,
        primaryMobile=data.primaryMobile,
        altMobile=data.altMobile,
        otherNumber=data.otherNumber,
        country=data.country,
        state=data.state,
        city=data.city,
        pincode=data.pincode,
        address=data.address,
        logoUrl=data.logoUrl,
        invoiceCompanyName=data.invoiceCompanyName,
        invoiceAddress=data.invoiceAddress,
        invoicePincode=data.invoicePincode,
        invoiceGstin=data.invoiceGstin,
        invoicePan=data.invoicePan,
        invoiceContactNo=data.invoiceContactNo,
        invoiceEmail=data.invoiceEmail,
        vendorMarginPercent=data.vendorMarginPercent,
        vendorMarginGstType=data.vendorMarginGstType,
        vendorMarginGstPct=data.vendorMarginGstPct,
    )

    db.add(vendor)
    db.commit()
    db.refresh(vendor)

    return vendor


def update_vendor(
    db: Session,
    vendor_id: int,
    data: VendorUpdate,
):
    vendor = get_vendor(db, vendor_id)

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(vendor, field, value)

    db.commit()
    db.refresh(vendor)

    return vendor


def delete_vendor(db: Session, vendor_id: int):
    vendor = get_vendor(db, vendor_id)

    db.delete(vendor)
    db.commit()

    return {
        "message": "Vendor deleted successfully"
    }