from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate, UserUpdate


def create_user(
    db: Session,
    user: UserCreate
):
    db_user = User(
        **user.model_dump()
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(User)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_user_by_id(
    db: Session,
    user_id
):
    return (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )


def update_user(
    db: Session,
    user_id,
    user_data: UserUpdate
):
    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    update_data = user_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id
):
    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user