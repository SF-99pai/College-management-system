from sqlalchemy.orm import Session

from models.fee_payment import FeePayment

from schemas.fee_payment import (
    FeePaymentCreate,
    FeePaymentUpdate
)


def create_fee_payment(
    db: Session,
    payment: FeePaymentCreate
):
    db_payment = FeePayment(
        **payment.model_dump()
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment


def get_fee_payments(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(FeePayment)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_fee_payment_by_id(
    db: Session,
    payment_id
):
    return (
        db.query(FeePayment)
        .filter(
            FeePayment.payment_id == payment_id
        )
        .first()
    )


def update_fee_payment(
    db: Session,
    payment_id,
    payment_data: FeePaymentUpdate
):
    payment = get_fee_payment_by_id(
        db,
        payment_id
    )

    if not payment:
        return None

    update_data = payment_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(payment, key, value)

    db.commit()
    db.refresh(payment)

    return payment


def delete_fee_payment(
    db: Session,
    payment_id
):
    payment = get_fee_payment_by_id(
        db,
        payment_id
    )

    if not payment:
        return None

    db.delete(payment)
    db.commit()

    return payment

