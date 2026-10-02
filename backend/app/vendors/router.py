
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.vendors.schemas import (
    VendorCreate,
    VendorUpdate,
    VendorResponse,
)

from app.vendors.service import (
    get_vendors,
    get_vendor,
    create_vendor,
    update_vendor,
    delete_vendor,
)


router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return get_vendors(db)


@router.get("/{vendor_id}", response_model=VendorResponse)
def get_single_vendor(
    vendor_id: int,
    db: Session = Depends(get_db),
):
    return get_vendor(db, vendor_id)


@router.post("/", response_model=VendorResponse)
def add_vendor(
    data: VendorCreate,
    db: Session = Depends(get_db),
):
    return create_vendor(db, data)


@router.put("/{vendor_id}", response_model=VendorResponse)
def edit_vendor(
    vendor_id: int,
    data: VendorUpdate,
    db: Session = Depends(get_db),
):
    return update_vendor(db, vendor_id, data)


@router.delete("/{vendor_id}")
def remove_vendor(
    vendor_id: int,
    db: Session = Depends(get_db),
):
    return delete_vendor(db, vendor_id)