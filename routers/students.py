from typing import List
from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from db.database import get_db

from crud import student as student_crud

from schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return student_crud.create_student(
        db,
        student
    )


@router.get(
    "/",
    response_model=List[StudentResponse]
)
def get_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return student_crud.get_students(
        db,
        skip,
        limit
    )


@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: UUID,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student_by_id(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: UUID,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = student_crud.update_student(
        db,
        student_id,
        student_data
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: UUID,
    db: Session = Depends(get_db)
):
    student = student_crud.delete_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return None