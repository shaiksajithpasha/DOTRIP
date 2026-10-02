
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.dependencies import require_admin

from app.invoices.schemas import (
    InvoiceCreate,
    InvoiceUpdate,
    InvoiceResponse,
)

from app.invoices.service import (
    get_invoices,
    get_invoice,
    create_invoice,
    update_invoice,
    delete_invoice,
)


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=list[InvoiceResponse])
def list_invoices(db: Session = Depends(get_db)):
    return get_invoices(db)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_single_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return get_invoice(db, invoice_id)


@router.post("/", response_model=InvoiceResponse)
def add_invoice(
    data: InvoiceCreate,
    db: Session = Depends(get_db),
):
    return create_invoice(db, data)


@router.put("/{invoice_id}", response_model=InvoiceResponse)
def edit_invoice(
    invoice_id: int,
    data: InvoiceUpdate,
    db: Session = Depends(get_db),
):
    return update_invoice(db, invoice_id, data)


@router.delete("/{invoice_id}")
def remove_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return delete_invoice(db, invoice_id)