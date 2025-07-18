# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AssemblyAIModels,
    AzureDocumentIntelligenceModels,
    AzureDocumentIntelligenceVersions,
    ContentClassificationServiceTypes,
    ContentIndexingServiceTypes,
    ContentTypes,
    DeepgramModels,
    EntityEnrichmentServiceTypes,
    EntityExtractionServiceTypes,
    EntityState,
    FilePreparationServiceTypes,
    FileTypes,
    IntegrationServiceTypes,
    LinkTypes,
    MCPServerTypes,
    ObservableTypes,
    ReductoEnrichmentModes,
    ReductoExtractionModes,
    ReductoOcrModes,
    ReductoOcrSystems,
    RegexSourceTypes,
    StoragePolicyTypes,
    SummarizationTypes,
)


class UpsertWorkflow(BaseModel):
    upsert_workflow: Optional["UpsertWorkflowUpsertWorkflow"] = Field(
        alias="upsertWorkflow"
    )


class UpsertWorkflowUpsertWorkflow(BaseModel):
    id: str
    name: str
    state: EntityState
    ingestion: Optional["UpsertWorkflowUpsertWorkflowIngestion"]
    indexing: Optional["UpsertWorkflowUpsertWorkflowIndexing"]
    preparation: Optional["UpsertWorkflowUpsertWorkflowPreparation"]
    extraction: Optional["UpsertWorkflowUpsertWorkflowExtraction"]
    classification: Optional["UpsertWorkflowUpsertWorkflowClassification"]
    enrichment: Optional["UpsertWorkflowUpsertWorkflowEnrichment"]
    storage: Optional["UpsertWorkflowUpsertWorkflowStorage"]
    actions: Optional[List[Optional["UpsertWorkflowUpsertWorkflowActions"]]]


class UpsertWorkflowUpsertWorkflowIngestion(BaseModel):
    if_: Optional["UpsertWorkflowUpsertWorkflowIngestionIf"] = Field(alias="if")
    collections: Optional[
        List[Optional["UpsertWorkflowUpsertWorkflowIngestionCollections"]]
    ]
    observations: Optional[
        List[Optional["UpsertWorkflowUpsertWorkflowIngestionObservations"]]
    ]
    enable_email_collections: Optional[bool] = Field(alias="enableEmailCollections")


class UpsertWorkflowUpsertWorkflowIngestionIf(BaseModel):
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    formats: Optional[List[Optional[str]]]
    file_extensions: Optional[List[str]] = Field(alias="fileExtensions")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")


class UpsertWorkflowUpsertWorkflowIngestionCollections(BaseModel):
    id: str


class UpsertWorkflowUpsertWorkflowIngestionObservations(BaseModel):
    type: ObservableTypes
    observable: "UpsertWorkflowUpsertWorkflowIngestionObservationsObservable"


class UpsertWorkflowUpsertWorkflowIngestionObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class UpsertWorkflowUpsertWorkflowIndexing(BaseModel):
    jobs: Optional[List[Optional["UpsertWorkflowUpsertWorkflowIndexingJobs"]]]


