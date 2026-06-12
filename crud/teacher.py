from sqlalchemy.orm import Session

from models.teacher import Teacher
from schemas.teacher import (
    TeacherCreate,
    TeacherUpdate
)


def create_teacher(
    db: Session,
    teacher: TeacherCreate
):
    db_teacher = Teacher(
        **teacher.model_dump()
    )

    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)

    return db_teacher


def get_teachers(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Teacher)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_teacher_by_id(
    db: Session,
    teacher_id
):
    return (
        db.query(Teacher)
        .filter(
            Teacher.teacher_id == teacher_id
        )
        .first()
    )


def update_teacher(
    db: Session,
    teacher_id,
    teacher_data: TeacherUpdate
):
    teacher = get_teacher_by_id(
        db,
        teacher_id
    )

    if not teacher:
        return None

    update_data = teacher_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(teacher, key, value)

    db.commit()
    db.refresh(teacher)

    return teacher


def delete_teacher(
    db: Session,
    teacher_id
):
    teacher = get_teacher_by_id(
        db,
        teacher_id
    )

    if not teacher:
        return None

    db.delete(teacher)
    db.commit()

    return teacher