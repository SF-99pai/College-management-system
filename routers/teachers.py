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

from crud import teacher as teacher_crud

from schemas.teacher import (
    TeacherCreate,
    TeacherUpdate,
    TeacherResponse
)

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@router.post(
    "/",
    response_model=TeacherResponse,
    status_code=status.HTTP_201_CREATED
)
def create_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    return teacher_crud.create_teacher(
        db,
        teacher
    )


@router.get(
    "/",
    response_model=List[TeacherResponse]
)
def get_teachers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return teacher_crud.get_teachers(
        db,
        skip,
        limit
    )


@router.get(
    "/{teacher_id}",
    response_model=TeacherResponse
)
def get_teacher(
    teacher_id: UUID,
    db: Session = Depends(get_db)
):
    teacher = teacher_crud.get_teacher_by_id(
        db,
        teacher_id
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher


@router.put(
    "/{teacher_id}",
    response_model=TeacherResponse
)
def update_teacher(
    teacher_id: UUID,
    teacher_data: TeacherUpdate,
    db: Session = Depends(get_db)
):
    teacher = teacher_crud.update_teacher(
        db,
        teacher_id,
        teacher_data
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher


@router.delete(
    "/{teacher_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_teacher(
    teacher_id: UUID,
    db: Session = Depends(get_db)
):
    teacher = teacher_crud.delete_teacher(
        db,
        teacher_id
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return None