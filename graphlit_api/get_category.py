# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCategory(BaseModel):
    category: Optional["GetCategoryCategory"]


class GetCategoryCategory(BaseModel):
    id: str
    name: str
    description: Optional[str]
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]


GetCategory.model_rebuild()
