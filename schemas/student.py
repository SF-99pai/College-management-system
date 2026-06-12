from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    department: str
    


class StudentCreate(StudentBase):
    user_id: UUID


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    department: Optional[str] = None


class StudentResponse(StudentBase):
    student_id: UUID
    user_id: UUID
    department: str

    class Config:
        from_attributes = True