from uuid import UUID
from typing import Optional
from datetime import date

from pydantic import BaseModel

class EnrollmentBase(BaseModel):
    student_id: UUID
    class_id: UUID
    
class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentUpdate(BaseModel):
    student_id: Optional[UUID] = None
    class_id: Optional[UUID] = None
   

class EnrollmentResponse(EnrollmentBase):
    enrollment_id: UUID

    class Config:
        from_attributes = True
