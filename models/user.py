import uuid

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from db.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    username = Column(
        String(100),
        nullable=False,
        unique=True
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    full_name = Column(
        String(255),
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )