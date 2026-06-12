from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db

from schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from crud import user as user_crud


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return user_crud.create_user(
        db,
        user
    )


@router.get(
    "/",
    response_model=List[UserResponse]
)
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return user_crud.get_users(
        db,
        skip,
        limit
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = user_crud.get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: UUID,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = user_crud.update_user(
        db,
        user_id,
        user_data
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = user_crud.delete_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return None