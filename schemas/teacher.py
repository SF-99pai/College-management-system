from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    department: str


class TeacherCreate(TeacherBase):
    user_id: UUID


class TeacherUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    department: Optional[str] = None


class TeacherResponse(TeacherBase):
    teacher_id: UUID
    user_id: UUID

    class Config:
        from_attributes = True