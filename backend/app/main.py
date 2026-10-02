from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import User
from app.auth.router import router as auth_router
from app.users.router import router as users_router
from app.dashboard.router import router as dashboard_router
from app.drivers.router import router as drivers_router
from app.vehicle_types.router import router as vehicle_types_router
from app.vehicles.router import router as vehicles_router
from app.vendors.router import router as vendors_router
from app.bookings.router import router as bookings_router
from app.trips.router import router as trips_router 
from app.invoices.router import router as invoices_router


app = FastAPI()


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)
app.include_router(drivers_router)
app.include_router(vehicle_types_router)
app.include_router(vehicles_router)
app.include_router(vendors_router)
app.include_router(bookings_router)
app.include_router(trips_router)
app.include_router(invoices_router)

@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }


@app.get("/test-db")
def test_db():
    try:
        with engine.connect():
            return {
                "status": "success",
                "message": "PostgreSQL connected successfully"
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }