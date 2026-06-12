from sqlalchemy.orm import Session

from models.attendance import Attendance

from schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate
)


def create_attendance(
    db: Session,
    attendance: AttendanceCreate
):
    db_attendance = Attendance(
        **attendance.model_dump()
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def get_attendance_records(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Attendance)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_attendance_by_id(
    db: Session,
    attendance_id
):
    return (
        db.query(Attendance)
        .filter(
            Attendance.attendance_id == attendance_id
        )
        .first()
    )


def update_attendance(
    db: Session,
    attendance_id,
    attendance_data: AttendanceUpdate
):
    attendance = get_attendance_by_id(
        db,
        attendance_id
    )

    if not attendance:
        return None

    update_data = attendance_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(attendance, key, value)

    db.commit()
    db.refresh(attendance)

    return attendance


def delete_attendance(
    db: Session,
    attendance_id
):
    attendance = get_attendance_by_id(
        db,
        attendance_id
    )

    if not attendance:
        return None

    db.delete(attendance)
    db.commit()

    return attendance