class UpsertWorkflowUpsertWorkflowIndexingJobs(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowIndexingJobsConnector"]


class UpsertWorkflowUpsertWorkflowIndexingJobsConnector(BaseModel):
    type: Optional[ContentIndexingServiceTypes]
    content_type: Optional[ContentTypes] = Field(alias="contentType")
    file_type: Optional[FileTypes] = Field(alias="fileType")


class UpsertWorkflowUpsertWorkflowPreparation(BaseModel):
    enable_unblocked_capture: Optional[bool] = Field(alias="enableUnblockedCapture")
    disable_smart_capture: Optional[bool] = Field(alias="disableSmartCapture")
    summarizations: Optional[
        List[Optional["UpsertWorkflowUpsertWorkflowPreparationSummarizations"]]
    ]
    jobs: Optional[List[Optional["UpsertWorkflowUpsertWorkflowPreparationJobs"]]]


class UpsertWorkflowUpsertWorkflowPreparationSummarizations(BaseModel):
    type: SummarizationTypes
    specification: Optional[
        "UpsertWorkflowUpsertWorkflowPreparationSummarizationsSpecification"
    ]
    tokens: Optional[int]
    items: Optional[int]
    prompt: Optional[str]


class UpsertWorkflowUpsertWorkflowPreparationSummarizationsSpecification(BaseModel):
    id: str


class UpsertWorkflowUpsertWorkflowPreparationJobs(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnector"]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnector(BaseModel):
    type: FilePreparationServiceTypes
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    azure_document: Optional[
        "UpsertWorkflowUpsertWorkflowPreparationJobsConnectorAzureDocument"
    ] = Field(alias="azureDocument")
    deepgram: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorDeepgram"]
    assembly_ai: Optional[
        "UpsertWorkflowUpsertWorkflowPreparationJobsConnectorAssemblyAi"
    ] = Field(alias="assemblyAI")
    page: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorPage"]
    document: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorDocument"]
    email: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorEmail"]
    model_document: Optional[
        "UpsertWorkflowUpsertWorkflowPreparationJobsConnectorModelDocument"
    ] = Field(alias="modelDocument")
    reducto: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorReducto"]
    mistral: Optional["UpsertWorkflowUpsertWorkflowPreparationJobsConnectorMistral"]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorAzureDocument(BaseModel):
    version: Optional[AzureDocumentIntelligenceVersions]
    model: Optional[AzureDocumentIntelligenceModels]
    endpoint: Optional[Any]
    key: Optional[str]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorDeepgram(BaseModel):
    model: Optional[DeepgramModels]
    key: Optional[str]
    enable_redaction: Optional[bool] = Field(alias="enableRedaction")
    enable_speaker_diarization: Optional[bool] = Field(alias="enableSpeakerDiarization")
    detect_language: Optional[bool] = Field(alias="detectLanguage")
    language: Optional[str]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorAssemblyAi(BaseModel):
    model: Optional[AssemblyAIModels]
    key: Optional[str]
    enable_redaction: Optional[bool] = Field(alias="enableRedaction")
    enable_speaker_diarization: Optional[bool] = Field(alias="enableSpeakerDiarization")
    detect_language: Optional[bool] = Field(alias="detectLanguage")
    language: Optional[str]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorPage(BaseModel):
    enable_screenshot: Optional[bool] = Field(alias="enableScreenshot")


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorDocument(BaseModel):
    include_images: Optional[bool] = Field(alias="includeImages")


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorEmail(BaseModel):
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorModelDocument(BaseModel):
    specification: Optional[
        "UpsertWorkflowUpsertWorkflowPreparationJobsConnectorModelDocumentSpecification"
    ]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorModelDocumentSpecification(
    BaseModel
):
    id: str


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorReducto(BaseModel):
    ocr_mode: Optional[ReductoOcrModes] = Field(alias="ocrMode")
    ocr_system: Optional[ReductoOcrSystems] = Field(alias="ocrSystem")
    extraction_mode: Optional[ReductoExtractionModes] = Field(alias="extractionMode")
    enable_enrichment: Optional[bool] = Field(alias="enableEnrichment")
    enrichment_mode: Optional[ReductoEnrichmentModes] = Field(alias="enrichmentMode")
    key: Optional[str]


class UpsertWorkflowUpsertWorkflowPreparationJobsConnectorMistral(BaseModel):
    key: Optional[str]


class UpsertWorkflowUpsertWorkflowExtraction(BaseModel):
    jobs: Optional[List[Optional["UpsertWorkflowUpsertWorkflowExtractionJobs"]]]


class UpsertWorkflowUpsertWorkflowExtractionJobs(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowExtractionJobsConnector"]


class UpsertWorkflowUpsertWorkflowExtractionJobsConnector(BaseModel):
    type: EntityExtractionServiceTypes
    content_types: Optional[List[ContentTypes]] = Field(alias="contentTypes")
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    extracted_types: Optional[List[ObservableTypes]] = Field(alias="extractedTypes")
    extracted_count: Optional[int] = Field(alias="extractedCount")
    azure_text: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorAzureText"
    ] = Field(alias="azureText")
    azure_image: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorAzureImage"
    ] = Field(alias="azureImage")
    model_image: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelImage"
    ] = Field(alias="modelImage")
    model_text: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelText"
    ] = Field(alias="modelText")


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorAzureText(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    enable_pii: Optional[bool] = Field(alias="enablePII")


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorAzureImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelImage(BaseModel):
    specification: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelImageSpecification"
    ]


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelImageSpecification(
    BaseModel
):
    id: str


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelText(BaseModel):
    specification: Optional[
        "UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelTextSpecification"
    ]


class UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelTextSpecification(
    BaseModel
):
    id: str


class UpsertWorkflowUpsertWorkflowClassification(BaseModel):
    jobs: Optional[List[Optional["UpsertWorkflowUpsertWorkflowClassificationJobs"]]]


class UpsertWorkflowUpsertWorkflowClassificationJobs(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowClassificationJobsConnector"]


class UpsertWorkflowUpsertWorkflowClassificationJobsConnector(BaseModel):
    type: ContentClassificationServiceTypes
    content_type: Optional[ContentTypes] = Field(alias="contentType")
    file_type: Optional[FileTypes] = Field(alias="fileType")
    model: Optional["UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModel"]
    regex: Optional["UpsertWorkflowUpsertWorkflowClassificationJobsConnectorRegex"]


class UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModel(BaseModel):
    specification: Optional[
        "UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModelSpecification"
    ]
    rules: Optional[
        List[
            Optional[
                "UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModelRules"
            ]
        ]
    ]


class UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModelSpecification(
    BaseModel
):
    id: str


class UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModelRules(BaseModel):
    then: Optional[str]
    if_: Optional[str] = Field(alias="if")


class UpsertWorkflowUpsertWorkflowClassificationJobsConnectorRegex(BaseModel):
    rules: Optional[
        List[
            Optional[
                "UpsertWorkflowUpsertWorkflowClassificationJobsConnectorRegexRules"
            ]
        ]
    ]


class UpsertWorkflowUpsertWorkflowClassificationJobsConnectorRegexRules(BaseModel):
    then: Optional[str]
    type: Optional[RegexSourceTypes]
    path: Optional[str]
    matches: Optional[str]


class UpsertWorkflowUpsertWorkflowEnrichment(BaseModel):
    link: Optional["UpsertWorkflowUpsertWorkflowEnrichmentLink"]
    jobs: Optional[List[Optional["UpsertWorkflowUpsertWorkflowEnrichmentJobs"]]]


class UpsertWorkflowUpsertWorkflowEnrichmentLink(BaseModel):
    enable_crawling: Optional[bool] = Field(alias="enableCrawling")
    allowed_domains: Optional[List[str]] = Field(alias="allowedDomains")
    excluded_domains: Optional[List[str]] = Field(alias="excludedDomains")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")
    allowed_links: Optional[List[LinkTypes]] = Field(alias="allowedLinks")
    excluded_links: Optional[List[LinkTypes]] = Field(alias="excludedLinks")
    allowed_files: Optional[List[FileTypes]] = Field(alias="allowedFiles")
    excluded_files: Optional[List[FileTypes]] = Field(alias="excludedFiles")
    allowed_content_types: Optional[List[ContentTypes]] = Field(
        alias="allowedContentTypes"
    )
    excluded_content_types: Optional[List[ContentTypes]] = Field(
        alias="excludedContentTypes"
    )
    allow_content_domain: Optional[bool] = Field(alias="allowContentDomain")
    maximum_links: Optional[int] = Field(alias="maximumLinks")


class UpsertWorkflowUpsertWorkflowEnrichmentJobs(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowEnrichmentJobsConnector"]


class UpsertWorkflowUpsertWorkflowEnrichmentJobsConnector(BaseModel):
    type: Optional[EntityEnrichmentServiceTypes]
    enriched_types: Optional[List[Optional[ObservableTypes]]] = Field(
        alias="enrichedTypes"
    )
    fhir: Optional["UpsertWorkflowUpsertWorkflowEnrichmentJobsConnectorFhir"]
    diffbot: Optional["UpsertWorkflowUpsertWorkflowEnrichmentJobsConnectorDiffbot"]


class UpsertWorkflowUpsertWorkflowEnrichmentJobsConnectorFhir(BaseModel):
    endpoint: Optional[Any]


class UpsertWorkflowUpsertWorkflowEnrichmentJobsConnectorDiffbot(BaseModel):
    key: Optional[Any]


class UpsertWorkflowUpsertWorkflowStorage(BaseModel):
    policy: Optional["UpsertWorkflowUpsertWorkflowStoragePolicy"]


class UpsertWorkflowUpsertWorkflowStoragePolicy(BaseModel):
    type: Optional[StoragePolicyTypes]
    allow_duplicates: Optional[bool] = Field(alias="allowDuplicates")


class UpsertWorkflowUpsertWorkflowActions(BaseModel):
    connector: Optional["UpsertWorkflowUpsertWorkflowActionsConnector"]


class UpsertWorkflowUpsertWorkflowActionsConnector(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["UpsertWorkflowUpsertWorkflowActionsConnectorSlack"]
    email: Optional["UpsertWorkflowUpsertWorkflowActionsConnectorEmail"]
    twitter: Optional["UpsertWorkflowUpsertWorkflowActionsConnectorTwitter"]
    mcp: Optional["UpsertWorkflowUpsertWorkflowActionsConnectorMcp"]


class UpsertWorkflowUpsertWorkflowActionsConnectorSlack(BaseModel):
    token: str
    channel: str


class UpsertWorkflowUpsertWorkflowActionsConnectorEmail(BaseModel):
    from_: str = Field(alias="from")
    subject: str
    to: List[str]


class UpsertWorkflowUpsertWorkflowActionsConnectorTwitter(BaseModel):
    consumer_key: str = Field(alias="consumerKey")
    consumer_secret: str = Field(alias="consumerSecret")
    access_token_key: str = Field(alias="accessTokenKey")
    access_token_secret: str = Field(alias="accessTokenSecret")


class UpsertWorkflowUpsertWorkflowActionsConnectorMcp(BaseModel):
    token: Optional[str]
    type: MCPServerTypes


UpsertWorkflow.model_rebuild()
UpsertWorkflowUpsertWorkflow.model_rebuild()
UpsertWorkflowUpsertWorkflowIngestion.model_rebuild()
UpsertWorkflowUpsertWorkflowIngestionObservations.model_rebuild()
UpsertWorkflowUpsertWorkflowIndexing.model_rebuild()
UpsertWorkflowUpsertWorkflowIndexingJobs.model_rebuild()
UpsertWorkflowUpsertWorkflowPreparation.model_rebuild()
UpsertWorkflowUpsertWorkflowPreparationSummarizations.model_rebuild()
UpsertWorkflowUpsertWorkflowPreparationJobs.model_rebuild()
UpsertWorkflowUpsertWorkflowPreparationJobsConnector.model_rebuild()
UpsertWorkflowUpsertWorkflowPreparationJobsConnectorModelDocument.model_rebuild()
UpsertWorkflowUpsertWorkflowExtraction.model_rebuild()
UpsertWorkflowUpsertWorkflowExtractionJobs.model_rebuild()
UpsertWorkflowUpsertWorkflowExtractionJobsConnector.model_rebuild()
UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelImage.model_rebuild()
UpsertWorkflowUpsertWorkflowExtractionJobsConnectorModelText.model_rebuild()
UpsertWorkflowUpsertWorkflowClassification.model_rebuild()
UpsertWorkflowUpsertWorkflowClassificationJobs.model_rebuild()
UpsertWorkflowUpsertWorkflowClassificationJobsConnector.model_rebuild()
UpsertWorkflowUpsertWorkflowClassificationJobsConnectorModel.model_rebuild()
UpsertWorkflowUpsertWorkflowClassificationJobsConnectorRegex.model_rebuild()
UpsertWorkflowUpsertWorkflowEnrichment.model_rebuild()
UpsertWorkflowUpsertWorkflowEnrichmentJobs.model_rebuild()
UpsertWorkflowUpsertWorkflowEnrichmentJobsConnector.model_rebuild()
UpsertWorkflowUpsertWorkflowStorage.model_rebuild()
UpsertWorkflowUpsertWorkflowActions.model_rebuild()
UpsertWorkflowUpsertWorkflowActionsConnector.model_rebuild()
