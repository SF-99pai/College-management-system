from uuid import UUID
from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel


class AttendanceBase(BaseModel):
    student_id: UUID
    class_id: UUID
    dates: date
    status: Literal["Present", "Absent", "Late"]


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    student_id: Optional[UUID] = None
    class_id: Optional[UUID] = None
    dates: Optional[date] = None
    status: Optional[
        Literal["Present", "Absent", "Late"]
    ] = None


class AttendanceResponse(AttendanceBase):
    attendance_id: UUID

    class Config:
        from_attributes = True