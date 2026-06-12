from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class ClassBase(BaseModel):
    course_id: UUID
    teacher_id: UUID
    semester: str
    academic_year: int
    room_number: str
    schedule_time: str


class ClassCreate(ClassBase):
    pass


class ClassUpdate(BaseModel):
    course_id: Optional[UUID] = None
    teacher_id: Optional[UUID] = None
    semester: Optional[str] = None
    academic_year: Optional[int] = None
    room_number: Optional[str] = None
    schedule_time: Optional[str] = None


class ClassResponse(ClassBase):
    class_id: UUID

    class Config:
        from_attributes = True