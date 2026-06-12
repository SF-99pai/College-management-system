import uuid

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class Grade(Base):
    __tablename__ = "grades"

    grade_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("students.student_id"),
        nullable=False
    )

    enrollment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("enrollments.enrollment_id"),
        nullable=False
    )

    assessment_type = Column(
        String(100),
        nullable=False
    )

    marks = Column(
        Float,
        nullable=False
    )