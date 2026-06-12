from sqlalchemy.orm import Session

from models.student import Student
from schemas.student import (
    StudentCreate,
    StudentUpdate
)


def create_student(
    db: Session,
    student: StudentCreate
):
    db_student = Student(
        **student.model_dump()
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Student)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_student_by_id(
    db: Session,
    student_id
):
    return (
        db.query(Student)
        .filter(
            Student.student_id == student_id
        )
        .first()
    )


def update_student(
    db: Session,
    student_id,
    student_data: StudentUpdate
):
    student = get_student_by_id(
        db,
        student_id
    )

    if not student:
        return None

    update_data = student_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


def delete_student(
    db: Session,
    student_id
):
    student = get_student_by_id(
        db,
        student_id
    )

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student