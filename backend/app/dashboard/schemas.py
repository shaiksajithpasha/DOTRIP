
from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_users: int
    total_drivers: int
    available_drivers: int
    total_vehicles: int
    total_vendors: int
    total_bookings: int
    pending_bookings: int
    total_trips: int
    ongoing_trips: int
    completed_trips: int
    total_invoices: int
    total_feedback: int