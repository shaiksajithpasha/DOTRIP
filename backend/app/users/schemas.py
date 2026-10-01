
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.models.enums import Role


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    role: Role = Role.RIDER


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    role: Optional[Role] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    role: Role

    class Config:
        from_attributes = True