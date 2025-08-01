# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryNotionPages(BaseModel):
    notion_pages: Optional["QueryNotionPagesNotionPages"] = Field(alias="notionPages")


class QueryNotionPagesNotionPages(BaseModel):
    results: Optional[List[Optional["QueryNotionPagesNotionPagesResults"]]]


class QueryNotionPagesNotionPagesResults(BaseModel):
    name: Optional[str]
    identifier: Optional[str]


QueryNotionPages.model_rebuild()
QueryNotionPagesNotionPages.model_rebuild()
