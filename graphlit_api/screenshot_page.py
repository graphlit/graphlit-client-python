# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ContentTypes, EntityState, FileTypes


class ScreenshotPage(BaseModel):
    screenshot_page: Optional["ScreenshotPageScreenshotPage"] = Field(
        alias="screenshotPage"
    )


class ScreenshotPageScreenshotPage(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    uri: Optional[Any]
    collections: Optional[List[Optional["ScreenshotPageScreenshotPageCollections"]]]


class ScreenshotPageScreenshotPageCollections(BaseModel):
    id: str
    name: str


ScreenshotPage.model_rebuild()
ScreenshotPageScreenshotPage.model_rebuild()
