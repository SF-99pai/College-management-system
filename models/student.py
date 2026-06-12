import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=False,
        unique=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    department = Column(
        String(100),
        nullable=False
    )