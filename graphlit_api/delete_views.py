# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteViews(BaseModel):
    delete_views: Optional[List[Optional["DeleteViewsDeleteViews"]]] = Field(
        alias="deleteViews"
    )


class DeleteViewsDeleteViews(BaseModel):
    id: str
    state: EntityState


DeleteViews.model_rebuild()
