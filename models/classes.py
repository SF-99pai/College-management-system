import uuid

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class Class(Base):
    __tablename__ = "classes"

    class_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    course_id = Column(
        UUID(as_uuid=True),
        ForeignKey("courses.course_id"),
        nullable=False
    )

    teacher_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teachers.teacher_id"),
        nullable=False
    )

    semester = Column(
        String(20),
        nullable=False
    )

    academic_year = Column(
        Integer,
        nullable=False
    )

    room_number = Column(
        String(20),
        nullable=False
    )

    schedule_time = Column(
        String(50),
        nullable=False
    )