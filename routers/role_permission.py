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

from crud import role_permission as rp_crud

from schemas.role_permission import (
    RolePermissionCreate,
    RolePermissionUpdate,
    RolePermissionResponse
)

router = APIRouter(
    prefix="/role-permissions",
    tags=["Role Permissions"]
)


@router.post(
    "/",
    response_model=RolePermissionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_role_permission(
    role_permission: RolePermissionCreate,
    db: Session = Depends(get_db)
):
    return rp_crud.create_role_permission(
        db,
        role_permission
    )


@router.get(
    "/",
    response_model=List[RolePermissionResponse]
)
def get_role_permissions(
    db: Session = Depends(get_db)
):
    return rp_crud.get_role_permissions(db)


@router.get(
    "/{role_id}",
    response_model=RolePermissionResponse
)
def get_role_permission(
    role_id: UUID,
    db: Session = Depends(get_db)
):
    role = rp_crud.get_role_permission_by_id(
        db,
        role_id
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


@router.put(
    "/{role_id}",
    response_model=RolePermissionResponse
)
def update_role_permission(
    role_id: UUID,
    role_data: RolePermissionUpdate,
    db: Session = Depends(get_db)
):
    role = rp_crud.update_role_permission(
        db,
        role_id,
        role_data
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


@router.delete(
    "/{role_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_role_permission(
    role_id: UUID,
    db: Session = Depends(get_db)
):
    role = rp_crud.delete_role_permission(
        db,
        role_id
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return None