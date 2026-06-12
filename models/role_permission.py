import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    role_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    permission_level = Column(
        String(50),
        nullable=False
    )