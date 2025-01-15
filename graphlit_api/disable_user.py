# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DisableUser(BaseModel):
    disable_user: Optional["DisableUserDisableUser"] = Field(alias="disableUser")


class DisableUserDisableUser(BaseModel):
    id: str
    state: EntityState


DisableUser.model_rebuild()