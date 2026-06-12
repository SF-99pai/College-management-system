import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    course_name = Column(
        String(255),
        nullable=False
    )

    course_code = Column(
        String(50),
        nullable=False,
        unique=True
    )
    teacher_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    credits = Column(
        Integer,
        nullable=False
    )

   
