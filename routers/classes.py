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

from crud.classes import (
    create_class,
    get_classes,
    get_class_by_id,
    update_class,
    delete_class
)

from schemas.classes import (
    ClassCreate,
    ClassUpdate,
    ClassResponse
)

router = APIRouter(
    prefix="/classes",
    tags=["Classes"]
)


@router.post(
    "/",
    response_model=ClassResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_class(
    class_data: ClassCreate,
    db: Session = Depends(get_db)
):
    return create_class(
        db=db,
        class_data=class_data
    )


@router.get(
    "/",
    response_model=List[ClassResponse]
)
def read_all_classes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_classes(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{class_id}",
    response_model=ClassResponse
)
def read_class(
    class_id: UUID,
    db: Session = Depends(get_db)
):
    db_class = get_class_by_id(
        db=db,
        class_id=class_id
    )

    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found"
        )

    return db_class


@router.put(
    "/{class_id}",
    response_model=ClassResponse
)
def update_existing_class(
    class_id: UUID,
    class_data: ClassUpdate,
    db: Session = Depends(get_db)
):
    db_class = update_class(
        db=db,
        class_id=class_id,
        class_data=class_data
    )

    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found"
        )

    return db_class


@router.delete(
    "/{class_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_class(
    class_id: UUID,
    db: Session = Depends(get_db)
):
    db_class = delete_class(
        db=db,
        class_id=class_id
    )

    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found"
        )

    return None