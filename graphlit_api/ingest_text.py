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


class IngestText(BaseModel):
    ingest_text: Optional["IngestTextIngestText"] = Field(alias="ingestText")


class IngestTextIngestText(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    uri: Optional[Any]
    identifier: Optional[str]
    collections: Optional[List[Optional["IngestTextIngestTextCollections"]]]
    observations: Optional[List[Optional["IngestTextIngestTextObservations"]]]


class IngestTextIngestTextCollections(BaseModel):
    id: str
    name: str


class IngestTextIngestTextObservations(BaseModel):
    id: str
    type: ObservableTypes
    observable: "IngestTextIngestTextObservationsObservable"
    related: Optional["IngestTextIngestTextObservationsRelated"]
    related_type: Optional[ObservableTypes] = Field(alias="relatedType")
    relation: Optional[str]
    occurrences: Optional[List[Optional["IngestTextIngestTextObservationsOccurrences"]]]
    state: EntityState


class IngestTextIngestTextObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class IngestTextIngestTextObservationsRelated(BaseModel):
    id: str
    name: Optional[str]


class IngestTextIngestTextObservationsOccurrences(BaseModel):
    type: Optional[OccurrenceTypes]
    confidence: Optional[float]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_index: Optional[int] = Field(alias="pageIndex")
    bounding_box: Optional["IngestTextIngestTextObservationsOccurrencesBoundingBox"] = (
        Field(alias="boundingBox")
    )


class IngestTextIngestTextObservationsOccurrencesBoundingBox(BaseModel):
    left: Optional[float]
    top: Optional[float]
    width: Optional[float]
    height: Optional[float]


IngestText.model_rebuild()
IngestTextIngestText.model_rebuild()
IngestTextIngestTextObservations.model_rebuild()
IngestTextIngestTextObservationsOccurrences.model_rebuild()
