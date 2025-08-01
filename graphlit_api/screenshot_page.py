# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentTypes,
    EntityState,
    FileTypes,
    ObservableTypes,
    OccurrenceTypes,
)


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
    identifier: Optional[str]
    collections: Optional[List[Optional["ScreenshotPageScreenshotPageCollections"]]]
    observations: Optional[List[Optional["ScreenshotPageScreenshotPageObservations"]]]


class ScreenshotPageScreenshotPageCollections(BaseModel):
    id: str
    name: str


class ScreenshotPageScreenshotPageObservations(BaseModel):
    id: str
    type: ObservableTypes
    observable: "ScreenshotPageScreenshotPageObservationsObservable"
    related: Optional["ScreenshotPageScreenshotPageObservationsRelated"]
    related_type: Optional[ObservableTypes] = Field(alias="relatedType")
    relation: Optional[str]
    occurrences: Optional[
        List[Optional["ScreenshotPageScreenshotPageObservationsOccurrences"]]
    ]
    state: EntityState


class ScreenshotPageScreenshotPageObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class ScreenshotPageScreenshotPageObservationsRelated(BaseModel):
    id: str
    name: Optional[str]


class ScreenshotPageScreenshotPageObservationsOccurrences(BaseModel):
    type: Optional[OccurrenceTypes]
    confidence: Optional[float]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_index: Optional[int] = Field(alias="pageIndex")
    bounding_box: Optional[
        "ScreenshotPageScreenshotPageObservationsOccurrencesBoundingBox"
    ] = Field(alias="boundingBox")


class ScreenshotPageScreenshotPageObservationsOccurrencesBoundingBox(BaseModel):
    left: Optional[float]
    top: Optional[float]
    width: Optional[float]
    height: Optional[float]


ScreenshotPage.model_rebuild()
ScreenshotPageScreenshotPage.model_rebuild()
ScreenshotPageScreenshotPageObservations.model_rebuild()
ScreenshotPageScreenshotPageObservationsOccurrences.model_rebuild()
