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

from crud.grades import (
    create_grade,
    get_grades,
    get_grade_by_id,
    update_grade,
    delete_grade
)

from schemas.grades import (
    GradeCreate,
    GradeUpdate,
    GradeResponse
)

router = APIRouter(
    prefix="/grades",
    tags=["Grades"]
)


@router.post(
    "/",
    response_model=GradeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_grade(
    grade: GradeCreate,
    db: Session = Depends(get_db)
):
    return create_grade(
        db=db,
        grade=grade
    )


@router.get(
    "/",
    response_model=List[GradeResponse]
)
def read_all_grades(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_grades(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{grade_id}",
    response_model=GradeResponse
)
def read_grade(
    grade_id: UUID,
    db: Session = Depends(get_db)
):
    grade = get_grade_by_id(
        db=db,
        grade_id=grade_id
    )

    if not grade:
        raise HTTPException(
            status_code=404,
            detail="Grade not found"
        )

    return grade


@router.put(
    "/{grade_id}",
    response_model=GradeResponse
)
def update_existing_grade(
    grade_id: UUID,
    grade_data: GradeUpdate,
    db: Session = Depends(get_db)
):
    grade = update_grade(
        db=db,
        grade_id=grade_id,
        grade_data=grade_data
    )

    if not grade:
        raise HTTPException(
            status_code=404,
            detail="Grade not found"
        )

    return grade


@router.delete(
    "/{grade_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_grade(
    grade_id: UUID,
    db: Session = Depends(get_db)
):
    grade = delete_grade(
        db=db,
        grade_id=grade_id
    )

    if not grade:
        raise HTTPException(
            status_code=404,
            detail="Grade not found"
        )

    return None