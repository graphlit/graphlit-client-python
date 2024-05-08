# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteSpecifications(BaseModel):
    delete_specifications: Optional[
        List[Optional["DeleteSpecificationsDeleteSpecifications"]]
    ] = Field(alias="deleteSpecifications")


class DeleteSpecificationsDeleteSpecifications(BaseModel):
    id: str
    state: EntityState


DeleteSpecifications.model_rebuild()