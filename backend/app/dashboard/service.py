
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.driver import Driver
from app.models.vehicle import Vehicle
from app.models.vendor import Vendor
from app.models.booking import Booking
from app.models.trip import Trip
from app.models.invoice import Invoice
from app.models.feedback import Feedback


def get_dashboard_stats(db: Session):

    total_users = db.query(User).count()

    total_drivers = db.query(Driver).count()

    available_drivers = (
        db.query(Driver)
        .filter(Driver.isAvailable.is_(True))
        .count()
    )

    total_vehicles = db.query(Vehicle).count()

    total_vendors = db.query(Vendor).count()

    total_bookings = db.query(Booking).count()

    pending_bookings = (
        db.query(Booking)
        .filter(Booking.status == "PENDING")
        .count()
    )

    total_trips = db.query(Trip).count()

    ongoing_trips = (
        db.query(Trip)
        .filter(Trip.status == "ONGOING")
        .count()
    )

    completed_trips = (
        db.query(Trip)
        .filter(Trip.status == "COMPLETED")
        .count()
    )

    total_invoices = db.query(Invoice).count()

    total_feedback = db.query(Feedback).count()

    return {
        "total_users": total_users,
        "total_drivers": total_drivers,
        "available_drivers": available_drivers,
        "total_vehicles": total_vehicles,
        "total_vendors": total_vendors,
        "total_bookings": total_bookings,
        "pending_bookings": pending_bookings,
        "total_trips": total_trips,
        "ongoing_trips": ongoing_trips,
        "completed_trips": completed_trips,
        "total_invoices": total_invoices,
        "total_feedback": total_feedback,
    }