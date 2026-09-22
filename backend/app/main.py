from fastapi import FastAPI

from app.database import Base, engine
from app.models import User

app = FastAPI()


Base.metadata.create_all(bind=engine)


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