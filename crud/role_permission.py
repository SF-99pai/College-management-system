from sqlalchemy.orm import Session

from models.role_permission import RolePermission
from schemas.role_permission import (
    RolePermissionCreate,
    RolePermissionUpdate
)


def create_role_permission(
    db: Session,
    role_permission: RolePermissionCreate
):
    db_role = RolePermission(
        **role_permission.model_dump()
    )

    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    return db_role


def get_role_permissions(
    db: Session
):
    return db.query(RolePermission).all()


def get_role_permission_by_id(
    db: Session,
    role_id
):
    return (
        db.query(RolePermission)
        .filter(RolePermission.role_id == role_id)
        .first()
    )


def update_role_permission(
    db: Session,
    role_id,
    role_data: RolePermissionUpdate
):
    db_role = get_role_permission_by_id(
        db,
        role_id
    )

    if not db_role:
        return None

    update_data = role_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)

    return db_role


def delete_role_permission(
    db: Session,
    role_id
):
    db_role = get_role_permission_by_id(
        db,
        role_id
    )

    if not db_role:
        return None

    db.delete(db_role)
    db.commit()

    return db_role