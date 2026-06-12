import uuid

from sqlalchemy import Column, String, Date, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class FeePayment(Base):
    __tablename__ = "fee_payments"

    payment_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("students.student_id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_date = Column(
        Date,
        nullable=False
    )

    payment_status = Column(
        String(20),
        nullable=False
    )