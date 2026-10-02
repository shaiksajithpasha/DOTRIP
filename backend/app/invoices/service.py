
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.invoices.schemas import InvoiceCreate, InvoiceUpdate


def get_invoices(db: Session):
    return db.query(Invoice).all()


def get_invoice(db: Session, invoice_id: int):
    invoice = (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )

    return invoice


def create_invoice(db: Session, data: InvoiceCreate):
    existing_invoice = (
        db.query(Invoice)
        .filter(Invoice.invoiceNumber == data.invoiceNumber)
        .first()
    )

    if existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invoice with this invoice number already exists",
        )

    existing_trip_invoice = (
        db.query(Invoice)
        .filter(Invoice.tripId == data.tripId)
        .first()
    )

    if existing_trip_invoice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An invoice already exists for this trip",
        )

    invoice = Invoice(
        invoiceNumber=data.invoiceNumber,
        subtotal=data.subtotal,
        vendorCommission=data.vendorCommission,
        adminCommission=data.adminCommission,
        totalAmount=data.totalAmount,
        pdfUrl=data.pdfUrl,
        tripId=data.tripId,
        vendorId=data.vendorId,
        userId=data.userId,
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice


def update_invoice(
    db: Session,
    invoice_id: int,
    data: InvoiceUpdate,
):
    invoice = get_invoice(db, invoice_id)

    update_data = data.model_dump(exclude_unset=True)

    if "invoiceNumber" in update_data:
        existing_invoice = (
            db.query(Invoice)
            .filter(
                Invoice.invoiceNumber == update_data["invoiceNumber"],
                Invoice.id != invoice_id,
            )
            .first()
        )

        if existing_invoice:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invoice with this invoice number already exists",
            )

    if "tripId" in update_data:
        existing_trip_invoice = (
            db.query(Invoice)
            .filter(
                Invoice.tripId == update_data["tripId"],
                Invoice.id != invoice_id,
            )
            .first()
        )

        if existing_trip_invoice:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An invoice already exists for this trip",
            )

    for field, value in update_data.items():
        setattr(invoice, field, value)

    db.commit()
    db.refresh(invoice)

    return invoice


def delete_invoice(db: Session, invoice_id: int):
    invoice = get_invoice(db, invoice_id)

    db.delete(invoice)
    db.commit()

    return {
        "message": "Invoice deleted successfully"
    }