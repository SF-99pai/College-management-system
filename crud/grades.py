from sqlalchemy.orm import Session

from models.grades import Grade
from schemas.grades import (
    GradeCreate,
    GradeUpdate
)


def create_grade(
    db: Session,
    grade: GradeCreate
):
    db_grade = Grade(
        **grade.model_dump()
    )

    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)

    return db_grade


def get_grades(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Grade)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_grade_by_id(
    db: Session,
    grade_id
):
    return (
        db.query(Grade)
        .filter(Grade.grade_id == grade_id)
        .first()
    )


def update_grade(
    db: Session,
    grade_id,
    grade_data: GradeUpdate
):
    grade = get_grade_by_id(
        db,
        grade_id
    )

    if not grade:
        return None

    update_data = grade_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(grade, key, value)

    db.commit()
    db.refresh(grade)

    return grade


def delete_grade(
    db: Session,
    grade_id
):
    grade = get_grade_by_id(
        db,
        grade_id
    )

    if not grade:
        return None

    db.delete(grade)
    db.commit()

    return grade