# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteUser(BaseModel):
    delete_user: Optional["DeleteUserDeleteUser"] = Field(alias="deleteUser")


class DeleteUserDeleteUser(BaseModel):
    id: str
    state: EntityState


DeleteUser.model_rebuild()