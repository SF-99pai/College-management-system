import uuid
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("students.student_id"),
        nullable=False
    )

    class_id = Column(
        UUID(as_uuid=True),
        ForeignKey("classes.class_id"),
        nullable=False
    )

    