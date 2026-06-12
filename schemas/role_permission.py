from uuid import UUID
from pydantic import BaseModel
from typing import Optional


class RolePermissionBase(BaseModel):
    role_name: str
    permission_level: str


class RolePermissionCreate(RolePermissionBase):
    pass


class RolePermissionUpdate(BaseModel):
    role_name: Optional[str] = None
    permission_level: Optional[str] = None


class RolePermissionResponse(RolePermissionBase):
    role_id: UUID

    class Config:
        from_attributes = True