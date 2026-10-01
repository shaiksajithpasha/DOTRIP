from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import User
from app.auth.router import router as auth_router
from app.users.router import router as users_router
from app.dashboard.router import router as dashboard_router

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