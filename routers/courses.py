from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db

from crud.course import (
    create_course,
    get_courses,
    get_course_by_id,
    update_course,
    delete_course
)

from schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return create_course(
        db=db,
        course=course
    )


@router.get(
    "/",
    response_model=List[CourseResponse]
)
def read_all_courses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_courses(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def read_course(
    course_id: UUID,
    db: Session = Depends(get_db)
):
    course = get_course_by_id(
        db=db,
        course_id=course_id
    )

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    return course


@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
def update_existing_course(
    course_id: UUID,
    course_data: CourseUpdate,
    db: Session = Depends(get_db)
):
    course = update_course(
        db=db,
        course_id=course_id,
        course_data=course_data
    )

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    return course


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_course(
    course_id: UUID,
    db: Session = Depends(get_db)
):
    course = delete_course(
        db=db,
        course_id=course_id
    )

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    return None