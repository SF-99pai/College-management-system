
from sqlalchemy.orm import Session

from models.course import Course
from schemas.course import CourseCreate, CourseUpdate


def create_course(
    db: Session,
    course: CourseCreate
):
    print(course.model_dump())
    db_course = Course(
        **course.model_dump()
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course

def get_courses(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Course)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_course_by_id(
    db: Session,
    course_id
):
    return (
        db.query(Course)
        .filter(Course.course_id == course_id)
        .first()
    )

def update_course(
    db: Session,
    course_id,
    course_data: CourseUpdate
):
    course = get_course_by_id(
        db,
        course_id
    )

    if not course:
        return None

    update_data = course_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course

def delete_course(
    db: Session,
    course_id
):
    course = get_course_by_id(
        db,
        course_id
    )

    if not course:
        return None

    db.delete(course)
    db.commit()

    return course

