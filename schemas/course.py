from uuid import UUID
from typing import Optional

from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    course_code: str
    course_name: str
    credits: int = Field(..., gt=0)
    teacher_id: Optional[UUID] = None


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    course_code: Optional[str] = None
    course_name: Optional[str] = None
    credits: Optional[int] = Field(None, gt=0)
    teacher_id: Optional[UUID] = None

class CourseResponse(CourseBase):
    course_id: UUID

    class Config:
        from_attributes = True