from uuid import UUID
from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel


class FeePaymentBase(BaseModel):
    student_id: UUID
    amount: float
    payment_date: date
    payment_status: Literal[
        "Paid",
        "Pending",
        "Failed"
    ]


class FeePaymentCreate(FeePaymentBase):
    pass


class FeePaymentUpdate(BaseModel):
    student_id: Optional[UUID] = None
    amount: Optional[float] = None
    payment_date: Optional[date] = None
    payment_status: Optional[
        Literal[
            "Paid",
            "Pending",
            "Failed"
        ]
    ] = None


class FeePaymentResponse(FeePaymentBase):
    payment_id: UUID

    class Config:
        from_attributes = True