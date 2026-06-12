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

from crud.attendance import (
    create_attendance,
    get_attendance_records,
    get_attendance_by_id,
    update_attendance,
    delete_attendance
)

from schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post(
    "/",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return create_attendance(
        db=db,
        attendance=attendance
    )


@router.get(
    "/",
    response_model=List[AttendanceResponse]
)
def read_all_attendance(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_attendance_records(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{attendance_id}",
    response_model=AttendanceResponse
)
def read_attendance(
    attendance_id: UUID,
    db: Session = Depends(get_db)
):
    attendance = get_attendance_by_id(
        db,
        attendance_id
    )

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance


@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponse
)
def update_existing_attendance(
    attendance_id: UUID,
    attendance_data: AttendanceUpdate,
    db: Session = Depends(get_db)
):
    attendance = update_attendance(
        db,
        attendance_id,
        attendance_data
    )

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance


@router.delete(
    "/{attendance_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_attendance(
    attendance_id: UUID,
    db: Session = Depends(get_db)
):
    attendance = delete_attendance(
        db,
        attendance_id
    )

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return None