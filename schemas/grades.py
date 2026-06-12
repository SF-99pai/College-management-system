from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class GradeBase(BaseModel):
    student_id: UUID
    enrollment_id: UUID
    assessment_type: str
    marks: float


class GradeCreate(GradeBase):
    pass


class GradeUpdate(BaseModel):
    student_id: Optional[UUID] = None
    enrollment_id: Optional[UUID] = None
    assessment_type: Optional[str] = None
    marks: Optional[float] = None


class GradeResponse(GradeBase):
    grade_id: UUID

    class Config:
        from_attributes = True