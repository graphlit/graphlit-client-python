# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AlertTypes,
    ContentPublishingServiceTypes,
    ContentTypes,
    ElevenLabsModels,
    EntityState,
    FileTypes,
    IntegrationServiceTypes,
    MCPServerTypes,
    ObservableTypes,
    OpenAIImageModels,
)


class GetAlert(BaseModel):
    alert: Optional["GetAlertAlert"]


class GetAlertAlert(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "GetAlertAlertOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: AlertTypes
    summary_prompt: Optional[str] = Field(alias="summaryPrompt")
    publish_prompt: str = Field(alias="publishPrompt")
    filter: Optional["GetAlertAlertFilter"]
    integration: "GetAlertAlertIntegration"
    publishing: "GetAlertAlertPublishing"
    summary_specification: Optional["GetAlertAlertSummarySpecification"] = Field(
        alias="summarySpecification"
    )
    publish_specification: Optional["GetAlertAlertPublishSpecification"] = Field(
        alias="publishSpecification"
    )
    last_alert_date: Optional[Any] = Field(alias="lastAlertDate")


class GetAlertAlertOwner(BaseModel):
    id: str


class GetAlertAlertFilter(BaseModel):
    date_range: Optional["GetAlertAlertFilterDateRange"] = Field(alias="dateRange")
    in_last: Optional[Any] = Field(alias="inLast")
    creation_date_range: Optional["GetAlertAlertFilterCreationDateRange"] = Field(
        alias="creationDateRange"
    )
    created_in_last: Optional[Any] = Field(alias="createdInLast")
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    formats: Optional[List[Optional[str]]]
    file_extensions: Optional[List[str]] = Field(alias="fileExtensions")
    file_size_range: Optional["GetAlertAlertFilterFileSizeRange"] = Field(
        alias="fileSizeRange"
    )
    similar_contents: Optional[List["GetAlertAlertFilterSimilarContents"]] = Field(
        alias="similarContents"
    )
    contents: Optional[List["GetAlertAlertFilterContents"]]
    feeds: Optional[List["GetAlertAlertFilterFeeds"]]
    workflows: Optional[List["GetAlertAlertFilterWorkflows"]]
    collections: Optional[List["GetAlertAlertFilterCollections"]]
    users: Optional[List["GetAlertAlertFilterUsers"]]
    observations: Optional[List["GetAlertAlertFilterObservations"]]
    or_: Optional[List["GetAlertAlertFilterOr"]] = Field(alias="or")
    and_: Optional[List["GetAlertAlertFilterAnd"]] = Field(alias="and")


class GetAlertAlertFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetAlertAlertFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetAlertAlertFilterFileSizeRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetAlertAlertFilterSimilarContents(BaseModel):
    id: str


class GetAlertAlertFilterContents(BaseModel):
    id: str


class GetAlertAlertFilterFeeds(BaseModel):
    id: str


class GetAlertAlertFilterWorkflows(BaseModel):
    id: str


class GetAlertAlertFilterCollections(BaseModel):
    id: str


class GetAlertAlertFilterUsers(BaseModel):
    id: str


class GetAlertAlertFilterObservations(BaseModel):
    type: ObservableTypes
    observable: "GetAlertAlertFilterObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetAlertAlertFilterObservationsObservable(BaseModel):
    id: str


class GetAlertAlertFilterOr(BaseModel):
    feeds: Optional[List["GetAlertAlertFilterOrFeeds"]]
    workflows: Optional[List["GetAlertAlertFilterOrWorkflows"]]
    collections: Optional[List["GetAlertAlertFilterOrCollections"]]
    users: Optional[List["GetAlertAlertFilterOrUsers"]]
    observations: Optional[List["GetAlertAlertFilterOrObservations"]]


class GetAlertAlertFilterOrFeeds(BaseModel):
    id: str


class GetAlertAlertFilterOrWorkflows(BaseModel):
    id: str


class GetAlertAlertFilterOrCollections(BaseModel):
    id: str


class GetAlertAlertFilterOrUsers(BaseModel):
    id: str


class GetAlertAlertFilterOrObservations(BaseModel):
    type: ObservableTypes
    observable: "GetAlertAlertFilterOrObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetAlertAlertFilterOrObservationsObservable(BaseModel):
    id: str


class GetAlertAlertFilterAnd(BaseModel):
    feeds: Optional[List["GetAlertAlertFilterAndFeeds"]]
    workflows: Optional[List["GetAlertAlertFilterAndWorkflows"]]
    collections: Optional[List["GetAlertAlertFilterAndCollections"]]
    users: Optional[List["GetAlertAlertFilterAndUsers"]]
    observations: Optional[List["GetAlertAlertFilterAndObservations"]]


class GetAlertAlertFilterAndFeeds(BaseModel):
    id: str


class GetAlertAlertFilterAndWorkflows(BaseModel):
    id: str


class GetAlertAlertFilterAndCollections(BaseModel):
    id: str


class GetAlertAlertFilterAndUsers(BaseModel):
    id: str


class GetAlertAlertFilterAndObservations(BaseModel):
    type: ObservableTypes
    observable: "GetAlertAlertFilterAndObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetAlertAlertFilterAndObservationsObservable(BaseModel):
    id: str


class GetAlertAlertIntegration(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["GetAlertAlertIntegrationSlack"]
    email: Optional["GetAlertAlertIntegrationEmail"]
    twitter: Optional["GetAlertAlertIntegrationTwitter"]
    mcp: Optional["GetAlertAlertIntegrationMcp"]


class GetAlertAlertIntegrationSlack(BaseModel):
    token: str
    channel: str


class GetAlertAlertIntegrationEmail(BaseModel):
    from_: str = Field(alias="from")
    subject: str
    to: List[str]


class GetAlertAlertIntegrationTwitter(BaseModel):
    consumer_key: str = Field(alias="consumerKey")
    consumer_secret: str = Field(alias="consumerSecret")
    access_token_key: str = Field(alias="accessTokenKey")
    access_token_secret: str = Field(alias="accessTokenSecret")


class GetAlertAlertIntegrationMcp(BaseModel):
    token: Optional[str]
    type: MCPServerTypes


class GetAlertAlertPublishing(BaseModel):
    type: ContentPublishingServiceTypes
    eleven_labs: Optional["GetAlertAlertPublishingElevenLabs"] = Field(
        alias="elevenLabs"
    )
    open_ai_image: Optional["GetAlertAlertPublishingOpenAiImage"] = Field(
        alias="openAIImage"
    )


class GetAlertAlertPublishingElevenLabs(BaseModel):
    model: Optional[ElevenLabsModels]
    voice: Optional[str]


class GetAlertAlertPublishingOpenAiImage(BaseModel):
    model: Optional[OpenAIImageModels]
    count: Optional[int]
    seed: Optional["GetAlertAlertPublishingOpenAiImageSeed"]


class GetAlertAlertPublishingOpenAiImageSeed(BaseModel):
    id: str


class GetAlertAlertSummarySpecification(BaseModel):
    id: str


class GetAlertAlertPublishSpecification(BaseModel):
    id: str


GetAlert.model_rebuild()
GetAlertAlert.model_rebuild()
GetAlertAlertFilter.model_rebuild()
GetAlertAlertFilterObservations.model_rebuild()
GetAlertAlertFilterOr.model_rebuild()
GetAlertAlertFilterOrObservations.model_rebuild()
GetAlertAlertFilterAnd.model_rebuild()
GetAlertAlertFilterAndObservations.model_rebuild()
GetAlertAlertIntegration.model_rebuild()
GetAlertAlertPublishing.model_rebuild()
GetAlertAlertPublishingOpenAiImage.model_rebuild()
