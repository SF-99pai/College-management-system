from sqlalchemy.orm import Session
from models.classes import Class
from schemas.classes import ClassCreate
from schemas.classes import ClassCreate, ClassUpdate
def create_class(
    db: Session,
    class_data: ClassCreate
):
    db_class = Class(
        **class_data.model_dump()
    )

    db.add(db_class)
    db.commit()
    db.refresh(db_class)

    return db_class

def get_classes(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Class)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_class_by_id(
    db: Session,
    class_id
):
    return (
        db.query(Class)
        .filter(Class.class_id == class_id)
        .first()
    )

def update_class(
    db: Session,
    class_id,
    class_data: ClassUpdate
):
    db_class = get_class_by_id(
        db,
        class_id
    )

    if not db_class:
        return None

    update_data = class_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_class, key, value)

    db.commit()
    db.refresh(db_class)

    return db_class

def delete_class(
    db: Session,
    class_id
):
    db_class = get_class_by_id(
        db,
        class_id
    )

    if not db_class:
        return None

    db.delete(db_class)
    db.commit()

    return db_class