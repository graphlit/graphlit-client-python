# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ViewExists(BaseModel):
    view_exists: Optional["ViewExistsViewExists"] = Field(alias="viewExists")


class ViewExistsViewExists(BaseModel):
    result: Optional[bool]


ViewExists.model_rebuild()
