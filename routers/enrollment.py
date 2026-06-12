from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  
from db.database import get_db
from crud.enrollment import create_enrollment, get_enrollments, get_enrollment_by_id, delete_enrollment
from schemas.enrollment import EnrollmentCreate, EnrollmentResponse
router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)   

@router.post("/", response_model=EnrollmentResponse)
def create_enrollment_endpoint(
    enrollment_data: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    return create_enrollment(
        db,
        enrollment_data
    )

@router.get("/", response_model=List[EnrollmentResponse])
def get_all_enrollments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_enrollments(db, skip=skip, limit=limit)

def get_enrollment(
    enrollment_id: UUID,
    db: Session = Depends(get_db)
):
    enrollment = get_enrollment_by_id(db, enrollment_id)

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment

@router.delete("/{enrollment_id}")
def delete_enrollment_endpoint(
    enrollment_id: UUID,
    db: Session = Depends(get_db)
):
    enrollment = get_enrollment_by_id(db, enrollment_id)

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    delete_enrollment(db, enrollment_id)

    return {"detail": "Enrollment deleted successfully"}