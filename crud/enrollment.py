from sqlalchemy.orm import Session
from models.enrollment import Enrollment
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate

def create_enrollment(
    db: Session,
    enrollment_data: EnrollmentCreate
):
    db_enrollment = Enrollment(
        **enrollment_data.model_dump()
    )

    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)

    return db_enrollment

def get_enrollments(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Enrollment)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_enrollment_by_id(
    db: Session,
    enrollment_id
):
    return (
        db.query(Enrollment)
        .filter(Enrollment.enrollment_id == enrollment_id)
        .first()
    )

def update_enrollment(
    db: Session,
    enrollment_id,
    enrollment_data: EnrollmentUpdate
):
    db_enrollment = get_enrollment_by_id(
        db,
        enrollment_id
    )

    if not db_enrollment:
        return None

    update_data = enrollment_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_enrollment, key, value)

    db.commit()
    db.refresh(db_enrollment)

    return db_enrollment

def delete_enrollment(
    db: Session,
    enrollment_id
):
    db_enrollment = get_enrollment_by_id(
        db,
        enrollment_id
    )

    if not db_enrollment:
        return None

    db.delete(db_enrollment)
    db.commit()

    return db_enrollment
