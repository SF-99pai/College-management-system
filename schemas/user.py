from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    
  

class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


class UserResponse(UserBase):
    user_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True