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

from crud.fee_payment import (
    create_fee_payment,
    get_fee_payments,
    get_fee_payment_by_id,
    update_fee_payment,
    delete_fee_payment
)

from schemas.fee_payment import (
    FeePaymentCreate,
    FeePaymentUpdate,
    FeePaymentResponse
)

router = APIRouter(
    prefix="/fee-payments",
    tags=["Fee Payments"]
)


@router.post(
    "/",
    response_model=FeePaymentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_fee_payment(
    payment: FeePaymentCreate,
    db: Session = Depends(get_db)
):
    return create_fee_payment(
        db=db,
        payment=payment
    )


@router.get(
    "/",
    response_model=List[FeePaymentResponse]
)
def read_all_fee_payments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_fee_payments(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{payment_id}",
    response_model=FeePaymentResponse
)
def read_fee_payment(
    payment_id: UUID,
    db: Session = Depends(get_db)
):
    payment = get_fee_payment_by_id(
        db=db,
        payment_id=payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.put(
    "/{payment_id}",
    response_model=FeePaymentResponse
)
def update_existing_fee_payment(
    payment_id: UUID,
    payment_data: FeePaymentUpdate,
    db: Session = Depends(get_db)
):
    payment = update_fee_payment(
        db=db,
        payment_id=payment_id,
        payment_data=payment_data
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.delete(
    "/{payment_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_fee_payment(
    payment_id: UUID,
    db: Session = Depends(get_db)
):
    payment = delete_fee_payment(
        db=db,
        payment_id=payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return None