# Graphlit Python SDK Reference

This is the complete API reference for the Graphlit Python SDK (`graphlit-client`).

All methods are async and called on `graphlit.client`.


## Setup

```python
from graphlit import Graphlit
from graphlit_api import *

graphlit = Graphlit()
```

## Operations

### count_alerts

```python
await graphlit.client.count_alerts(filter: Optional[AlertFilter], correlation_id: Optional[str]) -> CountAlerts
```

**Response:**
```
response.count_alerts
  .count: Optional[Any]
```

### create_alert

```python
await graphlit.client.create_alert(alert: AlertInput, correlation_id: Optional[str]) -> CreateAlert
```

**Response:**
```
response.create_alert
  .id: str
  .name: str
  .state: EntityState
  .type: AlertTypes
```

### delete_alert

```python
await graphlit.client.delete_alert(id: str) -> DeleteAlert
```

**Response:**
```
response.delete_alert
  .id: str
  .state: EntityState
```

### delete_alerts

```python
await graphlit.client.delete_alerts(ids: list[str], is_synchronous: Optional[bool]) -> DeleteAlerts
```

**Response:**
```
response.delete_alerts
  .id: str
  .state: EntityState
```

### delete_all_alerts

```python
await graphlit.client.delete_all_alerts(
    filter: Optional[AlertFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllAlerts
```

**Response:**
```
response.delete_all_alerts
  .id: str
  .state: EntityState
```

### disable_alert

```python
await graphlit.client.disable_alert(id: str) -> DisableAlert
```

**Response:**
```
response.disable_alert
  .id: str
  .state: EntityState
```

### enable_alert

```python
await graphlit.client.enable_alert(id: str) -> EnableAlert
```

**Response:**
```
response.enable_alert
  .id: str
  .state: EntityState
```

### get_alert

```python
await graphlit.client.get_alert(id: str, correlation_id: Optional[str]) -> GetAlert
```

**Response:**
```
response.alert
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetAlertAlertOwner"
  .state: EntityState
  .correlation_id: Optional[str]
  .type: AlertTypes
```

### query_alerts

```python
await graphlit.client.query_alerts(filter: Optional[AlertFilter], correlation_id: Optional[str]) -> QueryAlerts
```

**Response:**
```
response.alerts
  .results: Optional[list["QueryAlertsAlertsResults"]]
```

### update_alert

```python
await graphlit.client.update_alert(alert: AlertUpdateInput) -> UpdateAlert
```

**Response:**
```
response.update_alert
  .id: str
  .name: str
  .state: EntityState
  .type: AlertTypes
```

### upsert_alert

```python
await graphlit.client.upsert_alert(alert: AlertInput) -> UpsertAlert
```

**Response:**
```
response.upsert_alert
  .id: str
  .name: str
  .state: EntityState
  .type: AlertTypes
```

### count_categories

```python
await graphlit.client.count_categories(filter: Optional[CategoryFilter], correlation_id: Optional[str]) -> CountCategories
```

**Response:**
```
response.count_categories
  .count: Optional[Any]
```

### create_category

```python
await graphlit.client.create_category(category: CategoryInput) -> CreateCategory
```

**Response:**
```
response.create_category
  .id: str
  .name: str
```

### delete_all_categories

```python
await graphlit.client.delete_all_categories(
    filter: Optional[CategoryFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllCategories
```

**Response:**
```
response.delete_all_categories
  .id: str
  .state: EntityState
```

### delete_categories

```python
await graphlit.client.delete_categories(ids: list[str], is_synchronous: Optional[bool]) -> DeleteCategories
```

**Response:**
```
response.delete_categories
  .id: str
  .state: EntityState
```

### delete_category

```python
await graphlit.client.delete_category(id: str) -> DeleteCategory
```

**Response:**
```
response.delete_category
  .id: str
  .state: EntityState
```

### get_category

```python
await graphlit.client.get_category(id: str, correlation_id: Optional[str]) -> GetCategory
```

**Response:**
```
response.category
  .id: str
  .name: str
  .description: Optional[str]
  .creation_date: Any
  .feeds: Optional[list[Optional["GetCategoryCategoryFeeds"]]]
```

### query_categories

```python
await graphlit.client.query_categories(filter: Optional[CategoryFilter], correlation_id: Optional[str]) -> QueryCategories
```

**Response:**
```
response.categories
  .results: Optional[list[Optional["QueryCategoriesCategoriesResults"]]]
```

### update_category

```python
await graphlit.client.update_category(category: CategoryUpdateInput) -> UpdateCategory
```

**Response:**
```
response.update_category
  .id: str
  .name: str
```

### upsert_category

```python
await graphlit.client.upsert_category(category: CategoryInput) -> UpsertCategory
```

**Response:**
```
response.upsert_category
  .id: str
  .name: str
```

### add_contents_to_collections

```python
await graphlit.client.add_contents_to_collections(contents: list[EntityReferenceInput], collections: list[EntityReferenceInput]) -> AddContentsToCollections
```

**Response:**
```
response.add_contents_to_collections
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
  .contents: Optional[
```

### add_conversations_to_collections

```python
await graphlit.client.add_conversations_to_collections(conversations: list[EntityReferenceInput], collections: list[EntityReferenceInput]) -> AddConversationsToCollections
```

**Response:**
```
response.add_conversations_to_collections
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
  .contents: Optional[
```

### count_collections

```python
await graphlit.client.count_collections(filter: Optional[CollectionFilter], correlation_id: Optional[str]) -> CountCollections
```

**Response:**
```
response.count_collections
  .count: Optional[Any]
```

### create_collection

```python
await graphlit.client.create_collection(collection: CollectionInput) -> CreateCollection
```

**Response:**
```
response.create_collection
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
```

### delete_all_collections

```python
await graphlit.client.delete_all_collections(
    filter: Optional[CollectionFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllCollections
```

**Response:**
```
response.delete_all_collections
  .id: str
  .state: EntityState
```

### delete_collection

```python
await graphlit.client.delete_collection(id: str) -> DeleteCollection
```

**Response:**
```
response.delete_collection
  .id: str
  .state: EntityState
```

### delete_collections

```python
await graphlit.client.delete_collections(ids: list[str], is_synchronous: Optional[bool]) -> DeleteCollections
```

**Response:**
```
response.delete_collections
  .id: str
  .state: EntityState
```

### get_collection

```python
await graphlit.client.get_collection(id: str, correlation_id: Optional[str]) -> GetCollection
```

**Response:**
```
response.collection
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetCollectionCollectionOwner"
  .state: EntityState
  .type: Optional[CollectionTypes]
  .contents: Optional[list[Optional["GetCollectionCollectionContents"]]]
```

### query_collections

```python
await graphlit.client.query_collections(filter: Optional[CollectionFilter], correlation_id: Optional[str]) -> QueryCollections
```

**Response:**
```
response.collections
  .results: Optional[list["QueryCollectionsCollectionsResults"]]
```

### remove_contents_from_collection

```python
await graphlit.client.remove_contents_from_collection(contents: list[EntityReferenceInput], collection: EntityReferenceInput) -> RemoveContentsFromCollection
```

**Response:**
```
response.remove_contents_from_collection
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
  .contents: Optional[
```

### remove_conversations_from_collection

```python
await graphlit.client.remove_conversations_from_collection(conversations: list[EntityReferenceInput], collection: EntityReferenceInput) -> RemoveConversationsFromCollection
```

**Response:**
```
response.remove_conversations_from_collection
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
  .contents: Optional[
```

### update_collection

```python
await graphlit.client.update_collection(collection: CollectionUpdateInput) -> UpdateCollection
```

**Response:**
```
response.update_collection
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[CollectionTypes]
```

### count_connectors

```python
await graphlit.client.count_connectors(filter: Optional[ConnectorFilter], correlation_id: Optional[str]) -> CountConnectors
```

**Response:**
```
response.count_connectors
  .count: Optional[Any]
```

### create_connector

```python
await graphlit.client.create_connector(connector: ConnectorInput) -> CreateConnector
```

**Response:**
```
response.create_connector
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConnectorTypes]
```

### delete_connector

```python
await graphlit.client.delete_connector(id: str) -> DeleteConnector
```

**Response:**
```
response.delete_connector
  .id: str
  .state: EntityState
```

### get_connector

```python
await graphlit.client.get_connector(id: str, correlation_id: Optional[str]) -> GetConnector
```

**Response:**
```
response.connector
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetConnectorConnectorOwner"
  .state: EntityState
  .type: Optional[ConnectorTypes]
  .authentication: Optional["GetConnectorConnectorAuthentication"]
```

### query_connectors

```python
await graphlit.client.query_connectors(filter: Optional[ConnectorFilter], correlation_id: Optional[str]) -> QueryConnectors
```

**Response:**
```
response.connectors
  .results: Optional[list["QueryConnectorsConnectorsResults"]]
```

### update_connector

```python
await graphlit.client.update_connector(connector: ConnectorUpdateInput) -> UpdateConnector
```

**Response:**
```
response.update_connector
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConnectorTypes]
```

### approve_content

```python
await graphlit.client.approve_content(id: str) -> ApproveContent
```

**Response:**
```
response.approve_content
  .id: str
  .state: EntityState
```

### count_contents

```python
await graphlit.client.count_contents(filter: Optional[ContentFilter], correlation_id: Optional[str]) -> CountContents
```

**Response:**
```
response.count_contents
  .count: Optional[Any]
```

### delete_all_contents

```python
await graphlit.client.delete_all_contents(
    filter: Optional[ContentFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllContents
```

**Response:**
```
response.delete_all_contents
  .id: str
  .state: EntityState
```

### delete_content

```python
await graphlit.client.delete_content(id: str) -> DeleteContent
```

**Response:**
```
response.delete_content
  .id: str
  .state: EntityState
```

### delete_contents

```python
await graphlit.client.delete_contents(ids: list[str], is_synchronous: Optional[bool]) -> DeleteContents
```

**Response:**
```
response.delete_contents
  .id: str
  .state: EntityState
```

### describe_encoded_image

```python
await graphlit.client.describe_encoded_image(
    prompt: str,
    mime_type: str,
    data: str,
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> DescribeEncodedImage
```

**Response:**
```
response.describe_encoded_image
  .role: ConversationRoleTypes
  .author: Optional[str]
  .message: Optional[str]
  .citations: Optional[
  .tool_calls: Optional[
  .tokens: Optional[int]
  .throughput: Optional[float]
  .ttft: Optional[Any]
```

### describe_image

```python
await graphlit.client.describe_image(
    prompt: str,
    uri: Any,
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> DescribeImage
```

**Response:**
```
response.describe_image
  .role: ConversationRoleTypes
  .author: Optional[str]
  .message: Optional[str]
  .citations: Optional[list[Optional["DescribeImageDescribeImageCitations"]]]
  .tool_calls: Optional[list[Optional["DescribeImageDescribeImageToolCalls"]]]
  .tokens: Optional[int]
  .throughput: Optional[float]
  .ttft: Optional[Any]
```

### distribute_contents

```python
await graphlit.client.distribute_contents(
    connector: DistributionConnectorInput,
    authentication: EntityReferenceInput,
    text: Optional[str],
    text_type: Optional[TextTypes],
    name: Optional[str],
    filter: Optional[ContentFilter],
    correlation_id: Optional[str],
) -> DistributeContents
```

**Response:**
```
response.distribute_contents
  .uri: Optional[str]
  .identifier: Optional[str]
  .service_type: Optional[DistributionServiceTypes]
  .error: Optional[str]
```

### extract_contents

```python
await graphlit.client.extract_contents(
    prompt: str,
    tools: list[ToolDefinitionInput],
    filter: Optional[ContentFilter],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ExtractContents
```

**Response:**
```
response.extract_contents
  .specification: Optional["ExtractContentsExtractContentsSpecification"]
  .content: Optional["ExtractContentsExtractContentsContent"]
  .name: str
  .value: str
  .start_time: Optional[Any]
  .end_time: Optional[Any]
  .page_number: Optional[int]
  .error: Optional[str]
```

### extract_observables

```python
await graphlit.client.extract_observables(
    text: str,
    text_type: Optional[TextTypes],
    specification: Optional[EntityReferenceInput],
    observable_types: Optional[list[ObservableTypes]],
    correlation_id: Optional[str],
) -> ExtractObservables
```

**Response:**
```
response.extract_observables
  .labels: Optional[list[Optional["ExtractObservablesExtractObservablesLabels"]]]
  .categories: Optional[
  .emotions: Optional[list[Optional["ExtractObservablesExtractObservablesEmotions"]]]
  .persons: Optional[list[Optional["ExtractObservablesExtractObservablesPersons"]]]
  .organizations: Optional[
  .places: Optional[list[Optional["ExtractObservablesExtractObservablesPlaces"]]]
  .events: Optional[list[Optional["ExtractObservablesExtractObservablesEvents"]]]
  .products: Optional[list[Optional["ExtractObservablesExtractObservablesProducts"]]]
```

### extract_text

```python
await graphlit.client.extract_text(
    prompt: str,
    text: str,
    tools: list[ToolDefinitionInput],
    text_type: Optional[TextTypes],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ExtractText
```

**Response:**
```
response.extract_text
  .specification: Optional["ExtractTextExtractTextSpecification"]
  .content: Optional["ExtractTextExtractTextContent"]
  .name: str
  .value: str
  .start_time: Optional[Any]
  .end_time: Optional[Any]
  .page_number: Optional[int]
  .error: Optional[str]
```

### get_content

```python
await graphlit.client.get_content(id: str, correlation_id: Optional[str]) -> GetContent
```

**Response:**
```
response.content
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetContentContentOwner"
  .state: EntityState
  .original_date: Optional[Any]
  .finished_date: Optional[Any]
```

### ingest_batch

```python
await graphlit.client.ingest_batch(
    uris: list[Any],
    workflow: Optional[EntityReferenceInput],
    collections: Optional[list[EntityReferenceInput]],
    observations: Optional[list[ObservationReferenceInput]],
    correlation_id: Optional[str],
) -> IngestBatch
```

**Response:**
```
response.ingest_batch
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_encoded_file

```python
await graphlit.client.ingest_encoded_file(
    name: str,
    data: str,
    mime_type: str,
    id: Optional[str],
    identifier: Optional[str],
    file_creation_date: Optional[Any],
    file_modified_date: Optional[Any],
    is_synchronous: Optional[bool],
    collections: Optional[list[EntityReferenceInput]],
    observations: Optional[list[ObservationReferenceInput]],
    workflow: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> IngestEncodedFile
```

**Response:**
```
response.ingest_encoded_file
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_event

```python
await graphlit.client.ingest_event(
    markdown: str,
    name: Optional[str],
    description: Optional[str],
    event_date: Optional[Any],
    id: Optional[str],
    identifier: Optional[str],
    collections: Optional[list[EntityReferenceInput]],
    correlation_id: Optional[str],
) -> IngestEvent
```

**Response:**
```
response.ingest_event
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_memory

```python
await graphlit.client.ingest_memory(
    text: str,
    name: Optional[str],
    text_type: Optional[TextTypes],
    id: Optional[str],
    identifier: Optional[str],
    collections: Optional[list[EntityReferenceInput]],
    correlation_id: Optional[str],
) -> IngestMemory
```

**Response:**
```
response.ingest_memory
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_text

```python
await graphlit.client.ingest_text(
    text: str,
    name: Optional[str],
    text_type: Optional[TextTypes],
    uri: Optional[Any],
    id: Optional[str],
    identifier: Optional[str],
    is_synchronous: Optional[bool],
    workflow: Optional[EntityReferenceInput],
    collections: Optional[list[EntityReferenceInput]],
    observations: Optional[list[ObservationReferenceInput]],
    correlation_id: Optional[str],
) -> IngestText
```

**Response:**
```
response.ingest_text
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_text_batch

```python
await graphlit.client.ingest_text_batch(
    batch: list[TextContentInput],
    text_type: Optional[TextTypes],
    workflow: Optional[EntityReferenceInput],
    collections: Optional[list[EntityReferenceInput]],
    observations: Optional[list[ObservationReferenceInput]],
    correlation_id: Optional[str],
) -> IngestTextBatch
```

**Response:**
```
response.ingest_text_batch
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ingest_uri

```python
await graphlit.client.ingest_uri(
    uri: Any,
    name: Optional[str],
    id: Optional[str],
    mime_type: Optional[str],
    identifier: Optional[str],
    is_synchronous: Optional[bool],
    workflow: Optional[EntityReferenceInput],
    collections: Optional[list[EntityReferenceInput]],
    observations: Optional[list[ObservationReferenceInput]],
    correlation_id: Optional[str],
) -> IngestUri
```

**Response:**
```
response.ingest_uri
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### is_content_done

```python
await graphlit.client.is_content_done(id: str) -> IsContentDone
```

**Response:**
```
response.is_content_done
  .result: Optional[bool]
```

### lookup_contents

```python
await graphlit.client.lookup_contents(ids: list[str], correlation_id: Optional[str]) -> LookupContents
```

**Response:**
```
response.lookup_contents
  .results: Optional[list[Optional["LookupContentsLookupContentsResults"]]]
```

### lookup_entity

```python
await graphlit.client.lookup_entity(filter: EntityRelationshipsFilter, correlation_id: Optional[str]) -> LookupEntity
```

**Response:**
```
response.lookup_entity
  .entity: Optional["LookupEntityLookupEntityEntity"]
  .relationships: Optional[list["LookupEntityLookupEntityRelationships"]]
  .total_count: int
```

### publish_contents

```python
await graphlit.client.publish_contents(
    publish_prompt: str,
    connector: ContentPublishingConnectorInput,
    summary_prompt: Optional[str],
    filter: Optional[ContentFilter],
    include_details: Optional[bool],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
    name: Optional[str],
    summary_specification: Optional[EntityReferenceInput],
    publish_specification: Optional[EntityReferenceInput],
    workflow: Optional[EntityReferenceInput],
) -> PublishContents
```

**Response:**
```
response.publish_contents
  .contents: Optional[list[Optional["PublishContentsPublishContentsContents"]]]
  .details: Optional["PublishContentsPublishContentsDetails"]
```

### publish_text

```python
await graphlit.client.publish_text(
    text: str,
    connector: ContentPublishingConnectorInput,
    text_type: Optional[TextTypes],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
    name: Optional[str],
    workflow: Optional[EntityReferenceInput],
) -> PublishText
```

**Response:**
```
response.publish_text
  .contents: Optional[list[Optional["PublishTextPublishTextContents"]]]
  .details: Optional["PublishTextPublishTextDetails"]
```

### query_contents

```python
await graphlit.client.query_contents(filter: Optional[ContentFilter], correlation_id: Optional[str]) -> QueryContents
```

**Response:**
```
response.contents
  .results: Optional[list[Optional["QueryContentsContentsResults"]]]
```

### query_contents_facets

```python
await graphlit.client.query_contents_facets(
    filter: Optional[ContentFilter],
    facets: Optional[list[ContentFacetInput]],
    correlation_id: Optional[str],
) -> QueryContentsFacets
```

**Response:**
```
response.contents
  .facets: Optional[list[Optional["QueryContentsFacetsContentsFacets"]]]
```

### query_contents_graph

```python
await graphlit.client.query_contents_graph(
    filter: Optional[ContentFilter],
    graph: Optional[ContentGraphInput],
    correlation_id: Optional[str],
) -> QueryContentsGraph
```

**Response:**
```
response.contents
  .graph: Optional["QueryContentsGraphContentsGraph"]
```

### query_contents_observations

```python
await graphlit.client.query_contents_observations(filter: Optional[ContentFilter], correlation_id: Optional[str]) -> QueryContentsObservations
```

**Response:**
```
response.contents
  .results: Optional[list[Optional["QueryContentsObservationsContentsResults"]]]
```

### query_graph

```python
await graphlit.client.query_graph(
    filter: Optional[GraphFilter],
    graph: Optional[GraphInput],
    correlation_id: Optional[str],
) -> QueryGraph
```

**Response:**
```
response.graph
  .nodes: Optional[list[Optional["QueryGraphGraphNodes"]]]
  .edges: Optional[list[Optional["QueryGraphGraphEdges"]]]
```

### query_observables

```python
await graphlit.client.query_observables(filter: Optional[ContentFilter], correlation_id: Optional[str]) -> QueryObservables
```

**Response:**
```
response.observables
  .results: Optional[list[Optional["QueryObservablesObservablesResults"]]]
```

### reject_content

```python
await graphlit.client.reject_content(id: str, reason: Optional[str]) -> RejectContent
```

**Response:**
```
response.reject_content
  .id: str
  .state: EntityState
```

### research_contents

```python
await graphlit.client.research_contents(
    connector: ContentPublishingConnectorInput,
    filter: Optional[ContentFilter],
    name: Optional[str],
    summary_specification: Optional[EntityReferenceInput],
    publish_specification: Optional[EntityReferenceInput],
    workflow: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ResearchContents
```

**Response:**
```
response.research_contents
  .result: Optional[str]
```

### restart_content

```python
await graphlit.client.restart_content(id: str) -> RestartContent
```

**Response:**
```
response.restart_content
  .id: str
  .state: EntityState
```

### screenshot_page

```python
await graphlit.client.screenshot_page(
    uri: Any,
    maximum_height: Optional[int],
    is_synchronous: Optional[bool],
    workflow: Optional[EntityReferenceInput],
    collections: Optional[list[EntityReferenceInput]],
    correlation_id: Optional[str],
) -> ScreenshotPage
```

**Response:**
```
response.screenshot_page
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### summarize_contents

```python
await graphlit.client.summarize_contents(
    summarizations: list[SummarizationStrategyInput],
    filter: Optional[ContentFilter],
    correlation_id: Optional[str],
) -> SummarizeContents
```

**Response:**
```
response.summarize_contents
  .specification: Optional["SummarizeContentsSummarizeContentsSpecification"]
  .content: Optional["SummarizeContentsSummarizeContentsContent"]
  .type: SummarizationTypes
  .items: Optional[list["SummarizeContentsSummarizeContentsItems"]]
  .error: Optional[str]
```

### summarize_text

```python
await graphlit.client.summarize_text(
    summarization: SummarizationStrategyInput,
    text: str,
    text_type: Optional[TextTypes],
    correlation_id: Optional[str],
) -> SummarizeText
```

**Response:**
```
response.summarize_text
  .specification: Optional["SummarizeTextSummarizeTextSpecification"]
  .content: Optional["SummarizeTextSummarizeTextContent"]
  .type: SummarizationTypes
  .items: Optional[list["SummarizeTextSummarizeTextItems"]]
  .error: Optional[str]
```

### update_content

```python
await graphlit.client.update_content(content: ContentUpdateInput) -> UpdateContent
```

**Response:**
```
response.update_content
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ContentTypes]
  .file_type: Optional[FileTypes]
  .mime_type: Optional[str]
  .uri: Optional[Any]
  .identifier: Optional[str]
```

### ask_graphlit

```python
await graphlit.client.ask_graphlit(
    prompt: str,
    type: Optional[SdkTypes],
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> AskGraphlit
```

**Response:**
```
response.ask_graphlit
  .conversation: Optional["AskGraphlitAskGraphlitConversation"]
  .message: Optional["AskGraphlitAskGraphlitMessage"]
  .message_count: Optional[int]
```

### branch_conversation

```python
await graphlit.client.branch_conversation(id: str) -> BranchConversation
```

**Response:**
```
response.branch_conversation
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConversationTypes]
```

### clear_conversation

```python
await graphlit.client.clear_conversation(id: str) -> ClearConversation
```

**Response:**
```
response.clear_conversation
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConversationTypes]
```

### close_conversation

```python
await graphlit.client.close_conversation(id: str) -> CloseConversation
```

**Response:**
```
response.close_conversation
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConversationTypes]
```

### complete_conversation

```python
await graphlit.client.complete_conversation(
    completion: str,
    id: str,
    completion_time: Optional[Any],
    ttft: Optional[Any],
    throughput: Optional[float],
    artifacts: Optional[list[EntityReferenceInput]],
    messages: Optional[list[ConversationMessageInput]],
    correlation_id: Optional[str],
) -> CompleteConversation
```

**Response:**
```
response.complete_conversation
  .conversation: Optional["CompleteConversationCompleteConversationConversation"]
  .message: Optional["CompleteConversationCompleteConversationMessage"]
  .message_count: Optional[int]
  .facets: Optional[list[Optional["CompleteConversationCompleteConversationFacets"]]]
  .graph: Optional["CompleteConversationCompleteConversationGraph"]
  .details: Optional["CompleteConversationCompleteConversationDetails"]
```

### continue_conversation

```python
await graphlit.client.continue_conversation(
    id: str,
    responses: list[ConversationToolResponseInput],
    correlation_id: Optional[str],
) -> ContinueConversation
```

**Response:**
```
response.continue_conversation
  .conversation: Optional["ContinueConversationContinueConversationConversation"]
  .message: Optional["ContinueConversationContinueConversationMessage"]
  .message_count: Optional[int]
  .facets: Optional[list[Optional["ContinueConversationContinueConversationFacets"]]]
  .graph: Optional["ContinueConversationContinueConversationGraph"]
  .details: Optional["ContinueConversationContinueConversationDetails"]
```

### count_conversations

```python
await graphlit.client.count_conversations(filter: Optional[ConversationFilter], correlation_id: Optional[str]) -> CountConversations
```

**Response:**
```
response.count_conversations
  .count: Optional[Any]
```

### create_conversation

```python
await graphlit.client.create_conversation(conversation: ConversationInput, correlation_id: Optional[str]) -> CreateConversation
```

**Response:**
```
response.create_conversation
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConversationTypes]
```

### delete_all_conversations

```python
await graphlit.client.delete_all_conversations(
    filter: Optional[ConversationFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllConversations
```

**Response:**
```
response.delete_all_conversations
  .id: str
  .state: EntityState
```

### delete_conversation

```python
await graphlit.client.delete_conversation(id: str) -> DeleteConversation
```

**Response:**
```
response.delete_conversation
  .id: str
  .state: EntityState
```

### delete_conversations

```python
await graphlit.client.delete_conversations(ids: list[str], is_synchronous: Optional[bool]) -> DeleteConversations
```

**Response:**
```
response.delete_conversations
  .id: str
  .state: EntityState
```

### format_conversation

```python
await graphlit.client.format_conversation(
    prompt: str,
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    persona: Optional[EntityReferenceInput],
    tools: Optional[list[ToolDefinitionInput]],
    system_prompt: Optional[str],
    include_details: Optional[bool],
    correlation_id: Optional[str],
) -> FormatConversation
```

**Response:**
```
response.format_conversation
  .conversation: Optional["FormatConversationFormatConversationConversation"]
  .message: Optional["FormatConversationFormatConversationMessage"]
  .message_count: Optional[int]
  .facets: Optional[list[Optional["FormatConversationFormatConversationFacets"]]]
  .graph: Optional["FormatConversationFormatConversationGraph"]
  .details: Optional["FormatConversationFormatConversationDetails"]
```

### get_conversation

```python
await graphlit.client.get_conversation(id: str, correlation_id: Optional[str]) -> GetConversation
```

**Response:**
```
response.conversation
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetConversationConversationOwner"
  .state: EntityState
  .correlation_id: Optional[str]
  .type: Optional[ConversationTypes]
```

### prompt

```python
await graphlit.client.prompt(
    prompt: Optional[str],
    mime_type: Optional[str],
    data: Optional[str],
    specification: Optional[EntityReferenceInput],
    messages: Optional[list[ConversationMessageInput]],
    tools: Optional[list[ToolDefinitionInput]],
    require_tool: Optional[bool],
    correlation_id: Optional[str],
) -> Prompt
```

**Response:**
```
response.prompt
  .specification: Optional["PromptPromptSpecification"]
  .messages: Optional[list[Optional["PromptPromptMessages"]]]
  .error: Optional[str]
```

### prompt_conversation

```python
await graphlit.client.prompt_conversation(
    prompt: str,
    mime_type: Optional[str],
    data: Optional[str],
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    persona: Optional[EntityReferenceInput],
    system_prompt: Optional[str],
    tools: Optional[list[ToolDefinitionInput]],
    require_tool: Optional[bool],
    include_details: Optional[bool],
    correlation_id: Optional[str],
) -> PromptConversation
```

**Response:**
```
response.prompt_conversation
  .conversation: Optional["PromptConversationPromptConversationConversation"]
  .message: Optional["PromptConversationPromptConversationMessage"]
  .message_count: Optional[int]
  .facets: Optional[list[Optional["PromptConversationPromptConversationFacets"]]]
  .graph: Optional["PromptConversationPromptConversationGraph"]
  .details: Optional["PromptConversationPromptConversationDetails"]
```

### publish_conversation

```python
await graphlit.client.publish_conversation(
    id: str,
    connector: ContentPublishingConnectorInput,
    name: Optional[str],
    is_synchronous: Optional[bool],
    workflow: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> PublishConversation
```

**Response:**
```
response.publish_conversation
  .contents: Optional[list[Optional["PublishConversationPublishConversationContents"]]]
  .details: Optional["PublishConversationPublishConversationDetails"]
```

### query_conversations

```python
await graphlit.client.query_conversations(filter: Optional[ConversationFilter], correlation_id: Optional[str]) -> QueryConversations
```

**Response:**
```
response.conversations
  .results: Optional[list["QueryConversationsConversationsResults"]]
```

### query_conversations_clusters

```python
await graphlit.client.query_conversations_clusters(
    filter: Optional[ConversationFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryConversationsClusters
```

**Response:**
```
response.conversations
  .results: Optional[list["QueryConversationsClustersConversationsResults"]]
  .clusters: Optional[
```

### query_conversations_graph

```python
await graphlit.client.query_conversations_graph(
    filter: Optional[ConversationFilter],
    graph: Optional[ConversationGraphInput],
    correlation_id: Optional[str],
) -> QueryConversationsGraph
```

**Response:**
```
response.conversations
  .graph: Optional["QueryConversationsGraphConversationsGraph"]
```

### retrieve_entities

```python
await graphlit.client.retrieve_entities(
    prompt: str,
    types: Optional[list[ObservableTypes]],
    search_type: Optional[SearchTypes],
    limit: Optional[int],
    correlation_id: Optional[str],
) -> RetrieveEntities
```

**Response:**
```
response.retrieve_entities
  .results: Optional[list[Optional["RetrieveEntitiesRetrieveEntitiesResults"]]]
```

### retrieve_facts

```python
await graphlit.client.retrieve_facts(
    prompt: str,
    filter: Optional[FactFilter],
    correlation_id: Optional[str],
) -> RetrieveFacts
```

**Response:**
```
response.retrieve_facts
  .results: Optional[list[Optional["RetrieveFactsRetrieveFactsResults"]]]
```

### retrieve_sources

```python
await graphlit.client.retrieve_sources(
    prompt: str,
    filter: Optional[ContentFilter],
    augmented_filter: Optional[ContentFilter],
    retrieval_strategy: Optional[RetrievalStrategyInput],
    reranking_strategy: Optional[RerankingStrategyInput],
    correlation_id: Optional[str],
) -> RetrieveSources
```

**Response:**
```
response.retrieve_sources
  .results: Optional[list[Optional["RetrieveSourcesRetrieveSourcesResults"]]]
```

### retrieve_view

```python
await graphlit.client.retrieve_view(
    prompt: str,
    id: str,
    retrieval_strategy: Optional[RetrievalStrategyInput],
    reranking_strategy: Optional[RerankingStrategyInput],
    correlation_id: Optional[str],
) -> RetrieveView
```

**Response:**
```
response.retrieve_view
  .results: Optional[list[Optional["RetrieveViewRetrieveViewResults"]]]
```

### revise_content

```python
await graphlit.client.revise_content(
    prompt: str,
    content: EntityReferenceInput,
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ReviseContent
```

**Response:**
```
response.revise_content
  .conversation: Optional["ReviseContentReviseContentConversation"]
  .message: Optional["ReviseContentReviseContentMessage"]
  .message_count: Optional[int]
```

### revise_encoded_image

```python
await graphlit.client.revise_encoded_image(
    prompt: str,
    mime_type: str,
    data: str,
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ReviseEncodedImage
```

**Response:**
```
response.revise_encoded_image
  .conversation: Optional["ReviseEncodedImageReviseEncodedImageConversation"]
  .message: Optional["ReviseEncodedImageReviseEncodedImageMessage"]
  .message_count: Optional[int]
```

### revise_image

```python
await graphlit.client.revise_image(
    prompt: str,
    uri: Any,
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ReviseImage
```

**Response:**
```
response.revise_image
  .conversation: Optional["ReviseImageReviseImageConversation"]
  .message: Optional["ReviseImageReviseImageMessage"]
  .message_count: Optional[int]
```

### revise_text

```python
await graphlit.client.revise_text(
    prompt: str,
    text: str,
    id: Optional[str],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ReviseText
```

**Response:**
```
response.revise_text
  .conversation: Optional["ReviseTextReviseTextConversation"]
  .message: Optional["ReviseTextReviseTextMessage"]
  .message_count: Optional[int]
```

### suggest_conversation

```python
await graphlit.client.suggest_conversation(
    id: str,
    count: Optional[int],
    prompt: Optional[str],
    correlation_id: Optional[str],
) -> SuggestConversation
```

**Response:**
```
response.suggest_conversation
  .prompts: Optional[list[Optional[str]]]
```

### update_conversation

```python
await graphlit.client.update_conversation(conversation: ConversationUpdateInput) -> UpdateConversation
```

**Response:**
```
response.update_conversation
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ConversationTypes]
```

### count_emotions

```python
await graphlit.client.count_emotions(filter: Optional[EmotionFilter], correlation_id: Optional[str]) -> CountEmotions
```

**Response:**
```
response.count_emotions
  .count: Optional[Any]
```

### create_emotion

```python
await graphlit.client.create_emotion(emotion: EmotionInput) -> CreateEmotion
```

**Response:**
```
response.create_emotion
  .id: str
  .name: str
```

### delete_all_emotions

```python
await graphlit.client.delete_all_emotions(
    filter: Optional[EmotionFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllEmotions
```

**Response:**
```
response.delete_all_emotions
  .id: str
  .state: EntityState
```

### delete_emotion

```python
await graphlit.client.delete_emotion(id: str) -> DeleteEmotion
```

**Response:**
```
response.delete_emotion
  .id: str
  .state: EntityState
```

### delete_emotions

```python
await graphlit.client.delete_emotions(ids: list[str], is_synchronous: Optional[bool]) -> DeleteEmotions
```

**Response:**
```
response.delete_emotions
  .id: str
  .state: EntityState
```

### get_emotion

```python
await graphlit.client.get_emotion(id: str, correlation_id: Optional[str]) -> GetEmotion
```

**Response:**
```
response.emotion
  .id: str
  .name: str
  .description: Optional[str]
  .creation_date: Any
  .feeds: Optional[list[Optional["GetEmotionEmotionFeeds"]]]
```

### query_emotions

```python
await graphlit.client.query_emotions(filter: Optional[EmotionFilter], correlation_id: Optional[str]) -> QueryEmotions
```

**Response:**
```
response.emotions
  .results: Optional[list[Optional["QueryEmotionsEmotionsResults"]]]
```

### update_emotion

```python
await graphlit.client.update_emotion(emotion: EmotionUpdateInput) -> UpdateEmotion
```

**Response:**
```
response.update_emotion
  .id: str
  .name: str
```

### count_events

```python
await graphlit.client.count_events(filter: Optional[EventFilter], correlation_id: Optional[str]) -> CountEvents
```

**Response:**
```
response.count_events
  .count: Optional[Any]
```

### create_event

```python
await graphlit.client.create_event(event: EventInput) -> CreateEvent
```

**Response:**
```
response.create_event
  .id: str
  .name: str
```

### delete_all_events

```python
await graphlit.client.delete_all_events(
    filter: Optional[EventFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllEvents
```

**Response:**
```
response.delete_all_events
  .id: str
  .state: EntityState
```

### delete_event

```python
await graphlit.client.delete_event(id: str) -> DeleteEvent
```

**Response:**
```
response.delete_event
  .id: str
  .state: EntityState
```

### delete_events

```python
await graphlit.client.delete_events(ids: list[str], is_synchronous: Optional[bool]) -> DeleteEvents
```

**Response:**
```
response.delete_events
  .id: str
  .state: EntityState
```

### get_event

```python
await graphlit.client.get_event(id: str, correlation_id: Optional[str]) -> GetEvent
```

**Response:**
```
response.event
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetEventEventOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_events

```python
await graphlit.client.query_events(filter: Optional[EventFilter], correlation_id: Optional[str]) -> QueryEvents
```

**Response:**
```
response.events
  .results: Optional[list[Optional["QueryEventsEventsResults"]]]
```

### query_events_clusters

```python
await graphlit.client.query_events_clusters(
    filter: Optional[EventFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryEventsClusters
```

**Response:**
```
response.events
  .results: Optional[list[Optional["QueryEventsClustersEventsResults"]]]
  .clusters: Optional["QueryEventsClustersEventsClusters"]
```

### update_event

```python
await graphlit.client.update_event(event: EventUpdateInput) -> UpdateEvent
```

**Response:**
```
response.update_event
  .id: str
  .name: str
```

### count_facts

```python
await graphlit.client.count_facts(filter: Optional[FactFilter], correlation_id: Optional[str]) -> CountFacts
```

**Response:**
```
response.count_facts
  .count: Optional[Any]
```

### create_fact

```python
await graphlit.client.create_fact(fact: FactInput) -> CreateFact
```

**Response:**
```
response.create_fact
  .id: str
  .state: EntityState
```

### delete_all_facts

```python
await graphlit.client.delete_all_facts(
    filter: Optional[FactFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllFacts
```

**Response:**
```
response.delete_all_facts
  .id: str
  .state: EntityState
```

### delete_fact

```python
await graphlit.client.delete_fact(id: str) -> DeleteFact
```

**Response:**
```
response.delete_fact
  .id: str
  .state: EntityState
```

### delete_facts

```python
await graphlit.client.delete_facts(ids: list[str], is_synchronous: Optional[bool]) -> DeleteFacts
```

**Response:**
```
response.delete_facts
  .id: str
  .state: EntityState
```

### get_fact

```python
await graphlit.client.get_fact(id: str, correlation_id: Optional[str]) -> GetFact
```

**Response:**
```
response.fact
  .id: str
  .creation_date: Any
  .owner: "GetFactFactOwner"
  .state: EntityState
  .text: str
  .valid_at: Optional[Any]
  .invalid_at: Optional[Any]
  .relevance: Optional[float]
```

### query_facts

```python
await graphlit.client.query_facts(filter: Optional[FactFilter], correlation_id: Optional[str]) -> QueryFacts
```

**Response:**
```
response.facts
  .results: Optional[list[Optional["QueryFactsFactsResults"]]]
```

### query_facts_clusters

```python
await graphlit.client.query_facts_clusters(
    filter: Optional[FactFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryFactsClusters
```

**Response:**
```
response.facts
  .results: Optional[list[Optional["QueryFactsClustersFactsResults"]]]
  .clusters: Optional[list[Optional["QueryFactsClustersFactsClusters"]]]
```

### query_facts_graph

```python
await graphlit.client.query_facts_graph(
    filter: Optional[FactFilter],
    graph: Optional[FactGraphInput],
    correlation_id: Optional[str],
) -> QueryFactsGraph
```

**Response:**
```
response.facts
  .graph: Optional["QueryFactsGraphFactsGraph"]
```

### update_fact

```python
await graphlit.client.update_fact(fact: FactUpdateInput) -> UpdateFact
```

**Response:**
```
response.update_fact
  .id: str
  .state: EntityState
```

### count_feeds

```python
await graphlit.client.count_feeds(filter: Optional[FeedFilter], correlation_id: Optional[str]) -> CountFeeds
```

**Response:**
```
response.count_feeds
  .count: Optional[Any]
```

### create_feed

```python
await graphlit.client.create_feed(feed: FeedInput, correlation_id: Optional[str]) -> CreateFeed
```

**Response:**
```
response.create_feed
  .id: str
  .name: str
  .state: EntityState
  .identifier: Optional[str]
  .type: FeedTypes
```

### delete_all_feeds

```python
await graphlit.client.delete_all_feeds(
    filter: Optional[FeedFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllFeeds
```

**Response:**
```
response.delete_all_feeds
  .id: str
  .state: EntityState
```

### delete_feed

```python
await graphlit.client.delete_feed(id: str) -> DeleteFeed
```

**Response:**
```
response.delete_feed
  .id: str
  .state: EntityState
```

### delete_feeds

```python
await graphlit.client.delete_feeds(ids: list[str], is_synchronous: Optional[bool]) -> DeleteFeeds
```

**Response:**
```
response.delete_feeds
  .id: str
  .state: EntityState
```

### disable_feed

```python
await graphlit.client.disable_feed(id: str) -> DisableFeed
```

**Response:**
```
response.disable_feed
  .id: str
  .state: EntityState
```

### enable_feed

```python
await graphlit.client.enable_feed(id: str) -> EnableFeed
```

**Response:**
```
response.enable_feed
  .id: str
  .state: EntityState
```

### feed_exists

```python
await graphlit.client.feed_exists(filter: Optional[FeedFilter], correlation_id: Optional[str]) -> FeedExists
```

**Response:**
```
response.feed_exists
  .result: Optional[bool]
```

### get_feed

```python
await graphlit.client.get_feed(id: str, correlation_id: Optional[str]) -> GetFeed
```

**Response:**
```
response.feed
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetFeedFeedOwner"
  .state: EntityState
  .identifier: Optional[str]
  .description: Optional[str]
```

### get_share_point_consent_uri

```python
await graphlit.client.get_share_point_consent_uri(tenant_id: str) -> GetSharePointConsentUri
```

**Response:**
```
response.share_point_consent_uri
  .uri: Optional[Any]
```

### is_feed_done

```python
await graphlit.client.is_feed_done(id: str) -> IsFeedDone
```

**Response:**
```
response.is_feed_done
  .result: Optional[bool]
```

### query_asana_projects

```python
await graphlit.client.query_asana_projects(properties: AsanaProjectsInput) -> QueryAsanaProjects
```

**Response:**
```
response.asana_projects
  .results: Optional[list[str]]
```

### query_asana_workspaces

```python
await graphlit.client.query_asana_workspaces(properties: AsanaWorkspacesInput) -> QueryAsanaWorkspaces
```

**Response:**
```
response.asana_workspaces
  .results: Optional[list[str]]
```

### query_atlassian_sites

```python
await graphlit.client.query_atlassian_sites(properties: AtlassianSitesInput) -> QueryAtlassianSites
```

**Response:**
```
response.atlassian_sites
  .results: Optional[list[Optional["QueryAtlassianSitesAtlassianSitesResults"]]]
```

### query_bamboo_hr_departments

```python
await graphlit.client.query_bamboo_hr_departments(properties: BambooHROptionsInput) -> QueryBambooHRDepartments
```

### query_bamboo_hr_divisions

```python
await graphlit.client.query_bamboo_hr_divisions(properties: BambooHROptionsInput) -> QueryBambooHRDivisions
```

### query_bamboo_hr_employment_statuses

```python
await graphlit.client.query_bamboo_hr_employment_statuses(properties: BambooHROptionsInput) -> QueryBambooHREmploymentStatuses
```

### query_bamboo_hr_locations

```python
await graphlit.client.query_bamboo_hr_locations(properties: BambooHROptionsInput) -> QueryBambooHRLocations
```

### query_box_folders

```python
await graphlit.client.query_box_folders(properties: BoxFoldersInput, folder_id: Optional[str]) -> QueryBoxFolders
```

**Response:**
```
response.box_folders
  .results: Optional[list[Optional["QueryBoxFoldersBoxFoldersResults"]]]
```

### query_confluence_spaces

```python
await graphlit.client.query_confluence_spaces(properties: ConfluenceSpacesInput) -> QueryConfluenceSpaces
```

**Response:**
```
response.confluence_spaces
  .results: Optional[list[Optional["QueryConfluenceSpacesConfluenceSpacesResults"]]]
```

### query_discord_channels

```python
await graphlit.client.query_discord_channels(properties: DiscordChannelsInput) -> QueryDiscordChannels
```

**Response:**
```
response.discord_channels
  .results: Optional[list[Optional["QueryDiscordChannelsDiscordChannelsResults"]]]
```

### query_discord_guilds

```python
await graphlit.client.query_discord_guilds(properties: DiscordGuildsInput) -> QueryDiscordGuilds
```

**Response:**
```
response.discord_guilds
  .results: Optional[list[Optional["QueryDiscordGuildsDiscordGuildsResults"]]]
```

### query_dropbox_folders

```python
await graphlit.client.query_dropbox_folders(properties: DropboxFoldersInput, folder_path: Optional[str]) -> QueryDropboxFolders
```

**Response:**
```
response.dropbox_folders
  .results: Optional[list[Optional["QueryDropboxFoldersDropboxFoldersResults"]]]
```

### query_feeds

```python
await graphlit.client.query_feeds(filter: Optional[FeedFilter], correlation_id: Optional[str]) -> QueryFeeds
```

**Response:**
```
response.feeds
  .results: Optional[list["QueryFeedsFeedsResults"]]
```

### query_git_hub_repositories

```python
await graphlit.client.query_git_hub_repositories(properties: GitHubRepositoriesInput, sort_by: Optional[GitHubRepositorySortTypes]) -> QueryGitHubRepositories
```

**Response:**
```
response.git_hub_repositories
  .results: Optional[
```

### query_google_calendars

```python
await graphlit.client.query_google_calendars(properties: GoogleCalendarsInput) -> QueryGoogleCalendars
```

**Response:**
```
response.google_calendars
  .results: Optional[list[Optional["QueryGoogleCalendarsGoogleCalendarsResults"]]]
```

### query_google_drive_folders

```python
await graphlit.client.query_google_drive_folders(properties: GoogleDriveFoldersInput, folder_id: Optional[str]) -> QueryGoogleDriveFolders
```

**Response:**
```
response.google_drive_folders
  .results: Optional[
```

### query_gusto_companies

```python
await graphlit.client.query_gusto_companies(properties: GustoCompaniesInput) -> QueryGustoCompanies
```

**Response:**
```
response.gusto_companies
  .results: Optional[list[Optional["QueryGustoCompaniesGustoCompaniesResults"]]]
```

### query_gusto_departments

```python
await graphlit.client.query_gusto_departments(properties: GustoOptionsInput) -> QueryGustoDepartments
```

**Response:**
```
response.gusto_departments
  .results: Optional[list[Optional["QueryGustoDepartmentsGustoDepartmentsResults"]]]
```

### query_gusto_locations

```python
await graphlit.client.query_gusto_locations(properties: GustoOptionsInput) -> QueryGustoLocations
```

**Response:**
```
response.gusto_locations
  .results: Optional[list[Optional["QueryGustoLocationsGustoLocationsResults"]]]
```

### query_jira_projects

```python
await graphlit.client.query_jira_projects(properties: JiraProjectsInput) -> QueryJiraProjects
```

**Response:**
```
response.jira_projects
  .results: Optional[list[Optional["QueryJiraProjectsJiraProjectsResults"]]]
```

### query_linear_projects

```python
await graphlit.client.query_linear_projects(properties: LinearProjectsInput) -> QueryLinearProjects
```

**Response:**
```
response.linear_projects
  .results: Optional[list[str]]
```

### query_microsoft_calendars

```python
await graphlit.client.query_microsoft_calendars(properties: MicrosoftCalendarsInput) -> QueryMicrosoftCalendars
```

**Response:**
```
response.microsoft_calendars
  .results: Optional[
```

### query_microsoft_teams_channels

```python
await graphlit.client.query_microsoft_teams_channels(properties: MicrosoftTeamsChannelsInput, team_id: str) -> QueryMicrosoftTeamsChannels
```

**Response:**
```
response.microsoft_teams_channels
  .results: Optional[
```

### query_microsoft_teams_teams

```python
await graphlit.client.query_microsoft_teams_teams(properties: MicrosoftTeamsTeamsInput) -> QueryMicrosoftTeamsTeams
```

**Response:**
```
response.microsoft_teams_teams
  .results: Optional[
```

### query_monday_boards

```python
await graphlit.client.query_monday_boards(properties: MondayBoardsInput) -> QueryMondayBoards
```

**Response:**
```
response.monday_boards
  .results: Optional[list[str]]
```

### query_notion_databases

```python
await graphlit.client.query_notion_databases(properties: NotionDatabasesInput) -> QueryNotionDatabases
```

**Response:**
```
response.notion_databases
  .results: Optional[list[Optional["QueryNotionDatabasesNotionDatabasesResults"]]]
```

### query_notion_pages

```python
await graphlit.client.query_notion_pages(properties: NotionPagesInput, identifier: str) -> QueryNotionPages
```

**Response:**
```
response.notion_pages
  .results: Optional[list[Optional["QueryNotionPagesNotionPagesResults"]]]
```

### query_one_drive_folders

```python
await graphlit.client.query_one_drive_folders(properties: OneDriveFoldersInput, folder_id: Optional[str]) -> QueryOneDriveFolders
```

**Response:**
```
response.one_drive_folders
  .results: Optional[list[Optional["QueryOneDriveFoldersOneDriveFoldersResults"]]]
```

### query_share_point_folders

```python
await graphlit.client.query_share_point_folders(
    properties: SharePointFoldersInput,
    library_id: str,
    folder_id: Optional[str],
) -> QuerySharePointFolders
```

**Response:**
```
response.share_point_folders
  .account_name: Optional[str]
  .results: Optional[list[Optional["QuerySharePointFoldersSharePointFoldersResults"]]]
```

### query_share_point_libraries

```python
await graphlit.client.query_share_point_libraries(properties: SharePointLibrariesInput) -> QuerySharePointLibraries
```

**Response:**
```
response.share_point_libraries
  .account_name: Optional[str]
  .results: Optional[
```

### query_slack_channels

```python
await graphlit.client.query_slack_channels(properties: SlackChannelsInput) -> QuerySlackChannels
```

**Response:**
```
response.slack_channels
  .results: Optional[list[str]]
```

### trigger_feed

```python
await graphlit.client.trigger_feed(id: str) -> TriggerFeed
```

**Response:**
```
response.trigger_feed
  .id: str
  .state: EntityState
```

### update_feed

```python
await graphlit.client.update_feed(feed: FeedUpdateInput) -> UpdateFeed
```

**Response:**
```
response.update_feed
  .id: str
  .name: str
  .state: EntityState
  .identifier: Optional[str]
  .type: FeedTypes
```

### count_investments

```python
await graphlit.client.count_investments(filter: Optional[InvestmentFilter], correlation_id: Optional[str]) -> CountInvestments
```

**Response:**
```
response.count_investments
  .count: Optional[Any]
```

### create_investment

```python
await graphlit.client.create_investment(investment: InvestmentInput) -> CreateInvestment
```

**Response:**
```
response.create_investment
  .id: str
  .name: str
```

### delete_all_investments

```python
await graphlit.client.delete_all_investments(
    filter: Optional[InvestmentFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllInvestments
```

**Response:**
```
response.delete_all_investments
  .id: str
  .state: EntityState
```

### delete_investment

```python
await graphlit.client.delete_investment(id: str) -> DeleteInvestment
```

**Response:**
```
response.delete_investment
  .id: str
  .state: EntityState
```

### delete_investments

```python
await graphlit.client.delete_investments(ids: list[str], is_synchronous: Optional[bool]) -> DeleteInvestments
```

**Response:**
```
response.delete_investments
  .id: str
  .state: EntityState
```

### get_investment

```python
await graphlit.client.get_investment(id: str, correlation_id: Optional[str]) -> GetInvestment
```

**Response:**
```
response.investment
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetInvestmentInvestmentOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_investments

```python
await graphlit.client.query_investments(filter: Optional[InvestmentFilter], correlation_id: Optional[str]) -> QueryInvestments
```

**Response:**
```
response.investments
  .results: Optional[list[Optional["QueryInvestmentsInvestmentsResults"]]]
```

### query_investments_clusters

```python
await graphlit.client.query_investments_clusters(
    filter: Optional[InvestmentFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryInvestmentsClusters
```

**Response:**
```
response.investments
  .results: Optional[list[Optional["QueryInvestmentsClustersInvestmentsResults"]]]
  .clusters: Optional["QueryInvestmentsClustersInvestmentsClusters"]
```

### query_investments_expanded

```python
await graphlit.client.query_investments_expanded(filter: Optional[InvestmentFilter], correlation_id: Optional[str]) -> QueryInvestmentsExpanded
```

**Response:**
```
response.investments
  .results: Optional[list[Optional["QueryInvestmentsExpandedInvestmentsResults"]]]
```

### update_investment

```python
await graphlit.client.update_investment(investment: InvestmentUpdateInput) -> UpdateInvestment
```

**Response:**
```
response.update_investment
  .id: str
  .name: str
```

### count_investment_funds

```python
await graphlit.client.count_investment_funds(filter: Optional[InvestmentFundFilter], correlation_id: Optional[str]) -> CountInvestmentFunds
```

**Response:**
```
response.count_investment_funds
  .count: Optional[Any]
```

### create_investment_fund

```python
await graphlit.client.create_investment_fund(investment_fund: InvestmentFundInput) -> CreateInvestmentFund
```

**Response:**
```
response.create_investment_fund
  .id: str
  .name: str
```

### delete_all_investment_funds

```python
await graphlit.client.delete_all_investment_funds(
    filter: Optional[InvestmentFundFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllInvestmentFunds
```

**Response:**
```
response.delete_all_investment_funds
  .id: str
  .state: EntityState
```

### delete_investment_fund

```python
await graphlit.client.delete_investment_fund(id: str) -> DeleteInvestmentFund
```

**Response:**
```
response.delete_investment_fund
  .id: str
  .state: EntityState
```

### delete_investment_funds

```python
await graphlit.client.delete_investment_funds(ids: list[str], is_synchronous: Optional[bool]) -> DeleteInvestmentFunds
```

**Response:**
```
response.delete_investment_funds
  .id: str
  .state: EntityState
```

### get_investment_fund

```python
await graphlit.client.get_investment_fund(id: str, correlation_id: Optional[str]) -> GetInvestmentFund
```

**Response:**
```
response.investment_fund
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetInvestmentFundInvestmentFundOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_investment_funds

```python
await graphlit.client.query_investment_funds(filter: Optional[InvestmentFundFilter], correlation_id: Optional[str]) -> QueryInvestmentFunds
```

**Response:**
```
response.investment_funds
  .results: Optional[list[Optional["QueryInvestmentFundsInvestmentFundsResults"]]]
```

### query_investment_funds_clusters

```python
await graphlit.client.query_investment_funds_clusters(
    filter: Optional[InvestmentFundFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryInvestmentFundsClusters
```

**Response:**
```
response.investment_funds
  .results: Optional[
  .clusters: Optional["QueryInvestmentFundsClustersInvestmentFundsClusters"]
```

### query_investment_funds_expanded

```python
await graphlit.client.query_investment_funds_expanded(filter: Optional[InvestmentFundFilter], correlation_id: Optional[str]) -> QueryInvestmentFundsExpanded
```

**Response:**
```
response.investment_funds
  .results: Optional[
```

### update_investment_fund

```python
await graphlit.client.update_investment_fund(investment_fund: InvestmentFundUpdateInput) -> UpdateInvestmentFund
```

**Response:**
```
response.update_investment_fund
  .id: str
  .name: str
```

### count_labels

```python
await graphlit.client.count_labels(filter: Optional[LabelFilter], correlation_id: Optional[str]) -> CountLabels
```

**Response:**
```
response.count_labels
  .count: Optional[Any]
```

### create_label

```python
await graphlit.client.create_label(label: LabelInput) -> CreateLabel
```

**Response:**
```
response.create_label
  .id: str
  .name: str
```

### delete_all_labels

```python
await graphlit.client.delete_all_labels(
    filter: Optional[LabelFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllLabels
```

**Response:**
```
response.delete_all_labels
  .id: str
  .state: EntityState
```

### delete_label

```python
await graphlit.client.delete_label(id: str) -> DeleteLabel
```

**Response:**
```
response.delete_label
  .id: str
  .state: EntityState
```

### delete_labels

```python
await graphlit.client.delete_labels(ids: list[str], is_synchronous: Optional[bool]) -> DeleteLabels
```

**Response:**
```
response.delete_labels
  .id: str
  .state: EntityState
```

### get_label

```python
await graphlit.client.get_label(id: str, correlation_id: Optional[str]) -> GetLabel
```

**Response:**
```
response.label
  .id: str
  .name: str
  .description: Optional[str]
  .creation_date: Any
  .feeds: Optional[list[Optional["GetLabelLabelFeeds"]]]
```

### query_labels

```python
await graphlit.client.query_labels(filter: Optional[LabelFilter], correlation_id: Optional[str]) -> QueryLabels
```

**Response:**
```
response.labels
  .results: Optional[list[Optional["QueryLabelsLabelsResults"]]]
```

### update_label

```python
await graphlit.client.update_label(label: LabelUpdateInput) -> UpdateLabel
```

**Response:**
```
response.update_label
  .id: str
  .name: str
```

### upsert_label

```python
await graphlit.client.upsert_label(label: LabelInput) -> UpsertLabel
```

**Response:**
```
response.upsert_label
  .id: str
  .name: str
```

### count_medical_conditions

```python
await graphlit.client.count_medical_conditions(filter: Optional[MedicalConditionFilter], correlation_id: Optional[str]) -> CountMedicalConditions
```

**Response:**
```
response.count_medical_conditions
  .count: Optional[Any]
```

### create_medical_condition

```python
await graphlit.client.create_medical_condition(medical_condition: MedicalConditionInput) -> CreateMedicalCondition
```

**Response:**
```
response.create_medical_condition
  .id: str
  .name: str
```

### delete_all_medical_conditions

```python
await graphlit.client.delete_all_medical_conditions(
    filter: Optional[MedicalConditionFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalConditions
```

**Response:**
```
response.delete_all_medical_conditions
  .id: str
  .state: EntityState
```

### delete_medical_condition

```python
await graphlit.client.delete_medical_condition(id: str) -> DeleteMedicalCondition
```

**Response:**
```
response.delete_medical_condition
  .id: str
  .state: EntityState
```

### delete_medical_conditions

```python
await graphlit.client.delete_medical_conditions(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalConditions
```

**Response:**
```
response.delete_medical_conditions
  .id: str
  .state: EntityState
```

### get_medical_condition

```python
await graphlit.client.get_medical_condition(id: str, correlation_id: Optional[str]) -> GetMedicalCondition
```

**Response:**
```
response.medical_condition
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalConditionMedicalConditionOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_conditions

```python
await graphlit.client.query_medical_conditions(filter: Optional[MedicalConditionFilter], correlation_id: Optional[str]) -> QueryMedicalConditions
```

**Response:**
```
response.medical_conditions
  .results: Optional[list[Optional["QueryMedicalConditionsMedicalConditionsResults"]]]
```

### query_medical_conditions_clusters

```python
await graphlit.client.query_medical_conditions_clusters(
    filter: Optional[MedicalConditionFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalConditionsClusters
```

**Response:**
```
response.medical_conditions
  .results: Optional[
  .clusters: Optional["QueryMedicalConditionsClustersMedicalConditionsClusters"]
```

### update_medical_condition

```python
await graphlit.client.update_medical_condition(medical_condition: MedicalConditionUpdateInput) -> UpdateMedicalCondition
```

**Response:**
```
response.update_medical_condition
  .id: str
  .name: str
```

### count_medical_contraindications

```python
await graphlit.client.count_medical_contraindications(filter: Optional[MedicalContraindicationFilter], correlation_id: Optional[str]) -> CountMedicalContraindications
```

**Response:**
```
response.count_medical_contraindications
  .count: Optional[Any]
```

### create_medical_contraindication

```python
await graphlit.client.create_medical_contraindication(medical_contraindication: MedicalContraindicationInput) -> CreateMedicalContraindication
```

**Response:**
```
response.create_medical_contraindication
  .id: str
  .name: str
```

### delete_all_medical_contraindications

```python
await graphlit.client.delete_all_medical_contraindications(
    filter: Optional[MedicalContraindicationFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalContraindications
```

**Response:**
```
response.delete_all_medical_contraindications
  .id: str
  .state: EntityState
```

### delete_medical_contraindication

```python
await graphlit.client.delete_medical_contraindication(id: str) -> DeleteMedicalContraindication
```

**Response:**
```
response.delete_medical_contraindication
  .id: str
  .state: EntityState
```

### delete_medical_contraindications

```python
await graphlit.client.delete_medical_contraindications(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalContraindications
```

**Response:**
```
response.delete_medical_contraindications
  .id: str
  .state: EntityState
```

### get_medical_contraindication

```python
await graphlit.client.get_medical_contraindication(id: str, correlation_id: Optional[str]) -> GetMedicalContraindication
```

**Response:**
```
response.medical_contraindication
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalContraindicationMedicalContraindicationOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_contraindications

```python
await graphlit.client.query_medical_contraindications(filter: Optional[MedicalContraindicationFilter], correlation_id: Optional[str]) -> QueryMedicalContraindications
```

**Response:**
```
response.medical_contraindications
  .results: Optional[
```

### query_medical_contraindications_clusters

```python
await graphlit.client.query_medical_contraindications_clusters(
    filter: Optional[MedicalContraindicationFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalContraindicationsClusters
```

**Response:**
```
response.medical_contraindications
  .results: Optional[
  .clusters: Optional[
```

### update_medical_contraindication

```python
await graphlit.client.update_medical_contraindication(medical_contraindication: MedicalContraindicationUpdateInput) -> UpdateMedicalContraindication
```

**Response:**
```
response.update_medical_contraindication
  .id: str
  .name: str
```

### count_medical_devices

```python
await graphlit.client.count_medical_devices(filter: Optional[MedicalDeviceFilter], correlation_id: Optional[str]) -> CountMedicalDevices
```

**Response:**
```
response.count_medical_devices
  .count: Optional[Any]
```

### create_medical_device

```python
await graphlit.client.create_medical_device(medical_device: MedicalDeviceInput) -> CreateMedicalDevice
```

**Response:**
```
response.create_medical_device
  .id: str
  .name: str
```

### delete_all_medical_devices

```python
await graphlit.client.delete_all_medical_devices(
    filter: Optional[MedicalDeviceFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalDevices
```

**Response:**
```
response.delete_all_medical_devices
  .id: str
  .state: EntityState
```

### delete_medical_device

```python
await graphlit.client.delete_medical_device(id: str) -> DeleteMedicalDevice
```

**Response:**
```
response.delete_medical_device
  .id: str
  .state: EntityState
```

### delete_medical_devices

```python
await graphlit.client.delete_medical_devices(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalDevices
```

**Response:**
```
response.delete_medical_devices
  .id: str
  .state: EntityState
```

### get_medical_device

```python
await graphlit.client.get_medical_device(id: str, correlation_id: Optional[str]) -> GetMedicalDevice
```

**Response:**
```
response.medical_device
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalDeviceMedicalDeviceOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_devices

```python
await graphlit.client.query_medical_devices(filter: Optional[MedicalDeviceFilter], correlation_id: Optional[str]) -> QueryMedicalDevices
```

**Response:**
```
response.medical_devices
  .results: Optional[list[Optional["QueryMedicalDevicesMedicalDevicesResults"]]]
```

### query_medical_devices_clusters

```python
await graphlit.client.query_medical_devices_clusters(
    filter: Optional[MedicalDeviceFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalDevicesClusters
```

**Response:**
```
response.medical_devices
  .results: Optional[
  .clusters: Optional["QueryMedicalDevicesClustersMedicalDevicesClusters"]
```

### update_medical_device

```python
await graphlit.client.update_medical_device(medical_device: MedicalDeviceUpdateInput) -> UpdateMedicalDevice
```

**Response:**
```
response.update_medical_device
  .id: str
  .name: str
```

### count_medical_drugs

```python
await graphlit.client.count_medical_drugs(filter: Optional[MedicalDrugFilter], correlation_id: Optional[str]) -> CountMedicalDrugs
```

**Response:**
```
response.count_medical_drugs
  .count: Optional[Any]
```

### create_medical_drug

```python
await graphlit.client.create_medical_drug(medical_drug: MedicalDrugInput) -> CreateMedicalDrug
```

**Response:**
```
response.create_medical_drug
  .id: str
  .name: str
```

### delete_all_medical_drugs

```python
await graphlit.client.delete_all_medical_drugs(
    filter: Optional[MedicalDrugFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalDrugs
```

**Response:**
```
response.delete_all_medical_drugs
  .id: str
  .state: EntityState
```

### delete_medical_drug

```python
await graphlit.client.delete_medical_drug(id: str) -> DeleteMedicalDrug
```

**Response:**
```
response.delete_medical_drug
  .id: str
  .state: EntityState
```

### delete_medical_drugs

```python
await graphlit.client.delete_medical_drugs(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalDrugs
```

**Response:**
```
response.delete_medical_drugs
  .id: str
  .state: EntityState
```

### get_medical_drug

```python
await graphlit.client.get_medical_drug(id: str, correlation_id: Optional[str]) -> GetMedicalDrug
```

**Response:**
```
response.medical_drug
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalDrugMedicalDrugOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_drugs

```python
await graphlit.client.query_medical_drugs(filter: Optional[MedicalDrugFilter], correlation_id: Optional[str]) -> QueryMedicalDrugs
```

**Response:**
```
response.medical_drugs
  .results: Optional[list[Optional["QueryMedicalDrugsMedicalDrugsResults"]]]
```

### query_medical_drugs_clusters

```python
await graphlit.client.query_medical_drugs_clusters(
    filter: Optional[MedicalDrugFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalDrugsClusters
```

**Response:**
```
response.medical_drugs
  .results: Optional[list[Optional["QueryMedicalDrugsClustersMedicalDrugsResults"]]]
  .clusters: Optional["QueryMedicalDrugsClustersMedicalDrugsClusters"]
```

### update_medical_drug

```python
await graphlit.client.update_medical_drug(medical_drug: MedicalDrugUpdateInput) -> UpdateMedicalDrug
```

**Response:**
```
response.update_medical_drug
  .id: str
  .name: str
```

### count_medical_drug_classes

```python
await graphlit.client.count_medical_drug_classes(filter: Optional[MedicalDrugClassFilter], correlation_id: Optional[str]) -> CountMedicalDrugClasses
```

**Response:**
```
response.count_medical_drug_classes
  .count: Optional[Any]
```

### create_medical_drug_class

```python
await graphlit.client.create_medical_drug_class(medical_drug_class: MedicalDrugClassInput) -> CreateMedicalDrugClass
```

**Response:**
```
response.create_medical_drug_class
  .id: str
  .name: str
```

### delete_all_medical_drug_classes

```python
await graphlit.client.delete_all_medical_drug_classes(
    filter: Optional[MedicalDrugClassFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalDrugClasses
```

**Response:**
```
response.delete_all_medical_drug_classes
  .id: str
  .state: EntityState
```

### delete_medical_drug_class

```python
await graphlit.client.delete_medical_drug_class(id: str) -> DeleteMedicalDrugClass
```

**Response:**
```
response.delete_medical_drug_class
  .id: str
  .state: EntityState
```

### delete_medical_drug_classes

```python
await graphlit.client.delete_medical_drug_classes(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalDrugClasses
```

**Response:**
```
response.delete_medical_drug_classes
  .id: str
  .state: EntityState
```

### get_medical_drug_class

```python
await graphlit.client.get_medical_drug_class(id: str, correlation_id: Optional[str]) -> GetMedicalDrugClass
```

**Response:**
```
response.medical_drug_class
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalDrugClassMedicalDrugClassOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_drug_classes

```python
await graphlit.client.query_medical_drug_classes(filter: Optional[MedicalDrugClassFilter], correlation_id: Optional[str]) -> QueryMedicalDrugClasses
```

**Response:**
```
response.medical_drug_classes
  .results: Optional[
```

### query_medical_drug_classes_clusters

```python
await graphlit.client.query_medical_drug_classes_clusters(
    filter: Optional[MedicalDrugClassFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalDrugClassesClusters
```

**Response:**
```
response.medical_drug_classes
  .results: Optional[
  .clusters: Optional["QueryMedicalDrugClassesClustersMedicalDrugClassesClusters"]
```

### update_medical_drug_class

```python
await graphlit.client.update_medical_drug_class(medical_drug_class: MedicalDrugClassUpdateInput) -> UpdateMedicalDrugClass
```

**Response:**
```
response.update_medical_drug_class
  .id: str
  .name: str
```

### count_medical_guidelines

```python
await graphlit.client.count_medical_guidelines(filter: Optional[MedicalGuidelineFilter], correlation_id: Optional[str]) -> CountMedicalGuidelines
```

**Response:**
```
response.count_medical_guidelines
  .count: Optional[Any]
```

### create_medical_guideline

```python
await graphlit.client.create_medical_guideline(medical_guideline: MedicalGuidelineInput) -> CreateMedicalGuideline
```

**Response:**
```
response.create_medical_guideline
  .id: str
  .name: str
```

### delete_all_medical_guidelines

```python
await graphlit.client.delete_all_medical_guidelines(
    filter: Optional[MedicalGuidelineFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalGuidelines
```

**Response:**
```
response.delete_all_medical_guidelines
  .id: str
  .state: EntityState
```

### delete_medical_guideline

```python
await graphlit.client.delete_medical_guideline(id: str) -> DeleteMedicalGuideline
```

**Response:**
```
response.delete_medical_guideline
  .id: str
  .state: EntityState
```

### delete_medical_guidelines

```python
await graphlit.client.delete_medical_guidelines(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalGuidelines
```

**Response:**
```
response.delete_medical_guidelines
  .id: str
  .state: EntityState
```

### get_medical_guideline

```python
await graphlit.client.get_medical_guideline(id: str, correlation_id: Optional[str]) -> GetMedicalGuideline
```

**Response:**
```
response.medical_guideline
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalGuidelineMedicalGuidelineOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_guidelines

```python
await graphlit.client.query_medical_guidelines(filter: Optional[MedicalGuidelineFilter], correlation_id: Optional[str]) -> QueryMedicalGuidelines
```

**Response:**
```
response.medical_guidelines
  .results: Optional[list[Optional["QueryMedicalGuidelinesMedicalGuidelinesResults"]]]
```

### query_medical_guidelines_clusters

```python
await graphlit.client.query_medical_guidelines_clusters(
    filter: Optional[MedicalGuidelineFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalGuidelinesClusters
```

**Response:**
```
response.medical_guidelines
  .results: Optional[
  .clusters: Optional["QueryMedicalGuidelinesClustersMedicalGuidelinesClusters"]
```

### update_medical_guideline

```python
await graphlit.client.update_medical_guideline(medical_guideline: MedicalGuidelineUpdateInput) -> UpdateMedicalGuideline
```

**Response:**
```
response.update_medical_guideline
  .id: str
  .name: str
```

### count_medical_indications

```python
await graphlit.client.count_medical_indications(filter: Optional[MedicalIndicationFilter], correlation_id: Optional[str]) -> CountMedicalIndications
```

**Response:**
```
response.count_medical_indications
  .count: Optional[Any]
```

### create_medical_indication

```python
await graphlit.client.create_medical_indication(medical_indication: MedicalIndicationInput) -> CreateMedicalIndication
```

**Response:**
```
response.create_medical_indication
  .id: str
  .name: str
```

### delete_all_medical_indications

```python
await graphlit.client.delete_all_medical_indications(
    filter: Optional[MedicalIndicationFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalIndications
```

**Response:**
```
response.delete_all_medical_indications
  .id: str
  .state: EntityState
```

### delete_medical_indication

```python
await graphlit.client.delete_medical_indication(id: str) -> DeleteMedicalIndication
```

**Response:**
```
response.delete_medical_indication
  .id: str
  .state: EntityState
```

### delete_medical_indications

```python
await graphlit.client.delete_medical_indications(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalIndications
```

**Response:**
```
response.delete_medical_indications
  .id: str
  .state: EntityState
```

### get_medical_indication

```python
await graphlit.client.get_medical_indication(id: str, correlation_id: Optional[str]) -> GetMedicalIndication
```

**Response:**
```
response.medical_indication
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalIndicationMedicalIndicationOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_indications

```python
await graphlit.client.query_medical_indications(filter: Optional[MedicalIndicationFilter], correlation_id: Optional[str]) -> QueryMedicalIndications
```

**Response:**
```
response.medical_indications
  .results: Optional[
```

### query_medical_indications_clusters

```python
await graphlit.client.query_medical_indications_clusters(
    filter: Optional[MedicalIndicationFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalIndicationsClusters
```

**Response:**
```
response.medical_indications
  .results: Optional[
  .clusters: Optional["QueryMedicalIndicationsClustersMedicalIndicationsClusters"]
```

### update_medical_indication

```python
await graphlit.client.update_medical_indication(medical_indication: MedicalIndicationUpdateInput) -> UpdateMedicalIndication
```

**Response:**
```
response.update_medical_indication
  .id: str
  .name: str
```

### count_medical_procedures

```python
await graphlit.client.count_medical_procedures(filter: Optional[MedicalProcedureFilter], correlation_id: Optional[str]) -> CountMedicalProcedures
```

**Response:**
```
response.count_medical_procedures
  .count: Optional[Any]
```

### create_medical_procedure

```python
await graphlit.client.create_medical_procedure(medical_procedure: MedicalProcedureInput) -> CreateMedicalProcedure
```

**Response:**
```
response.create_medical_procedure
  .id: str
  .name: str
```

### delete_all_medical_procedures

```python
await graphlit.client.delete_all_medical_procedures(
    filter: Optional[MedicalProcedureFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalProcedures
```

**Response:**
```
response.delete_all_medical_procedures
  .id: str
  .state: EntityState
```

### delete_medical_procedure

```python
await graphlit.client.delete_medical_procedure(id: str) -> DeleteMedicalProcedure
```

**Response:**
```
response.delete_medical_procedure
  .id: str
  .state: EntityState
```

### delete_medical_procedures

```python
await graphlit.client.delete_medical_procedures(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalProcedures
```

**Response:**
```
response.delete_medical_procedures
  .id: str
  .state: EntityState
```

### get_medical_procedure

```python
await graphlit.client.get_medical_procedure(id: str, correlation_id: Optional[str]) -> GetMedicalProcedure
```

**Response:**
```
response.medical_procedure
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalProcedureMedicalProcedureOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_procedures

```python
await graphlit.client.query_medical_procedures(filter: Optional[MedicalProcedureFilter], correlation_id: Optional[str]) -> QueryMedicalProcedures
```

**Response:**
```
response.medical_procedures
  .results: Optional[list[Optional["QueryMedicalProceduresMedicalProceduresResults"]]]
```

### query_medical_procedures_clusters

```python
await graphlit.client.query_medical_procedures_clusters(
    filter: Optional[MedicalProcedureFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalProceduresClusters
```

**Response:**
```
response.medical_procedures
  .results: Optional[
  .clusters: Optional["QueryMedicalProceduresClustersMedicalProceduresClusters"]
```

### update_medical_procedure

```python
await graphlit.client.update_medical_procedure(medical_procedure: MedicalProcedureUpdateInput) -> UpdateMedicalProcedure
```

**Response:**
```
response.update_medical_procedure
  .id: str
  .name: str
```

### count_medical_studies

```python
await graphlit.client.count_medical_studies(filter: Optional[MedicalStudyFilter], correlation_id: Optional[str]) -> CountMedicalStudies
```

**Response:**
```
response.count_medical_studies
  .count: Optional[Any]
```

### create_medical_study

```python
await graphlit.client.create_medical_study(medical_study: MedicalStudyInput) -> CreateMedicalStudy
```

**Response:**
```
response.create_medical_study
  .id: str
  .name: str
```

### delete_all_medical_studies

```python
await graphlit.client.delete_all_medical_studies(
    filter: Optional[MedicalStudyFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalStudies
```

**Response:**
```
response.delete_all_medical_studies
  .id: str
  .state: EntityState
```

### delete_medical_studies

```python
await graphlit.client.delete_medical_studies(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalStudies
```

**Response:**
```
response.delete_medical_studies
  .id: str
  .state: EntityState
```

### delete_medical_study

```python
await graphlit.client.delete_medical_study(id: str) -> DeleteMedicalStudy
```

**Response:**
```
response.delete_medical_study
  .id: str
  .state: EntityState
```

### get_medical_study

```python
await graphlit.client.get_medical_study(id: str, correlation_id: Optional[str]) -> GetMedicalStudy
```

**Response:**
```
response.medical_study
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalStudyMedicalStudyOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_studies

```python
await graphlit.client.query_medical_studies(filter: Optional[MedicalStudyFilter], correlation_id: Optional[str]) -> QueryMedicalStudies
```

**Response:**
```
response.medical_studies
  .results: Optional[list[Optional["QueryMedicalStudiesMedicalStudiesResults"]]]
```

### query_medical_studies_clusters

```python
await graphlit.client.query_medical_studies_clusters(
    filter: Optional[MedicalStudyFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalStudiesClusters
```

**Response:**
```
response.medical_studies
  .results: Optional[
  .clusters: Optional["QueryMedicalStudiesClustersMedicalStudiesClusters"]
```

### update_medical_study

```python
await graphlit.client.update_medical_study(medical_study: MedicalStudyUpdateInput) -> UpdateMedicalStudy
```

**Response:**
```
response.update_medical_study
  .id: str
  .name: str
```

### count_medical_tests

```python
await graphlit.client.count_medical_tests(filter: Optional[MedicalTestFilter], correlation_id: Optional[str]) -> CountMedicalTests
```

**Response:**
```
response.count_medical_tests
  .count: Optional[Any]
```

### create_medical_test

```python
await graphlit.client.create_medical_test(medical_test: MedicalTestInput) -> CreateMedicalTest
```

**Response:**
```
response.create_medical_test
  .id: str
  .name: str
```

### delete_all_medical_tests

```python
await graphlit.client.delete_all_medical_tests(
    filter: Optional[MedicalTestFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalTests
```

**Response:**
```
response.delete_all_medical_tests
  .id: str
  .state: EntityState
```

### delete_medical_test

```python
await graphlit.client.delete_medical_test(id: str) -> DeleteMedicalTest
```

**Response:**
```
response.delete_medical_test
  .id: str
  .state: EntityState
```

### delete_medical_tests

```python
await graphlit.client.delete_medical_tests(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalTests
```

**Response:**
```
response.delete_medical_tests
  .id: str
  .state: EntityState
```

### get_medical_test

```python
await graphlit.client.get_medical_test(id: str, correlation_id: Optional[str]) -> GetMedicalTest
```

**Response:**
```
response.medical_test
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalTestMedicalTestOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_tests

```python
await graphlit.client.query_medical_tests(filter: Optional[MedicalTestFilter], correlation_id: Optional[str]) -> QueryMedicalTests
```

**Response:**
```
response.medical_tests
  .results: Optional[list[Optional["QueryMedicalTestsMedicalTestsResults"]]]
```

### query_medical_tests_clusters

```python
await graphlit.client.query_medical_tests_clusters(
    filter: Optional[MedicalTestFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalTestsClusters
```

**Response:**
```
response.medical_tests
  .results: Optional[list[Optional["QueryMedicalTestsClustersMedicalTestsResults"]]]
  .clusters: Optional["QueryMedicalTestsClustersMedicalTestsClusters"]
```

### update_medical_test

```python
await graphlit.client.update_medical_test(medical_test: MedicalTestUpdateInput) -> UpdateMedicalTest
```

**Response:**
```
response.update_medical_test
  .id: str
  .name: str
```

### count_medical_therapies

```python
await graphlit.client.count_medical_therapies(filter: Optional[MedicalTherapyFilter], correlation_id: Optional[str]) -> CountMedicalTherapies
```

**Response:**
```
response.count_medical_therapies
  .count: Optional[Any]
```

### create_medical_therapy

```python
await graphlit.client.create_medical_therapy(medical_therapy: MedicalTherapyInput) -> CreateMedicalTherapy
```

**Response:**
```
response.create_medical_therapy
  .id: str
  .name: str
```

### delete_all_medical_therapies

```python
await graphlit.client.delete_all_medical_therapies(
    filter: Optional[MedicalTherapyFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllMedicalTherapies
```

**Response:**
```
response.delete_all_medical_therapies
  .id: str
  .state: EntityState
```

### delete_medical_therapies

```python
await graphlit.client.delete_medical_therapies(ids: list[str], is_synchronous: Optional[bool]) -> DeleteMedicalTherapies
```

**Response:**
```
response.delete_medical_therapies
  .id: str
  .state: EntityState
```

### delete_medical_therapy

```python
await graphlit.client.delete_medical_therapy(id: str) -> DeleteMedicalTherapy
```

**Response:**
```
response.delete_medical_therapy
  .id: str
  .state: EntityState
```

### get_medical_therapy

```python
await graphlit.client.get_medical_therapy(id: str, correlation_id: Optional[str]) -> GetMedicalTherapy
```

**Response:**
```
response.medical_therapy
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetMedicalTherapyMedicalTherapyOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_medical_therapies

```python
await graphlit.client.query_medical_therapies(filter: Optional[MedicalTherapyFilter], correlation_id: Optional[str]) -> QueryMedicalTherapies
```

**Response:**
```
response.medical_therapies
  .results: Optional[list[Optional["QueryMedicalTherapiesMedicalTherapiesResults"]]]
```

### query_medical_therapies_clusters

```python
await graphlit.client.query_medical_therapies_clusters(
    filter: Optional[MedicalTherapyFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryMedicalTherapiesClusters
```

**Response:**
```
response.medical_therapies
  .results: Optional[
  .clusters: Optional["QueryMedicalTherapiesClustersMedicalTherapiesClusters"]
```

### update_medical_therapy

```python
await graphlit.client.update_medical_therapy(medical_therapy: MedicalTherapyUpdateInput) -> UpdateMedicalTherapy
```

**Response:**
```
response.update_medical_therapy
  .id: str
  .name: str
```

### send_notification

```python
await graphlit.client.send_notification(
    connector: IntegrationConnectorInput,
    text: str,
    text_type: Optional[TextTypes],
) -> SendNotification
```

**Response:**
```
response.send_notification
  .result: Optional[bool]
```

### create_observation

```python
await graphlit.client.create_observation(observation: ObservationInput) -> CreateObservation
```

**Response:**
```
response.create_observation
  .id: str
  .state: EntityState
```

### delete_observation

```python
await graphlit.client.delete_observation(id: str) -> DeleteObservation
```

**Response:**
```
response.delete_observation
  .id: str
  .state: EntityState
```

### match_entity

```python
await graphlit.client.match_entity(
    observable: ObservableInput,
    candidates: list[EntityReferenceInput],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> MatchEntity
```

**Response:**
```
response.match_entity
  .reference: Optional["MatchEntityMatchEntityReference"]
  .relevance: Optional[float]
  .reasoning: Optional[str]
```

### resolve_entities

```python
await graphlit.client.resolve_entities(
    type: ObservableTypes,
    entities: list[EntityReferenceInput],
    threshold: Optional[float],
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ResolveEntities
```

**Response:**
```
response.resolve_entities
  .type: ObservableTypes
  .primary: Optional["ResolveEntitiesResolveEntitiesPrimary"]
  .resolved: Optional[list["ResolveEntitiesResolveEntitiesResolved"]]
  .relevance: float
  .reasoning: str
  .primary_cluster: Optional["ResolveEntitiesResolveEntitiesPrimaryCluster"]
  .outlier_clusters: Optional[
```

### resolve_entity

```python
await graphlit.client.resolve_entity(
    type: ObservableTypes,
    source: EntityReferenceInput,
    target: EntityReferenceInput,
    specification: Optional[EntityReferenceInput],
    correlation_id: Optional[str],
) -> ResolveEntity
```

**Response:**
```
response.resolve_entity
  .reference: Optional["ResolveEntityResolveEntityReference"]
  .relevance: Optional[float]
  .reasoning: Optional[str]
```

### update_observation

```python
await graphlit.client.update_observation(observation: ObservationUpdateInput) -> UpdateObservation
```

**Response:**
```
response.update_observation
  .id: str
  .state: EntityState
```

### count_organizations

```python
await graphlit.client.count_organizations(filter: Optional[OrganizationFilter], correlation_id: Optional[str]) -> CountOrganizations
```

**Response:**
```
response.count_organizations
  .count: Optional[Any]
```

### create_organization

```python
await graphlit.client.create_organization(organization: OrganizationInput) -> CreateOrganization
```

**Response:**
```
response.create_organization
  .id: str
  .name: str
```

### delete_all_organizations

```python
await graphlit.client.delete_all_organizations(
    filter: Optional[OrganizationFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllOrganizations
```

**Response:**
```
response.delete_all_organizations
  .id: str
  .state: EntityState
```

### delete_organization

```python
await graphlit.client.delete_organization(id: str) -> DeleteOrganization
```

**Response:**
```
response.delete_organization
  .id: str
  .state: EntityState
```

### delete_organizations

```python
await graphlit.client.delete_organizations(ids: list[str], is_synchronous: Optional[bool]) -> DeleteOrganizations
```

**Response:**
```
response.delete_organizations
  .id: str
  .state: EntityState
```

### enrich_organizations

```python
await graphlit.client.enrich_organizations(
    connector: EntityEnrichmentConnectorInput,
    filter: Optional[OrganizationFilter],
    correlation_id: Optional[str],
) -> EnrichOrganizations
```

**Response:**
```
response.enrich_organizations
  .id: str
  .name: str
```

### get_organization

```python
await graphlit.client.get_organization(id: str, correlation_id: Optional[str]) -> GetOrganization
```

**Response:**
```
response.organization
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetOrganizationOrganizationOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_organizations

```python
await graphlit.client.query_organizations(filter: Optional[OrganizationFilter], correlation_id: Optional[str]) -> QueryOrganizations
```

**Response:**
```
response.organizations
  .results: Optional[list[Optional["QueryOrganizationsOrganizationsResults"]]]
```

### query_organizations_clusters

```python
await graphlit.client.query_organizations_clusters(
    filter: Optional[OrganizationFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryOrganizationsClusters
```

**Response:**
```
response.organizations
  .results: Optional[list[Optional["QueryOrganizationsClustersOrganizationsResults"]]]
  .clusters: Optional["QueryOrganizationsClustersOrganizationsClusters"]
```

### query_organizations_expanded

```python
await graphlit.client.query_organizations_expanded(filter: Optional[OrganizationFilter], correlation_id: Optional[str]) -> QueryOrganizationsExpanded
```

**Response:**
```
response.organizations
  .results: Optional[list[Optional["QueryOrganizationsExpandedOrganizationsResults"]]]
```

### update_organization

```python
await graphlit.client.update_organization(organization: OrganizationUpdateInput) -> UpdateOrganization
```

**Response:**
```
response.update_organization
  .id: str
  .name: str
```

### count_persons

```python
await graphlit.client.count_persons(filter: Optional[PersonFilter], correlation_id: Optional[str]) -> CountPersons
```

**Response:**
```
response.count_persons
  .count: Optional[Any]
```

### create_person

```python
await graphlit.client.create_person(person: PersonInput) -> CreatePerson
```

**Response:**
```
response.create_person
  .id: str
  .name: str
```

### delete_all_persons

```python
await graphlit.client.delete_all_persons(
    filter: Optional[PersonFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllPersons
```

**Response:**
```
response.delete_all_persons
  .id: str
  .state: EntityState
```

### delete_person

```python
await graphlit.client.delete_person(id: str) -> DeletePerson
```

**Response:**
```
response.delete_person
  .id: str
  .state: EntityState
```

### delete_persons

```python
await graphlit.client.delete_persons(ids: list[str], is_synchronous: Optional[bool]) -> DeletePersons
```

**Response:**
```
response.delete_persons
  .id: str
  .state: EntityState
```

### enrich_persons

```python
await graphlit.client.enrich_persons(
    connector: EntityEnrichmentConnectorInput,
    filter: Optional[PersonFilter],
    correlation_id: Optional[str],
) -> EnrichPersons
```

**Response:**
```
response.enrich_persons
  .id: str
  .name: str
```

### get_person

```python
await graphlit.client.get_person(id: str, correlation_id: Optional[str]) -> GetPerson
```

**Response:**
```
response.person
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetPersonPersonOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_persons

```python
await graphlit.client.query_persons(filter: Optional[PersonFilter], correlation_id: Optional[str]) -> QueryPersons
```

**Response:**
```
response.persons
  .results: Optional[list[Optional["QueryPersonsPersonsResults"]]]
```

### query_persons_clusters

```python
await graphlit.client.query_persons_clusters(
    filter: Optional[PersonFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryPersonsClusters
```

**Response:**
```
response.persons
  .results: Optional[list[Optional["QueryPersonsClustersPersonsResults"]]]
  .clusters: Optional["QueryPersonsClustersPersonsClusters"]
```

### query_persons_expanded

```python
await graphlit.client.query_persons_expanded(filter: Optional[PersonFilter], correlation_id: Optional[str]) -> QueryPersonsExpanded
```

**Response:**
```
response.persons
  .results: Optional[list[Optional["QueryPersonsExpandedPersonsResults"]]]
```

### update_person

```python
await graphlit.client.update_person(person: PersonUpdateInput) -> UpdatePerson
```

**Response:**
```
response.update_person
  .id: str
  .name: str
```

### count_personas

```python
await graphlit.client.count_personas(filter: Optional[PersonaFilter], correlation_id: Optional[str]) -> CountPersonas
```

**Response:**
```
response.count_personas
  .count: Optional[Any]
```

### create_persona

```python
await graphlit.client.create_persona(persona: PersonaInput) -> CreatePersona
```

**Response:**
```
response.create_persona
  .id: str
  .name: str
  .state: EntityState
  .role: Optional[str]
```

### delete_all_personas

```python
await graphlit.client.delete_all_personas(
    filter: Optional[PersonaFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllPersonas
```

**Response:**
```
response.delete_all_personas
  .id: str
  .state: EntityState
```

### delete_persona

```python
await graphlit.client.delete_persona(id: str) -> DeletePersona
```

**Response:**
```
response.delete_persona
  .id: str
  .state: EntityState
```

### delete_personas

```python
await graphlit.client.delete_personas(ids: list[str], is_synchronous: Optional[bool]) -> DeletePersonas
```

**Response:**
```
response.delete_personas
  .id: str
  .state: EntityState
```

### get_persona

```python
await graphlit.client.get_persona(id: str, correlation_id: Optional[str]) -> GetPersona
```

**Response:**
```
response.persona
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetPersonaPersonaOwner"
  .state: EntityState
  .role: Optional[str]
  .instructions: Optional[str]
```

### query_personas

```python
await graphlit.client.query_personas(filter: Optional[PersonaFilter], correlation_id: Optional[str]) -> QueryPersonas
```

**Response:**
```
response.personas
  .results: Optional[list["QueryPersonasPersonasResults"]]
```

### update_persona

```python
await graphlit.client.update_persona(persona: PersonaUpdateInput) -> UpdatePersona
```

**Response:**
```
response.update_persona
  .id: str
  .name: str
  .state: EntityState
  .role: Optional[str]
```

### count_places

```python
await graphlit.client.count_places(filter: Optional[PlaceFilter], correlation_id: Optional[str]) -> CountPlaces
```

**Response:**
```
response.count_places
  .count: Optional[Any]
```

### create_place

```python
await graphlit.client.create_place(place: PlaceInput) -> CreatePlace
```

**Response:**
```
response.create_place
  .id: str
  .name: str
```

### delete_all_places

```python
await graphlit.client.delete_all_places(
    filter: Optional[PlaceFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllPlaces
```

**Response:**
```
response.delete_all_places
  .id: str
  .state: EntityState
```

### delete_place

```python
await graphlit.client.delete_place(id: str) -> DeletePlace
```

**Response:**
```
response.delete_place
  .id: str
  .state: EntityState
```

### delete_places

```python
await graphlit.client.delete_places(ids: list[str], is_synchronous: Optional[bool]) -> DeletePlaces
```

**Response:**
```
response.delete_places
  .id: str
  .state: EntityState
```

### enrich_places

```python
await graphlit.client.enrich_places(
    connector: EntityEnrichmentConnectorInput,
    filter: Optional[PlaceFilter],
    correlation_id: Optional[str],
) -> EnrichPlaces
```

**Response:**
```
response.enrich_places
  .id: str
  .name: str
```

### get_place

```python
await graphlit.client.get_place(id: str, correlation_id: Optional[str]) -> GetPlace
```

**Response:**
```
response.place
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetPlacePlaceOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_places

```python
await graphlit.client.query_places(filter: Optional[PlaceFilter], correlation_id: Optional[str]) -> QueryPlaces
```

**Response:**
```
response.places
  .results: Optional[list[Optional["QueryPlacesPlacesResults"]]]
```

### query_places_clusters

```python
await graphlit.client.query_places_clusters(
    filter: Optional[PlaceFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryPlacesClusters
```

**Response:**
```
response.places
  .results: Optional[list[Optional["QueryPlacesClustersPlacesResults"]]]
  .clusters: Optional["QueryPlacesClustersPlacesClusters"]
```

### update_place

```python
await graphlit.client.update_place(place: PlaceUpdateInput) -> UpdatePlace
```

**Response:**
```
response.update_place
  .id: str
  .name: str
```

### count_products

```python
await graphlit.client.count_products(filter: Optional[ProductFilter], correlation_id: Optional[str]) -> CountProducts
```

**Response:**
```
response.count_products
  .count: Optional[Any]
```

### create_product

```python
await graphlit.client.create_product(product: ProductInput) -> CreateProduct
```

**Response:**
```
response.create_product
  .id: str
  .name: str
```

### delete_all_products

```python
await graphlit.client.delete_all_products(
    filter: Optional[ProductFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllProducts
```

**Response:**
```
response.delete_all_products
  .id: str
  .state: EntityState
```

### delete_product

```python
await graphlit.client.delete_product(id: str) -> DeleteProduct
```

**Response:**
```
response.delete_product
  .id: str
  .state: EntityState
```

### delete_products

```python
await graphlit.client.delete_products(ids: list[str], is_synchronous: Optional[bool]) -> DeleteProducts
```

**Response:**
```
response.delete_products
  .id: str
  .state: EntityState
```

### enrich_products

```python
await graphlit.client.enrich_products(
    connector: EntityEnrichmentConnectorInput,
    filter: Optional[ProductFilter],
    correlation_id: Optional[str],
) -> EnrichProducts
```

**Response:**
```
response.enrich_products
  .id: str
  .name: str
```

### get_product

```python
await graphlit.client.get_product(id: str, correlation_id: Optional[str]) -> GetProduct
```

**Response:**
```
response.product
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetProductProductOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_products

```python
await graphlit.client.query_products(filter: Optional[ProductFilter], correlation_id: Optional[str]) -> QueryProducts
```

**Response:**
```
response.products
  .results: Optional[list[Optional["QueryProductsProductsResults"]]]
```

### query_products_clusters

```python
await graphlit.client.query_products_clusters(
    filter: Optional[ProductFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryProductsClusters
```

**Response:**
```
response.products
  .results: Optional[list[Optional["QueryProductsClustersProductsResults"]]]
  .clusters: Optional["QueryProductsClustersProductsClusters"]
```

### update_product

```python
await graphlit.client.update_product(product: ProductUpdateInput) -> UpdateProduct
```

**Response:**
```
response.update_product
  .id: str
  .name: str
```

### get_project

```python
await graphlit.client.get_project() -> GetProject
```

**Response:**
```
response.project
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .state: EntityState
  .environment_type: Optional[EnvironmentTypes]
  .platform: Optional[ResourceConnectorTypes]
  .region: Optional[str]
```

### lookup_credits

```python
await graphlit.client.lookup_credits(
    correlation_id: str,
    start_date: Optional[Any],
    duration: Optional[Any],
) -> LookupCredits
```

**Response:**
```
response.lookup_credits
  .correlation_id: Optional[str]
  .owner_id: Optional[str]
  .credits: Optional[Any]
  .storage_ratio: Optional[Any]
  .compute_ratio: Optional[Any]
  .embedding_ratio: Optional[Any]
  .completion_ratio: Optional[Any]
  .generation_ratio: Optional[Any]
```

### lookup_usage

```python
await graphlit.client.lookup_usage(
    correlation_id: str,
    start_date: Optional[Any],
    duration: Optional[Any],
) -> LookupUsage
```

**Response:**
```
response.lookup_usage
  .id: Optional[str]
  .correlation_id: Optional[str]
  .date: Any
  .credits: Optional[Any]
  .name: str
  .metric: Optional[BillableMetrics]
  .workflow: Optional[str]
  .entity_type: Optional[EntityTypes]
```

### query_credits

```python
await graphlit.client.query_credits(start_date: Any, duration: Any) -> QueryCredits
```

**Response:**
```
response.credits
  .correlation_id: Optional[str]
  .owner_id: Optional[str]
  .credits: Optional[Any]
  .storage_ratio: Optional[Any]
  .compute_ratio: Optional[Any]
  .embedding_ratio: Optional[Any]
  .completion_ratio: Optional[Any]
  .generation_ratio: Optional[Any]
```

### query_tokens

```python
await graphlit.client.query_tokens(start_date: Any, duration: Any) -> QueryTokens
```

**Response:**
```
response.tokens
  .correlation_id: Optional[str]
  .owner_id: Optional[str]
  .embedding_input_tokens: Optional[int]
  .embedding_model_services: Optional[list[Optional[str]]]
  .completion_input_tokens: Optional[int]
  .completion_output_tokens: Optional[int]
  .completion_model_services: Optional[list[Optional[str]]]
  .preparation_input_tokens: Optional[int]
```

### query_usage

```python
await graphlit.client.query_usage(
    start_date: Any,
    duration: Any,
    names: Optional[list[str]],
    excluded_names: Optional[list[str]],
    offset: Optional[int],
    limit: Optional[int],
) -> QueryUsage
```

**Response:**
```
response.usage
  .id: Optional[str]
  .correlation_id: Optional[str]
  .date: Any
  .credits: Optional[Any]
  .name: str
  .metric: Optional[BillableMetrics]
  .workflow: Optional[str]
  .entity_type: Optional[EntityTypes]
```

### update_project

```python
await graphlit.client.update_project(project: ProjectUpdateInput) -> UpdateProject
```

**Response:**
```
response.update_project
  .id: str
  .name: str
```

### count_repos

```python
await graphlit.client.count_repos(filter: Optional[RepoFilter], correlation_id: Optional[str]) -> CountRepos
```

**Response:**
```
response.count_repos
  .count: Optional[Any]
```

### create_repo

```python
await graphlit.client.create_repo(repo: RepoInput) -> CreateRepo
```

**Response:**
```
response.create_repo
  .id: str
  .name: str
```

### delete_all_repos

```python
await graphlit.client.delete_all_repos(
    filter: Optional[RepoFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllRepos
```

**Response:**
```
response.delete_all_repos
  .id: str
  .state: EntityState
```

### delete_repo

```python
await graphlit.client.delete_repo(id: str) -> DeleteRepo
```

**Response:**
```
response.delete_repo
  .id: str
  .state: EntityState
```

### delete_repos

```python
await graphlit.client.delete_repos(ids: list[str], is_synchronous: Optional[bool]) -> DeleteRepos
```

**Response:**
```
response.delete_repos
  .id: str
  .state: EntityState
```

### get_repo

```python
await graphlit.client.get_repo(id: str, correlation_id: Optional[str]) -> GetRepo
```

**Response:**
```
response.repo
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetRepoRepoOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_repos

```python
await graphlit.client.query_repos(filter: Optional[RepoFilter], correlation_id: Optional[str]) -> QueryRepos
```

**Response:**
```
response.repos
  .results: Optional[list[Optional["QueryReposReposResults"]]]
```

### query_repos_clusters

```python
await graphlit.client.query_repos_clusters(
    filter: Optional[RepoFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QueryReposClusters
```

**Response:**
```
response.repos
  .results: Optional[list[Optional["QueryReposClustersReposResults"]]]
  .clusters: Optional["QueryReposClustersReposClusters"]
```

### update_repo

```python
await graphlit.client.update_repo(repo: RepoUpdateInput) -> UpdateRepo
```

**Response:**
```
response.update_repo
  .id: str
  .name: str
```

### map_web

```python
await graphlit.client.map_web(
    uri: Any,
    allowed_paths: Optional[list[str]],
    excluded_paths: Optional[list[str]],
    correlation_id: Optional[str],
) -> MapWeb
```

**Response:**
```
response.map_web
  .results: Optional[list[Optional[Any]]]
```

### search_web

```python
await graphlit.client.search_web(
    text: str,
    service: Optional[SearchServiceTypes],
    limit: Optional[int],
    correlation_id: Optional[str],
) -> SearchWeb
```

**Response:**
```
response.search_web
  .results: Optional[list["SearchWebSearchWebResults"]]
```

### count_softwares

```python
await graphlit.client.count_softwares(filter: Optional[SoftwareFilter], correlation_id: Optional[str]) -> CountSoftwares
```

**Response:**
```
response.count_softwares
  .count: Optional[Any]
```

### create_software

```python
await graphlit.client.create_software(software: SoftwareInput) -> CreateSoftware
```

**Response:**
```
response.create_software
  .id: str
  .name: str
```

### delete_all_softwares

```python
await graphlit.client.delete_all_softwares(
    filter: Optional[SoftwareFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllSoftwares
```

**Response:**
```
response.delete_all_softwares
  .id: str
  .state: EntityState
```

### delete_software

```python
await graphlit.client.delete_software(id: str) -> DeleteSoftware
```

**Response:**
```
response.delete_software
  .id: str
  .state: EntityState
```

### delete_softwares

```python
await graphlit.client.delete_softwares(ids: list[str], is_synchronous: Optional[bool]) -> DeleteSoftwares
```

**Response:**
```
response.delete_softwares
  .id: str
  .state: EntityState
```

### get_software

```python
await graphlit.client.get_software(id: str, correlation_id: Optional[str]) -> GetSoftware
```

**Response:**
```
response.software
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetSoftwareSoftwareOwner"
  .state: EntityState
  .alternate_names: Optional[list[Optional[str]]]
  .uri: Optional[Any]
```

### query_softwares

```python
await graphlit.client.query_softwares(filter: Optional[SoftwareFilter], correlation_id: Optional[str]) -> QuerySoftwares
```

**Response:**
```
response.softwares
  .results: Optional[list[Optional["QuerySoftwaresSoftwaresResults"]]]
```

### query_softwares_clusters

```python
await graphlit.client.query_softwares_clusters(
    filter: Optional[SoftwareFilter],
    clusters: Optional[EntityClustersInput],
    correlation_id: Optional[str],
) -> QuerySoftwaresClusters
```

**Response:**
```
response.softwares
  .results: Optional[list[Optional["QuerySoftwaresClustersSoftwaresResults"]]]
  .clusters: Optional["QuerySoftwaresClustersSoftwaresClusters"]
```

### update_software

```python
await graphlit.client.update_software(software: SoftwareUpdateInput) -> UpdateSoftware
```

**Response:**
```
response.update_software
  .id: str
  .name: str
```

### count_specifications

```python
await graphlit.client.count_specifications(filter: Optional[SpecificationFilter], correlation_id: Optional[str]) -> CountSpecifications
```

**Response:**
```
response.count_specifications
  .count: Optional[Any]
```

### create_specification

```python
await graphlit.client.create_specification(specification: SpecificationInput) -> CreateSpecification
```

**Response:**
```
response.create_specification
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[SpecificationTypes]
  .service_type: Optional[ModelServiceTypes]
```

### delete_all_specifications

```python
await graphlit.client.delete_all_specifications(
    filter: Optional[SpecificationFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllSpecifications
```

**Response:**
```
response.delete_all_specifications
  .id: str
  .state: EntityState
```

### delete_specification

```python
await graphlit.client.delete_specification(id: str) -> DeleteSpecification
```

**Response:**
```
response.delete_specification
  .id: str
  .state: EntityState
```

### delete_specifications

```python
await graphlit.client.delete_specifications(ids: list[str], is_synchronous: Optional[bool]) -> DeleteSpecifications
```

**Response:**
```
response.delete_specifications
  .id: str
  .state: EntityState
```

### get_specification

```python
await graphlit.client.get_specification(id: str, correlation_id: Optional[str]) -> GetSpecification
```

**Response:**
```
response.specification
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetSpecificationSpecificationOwner"
  .state: EntityState
  .type: Optional[SpecificationTypes]
  .service_type: Optional[ModelServiceTypes]
```

### prompt_specifications

```python
await graphlit.client.prompt_specifications(prompt: str, ids: list[str]) -> PromptSpecifications
```

**Response:**
```
response.prompt_specifications
  .specification: Optional["PromptSpecificationsPromptSpecificationsSpecification"]
  .messages: Optional[
  .error: Optional[str]
```

### query_models

```python
await graphlit.client.query_models(filter: Optional[ModelFilter]) -> QueryModels
```

**Response:**
```
response.models
  .results: Optional[list["QueryModelsModelsResults"]]
```

### query_specifications

```python
await graphlit.client.query_specifications(filter: Optional[SpecificationFilter], correlation_id: Optional[str]) -> QuerySpecifications
```

**Response:**
```
response.specifications
  .results: Optional[list["QuerySpecificationsSpecificationsResults"]]
```

### specification_exists

```python
await graphlit.client.specification_exists(filter: Optional[SpecificationFilter], correlation_id: Optional[str]) -> SpecificationExists
```

**Response:**
```
response.specification_exists
  .result: Optional[bool]
```

### update_specification

```python
await graphlit.client.update_specification(specification: SpecificationUpdateInput) -> UpdateSpecification
```

**Response:**
```
response.update_specification
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[SpecificationTypes]
  .service_type: Optional[ModelServiceTypes]
```

### upsert_specification

```python
await graphlit.client.upsert_specification(specification: SpecificationInput) -> UpsertSpecification
```

**Response:**
```
response.upsert_specification
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[SpecificationTypes]
  .service_type: Optional[ModelServiceTypes]
```

### count_users

```python
await graphlit.client.count_users(filter: Optional[UserFilter], correlation_id: Optional[str]) -> CountUsers
```

**Response:**
```
response.count_users
  .count: Optional[Any]
```

### create_user

```python
await graphlit.client.create_user(user: UserInput) -> CreateUser
```

**Response:**
```
response.create_user
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[UserTypes]
  .description: Optional[str]
  .identifier: str
```

### delete_user

```python
await graphlit.client.delete_user(id: str) -> DeleteUser
```

**Response:**
```
response.delete_user
  .id: str
  .state: EntityState
```

### disable_user

```python
await graphlit.client.disable_user(id: str) -> DisableUser
```

**Response:**
```
response.disable_user
  .id: str
  .state: EntityState
```

### enable_user

```python
await graphlit.client.enable_user(id: str) -> EnableUser
```

**Response:**
```
response.enable_user
  .id: str
  .state: EntityState
```

### get_user

```python
await graphlit.client.get_user() -> GetUser
```

**Response:**
```
response.user
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .relevance: Optional[float]
  .owner: "GetUserUserOwner"
  .state: EntityState
  .type: Optional[UserTypes]
```

### get_user_by_identifier

```python
await graphlit.client.get_user_by_identifier(identifier: str) -> GetUserByIdentifier
```

**Response:**
```
response.user_by_identifier
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .relevance: Optional[float]
  .owner: "GetUserByIdentifierUserByIdentifierOwner"
  .state: EntityState
  .type: Optional[UserTypes]
```

### query_users

```python
await graphlit.client.query_users(filter: Optional[UserFilter], correlation_id: Optional[str]) -> QueryUsers
```

**Response:**
```
response.users
  .results: Optional[list["QueryUsersUsersResults"]]
```

### update_user

```python
await graphlit.client.update_user(user: UserUpdateInput) -> UpdateUser
```

**Response:**
```
response.update_user
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[UserTypes]
  .description: Optional[str]
  .identifier: str
```

### count_views

```python
await graphlit.client.count_views(filter: Optional[ViewFilter], correlation_id: Optional[str]) -> CountViews
```

**Response:**
```
response.count_views
  .count: Optional[Any]
```

### create_view

```python
await graphlit.client.create_view(view: ViewInput) -> CreateView
```

**Response:**
```
response.create_view
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ViewTypes]
  .filter: Optional["CreateViewCreateViewFilter"]
  .augmented_filter: Optional["CreateViewCreateViewAugmentedFilter"]
```

### delete_all_views

```python
await graphlit.client.delete_all_views(
    filter: Optional[ViewFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllViews
```

**Response:**
```
response.delete_all_views
  .id: str
  .state: EntityState
```

### delete_view

```python
await graphlit.client.delete_view(id: str) -> DeleteView
```

**Response:**
```
response.delete_view
  .id: str
  .state: EntityState
```

### delete_views

```python
await graphlit.client.delete_views(ids: list[str], is_synchronous: Optional[bool]) -> DeleteViews
```

**Response:**
```
response.delete_views
  .id: str
  .state: EntityState
```

### get_view

```python
await graphlit.client.get_view(id: str, correlation_id: Optional[str]) -> GetView
```

**Response:**
```
response.view
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetViewViewOwner"
  .state: EntityState
  .type: Optional[ViewTypes]
  .filter: Optional["GetViewViewFilter"]
```

### query_views

```python
await graphlit.client.query_views(filter: Optional[ViewFilter], correlation_id: Optional[str]) -> QueryViews
```

**Response:**
```
response.views
  .results: Optional[list["QueryViewsViewsResults"]]
```

### update_view

```python
await graphlit.client.update_view(view: ViewUpdateInput) -> UpdateView
```

**Response:**
```
response.update_view
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ViewTypes]
  .filter: Optional["UpdateViewUpdateViewFilter"]
  .augmented_filter: Optional["UpdateViewUpdateViewAugmentedFilter"]
```

### upsert_view

```python
await graphlit.client.upsert_view(view: ViewInput) -> UpsertView
```

**Response:**
```
response.upsert_view
  .id: str
  .name: str
  .state: EntityState
  .type: Optional[ViewTypes]
  .filter: Optional["UpsertViewUpsertViewFilter"]
  .augmented_filter: Optional["UpsertViewUpsertViewAugmentedFilter"]
```

### view_exists

```python
await graphlit.client.view_exists(filter: Optional[ViewFilter], correlation_id: Optional[str]) -> ViewExists
```

**Response:**
```
response.view_exists
  .result: Optional[bool]
```

### count_workflows

```python
await graphlit.client.count_workflows(filter: Optional[WorkflowFilter], correlation_id: Optional[str]) -> CountWorkflows
```

**Response:**
```
response.count_workflows
  .count: Optional[Any]
```

### create_workflow

```python
await graphlit.client.create_workflow(workflow: WorkflowInput) -> CreateWorkflow
```

**Response:**
```
response.create_workflow
  .id: str
  .name: str
  .state: EntityState
  .ingestion: Optional["CreateWorkflowCreateWorkflowIngestion"]
  .indexing: Optional["CreateWorkflowCreateWorkflowIndexing"]
  .preparation: Optional["CreateWorkflowCreateWorkflowPreparation"]
  .extraction: Optional["CreateWorkflowCreateWorkflowExtraction"]
  .classification: Optional["CreateWorkflowCreateWorkflowClassification"]
```

### delete_all_workflows

```python
await graphlit.client.delete_all_workflows(
    filter: Optional[WorkflowFilter],
    is_synchronous: Optional[bool],
    correlation_id: Optional[str],
) -> DeleteAllWorkflows
```

**Response:**
```
response.delete_all_workflows
  .id: str
  .state: EntityState
```

### delete_workflow

```python
await graphlit.client.delete_workflow(id: str) -> DeleteWorkflow
```

**Response:**
```
response.delete_workflow
  .id: str
  .state: EntityState
```

### delete_workflows

```python
await graphlit.client.delete_workflows(ids: list[str], is_synchronous: Optional[bool]) -> DeleteWorkflows
```

**Response:**
```
response.delete_workflows
  .id: str
  .state: EntityState
```

### get_workflow

```python
await graphlit.client.get_workflow(id: str, correlation_id: Optional[str]) -> GetWorkflow
```

**Response:**
```
response.workflow
  .id: str
  .name: str
  .creation_date: Any
  .modified_date: Optional[Any]
  .owner: "GetWorkflowWorkflowOwner"
  .state: EntityState
  .ingestion: Optional["GetWorkflowWorkflowIngestion"]
  .indexing: Optional["GetWorkflowWorkflowIndexing"]
```

### query_workflows

```python
await graphlit.client.query_workflows(filter: Optional[WorkflowFilter], correlation_id: Optional[str]) -> QueryWorkflows
```

**Response:**
```
response.workflows
  .results: Optional[list["QueryWorkflowsWorkflowsResults"]]
```

### update_workflow

```python
await graphlit.client.update_workflow(workflow: WorkflowUpdateInput) -> UpdateWorkflow
```

**Response:**
```
response.update_workflow
  .id: str
  .name: str
  .state: EntityState
  .ingestion: Optional["UpdateWorkflowUpdateWorkflowIngestion"]
  .indexing: Optional["UpdateWorkflowUpdateWorkflowIndexing"]
  .preparation: Optional["UpdateWorkflowUpdateWorkflowPreparation"]
  .extraction: Optional["UpdateWorkflowUpdateWorkflowExtraction"]
  .classification: Optional["UpdateWorkflowUpdateWorkflowClassification"]
```

### upsert_workflow

```python
await graphlit.client.upsert_workflow(workflow: WorkflowInput) -> UpsertWorkflow
```

**Response:**
```
response.upsert_workflow
  .id: str
  .name: str
  .state: EntityState
  .ingestion: Optional["UpsertWorkflowUpsertWorkflowIngestion"]
  .indexing: Optional["UpsertWorkflowUpsertWorkflowIndexing"]
  .preparation: Optional["UpsertWorkflowUpsertWorkflowPreparation"]
  .extraction: Optional["UpsertWorkflowUpsertWorkflowExtraction"]
  .classification: Optional["UpsertWorkflowUpsertWorkflowClassification"]
```

### workflow_exists

```python
await graphlit.client.workflow_exists(filter: Optional[WorkflowFilter], correlation_id: Optional[str]) -> WorkflowExists
```

**Response:**
```
response.workflow_exists
  .result: Optional[bool]
```

## Input Types

### MicrosoftContactsCRMFeedPropertiesUpdateInput
```
  authentication_type: Optional[MicrosoftContactsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  tenant_id: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### DiffbotEnrichmentPropertiesInput
```
  key: Optional[str]
```

### AnthropicModelPropertiesInput
```
  model: AnthropicModels
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  completion_token_limit: Optional[int]
  enable_thinking: Optional[bool]
  thinking_token_limit: Optional[int]
  effort: Optional[AnthropicEffortLevels]
```

### MedicalProcedureUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### MicrosoftTeamsFeedPropertiesUpdateInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[MicrosoftTeamsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  team_id: str
  channel_id: str
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### RevisionStrategyUpdateInput
```
  type: Optional[RevisionStrategyTypes]
  custom_revision: Optional[str]
  count: Optional[int]
```

### Int64RangeInput
```
  from_: Optional[Any]
  to: Optional[Any]
```

### ZendeskTicketsFeedPropertiesUpdateInput
```
  authentication_type: Optional[ZendeskIssueAuthenticationTypes]
  subdomain: Optional[str]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### AsanaFeedPropertiesUpdateInput
```
  authentication_type: Optional[AsanaAuthenticationTypes]
  personal_access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  workspace_id: Optional[str]
  project_id: Optional[str]
```

### AttioCRMFeedPropertiesUpdateInput
```
  authentication_type: Optional[AttioAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### PlaceInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  telephone: Optional[str]
  opening_hours: Optional[str]
  price_range: Optional[str]
```

### PersonaInput
```
  name: str
  role: Optional[str]
  instructions: Optional[str]
```

### CalendarAttendeeInput
```
  name: Optional[str]
  email: Optional[str]
  display_name: Optional[str]
  is_optional: Optional[bool]
  is_organizer: Optional[bool]
  is_required: Optional[bool]
  is_resource: Optional[bool]
  response_status: Optional[CalendarAttendeeResponseStatus]
```

### EntityReferenceInput
```
  id: str
```

### InvestmentFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_investments: Optional[list["EntityReferenceFilter"]]
  investments: Optional[list["EntityReferenceFilter"]]
```

### SlackChannelsInput
```
  authentication_type: Optional[SlackAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### TextContentInput
```
  name: str
  text: str
```

### GroqModelPropertiesUpdateInput
```
  model: Optional[GroqModels]
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### AlertSchedulePolicyInput
```
  recurrence_type: Optional[TimedPolicyRecurrenceTypes]
  repeat_interval: Optional[Any]
  cron: Optional[str]
  time_zone_id: Optional[str]
```

### AttioMeetingPropertiesUpdateInput
```
  authentication_type: Optional[AttioMeetingAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### SharePointDistributionPropertiesInput
```
  site_id: str
  title: Optional[str]
```

### PersonUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  given_name: Optional[str]
  family_name: Optional[str]
  phone_number: Optional[str]
  email: Optional[str]
  birth_date: Optional[Any]
  title: Optional[str]
  occupation: Optional[str]
  education: Optional[str]
```

### SpecificationInput
```
  name: str
  type: Optional[SpecificationTypes]
  service_type: ModelServiceTypes
  search_type: Optional[ConversationSearchTypes]
  number_similar: Optional[int]
  system_prompt: Optional[str]
  custom_guidance: Optional[str]
  custom_instructions: Optional[str]
  strategy: Optional["ConversationStrategyInput"]
  prompt_strategy: Optional["PromptStrategyInput"]
  retrieval_strategy: Optional["RetrievalStrategyInput"]
  reranking_strategy: Optional["RerankingStrategyInput"]
  graph_strategy: Optional["GraphStrategyInput"]
  fact_strategy: Optional["FactStrategyInput"]
  revision_strategy: Optional["RevisionStrategyInput"]
  azure_ai: Optional["AzureAIModelPropertiesInput"]
  open_ai: Optional["OpenAIModelPropertiesInput"]
  azure_open_ai: Optional["AzureOpenAIModelPropertiesInput"]
  cohere: Optional["CohereModelPropertiesInput"]
  anthropic: Optional["AnthropicModelPropertiesInput"]
  google: Optional["GoogleModelPropertiesInput"]
  replicate: Optional["ReplicateModelPropertiesInput"]
  mistral: Optional["MistralModelPropertiesInput"]
  bedrock: Optional["BedrockModelPropertiesInput"]
  xai: Optional["XAIModelPropertiesInput"]
  groq: Optional["GroqModelPropertiesInput"]
  cerebras: Optional["CerebrasModelPropertiesInput"]
  deepseek: Optional["DeepseekModelPropertiesInput"]
  jina: Optional["JinaModelPropertiesInput"]
  voyage: Optional["VoyageModelPropertiesInput"]
  twelve_labs: Optional["TwelveLabsModelPropertiesInput"]
```

### CerebrasModelPropertiesInput
```
  model: CerebrasModels
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### IntegrationConnectorInput
```
  type: IntegrationServiceTypes
  uri: Optional[str]
  slack: Optional["SlackIntegrationPropertiesInput"]
  email: Optional["EmailIntegrationPropertiesInput"]
  twitter: Optional["TwitterIntegrationPropertiesInput"]
  mcp: Optional["MCPIntegrationPropertiesInput"]
```

### SalesforceFeedPropertiesInput
```
  authentication_type: Optional[SalesforceFeedAuthenticationTypes]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### ModelImageExtractionPropertiesInput
```
  specification: Optional["EntityReferenceInput"]
```

### StoragePolicyInput
```
  type: Optional[StoragePolicyTypes]
  allow_duplicates: Optional[bool]
  embedding_types: Optional[list[EmbeddingTypes]]
  enable_snapshots: Optional[bool]
  snapshot_count: Optional[int]
```

### MicrosoftEmailFeedPropertiesUpdateInput
```
  type: Optional[EmailListingTypes]
  filter: Optional[str]
  inbox_only: Optional[bool]
  include_deleted_items: Optional[bool]
  exclude_sent_items: Optional[bool]
  include_spam: Optional[bool]
  authentication_type: Optional[MicrosoftEmailAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### AzureFileFeedPropertiesInput
```
  storage_access_key: str
  account_name: str
  share_name: str
  prefix: Optional[str]
```

### SalesforceCRMFeedPropertiesInput
```
  authentication_type: Optional[SalesforceAuthenticationTypes]
  instance_url: Optional[str]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### ElevenLabsScribeAudioPreparationPropertiesInput
```
  model: Optional[ElevenLabsScribeModels]
  key: Optional[str]
  enable_speaker_diarization: Optional[bool]
  detect_language: Optional[bool]
  language: Optional[str]
  tag_audio_events: Optional[bool]
```

### DiscordDistributionPropertiesInput
```
  channel_id: str
  thread_id: Optional[str]
```

### SearchFeedPropertiesUpdateInput
```
  type: Optional[SearchServiceTypes]
  text: Optional[str]
  exa: Optional["ExaSearchPropertiesInput"]
  read_limit: Optional[int]
```

### TwitterFeedPropertiesUpdateInput
```
  authentication_type: Optional[TwitterAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[TwitterListingTypes]
  user_name: Optional[str]
  query: Optional[str]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### MedicalIndicationFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_indications: Optional[list["EntityReferenceFilter"]]
  medical_indications: Optional[list["EntityReferenceFilter"]]
```

### GoogleModelPropertiesInput
```
  model: GoogleModels
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  enable_thinking: Optional[bool]
  thinking_token_limit: Optional[int]
  thinking_level: Optional[GoogleThinkingLevels]
```

### EventInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  start_date: Optional[Any]
  end_date: Optional[Any]
  availability_start_date: Optional[Any]
  availability_end_date: Optional[Any]
  price: Optional[Any]
  min_price: Optional[Any]
  max_price: Optional[Any]
  price_currency: Optional[str]
  is_accessible_for_free: Optional[bool]
  typical_age_range: Optional[str]
  organizer: Optional[str]
  performer: Optional[str]
  sponsor: Optional[str]
  event_status: Optional[str]
```

### XAIModelPropertiesInput
```
  model: XAIModels
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### EmailFeedPropertiesInput
```
  type: FeedServiceTypes
  include_attachments: Optional[bool]
  google: Optional["GoogleEmailFeedPropertiesInput"]
  microsoft: Optional["MicrosoftEmailFeedPropertiesInput"]
  read_limit: Optional[int]
```

### LanguageMetadataInput
```
  languages: Optional[list[Optional[str]]]
```

### OpenAIModelPropertiesUpdateInput
```
  model: Optional[OpenAIModels]
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  detail_level: Optional[OpenAIVisionDetailLevels]
  reasoning_effort: Optional[OpenAIReasoningEffortLevels]
```

### FactAssertionInput
```
  text: str
  mentions: Optional[list[Optional["MentionReferenceInput"]]]
```

### GustoOptionsInput
```
  client_id: str
  client_secret: str
  refresh_token: str
  company_id: str
```

### LabelFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
```

### IntercomConversationsFeedPropertiesUpdateInput
```
  authentication_type: Optional[IntercomConversationsAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  state: Optional[str]
  include_notes: Optional[bool]
  include_attachments: Optional[bool]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### MedicalTherapyInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ExaSearchPropertiesInput
```
  search_type: Optional[ExaSearchTypes]
```

### LinearFeedPropertiesInput
```
  authentication_type: Optional[LinearIssueAuthenticationTypes]
  key: Optional[str]
  project: str
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### ProductFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[ProductFacetTypes]
```

### CollectionInput
```
  name: str
  type: Optional[CollectionTypes]
  contents: Optional[list["EntityReferenceInput"]]
  conversations: Optional[list["EntityReferenceInput"]]
  expected_count: Optional[int]
```

### EmbeddingsStrategyInput
```
  text_specification: Optional["EntityReferenceInput"]
  image_specification: Optional["EntityReferenceInput"]
  multimodal_specification: Optional["EntityReferenceInput"]
```

### InvestmentFundInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  amount_currency: Optional[str]
  amount: Optional[Any]
  fund_type: Optional[str]
  vintage: Optional[int]
  target_size: Optional[Any]
  target_size_currency: Optional[str]
```

### PreparationWorkflowJobInput
```
  connector: Optional["FilePreparationConnectorInput"]
```

### ObservationUpdateInput
```
  id: str
  type: Optional[ObservableTypes]
  observable: Optional["NamedEntityReferenceInput"]
  related: Optional["NamedEntityReferenceInput"]
  related_type: Optional[ObservableTypes]
  relation: Optional[str]
  occurrences: Optional[list["ObservationOccurrenceInput"]]
```

### MedicalIndicationInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### JiraDistributionPropertiesInput
```
  project_key: str
  issue_type: str
  summary: Optional[str]
  priority: Optional[str]
  assignee_id: Optional[str]
  labels: Optional[list[str]]
```

### FactFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  content: Optional["EntityReferenceFilter"]
  valid_at: Optional[Any]
  mentions: Optional[list[Optional["MentionReferenceFilter"]]]
  feeds: Optional[list[Optional["EntityReferenceFilter"]]]
  categories: Optional[list[Optional[FactCategory]]]
  min_confidence: Optional[float]
  similar_facts: Optional[list[Optional["EntityReferenceFilter"]]]
  facts: Optional[list[Optional["EntityReferenceFilter"]]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  disable_inheritance: Optional[bool]
```

### LinkReferenceInput
```
  uri: Optional[Any]
  link_type: Optional[LinkTypes]
  excerpts: Optional[str]
```

### PromptStrategyUpdateInput
```
  type: Optional[PromptStrategyTypes]
```

### GoogleEmailFeedPropertiesUpdateInput
```
  type: Optional[EmailListingTypes]
  filter: Optional[str]
  inbox_only: Optional[bool]
  include_deleted_items: Optional[bool]
  exclude_sent_items: Optional[bool]
  include_spam: Optional[bool]
  authentication_type: Optional[GoogleEmailAuthenticationTypes]
  refresh_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### PersonInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  given_name: Optional[str]
  family_name: Optional[str]
  phone_number: Optional[str]
  email: Optional[str]
  birth_date: Optional[Any]
  title: Optional[str]
  occupation: Optional[str]
  education: Optional[str]
```

### ConversationStrategyUpdateInput
```
  type: Optional[ConversationStrategyTypes]
  message_limit: Optional[int]
  embed_citations: Optional[bool]
  flatten_citations: Optional[bool]
  enable_facets: Optional[bool]
  enable_summarization: Optional[bool]
  enable_entity_extraction: Optional[bool]
  enable_fact_extraction: Optional[bool]
  entity_extraction_limit: Optional[int]
  fact_extraction_limit: Optional[int]
  messages_weight: Optional[float]
  contents_weight: Optional[float]
  tool_result_token_limit: Optional[int]
  tool_round_limit: Optional[int]
  tool_budget_threshold: Optional[float]
```

### ExtractionWorkflowStageInput
```
  jobs: Optional[list[Optional["ExtractionWorkflowJobInput"]]]
```

### MedicalTestInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ReductoDocumentPreparationPropertiesInput
```
  ocr_mode: Optional[ReductoOcrModes]
  ocr_system: Optional[ReductoOcrSystems]
  extraction_mode: Optional[ReductoExtractionModes]
  enable_enrichment: Optional[bool]
  enrichment_mode: Optional[ReductoEnrichmentModes]
  key: Optional[str]
```

### MedicalTherapyUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### SlackFeedPropertiesUpdateInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[SlackAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  channel: Optional[str]
  include_attachments: Optional[bool]
  signing_secret: Optional[str]
  read_limit: Optional[int]
```

### ModelContentClassificationPropertiesInput
```
  specification: Optional["EntityReferenceInput"]
  rules: Optional[list[Optional["PromptClassificationRuleInput"]]]
```

### MCPIntegrationPropertiesInput
```
  type: MCPServerTypes
  token: Optional[str]
```

### OrganizationFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[OrganizationFacetTypes]
```

### OrganizationFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  uri: Optional[Any]
  similar_organizations: Optional[list["EntityReferenceFilter"]]
  organizations: Optional[list["EntityReferenceFilter"]]
```

### GoogleDocsDistributionPropertiesInput
```
  folder_id: Optional[str]
  title: Optional[str]
```

### GoogleContactsCRMFeedPropertiesInput
```
  authentication_type: Optional[GoogleContactsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### PullRequestFeedPropertiesUpdateInput
```
  github: Optional["GitHubPullRequestsFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### MedicalIndicationFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalIndicationFacetTypes]
```

### CategoryFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[CategoryFacetTypes]
```

### ZendeskTicketsFeedPropertiesInput
```
  authentication_type: Optional[ZendeskIssueAuthenticationTypes]
  subdomain: str
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalTestFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_tests: Optional[list["EntityReferenceFilter"]]
  medical_tests: Optional[list["EntityReferenceFilter"]]
```

### ParallelFeedPropertiesUpdateInput
```
  processor: Optional[ParallelProcessors]
```

### AzureAIModelPropertiesInput
```
  key: str
  endpoint: Any
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: int
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### GmailDistributionPropertiesInput
```
  to: list[str]
  subject: str
  cc: Optional[list[str]]
  bcc: Optional[list[str]]
```

### MicrosoftTeamsDistributionPropertiesInput
```
  team_id: str
  channel_id: str
  thread_id: Optional[str]
```

### OneDriveFeedPropertiesUpdateInput
```
  authentication_type: Optional[OneDriveAuthenticationTypes]
  files: Optional[list[Optional[str]]]
  folder_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### EmotionFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[EmotionFacetTypes]
```

### EventUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  start_date: Optional[Any]
  end_date: Optional[Any]
  availability_start_date: Optional[Any]
  availability_end_date: Optional[Any]
  price: Optional[Any]
  min_price: Optional[Any]
  max_price: Optional[Any]
  price_currency: Optional[str]
  is_accessible_for_free: Optional[bool]
  typical_age_range: Optional[str]
  organizer: Optional[str]
  performer: Optional[str]
  sponsor: Optional[str]
  event_status: Optional[str]
```

### BedrockModelPropertiesUpdateInput
```
  model: Optional[BedrockModels]
  model_name: Optional[str]
  access_key: Optional[str]
  secret_access_key: Optional[str]
  endpoint: Optional[Any]
  region: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### BedrockModelPropertiesInput
```
  model: BedrockModels
  model_name: Optional[str]
  access_key: Optional[str]
  secret_access_key: Optional[str]
  endpoint: Optional[Any]
  region: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### DateRangeInput
```
  from_: Optional[Any]
  to: Optional[Any]
```

### UserFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  identifier: Optional[str]
```

### FactStrategyInput
```
  fact_limit: Optional[int]
```

### MicrosoftTeamsFeedPropertiesInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[MicrosoftTeamsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  team_id: str
  channel_id: str
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### AzureTextExtractionPropertiesInput
```
  enable_pii: Optional[bool]
  confidence_threshold: Optional[float]
```

### AzureImageExtractionPropertiesInput
```
  confidence_threshold: Optional[float]
```

### MetadataFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  metadata_types: Optional[list[MetadataTypes]]
  content: Optional["EntityReferenceFilter"]
```

### ZendeskFeedPropertiesUpdateInput
```
  authentication_type: Optional[ZendeskAuthenticationTypes]
  subdomain: Optional[str]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  read_limit: Optional[int]
```

### MedicalStudyFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_studies: Optional[list["EntityReferenceFilter"]]
  medical_studies: Optional[list["EntityReferenceFilter"]]
```

### MicrosoftCalendarFeedPropertiesInput
```
  type: Optional[CalendarListingTypes]
  calendar_id: Optional[str]
  before_date: Optional[Any]
  after_date: Optional[Any]
  authentication_type: Optional[MicrosoftCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MistralModelPropertiesInput
```
  model: MistralModels
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### VoyageModelPropertiesUpdateInput
```
  model: Optional[VoyageModels]
  model_name: Optional[str]
  key: Optional[str]
  chunk_token_limit: Optional[int]
```

### MedicalDrugClassUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### EntityClustersInput
```
  threshold: Optional[float]
```

### GustoHRISFeedPropertiesInput
```
  authentication_type: Optional[GustoAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  company_id: Optional[str]
```

### IntercomFeedPropertiesUpdateInput
```
  authentication_type: Optional[IntercomAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  read_limit: Optional[int]
```

### ConfluenceFeedPropertiesInput
```
  is_recursive: Optional[bool]
  authentication_type: Optional[ConfluenceAuthenticationTypes]
  uri: Optional[str]
  email: Optional[str]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
  type: ConfluenceTypes
  space_keys: Optional[list[str]]
  identifiers: Optional[list[str]]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### MicrosoftTeamsTeamsInput
```
  authentication_type: Optional[MicrosoftTeamsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### IntercomTicketsFeedPropertiesUpdateInput
```
  authentication_type: Optional[IntercomIssueAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### GoogleCalendarDistributionPropertiesInput
```
  calendar_id: Optional[str]
  summary: Optional[str]
  start_date_time: Any
  end_date_time: Any
  time_zone: Optional[str]
  location: Optional[str]
  attendees: Optional[list[str]]
```

### GraphStrategyUpdateInput
```
  type: Optional[GraphStrategyTypes]
  generate_graph: Optional[bool]
  observable_limit: Optional[int]
```

### AddressInput
```
  street_address: Optional[str]
  city: Optional[str]
  region: Optional[str]
  country: Optional[str]
  postal_code: Optional[str]
```

### SlackIntegrationPropertiesInput
```
  channel: str
  token: str
```

### ViewInput
```
  name: str
  type: Optional[ViewTypes]
  filter: Optional["ContentCriteriaInput"]
  augmented_filter: Optional["ContentCriteriaInput"]
```

### GoogleCalendarsInput
```
  authentication_type: Optional[GoogleCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### TrelloFeedPropertiesUpdateInput
```
  key: Optional[str]
  token: Optional[str]
  type: Optional[TrelloTypes]
  identifiers: Optional[list[str]]
```

### UserInput
```
  name: str
  type: Optional[UserTypes]
  identifier: str
  description: Optional[str]
```

### AttioCRMFeedPropertiesInput
```
  authentication_type: Optional[AttioAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### OneDriveFeedPropertiesInput
```
  authentication_type: Optional[OneDriveAuthenticationTypes]
  files: Optional[list[Optional[str]]]
  folder_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### GitHubIssuesFeedPropertiesInput
```
  authentication_type: Optional[GitHubIssueAuthenticationTypes]
  repository_owner: str
  repository_name: str
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### FeedUpdateInput
```
  id: str
  name: Optional[str]
  identifier: Optional[str]
  description: Optional[str]
  type: Optional[FeedTypes]
  sync_mode: Optional[FeedSyncMode]
  site: Optional["SiteFeedPropertiesUpdateInput"]
  calendar: Optional["CalendarFeedPropertiesUpdateInput"]
  email: Optional["EmailFeedPropertiesUpdateInput"]
  crm: Optional["CRMFeedPropertiesUpdateInput"]
  hris: Optional["HRISFeedPropertiesUpdateInput"]
  issue: Optional["IssueFeedPropertiesUpdateInput"]
  pull_request: Optional["PullRequestFeedPropertiesUpdateInput"]
  commit: Optional["CommitFeedPropertiesUpdateInput"]
  rss: Optional["RSSFeedPropertiesUpdateInput"]
  web: Optional["WebFeedPropertiesUpdateInput"]
  search: Optional["SearchFeedPropertiesUpdateInput"]
  reddit: Optional["RedditFeedPropertiesUpdateInput"]
  youtube: Optional["YouTubeFeedPropertiesUpdateInput"]
  notion: Optional["NotionFeedPropertiesUpdateInput"]
  confluence: Optional["ConfluenceFeedPropertiesUpdateInput"]
  twitter: Optional["TwitterFeedPropertiesUpdateInput"]
  slack: Optional["SlackFeedPropertiesUpdateInput"]
  microsoft_teams: Optional["MicrosoftTeamsFeedPropertiesUpdateInput"]
  discord: Optional["DiscordFeedPropertiesUpdateInput"]
  attio: Optional["AttioFeedPropertiesUpdateInput"]
  salesforce: Optional["SalesforceFeedPropertiesUpdateInput"]
  hub_spot_conversations: Optional[
  intercom: Optional["IntercomFeedPropertiesUpdateInput"]
  zendesk: Optional["ZendeskFeedPropertiesUpdateInput"]
  intercom_conversations: Optional[
  research: Optional["ResearchFeedPropertiesUpdateInput"]
  entity: Optional["EntityFeedPropertiesUpdateInput"]
  meeting: Optional["MeetingFeedPropertiesUpdateInput"]
  schedule_policy: Optional["FeedSchedulePolicyInput"]
  workflow: Optional["EntityReferenceInput"]
```

### IssueMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  title: Optional[str]
  project: Optional[str]
  team: Optional[str]
  status: Optional[str]
  priority: Optional[str]
  type: Optional[str]
  identifier: Optional[str]
  labels: Optional[list[Optional[str]]]
  links: Optional[list[Optional[Any]]]
```

### GoogleFeedPropertiesInput
```
  credentials: str
  container_name: str
  prefix: Optional[str]
```

### IntegrationConnectorUpdateInput
```
  service_type: IntegrationServiceTypes
  uri: Optional[str]
  slack: Optional["SlackIntegrationPropertiesInput"]
  email: Optional["EmailIntegrationPropertiesInput"]
  twitter: Optional["TwitterIntegrationPropertiesInput"]
  mcp: Optional["MCPIntegrationPropertiesInput"]
```

### MedicalDrugUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### SlackDistributionPropertiesInput
```
  channel_id: str
  thread_ts: Optional[str]
```

### SalesforceDistributionPropertiesInput
```
  object_type: str
  object_id: str
  title: Optional[str]
```

### DistributionConnectorInput
```
  type: DistributionServiceTypes
  notion: Optional["NotionDistributionPropertiesInput"]
  google_drive: Optional["GoogleDriveDistributionPropertiesInput"]
  one_drive: Optional["OneDriveDistributionPropertiesInput"]
  confluence: Optional["ConfluenceDistributionPropertiesInput"]
  slack: Optional["SlackDistributionPropertiesInput"]
  gmail: Optional["GmailDistributionPropertiesInput"]
  microsoft_outlook: Optional["MicrosoftOutlookDistributionPropertiesInput"]
  hub_spot: Optional["HubSpotDistributionPropertiesInput"]
  salesforce: Optional["SalesforceDistributionPropertiesInput"]
  attio: Optional["AttioDistributionPropertiesInput"]
  google_calendar: Optional["GoogleCalendarDistributionPropertiesInput"]
  microsoft_calendar: Optional["MicrosoftCalendarDistributionPropertiesInput"]
  linear: Optional["LinearDistributionPropertiesInput"]
  jira: Optional["JiraDistributionPropertiesInput"]
  google_docs: Optional["GoogleDocsDistributionPropertiesInput"]
  microsoft_word: Optional["MicrosoftWordDistributionPropertiesInput"]
  share_point: Optional["SharePointDistributionPropertiesInput"]
  discord: Optional["DiscordDistributionPropertiesInput"]
  microsoft_teams: Optional["MicrosoftTeamsDistributionPropertiesInput"]
  twitter: Optional["TwitterDistributionPropertiesInput"]
  github: Optional["GitHubDistributionPropertiesInput"]
  attio_tasks: Optional["AttioTasksDistributionPropertiesInput"]
```

### MicrosoftCalendarFeedPropertiesUpdateInput
```
  type: Optional[CalendarListingTypes]
  calendar_id: Optional[str]
  before_date: Optional[Any]
  after_date: Optional[Any]
  authentication_type: Optional[MicrosoftCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### ClassificationWorkflowStageInput
```
  jobs: Optional[list[Optional["ClassificationWorkflowJobInput"]]]
```

### VideoMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  width: Optional[int]
  height: Optional[int]
  duration: Optional[str]
  software: Optional[str]
  make: Optional[str]
  model: Optional[str]
```

### RerankingStrategyInput
```
  service_type: RerankingModelServiceTypes
  threshold: Optional[float]
```

### OneDriveFoldersInput
```
  authentication_type: Optional[OneDriveAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### GitHubFeedPropertiesInput
```
  authentication_type: Optional[GitHubAuthenticationTypes]
  repository_owner: str
  repository_name: str
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### HumeExtractionPropertiesInput
```
  confidence_threshold: Optional[float]
```

### InvestmentFundUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  amount_currency: Optional[str]
  amount: Optional[Any]
  fund_type: Optional[str]
  vintage: Optional[int]
  target_size: Optional[Any]
  target_size_currency: Optional[str]
```

### AzureFileFeedPropertiesUpdateInput
```
  storage_access_key: Optional[str]
  account_name: Optional[str]
  share_name: Optional[str]
  prefix: Optional[str]
```

### RedditFeedPropertiesUpdateInput
```
  read_limit: Optional[int]
```

### GoogleEmailFeedPropertiesInput
```
  type: Optional[EmailListingTypes]
  filter: Optional[str]
  inbox_only: Optional[bool]
  include_deleted_items: Optional[bool]
  exclude_sent_items: Optional[bool]
  include_spam: Optional[bool]
  authentication_type: Optional[GoogleEmailAuthenticationTypes]
  refresh_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### DocumentMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  title: Optional[str]
  subject: Optional[str]
  author: Optional[str]
  software: Optional[str]
  publisher: Optional[str]
  description: Optional[str]
  summary: Optional[str]
  comments: Optional[str]
  identifier: Optional[str]
  keywords: Optional[list[Optional[str]]]
  links: Optional[list[Optional[Any]]]
  page_count: Optional[int]
  worksheet_count: Optional[int]
  slide_count: Optional[int]
  word_count: Optional[int]
  line_count: Optional[int]
  paragraph_count: Optional[int]
  character_count: Optional[int]
  total_editing_time: Optional[str]
  is_encrypted: Optional[bool]
  has_digital_signature: Optional[bool]
```

### HubSpotMeetingPropertiesInput
```
  authentication_type: Optional[HubSpotFeedAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  include_transcripts: Optional[bool]
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### CalendarReminderInput
```
  minutes_before: Optional[int]
  method: Optional[CalendarReminderMethod]
```

### IngestionContentFilterInput
```
  types: Optional[list[ContentTypes]]
  file_types: Optional[list[FileTypes]]
  formats: Optional[list[Optional[str]]]
  file_extensions: Optional[list[str]]
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
```

### BoxFeedPropertiesUpdateInput
```
  authentication_type: Optional[BoxAuthenticationTypes]
  folder_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  redirect_uri: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### WorkflowFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
```

### AmazonFeedPropertiesUpdateInput
```
  access_key: Optional[str]
  secret_access_key: Optional[str]
  bucket_name: Optional[str]
  prefix: Optional[str]
  region: Optional[str]
  custom_endpoint: Optional[str]
```

### ModelFilter
```
  types: Optional[list[ModelTypes]]
  service_types: Optional[list[ModelServiceTypes]]
```

### IssueFeedPropertiesUpdateInput
```
  include_attachments: Optional[bool]
  jira: Optional["AtlassianJiraFeedPropertiesUpdateInput"]
  linear: Optional["LinearFeedPropertiesUpdateInput"]
  github: Optional["GitHubIssuesFeedPropertiesUpdateInput"]
  intercom: Optional["IntercomTicketsFeedPropertiesUpdateInput"]
  zendesk: Optional["ZendeskTicketsFeedPropertiesUpdateInput"]
  trello: Optional["TrelloFeedPropertiesUpdateInput"]
  attio: Optional["AttioTasksFeedPropertiesUpdateInput"]
  salesforce: Optional["SalesforceTasksFeedPropertiesUpdateInput"]
  hub_spot: Optional["HubSpotTasksFeedPropertiesUpdateInput"]
  asana: Optional["AsanaFeedPropertiesUpdateInput"]
  monday: Optional["MondayFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### ContentIndexingConnectorInput
```
  type: Optional[ContentIndexingServiceTypes]
  content_type: Optional[ContentTypes]
  file_type: Optional[FileTypes]
```

### Int64RangeFilter
```
  from_: Optional[Any]
  to: Optional[Any]
```

### ContentPublishingConnectorInput
```
  type: ContentPublishingServiceTypes
  format: ContentPublishingFormats
  eleven_labs: Optional["ElevenLabsPublishingPropertiesInput"]
  open_ai_image: Optional["OpenAIImagePublishingPropertiesInput"]
  google_image: Optional["GoogleImagePublishingPropertiesInput"]
  open_ai_video: Optional["OpenAIVideoPublishingPropertiesInput"]
  google_video: Optional["GoogleVideoPublishingPropertiesInput"]
  parallel: Optional["ParallelPublishingPropertiesInput"]
```

### AttioMeetingPropertiesInput
```
  authentication_type: Optional[AttioMeetingAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### FactStrategyUpdateInput
```
  fact_limit: Optional[int]
```

### SharePointFoldersInput
```
  authentication_type: SharePointAuthenticationTypes
  tenant_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### LabelUpdateInput
```
  id: str
  name: Optional[str]
  description: Optional[str]
```

### FirefliesFeedPropertiesInput
```
  api_key: str
  before_date: Optional[Any]
  after_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### GraphInput
```
  types: Optional[list[ObservableTypes]]
```

### RSSFeedPropertiesUpdateInput
```
  read_limit: Optional[int]
```

### ModelTextExtractionPropertiesInput
```
  specification: Optional["EntityReferenceInput"]
  token_threshold: Optional[int]
  time_budget: Optional[Any]
  entity_budget: Optional[int]
  page_budget: Optional[int]
  token_budget: Optional[int]
  extraction_type: Optional[ExtractionTypes]
```

### EmotionUpdateInput
```
  id: str
  name: Optional[str]
  description: Optional[str]
```

### MedicalConditionFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalConditionFacetTypes]
```

### YouTubeFeedPropertiesInput
```
  type: YouTubeTypes
  video_name: Optional[str]
  video_identifiers: Optional[list[str]]
  channel_identifier: Optional[str]
  playlist_identifier: Optional[str]
  read_limit: Optional[int]
```

### ClassificationWorkflowJobInput
```
  connector: Optional["ContentClassificationConnectorInput"]
```

### DiscordGuildsInput
```
  token: str
```

### RetrievalStrategyInput
```
  type: RetrievalStrategyTypes
  content_limit: Optional[int]
  disable_fallback: Optional[bool]
```

### RepoFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_repos: Optional[list["EntityReferenceFilter"]]
  repos: Optional[list["EntityReferenceFilter"]]
```

### MistralModelPropertiesUpdateInput
```
  model: Optional[MistralModels]
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### AsanaProjectsInput
```
  personal_access_token: str
  workspace_id: str
```

### RepoInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ConversationGraphInput
```
  types: Optional[list[ObservableTypes]]
```

### GustoCompaniesInput
```
  client_id: str
  client_secret: str
  refresh_token: str
```

### IntercomFeedPropertiesInput
```
  authentication_type: Optional[IntercomAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  read_limit: Optional[int]
```

### ConnectorUpdateInput
```
  id: str
  name: Optional[str]
  authentication: Optional["AuthenticationConnectorInput"]
  integration: Optional["IntegrationConnectorInput"]
```

### MedicalConditionFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_conditions: Optional[list["EntityReferenceFilter"]]
  medical_conditions: Optional[list["EntityReferenceFilter"]]
```

### MetadataUpdateInput
```
  id: str
  name: Optional[str]
  mime_type: Optional[str]
  value: Optional[str]
  content: Optional["EntityReferenceInput"]
```

### AttioFeedPropertiesInput
```
  authentication_type: Optional[AttioFeedAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### MondayFeedPropertiesInput
```
  api_token: str
  board_id: str
```

### PostMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  identifier: Optional[str]
  title: Optional[str]
  author: Optional["PersonReferenceInput"]
  upvotes: Optional[int]
  downvotes: Optional[int]
  comment_count: Optional[int]
  links: Optional[list[Optional["LinkReferenceInput"]]]
```

### ParallelEnrichmentPropertiesInput
```
  processor: Optional[ParallelProcessors]
  is_synchronous: Optional[bool]
```

### LinearFeedPropertiesUpdateInput
```
  authentication_type: Optional[LinearIssueAuthenticationTypes]
  key: Optional[str]
  project: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalContraindicationInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### SpecificationFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[SpecificationTypes]]
  service_types: Optional[list[ModelServiceTypes]]
```

### ToolDefinitionInput
```
  name: str
  description: Optional[str]
  schema_: str
```

### AlertUpdateInput
```
  id: str
  name: Optional[str]
  summary_prompt: Optional[str]
  publish_prompt: Optional[str]
  view: Optional["EntityReferenceInput"]
  filter: Optional["ContentCriteriaInput"]
  publishing: Optional["ContentPublishingConnectorUpdateInput"]
  integration: Optional["IntegrationConnectorUpdateInput"]
  summary_specification: Optional["EntityReferenceInput"]
  publish_specification: Optional["EntityReferenceInput"]
  schedule_policy: Optional["AlertSchedulePolicyInput"]
```

### AsanaFeedPropertiesInput
```
  authentication_type: Optional[AsanaAuthenticationTypes]
  personal_access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  workspace_id: Optional[str]
  project_id: Optional[str]
```

### ConfluenceFeedPropertiesUpdateInput
```
  is_recursive: Optional[bool]
  authentication_type: Optional[ConfluenceAuthenticationTypes]
  uri: Optional[str]
  email: Optional[str]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
  type: Optional[ConfluenceTypes]
  space_keys: Optional[list[str]]
  identifiers: Optional[list[str]]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### NotionPagesInput
```
  authentication_type: Optional[NotionAuthenticationTypes]
  token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### EntityExtractionConnectorInput
```
  type: EntityExtractionServiceTypes
  content_types: Optional[list[ContentTypes]]
  file_types: Optional[list[FileTypes]]
  extracted_types: Optional[list[ObservableTypes]]
  extracted_count: Optional[int]
  azure_text: Optional["AzureTextExtractionPropertiesInput"]
  azure_image: Optional["AzureImageExtractionPropertiesInput"]
  model_text: Optional["ModelTextExtractionPropertiesInput"]
  model_image: Optional["ModelImageExtractionPropertiesInput"]
  hume: Optional["HumeExtractionPropertiesInput"]
```

### PullRequestFeedPropertiesInput
```
  type: FeedServiceTypes
  github: Optional["GitHubPullRequestsFeedPropertiesInput"]
  read_limit: Optional[int]
```

### RetrievalStrategyUpdateInput
```
  type: Optional[RetrievalStrategyTypes]
  content_limit: Optional[int]
```

### CalendarFeedPropertiesUpdateInput
```
  include_attachments: Optional[bool]
  enable_meeting_recording: Optional[bool]
  meeting_bot_name: Optional[str]
  google: Optional["GoogleCalendarFeedPropertiesUpdateInput"]
  microsoft: Optional["MicrosoftCalendarFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### WorkflowActionInput
```
  connector: Optional["IntegrationConnectorInput"]
```

### MedicalConditionUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### PackageMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  file_count: Optional[int]
  folder_count: Optional[int]
```

### MedicalProcedureFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_procedures: Optional[list["EntityReferenceFilter"]]
  medical_procedures: Optional[list["EntityReferenceFilter"]]
```

### SalesforceTasksFeedPropertiesInput
```
  authentication_type: Optional[SalesforceIssueAuthenticationTypes]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### HubSpotConversationsFeedPropertiesInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[HubSpotFeedAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  inbox_id: Optional[str]
  include_closed_threads: Optional[bool]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### FathomPropertiesInput
```
  api_key: str
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### MedicalGuidelineFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalGuidelineFacetTypes]
```

### EventFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[EventFacetTypes]
```

### AtlassianJiraFeedPropertiesUpdateInput
```
  authentication_type: Optional[JiraAuthenticationTypes]
  uri: Optional[Any]
  project: Optional[str]
  email: Optional[str]
  token: Optional[str]
  offset: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
```

### MedicalProcedureFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalProcedureFacetTypes]
```

### ObservationCriteriaInput
```
  type: Optional[ObservableTypes]
  observable: Optional["EntityReferenceInput"]
  states: Optional[list[EntityState]]
```

### InvestmentUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  amount_currency: Optional[str]
  amount: Optional[Any]
  status: Optional[str]
  stage: Optional[str]
  investment_date: Optional[Any]
  round_size: Optional[Any]
  round_size_currency: Optional[str]
  post_valuation: Optional[Any]
  post_valuation_currency: Optional[str]
  shares_owned: Optional[Any]
  vehicle: Optional[str]
  entry_price_per_share: Optional[Any]
  current_price_per_share: Optional[Any]
  discount_percent: Optional[Any]
  pro_rata_rights: Optional[bool]
  investor: Optional["EntityReferenceInput"]
  organization: Optional["EntityReferenceInput"]
```

### MedicalIndicationUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ObservationOccurrenceInput
```
  type: OccurrenceTypes
  confidence: Optional[float]
  bounding_box: Optional["BoundingBoxInput"]
  page_index: Optional[int]
  start_time: Optional[Any]
  end_time: Optional[Any]
```

### JinaModelPropertiesInput
```
  model: JinaModels
  model_name: Optional[str]
  key: Optional[str]
  chunk_token_limit: Optional[int]
```

### ContentFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  embedding_types: Optional[list[EmbeddingTypes]]
  number_similar: Optional[int]
  image_data: Optional[str]
  image_mime_type: Optional[str]
  disable_inheritance: Optional[bool]
  types: Optional[list[ContentTypes]]
  file_types: Optional[list[FileTypes]]
  uri: Optional[Any]
  identifier: Optional[str]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[Optional[str]]]
  in_last: Optional[Any]
  original_date_range: Optional["DateRangeFilter"]
  c_4_id: Optional[str]
  formats: Optional[list[Optional[str]]]
  file_extensions: Optional[list[str]]
  file_size_range: Optional["Int64RangeFilter"]
  similar_contents: Optional[list["EntityReferenceFilter"]]
  contents: Optional[list["EntityReferenceFilter"]]
  feeds: Optional[list["EntityReferenceFilter"]]
  workflows: Optional[list["EntityReferenceFilter"]]
  collections: Optional[list["EntityReferenceFilter"]]
  users: Optional[list["EntityReferenceFilter"]]
  observations: Optional[list["ObservationReferenceFilter"]]
  has_feeds: Optional[bool]
  has_workflows: Optional[bool]
  has_collections: Optional[bool]
  has_observations: Optional[bool]
  collection_mode: Optional[FilterMode]
  observation_mode: Optional[FilterMode]
  or_: Optional[list[Optional["ContentFilterLevel"]]]
  and_: Optional[list[Optional["ContentFilterLevel"]]]
```

### LabelFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[LabelFacetTypes]
```

### MedicalConditionInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ProjectQuotaInput
```
  storage: Optional[Any]
  contents: Optional[int]
  feeds: Optional[int]
  posts: Optional[int]
  conversations: Optional[int]
```

### NotionDatabasesInput
```
  authentication_type: Optional[NotionAuthenticationTypes]
  token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### EmailFeedPropertiesUpdateInput
```
  include_attachments: Optional[bool]
  google: Optional["GoogleEmailFeedPropertiesUpdateInput"]
  microsoft: Optional["MicrosoftEmailFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### GoogleFeedPropertiesUpdateInput
```
  credentials: Optional[str]
  container_name: Optional[str]
  prefix: Optional[str]
```

### ObservableInput
```
  name: str
  type: ObservableTypes
  metadata: Optional[str]
```

### AddressFilter
```
  street_address: Optional[str]
  city: Optional[str]
  region: Optional[str]
  country: Optional[str]
  postal_code: Optional[str]
```

### InvestmentFundFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[InvestmentFundFacetTypes]
```

### DropboxFoldersInput
```
  authentication_type: Optional[DropboxAuthenticationTypes]
  app_key: Optional[str]
  app_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### AzureOpenAIModelPropertiesUpdateInput
```
  model: Optional[AzureOpenAIModels]
  deployment_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### AlertInput
```
  name: str
  type: AlertTypes
  summary_prompt: Optional[str]
  publish_prompt: str
  view: Optional["EntityReferenceInput"]
  filter: Optional["ContentCriteriaInput"]
  publishing: "ContentPublishingConnectorInput"
  integration: "IntegrationConnectorInput"
  summary_specification: Optional["EntityReferenceInput"]
  publish_specification: Optional["EntityReferenceInput"]
  schedule_policy: Optional["AlertSchedulePolicyInput"]
```

### GoogleDriveFoldersInput
```
  authentication_type: Optional[GoogleDriveAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalContraindicationFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_contraindications: Optional[list["EntityReferenceFilter"]]
  medical_contraindications: Optional[list["EntityReferenceFilter"]]
```

### ShapeMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  feature_count: Optional[int]
  attribute_count: Optional[int]
```

### UserUpdateInput
```
  id: str
  name: Optional[str]
  type: Optional[UserTypes]
  identifier: Optional[str]
  description: Optional[str]
```

### ViewUpdateInput
```
  id: str
  name: Optional[str]
  type: Optional[ViewTypes]
  filter: Optional["ContentCriteriaInput"]
  augmented_filter: Optional["ContentCriteriaInput"]
```

### OneDriveDistributionPropertiesInput
```
  folder_id: Optional[str]
  file_name: Optional[str]
```

### DropboxFeedPropertiesInput
```
  authentication_type: Optional[DropboxAuthenticationTypes]
  path: Optional[str]
  app_key: Optional[str]
  app_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### PersonReferenceInput
```
  name: Optional[str]
  given_name: Optional[str]
  family_name: Optional[str]
  email: Optional[str]
```

### ParallelFeedPropertiesInput
```
  processor: Optional[ParallelProcessors]
```

### ElevenLabsPublishingPropertiesInput
```
  model: Optional[ElevenLabsModels]
  voice: Optional[str]
```

### ZendeskFeedPropertiesInput
```
  authentication_type: Optional[ZendeskAuthenticationTypes]
  subdomain: str
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  read_limit: Optional[int]
```

### MedicalTherapyFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalTherapyFacetTypes]
```

### MedicalDrugFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_drugs: Optional[list["EntityReferenceFilter"]]
  medical_drugs: Optional[list["EntityReferenceFilter"]]
```

### ConversationToolResponseInput
```
  id: str
  content: str
```

### InvestmentInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  amount_currency: Optional[str]
  amount: Optional[Any]
  status: Optional[str]
  stage: Optional[str]
  investment_date: Optional[Any]
  round_size: Optional[Any]
  round_size_currency: Optional[str]
  post_valuation: Optional[Any]
  post_valuation_currency: Optional[str]
  shares_owned: Optional[Any]
  vehicle: Optional[str]
  entry_price_per_share: Optional[Any]
  current_price_per_share: Optional[Any]
  discount_percent: Optional[Any]
  pro_rata_rights: Optional[bool]
  investor: Optional["EntityReferenceInput"]
  organization: Optional["EntityReferenceInput"]
```

### ContentInput
```
  name: str
  type: Optional[ContentTypes]
  uri: Optional[Any]
  description: Optional[str]
  text: Optional[str]
  identifier: Optional[str]
  file_creation_date: Optional[Any]
  file_modified_date: Optional[Any]
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  workflow: Optional["EntityReferenceInput"]
```

### LinearProjectsInput
```
  authentication_type: Optional[LinearIssueAuthenticationTypes]
  key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### TwelveLabsModelPropertiesUpdateInput
```
  model: Optional[TwelveLabsModels]
  key: Optional[str]
  embedding_options: Optional[list[TwelveLabsEmbeddingOptions]]
  embedding_scopes: Optional[list[TwelveLabsEmbeddingScopes]]
  segmentation_method: Optional[TwelveLabsSegmentationMethods]
  segmentation_duration: Optional[int]
```

### ContentCriteriaLevelInput
```
  feeds: Optional[list["EntityReferenceInput"]]
  workflows: Optional[list["EntityReferenceInput"]]
  collections: Optional[list["EntityReferenceInput"]]
  observations: Optional[list["ObservationCriteriaInput"]]
```

### H3IndexFilter
```
  resolution: Optional[H3ResolutionTypes]
  key: Optional[str]
```

### FactGraphInput
```
  types: Optional[list[ObservableTypes]]
```

### FirefliesFeedPropertiesUpdateInput
```
  api_key: Optional[str]
  before_date: Optional[Any]
  after_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### MeetingFeedPropertiesUpdateInput
```
  content_type: Optional[MeetingContentTypes]
  fireflies: Optional["FirefliesFeedPropertiesUpdateInput"]
  attio: Optional["AttioMeetingPropertiesUpdateInput"]
  fathom: Optional["FathomPropertiesUpdateInput"]
  hub_spot: Optional["HubSpotMeetingPropertiesUpdateInput"]
  krisp: Optional["KrispPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### EntityResolutionStrategyInput
```
  strategy: Optional[EntityResolutionStrategyTypes]
  threshold: Optional[float]
  specification: Optional["EntityReferenceInput"]
```

### DiscordFeedPropertiesInput
```
  type: Optional[FeedListingTypes]
  token: str
  channel: str
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### SoftwareUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  developer: Optional[str]
  release_date: Optional[Any]
```

### NotionDistributionPropertiesInput
```
  parent_page_id: Optional[str]
  database_id: Optional[str]
  title: Optional[str]
```

### GoogleDriveDistributionPropertiesInput
```
  folder_id: Optional[str]
  file_name: Optional[str]
```

### AssemblyAIAudioPreparationPropertiesInput
```
  model: Optional[AssemblyAIModels]
  key: Optional[str]
  enable_redaction: Optional[bool]
  enable_speaker_diarization: Optional[bool]
  detect_language: Optional[bool]
  language: Optional[str]
```

### FeedSchedulePolicyInput
```
  recurrence_type: TimedPolicyRecurrenceTypes
  repeat_interval: Optional[Any]
```

### FHIREnrichmentPropertiesInput
```
  endpoint: Optional[Any]
```

### MicrosoftCalendarsInput
```
  authentication_type: Optional[MicrosoftCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalDrugClassFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_classes: Optional[list["EntityReferenceFilter"]]
  medical_drug_classes: Optional[list["EntityReferenceFilter"]]
```

### MetadataInput
```
  name: str
  mime_type: Optional[str]
  value: Optional[str]
  content: Optional["EntityReferenceInput"]
```

### CategoryInput
```
  name: str
  description: Optional[str]
```

### CohereModelPropertiesUpdateInput
```
  model: Optional[CohereModels]
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### MedicalGuidelineUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### AtlassianSitesInput
```
  authentication_type: Optional[ConfluenceAuthenticationTypes]
  token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### GroqModelPropertiesInput
```
  model: GroqModels
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### ConfluenceSpacesInput
```
  authentication_type: Optional[ConfluenceAuthenticationTypes]
  uri: Optional[str]
  email_address: Optional[str]
  token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
```

### EntityFeedPropertiesInput
```
  type: FeedServiceTypes
  query: str
  parallel: Optional["ParallelEntityFeedPropertiesInput"]
  read_limit: Optional[int]
```

### CommitFeedPropertiesInput
```
  type: FeedServiceTypes
  github: Optional["GitHubCommitsFeedPropertiesInput"]
  read_limit: Optional[int]
```

### SoftwareFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_softwares: Optional[list["EntityReferenceFilter"]]
  softwares: Optional[list["EntityReferenceFilter"]]
```

### CerebrasModelPropertiesUpdateInput
```
  model: Optional[CerebrasModels]
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### EmailMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  subject: Optional[str]
  identifier: Optional[str]
  thread_identifier: Optional[str]
  sensitivity: Optional[MailSensitivity]
  priority: Optional[MailPriority]
  importance: Optional[MailImportance]
  labels: Optional[list[Optional[str]]]
  links: Optional[list[Optional[Any]]]
  attachment_count: Optional[int]
  unsubscribe_url: Optional[str]
  publication_name: Optional[str]
  publication_url: Optional[str]
```

### SharePointLibrariesInput
```
  authentication_type: SharePointAuthenticationTypes
  tenant_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### SharePointFeedPropertiesInput
```
  authentication_type: SharePointAuthenticationTypes
  tenant_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  account_name: str
  library_id: str
  folder_id: Optional[str]
```

### EmailIntegrationPropertiesInput
```
  subject: str
  from_: str
  to: list[str]
```

### AttioTasksDistributionPropertiesInput
```
  title: Optional[str]
  assignees: Optional[list[str]]
  linked_record_id: Optional[str]
  linked_object_type: Optional[str]
  deadline: Optional[Any]
```

### OpenAIImagePublishingPropertiesInput
```
  model: Optional[OpenAIImageModels]
  count: Optional[int]
  seed: Optional["EntityReferenceInput"]
```

### ModelDocumentPreparationPropertiesInput
```
  specification: Optional["EntityReferenceInput"]
```

### FilePreparationConnectorInput
```
  type: FilePreparationServiceTypes
  file_types: Optional[list[FileTypes]]
  page: Optional["PagePreparationPropertiesInput"]
  document: Optional["DocumentPreparationPropertiesInput"]
  email: Optional["EmailPreparationPropertiesInput"]
  azure_document: Optional["AzureDocumentPreparationPropertiesInput"]
  deepgram: Optional["DeepgramAudioPreparationPropertiesInput"]
  assembly_ai: Optional["AssemblyAIAudioPreparationPropertiesInput"]
  eleven_labs_scribe: Optional["ElevenLabsScribeAudioPreparationPropertiesInput"]
  mistral: Optional["MistralDocumentPreparationPropertiesInput"]
  model_document: Optional["ModelDocumentPreparationPropertiesInput"]
  reducto: Optional["ReductoDocumentPreparationPropertiesInput"]
```

### ParallelEntityFeedPropertiesUpdateInput
```
  generator: Optional[ParallelGenerators]
  processor: Optional[ParallelProcessors]
```

### HubSpotTasksFeedPropertiesUpdateInput
```
  authentication_type: Optional[HubSpotIssueAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### AnthropicModelPropertiesUpdateInput
```
  model: Optional[AnthropicModels]
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  completion_token_limit: Optional[int]
  enable_thinking: Optional[bool]
  thinking_token_limit: Optional[int]
  effort: Optional[AnthropicEffortLevels]
```

### IntercomTicketsFeedPropertiesInput
```
  authentication_type: Optional[IntercomIssueAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### EntityEnrichmentConnectorInput
```
  type: EntityEnrichmentServiceTypes
  enriched_types: Optional[list[ObservableTypes]]
  parallel: Optional["ParallelEnrichmentPropertiesInput"]
  fhir: Optional["FHIREnrichmentPropertiesInput"]
  diffbot: Optional["DiffbotEnrichmentPropertiesInput"]
```

### AttioFeedPropertiesUpdateInput
```
  authentication_type: Optional[AttioFeedAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### MicrosoftAuthenticationPropertiesInput
```
  tenant_id: str
  client_id: str
  client_secret: str
```

### AzureOpenAIModelPropertiesInput
```
  model: AzureOpenAIModels
  deployment_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### ContentFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[ContentFacetTypes]
```

### ObservationReferenceInput
```
  type: ObservableTypes
  observable: "NamedEntityReferenceInput"
```

### TwitterFeedPropertiesInput
```
  authentication_type: Optional[TwitterAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[TwitterListingTypes]
  user_name: Optional[str]
  query: Optional[str]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### TwelveLabsModelPropertiesInput
```
  model: TwelveLabsModels
  key: Optional[str]
  embedding_options: Optional[list[TwelveLabsEmbeddingOptions]]
  embedding_scopes: Optional[list[TwelveLabsEmbeddingScopes]]
  segmentation_method: Optional[TwelveLabsSegmentationMethods]
  segmentation_duration: Optional[int]
```

### MedicalDeviceFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalDeviceFacetTypes]
```

### KrispPropertiesUpdateInput
```
  auth_token: Optional[str]
  type: Optional[FeedListingTypes]
```

### WorkflowInput
```
  name: str
  ingestion: Optional["IngestionWorkflowStageInput"]
  indexing: Optional["IndexingWorkflowStageInput"]
  preparation: Optional["PreparationWorkflowStageInput"]
  extraction: Optional["ExtractionWorkflowStageInput"]
  enrichment: Optional["EnrichmentWorkflowStageInput"]
  classification: Optional["ClassificationWorkflowStageInput"]
  storage: Optional["StorageWorkflowStageInput"]
  actions: Optional[list[Optional["WorkflowActionInput"]]]
```

### AmazonFeedPropertiesInput
```
  access_key: str
  secret_access_key: str
  bucket_name: str
  prefix: Optional[str]
  region: Optional[str]
  custom_endpoint: Optional[str]
```

### GraphStrategyInput
```
  type: Optional[GraphStrategyTypes]
  generate_graph: Optional[bool]
  observable_limit: Optional[int]
```

### RepoUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### MicrosoftWordDistributionPropertiesInput
```
  folder_id: Optional[str]
  file_name: Optional[str]
```

### NotionFeedPropertiesInput
```
  is_recursive: Optional[bool]
  authentication_type: Optional[NotionAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: NotionTypes
  identifiers: list[str]
  read_limit: Optional[int]
```

### AsanaWorkspacesInput
```
  personal_access_token: str
```

### ReplicateModelPropertiesUpdateInput
```
  model: Optional[ReplicateModels]
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### GitHubDistributionPropertiesInput
```
  repository_owner: str
  repository_name: str
  title: Optional[str]
  labels: Optional[list[str]]
  assignees: Optional[list[str]]
  milestone: Optional[int]
```

### TwitterIntegrationPropertiesInput
```
  consumer_key: str
  consumer_secret: str
  access_token_key: str
  access_token_secret: str
```

### PlaceUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  telephone: Optional[str]
  opening_hours: Optional[str]
  price_range: Optional[str]
```

### GitHubRepositoriesInput
```
  authentication_type: GitHubAuthenticationTypes
  uri: Optional[str]
  personal_access_token: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### PointFilter
```
  latitude: float
  longitude: float
  distance: Optional[float]
```

### DeepgramAudioPreparationPropertiesInput
```
  model: Optional[DeepgramModels]
  key: Optional[str]
  enable_redaction: Optional[bool]
  enable_speaker_diarization: Optional[bool]
  detect_language: Optional[bool]
  language: Optional[str]
```

### GustoHRISFeedPropertiesUpdateInput
```
  authentication_type: Optional[GustoAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  company_id: Optional[str]
```

### ConversationInput
```
  name: str
  type: Optional[ConversationTypes]
  messages: Optional[list["ConversationMessageInput"]]
  tools: Optional[list["ToolDefinitionInput"]]
  persona: Optional["EntityReferenceInput"]
  specification: Optional["EntityReferenceInput"]
  fallbacks: Optional[list[Optional["EntityReferenceInput"]]]
  filter: Optional["ContentCriteriaInput"]
  augmented_filter: Optional["ContentCriteriaInput"]
```

### MedicalTestUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ProductUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  production_date: Optional[Any]
  release_date: Optional[Any]
  sku: Optional[str]
  upc: Optional[str]
  manufacturer: Optional[str]
  brand: Optional[str]
  model: Optional[str]
  gtin: Optional[str]
  mpn: Optional[str]
```

### EmotionInput
```
  name: str
  description: Optional[str]
```

### MentionReferenceInput
```
  type: Optional[ObservableTypes]
  observable: Optional["NamedEntityReferenceInput"]
  start: Optional[int]
  end: Optional[int]
```

### RerankingStrategyUpdateInput
```
  service_type: Optional[RerankingModelServiceTypes]
  threshold: Optional[float]
```

### IngestionWorkflowStageInput
```
  if_: Optional["IngestionContentFilterInput"]
  collections: Optional[list[Optional["EntityReferenceInput"]]]
  observations: Optional[list[Optional["ObservationReferenceInput"]]]
  enable_email_collections: Optional[bool]
  enable_folder_collections: Optional[bool]
  enable_message_collections: Optional[bool]
```

### AtlassianJiraFeedPropertiesInput
```
  authentication_type: Optional[JiraAuthenticationTypes]
  uri: Optional[Any]
  project: Optional[str]
  email: Optional[str]
  token: Optional[str]
  offset: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
```

### DiscordChannelsInput
```
  token: str
  guild_id: str
```

### BoxFeedPropertiesInput
```
  authentication_type: Optional[BoxAuthenticationTypes]
  folder_id: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  redirect_uri: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### ContentFilterLevel
```
  feeds: Optional[list["EntityReferenceFilter"]]
  workflows: Optional[list["EntityReferenceFilter"]]
  collections: Optional[list["EntityReferenceFilter"]]
  users: Optional[list["EntityReferenceFilter"]]
  observations: Optional[list["ObservationReferenceFilter"]]
```

### MistralDocumentPreparationPropertiesInput
```
  key: Optional[str]
```

### H3Filter
```
  indexes: Optional[list["H3IndexFilter"]]
```

### EmailPreparationPropertiesInput
```
  include_attachments: Optional[bool]
```

### MedicalDeviceUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### MondayBoardsInput
```
  api_token: str
```

### AttioDistributionPropertiesInput
```
  parent_object: str
  parent_record_id: str
  title: Optional[str]
```

### AttioTasksFeedPropertiesInput
```
  authentication_type: Optional[AttioIssueAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### PointInput
```
  latitude: float
  longitude: float
  distance: Optional[float]
```

### MicrosoftContactsCRMFeedPropertiesInput
```
  authentication_type: Optional[MicrosoftContactsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  tenant_id: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### SharePointFeedPropertiesUpdateInput
```
  authentication_type: Optional[SharePointAuthenticationTypes]
  tenant_id: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  account_name: Optional[str]
  library_id: Optional[str]
  folder_id: Optional[str]
```

### AudioMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  keywords: Optional[list[Optional[str]]]
  author: Optional[str]
  series: Optional[str]
  episode: Optional[str]
  episode_type: Optional[str]
  season: Optional[str]
  publisher: Optional[str]
  copyright: Optional[str]
  genre: Optional[str]
  title: Optional[str]
  bitrate: Optional[int]
  channels: Optional[int]
  sample_rate: Optional[int]
  bits_per_sample: Optional[int]
  duration: Optional[str]
```

### MedicalDrugInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### IndexingWorkflowJobInput
```
  connector: Optional["ContentIndexingConnectorInput"]
```

### IndexingWorkflowStageInput
```
  jobs: Optional[list[Optional["IndexingWorkflowJobInput"]]]
```

### DeepseekModelPropertiesUpdateInput
```
  model: Optional[DeepseekModels]
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### FactUpdateInput
```
  id: str
  text: Optional[str]
  valid_at: Optional[Any]
  invalid_at: Optional[Any]
```

### AzureAIModelPropertiesUpdateInput
```
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### SpecificationUpdateInput
```
  id: str
  name: Optional[str]
  type: Optional[SpecificationTypes]
  service_type: ModelServiceTypes
  search_type: Optional[ConversationSearchTypes]
  number_similar: Optional[int]
  system_prompt: Optional[str]
  custom_guidance: Optional[str]
  custom_instructions: Optional[str]
  strategy: Optional["ConversationStrategyUpdateInput"]
  prompt_strategy: Optional["PromptStrategyUpdateInput"]
  retrieval_strategy: Optional["RetrievalStrategyUpdateInput"]
  reranking_strategy: Optional["RerankingStrategyUpdateInput"]
  graph_strategy: Optional["GraphStrategyUpdateInput"]
  fact_strategy: Optional["FactStrategyUpdateInput"]
  revision_strategy: Optional["RevisionStrategyUpdateInput"]
  azure_ai: Optional["AzureAIModelPropertiesUpdateInput"]
  open_ai: Optional["OpenAIModelPropertiesUpdateInput"]
  azure_open_ai: Optional["AzureOpenAIModelPropertiesUpdateInput"]
  cohere: Optional["CohereModelPropertiesUpdateInput"]
  anthropic: Optional["AnthropicModelPropertiesUpdateInput"]
  google: Optional["GoogleModelPropertiesUpdateInput"]
  replicate: Optional["ReplicateModelPropertiesUpdateInput"]
  mistral: Optional["MistralModelPropertiesUpdateInput"]
  bedrock: Optional["BedrockModelPropertiesUpdateInput"]
  xai: Optional["XAIModelPropertiesUpdateInput"]
  groq: Optional["GroqModelPropertiesUpdateInput"]
  cerebras: Optional["CerebrasModelPropertiesUpdateInput"]
  deepseek: Optional["DeepseekModelPropertiesUpdateInput"]
  jina: Optional["JinaModelPropertiesUpdateInput"]
  voyage: Optional["VoyageModelPropertiesUpdateInput"]
  twelve_labs: Optional["TwelveLabsModelPropertiesUpdateInput"]
```

### EnrichmentWorkflowStageInput
```
  link: Optional["LinkStrategyInput"]
  jobs: Optional[list[Optional["EnrichmentWorkflowJobInput"]]]
  entity_resolution: Optional["EntityResolutionStrategyInput"]
```

### FeedFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  identifier: Optional[str]
  types: Optional[list[FeedTypes]]
```

### ViewFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[Optional[ViewTypes]]]
```

### EventFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  start_date_range: Optional["DateRangeFilter"]
  end_date_range: Optional["DateRangeFilter"]
  availability_start_date_range: Optional["DateRangeFilter"]
  availability_end_date_range: Optional["DateRangeFilter"]
  price: Optional[Any]
  min_price: Optional[Any]
  max_price: Optional[Any]
  price_currency: Optional[str]
  is_accessible_for_free: Optional[bool]
  typical_age_range: Optional[str]
  similar_events: Optional[list["EntityReferenceFilter"]]
  events: Optional[list["EntityReferenceFilter"]]
```

### YouTubeFeedPropertiesUpdateInput
```
  type: Optional[YouTubeTypes]
  video_name: Optional[str]
  video_identifiers: Optional[list[str]]
  channel_identifier: Optional[str]
  playlist_identifier: Optional[str]
  read_limit: Optional[int]
```

### MedicalTestFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalTestFacetTypes]
```

### OAuthAuthenticationPropertiesInput
```
  provider: OAuthProviders
  client_id: str
  client_secret: str
  refresh_token: str
  redirect_uri: Optional[str]
  metadata: Optional[str]
```

### DeepseekModelPropertiesInput
```
  model: DeepseekModels
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### SlackFeedPropertiesInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[SlackAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  channel: str
  include_attachments: Optional[bool]
  signing_secret: Optional[str]
  read_limit: Optional[int]
```

### PersonaFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
```

### RegexContentClassificationPropertiesInput
```
  rules: Optional[list[Optional["RegexClassificationRuleInput"]]]
```

### EntityRelationshipsFilter
```
  id: str
  limit: Optional[int]
  relationship_types: Optional[list[str]]
  include_metadata: Optional[bool]
  disable_inheritance: Optional[bool]
```

### SoftwareFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[SoftwareFacetTypes]
```

### ObservationInput
```
  content: "EntityReferenceInput"
  type: ObservableTypes
  observable: "NamedEntityReferenceInput"
  related: Optional["NamedEntityReferenceInput"]
  related_type: Optional[ObservableTypes]
  relation: Optional[str]
  occurrences: list["ObservationOccurrenceInput"]
```

### DocumentPreparationPropertiesInput
```
  include_images: Optional[bool]
```

### MedicalDeviceFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_devices: Optional[list["EntityReferenceFilter"]]
  medical_devices: Optional[list["EntityReferenceFilter"]]
```

### EntityFeedPropertiesUpdateInput
```
  query: Optional[str]
  parallel: Optional["ParallelEntityFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### CalendarFeedPropertiesInput
```
  type: FeedServiceTypes
  include_attachments: Optional[bool]
  enable_meeting_recording: Optional[bool]
  meeting_bot_name: Optional[str]
  google: Optional["GoogleCalendarFeedPropertiesInput"]
  microsoft: Optional["MicrosoftCalendarFeedPropertiesInput"]
  read_limit: Optional[int]
```

### MicrosoftEmailFeedPropertiesInput
```
  type: Optional[EmailListingTypes]
  filter: Optional[str]
  inbox_only: Optional[bool]
  include_deleted_items: Optional[bool]
  exclude_sent_items: Optional[bool]
  include_spam: Optional[bool]
  authentication_type: Optional[MicrosoftEmailAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### ProjectUpdateInput
```
  workflow: Optional["EntityReferenceInput"]
  specification: Optional["EntityReferenceInput"]
  embeddings: Optional["EmbeddingsStrategyInput"]
  callback_uri: Optional[Any]
```

### ProjectFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
```

### SummarizationStrategyInput
```
  type: SummarizationTypes
  specification: Optional["EntityReferenceInput"]
  tokens: Optional[int]
  items: Optional[int]
  prompt: Optional[str]
```

### ProductFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  production_date_range: Optional["DateRangeFilter"]
  release_date_range: Optional["DateRangeFilter"]
  sku: Optional[str]
  upc: Optional[str]
  manufacturer: Optional[str]
  brand: Optional[str]
  model: Optional[str]
  similar_products: Optional[list["EntityReferenceFilter"]]
  products: Optional[list["EntityReferenceFilter"]]
```

### ProjectInput
```
  name: str
  environment_type: EnvironmentTypes
  platform: ResourceConnectorTypes
  region: str
  jwt_secret: str
  quota: Optional["ProjectQuotaInput"]
  callback_uri: Optional[Any]
```

### ContentClassificationConnectorInput
```
  type: Optional[ContentClassificationServiceTypes]
  content_type: Optional[ContentTypes]
  file_type: Optional[FileTypes]
  model: Optional["ModelContentClassificationPropertiesInput"]
  regex: Optional["RegexContentClassificationPropertiesInput"]
```

### ContentPublishingConnectorUpdateInput
```
  type: ContentPublishingServiceTypes
  format: ContentPublishingFormats
  eleven_labs: Optional["ElevenLabsPublishingPropertiesInput"]
  open_ai_image: Optional["OpenAIImagePublishingPropertiesInput"]
  google_image: Optional["GoogleImagePublishingPropertiesInput"]
  open_ai_video: Optional["OpenAIVideoPublishingPropertiesInput"]
  google_video: Optional["GoogleVideoPublishingPropertiesInput"]
  parallel: Optional["ParallelPublishingPropertiesInput"]
```

### CRMFeedPropertiesInput
```
  type: FeedServiceTypes
  attio: Optional["AttioCRMFeedPropertiesInput"]
  google_contacts: Optional["GoogleContactsCRMFeedPropertiesInput"]
  microsoft_contacts: Optional["MicrosoftContactsCRMFeedPropertiesInput"]
  salesforce: Optional["SalesforceCRMFeedPropertiesInput"]
  hub_spot: Optional["HubSpotCRMFeedPropertiesInput"]
  read_limit: Optional[int]
```

### VoyageModelPropertiesInput
```
  model: VoyageModels
  model_name: Optional[str]
  key: Optional[str]
  chunk_token_limit: Optional[int]
```

### ParallelEntityFeedPropertiesInput
```
  generator: Optional[ParallelGenerators]
  processor: Optional[ParallelProcessors]
```

### OrganizationUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  founding_date: Optional[Any]
  email: Optional[str]
  telephone: Optional[str]
  legal_name: Optional[str]
  industries: Optional[list[Optional[str]]]
  revenue_currency: Optional[str]
  revenue: Optional[Any]
  investment_currency: Optional[str]
  investment: Optional[Any]
```

### GoogleCalendarFeedPropertiesUpdateInput
```
  type: Optional[CalendarListingTypes]
  calendar_id: Optional[str]
  before_date: Optional[Any]
  after_date: Optional[Any]
  authentication_type: Optional[GoogleCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### SalesforceCRMFeedPropertiesUpdateInput
```
  authentication_type: Optional[SalesforceAuthenticationTypes]
  instance_url: Optional[str]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### PointCloudMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  software: Optional[str]
  description: Optional[str]
  identifier: Optional[str]
  point_count: Optional[Any]
```

### BoundingBoxInput
```
  left: Optional[float]
  top: Optional[float]
  width: Optional[float]
  height: Optional[float]
```

### ReplicateModelPropertiesInput
```
  model: ReplicateModels
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### ObservationReferenceFilter
```
  type: ObservableTypes
  observable: "EntityReferenceFilter"
  states: Optional[list[EntityState]]
```

### PromptStrategyInput
```
  type: Optional[PromptStrategyTypes]
```

### ConversationMessageInput
```
  role: ConversationRoleTypes
  author: Optional[str]
  message: Optional[str]
  tool_calls: Optional[list["ConversationToolCallInput"]]
  tool_call_id: Optional[str]
  tool_call_response: Optional[str]
  tokens: Optional[int]
  throughput: Optional[float]
  ttft: Optional[Any]
  completion_time: Optional[Any]
  timestamp: Optional[Any]
  data: Optional[str]
  mime_type: Optional[str]
  artifacts: Optional[list[Optional["EntityReferenceInput"]]]
```

### GitHubCommitsFeedPropertiesInput
```
  authentication_type: Optional[GitHubCommitAuthenticationTypes]
  repository_owner: str
  repository_name: str
  branch: Optional[str]
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### StorageGateRuleInput
```
  if_: str
```

### HubSpotCRMFeedPropertiesUpdateInput
```
  authentication_type: Optional[HubSpotAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### NotionFeedPropertiesUpdateInput
```
  is_recursive: Optional[bool]
  authentication_type: Optional[NotionAuthenticationTypes]
  token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[NotionTypes]
  identifiers: Optional[list[str]]
  read_limit: Optional[int]
```

### ResearchFeedPropertiesInput
```
  type: Optional[FeedServiceTypes]
  query: str
  parallel: Optional["ParallelFeedPropertiesInput"]
  read_limit: Optional[int]
```

### AuthenticationConnectorInput
```
  type: AuthenticationServiceTypes
  token: Optional[str]
  api_key: Optional[str]
  microsoft: Optional["MicrosoftAuthenticationPropertiesInput"]
  google: Optional["GoogleAuthenticationPropertiesInput"]
  arcade: Optional["ArcadeAuthenticationPropertiesInput"]
  oauth: Optional["OAuthAuthenticationPropertiesInput"]
```

### ConversationToolCallInput
```
  id: str
  name: str
  arguments: Optional[str]
```

### ExtractionWorkflowJobInput
```
  connector: Optional["EntityExtractionConnectorInput"]
```

### PreparationWorkflowStageInput
```
  enable_unblocked_capture: Optional[bool]
  disable_smart_capture: Optional[bool]
  summarizations: Optional[list[Optional["SummarizationStrategyInput"]]]
  jobs: Optional[list[Optional["PreparationWorkflowJobInput"]]]
```

### HRISFeedPropertiesUpdateInput
```
  bamboo_hr: Optional["BambooHRHRISFeedPropertiesUpdateInput"]
  gusto: Optional["GustoHRISFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### PromptClassificationRuleInput
```
  if_: Optional[str]
  then: Optional[str]
```

### LinearDistributionPropertiesInput
```
  team_id: str
  title: Optional[str]
  priority: Optional[int]
  state_id: Optional[str]
  assignee_id: Optional[str]
  label_ids: Optional[list[str]]
  project_id: Optional[str]
```

### RegexClassificationRuleInput
```
  type: Optional[RegexSourceTypes]
  path: Optional[str]
  matches: Optional[str]
  then: Optional[str]
```

### StorageGateInput
```
  type: StorageGateTypes
  specification: Optional["EntityReferenceInput"]
  rules: Optional[list["StorageGateRuleInput"]]
  uri: Optional[Any]
  on_reject: Optional[StorageGateRejectionActions]
```

### GoogleImagePublishingPropertiesInput
```
  model: Optional[GoogleImageModels]
  count: Optional[int]
  seed: Optional["EntityReferenceInput"]
```

### MedicalStudyUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
```

### GoogleDriveFeedPropertiesInput
```
  authentication_type: Optional[GoogleDriveAuthenticationTypes]
  files: Optional[list[Optional[str]]]
  folder_id: Optional[str]
  refresh_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  service_account_json: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### NamedEntityReferenceInput
```
  id: Optional[str]
  name: Optional[str]
```

### CohereModelPropertiesInput
```
  model: CohereModels
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
```

### KrispPropertiesInput
```
  auth_token: Optional[str]
  type: Optional[FeedListingTypes]
```

### CollectionUpdateInput
```
  id: str
  name: Optional[str]
  type: Optional[CollectionTypes]
  contents: Optional[list["EntityReferenceInput"]]
  conversations: Optional[list["EntityReferenceInput"]]
  expected_count: Optional[int]
```

### HubSpotConversationsFeedPropertiesUpdateInput
```
  type: Optional[FeedListingTypes]
  authentication_type: Optional[HubSpotFeedAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  inbox_id: Optional[str]
  include_closed_threads: Optional[bool]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### HubSpotDistributionPropertiesInput
```
  object_type: str
  object_id: str
```

### FathomPropertiesUpdateInput
```
  api_key: Optional[str]
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
```

### GoogleModelPropertiesUpdateInput
```
  model: Optional[GoogleModels]
  model_name: Optional[str]
  key: Optional[str]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  enable_thinking: Optional[bool]
  thinking_token_limit: Optional[int]
  thinking_level: Optional[GoogleThinkingLevels]
```

### GoogleVideoPublishingPropertiesInput
```
  model: Optional[GoogleVideoModels]
  seconds: Optional[int]
  aspect_ratio: Optional[VideoAspectRatioTypes]
  seed: Optional["EntityReferenceInput"]
```

### SearchFeedPropertiesInput
```
  type: Optional[SearchServiceTypes]
  text: str
  exa: Optional["ExaSearchPropertiesInput"]
  read_limit: Optional[int]
```

### MedicalDrugClassInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### HRISFeedPropertiesInput
```
  type: FeedServiceTypes
  bamboo_hr: Optional["BambooHRHRISFeedPropertiesInput"]
  gusto: Optional["GustoHRISFeedPropertiesInput"]
  read_limit: Optional[int]
```

### WebFeedPropertiesUpdateInput
```
  uri: Optional[Any]
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
  include_files: Optional[bool]
  read_limit: Optional[int]
```

### RSSFeedPropertiesInput
```
  uri: Any
  read_limit: Optional[int]
```

### HubSpotMeetingPropertiesUpdateInput
```
  authentication_type: Optional[HubSpotFeedAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  include_transcripts: Optional[bool]
  after_date: Optional[Any]
  before_date: Optional[Any]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### RedditFeedPropertiesInput
```
  subreddit_name: str
  read_limit: Optional[int]
```

### MedicalTherapyFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_therapies: Optional[list["EntityReferenceFilter"]]
  medical_therapies: Optional[list["EntityReferenceFilter"]]
```

### GraphFilter
```
  types: Optional[list[ObservableTypes]]
  feeds: Optional[list["EntityReferenceFilter"]]
  creation_date_range: Optional["DateRangeFilter"]
  created_in_last: Optional[Any]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[Optional[str]]]
  search: Optional[str]
  search_type: Optional[SearchTypes]
  offset: Optional[int]
  limit: Optional[int]
  disable_inheritance: Optional[bool]
```

### BoxFoldersInput
```
  authentication_type: Optional[BoxAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  redirect_uri: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### ConversationUpdateInput
```
  id: str
  name: Optional[str]
  messages: Optional[list["ConversationMessageInput"]]
  tools: Optional[list["ToolDefinitionInput"]]
  persona: Optional["EntityReferenceInput"]
  specification: Optional["EntityReferenceInput"]
  fallbacks: Optional[list[Optional["EntityReferenceInput"]]]
  filter: Optional["ContentCriteriaInput"]
  augmented_filter: Optional["ContentCriteriaInput"]
```

### MedicalDeviceInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### PlaceFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_places: Optional[list["EntityReferenceFilter"]]
  places: Optional[list["EntityReferenceFilter"]]
```

### SiteFeedPropertiesUpdateInput
```
  is_recursive: Optional[bool]
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
  s_3: Optional["AmazonFeedPropertiesUpdateInput"]
  azure_blob: Optional["AzureBlobFeedPropertiesUpdateInput"]
  azure_file: Optional["AzureFileFeedPropertiesUpdateInput"]
  google: Optional["GoogleFeedPropertiesUpdateInput"]
  share_point: Optional["SharePointFeedPropertiesUpdateInput"]
  one_drive: Optional["OneDriveFeedPropertiesUpdateInput"]
  google_drive: Optional["GoogleDriveFeedPropertiesUpdateInput"]
  github: Optional["GitHubFeedPropertiesUpdateInput"]
  dropbox: Optional["DropboxFeedPropertiesUpdateInput"]
  box: Optional["BoxFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### ContentUpdateInput
```
  id: str
  name: Optional[str]
  description: Optional[str]
  identifier: Optional[str]
  file_creation_date: Optional[Any]
  file_modified_date: Optional[Any]
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  summary: Optional[str]
  custom_summary: Optional[str]
  keywords: Optional[list[str]]
  bullets: Optional[list[str]]
  headlines: Optional[list[str]]
  posts: Optional[list[str]]
  chapters: Optional[list[str]]
  questions: Optional[list[str]]
  quotes: Optional[list[str]]
  video: Optional["VideoMetadataInput"]
  audio: Optional["AudioMetadataInput"]
  image: Optional["ImageMetadataInput"]
  document: Optional["DocumentMetadataInput"]
  email: Optional["EmailMetadataInput"]
  event: Optional["EventMetadataInput"]
  issue: Optional["IssueMetadataInput"]
  message: Optional["MessageMetadataInput"]
  post: Optional["PostMetadataInput"]
  drawing: Optional["DrawingMetadataInput"]
  shape: Optional["ShapeMetadataInput"]
  geometry: Optional["GeometryMetadataInput"]
  point_cloud: Optional["PointCloudMetadataInput"]
  package: Optional["PackageMetadataInput"]
  language: Optional["LanguageMetadataInput"]
```

### MedicalContraindicationFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalContraindicationFacetTypes]
```

### EmotionFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
```

### SoftwareInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  developer: Optional[str]
  release_date: Optional[Any]
```

### AzureDocumentPreparationPropertiesInput
```
  model: Optional[AzureDocumentIntelligenceModels]
  endpoint: Optional[Any]
  key: Optional[str]
  version: Optional[AzureDocumentIntelligenceVersions]
```

### MicrosoftCalendarDistributionPropertiesInput
```
  calendar_id: Optional[str]
  subject: Optional[str]
  start_date_time: Any
  end_date_time: Any
  time_zone: Optional[str]
  location: Optional[str]
  attendees: Optional[list[str]]
  is_online_meeting: Optional[bool]
```

### GoogleAuthenticationPropertiesInput
```
  client_id: str
  client_secret: str
```

### GoogleCalendarFeedPropertiesInput
```
  type: Optional[CalendarListingTypes]
  calendar_id: Optional[str]
  before_date: Optional[Any]
  after_date: Optional[Any]
  authentication_type: Optional[GoogleCalendarAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### CategoryFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
```

### BambooHRHRISFeedPropertiesInput
```
  authentication_type: Optional[BambooHRAuthenticationTypes]
  api_key: Optional[str]
  company_domain: Optional[str]
```

### AzureBlobFeedPropertiesInput
```
  storage_access_key: str
  account_name: str
  container_name: str
  prefix: Optional[str]
  list_type: Optional[BlobListingTypes]
```

### GeometryMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  triangle_count: Optional[Any]
  vertex_count: Optional[Any]
```

### MeetingFeedPropertiesInput
```
  type: FeedServiceTypes
  content_type: Optional[MeetingContentTypes]
  fireflies: Optional["FirefliesFeedPropertiesInput"]
  attio: Optional["AttioMeetingPropertiesInput"]
  fathom: Optional["FathomPropertiesInput"]
  hub_spot: Optional["HubSpotMeetingPropertiesInput"]
  krisp: Optional["KrispPropertiesInput"]
  read_limit: Optional[int]
```

### ProductInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  production_date: Optional[Any]
  release_date: Optional[Any]
  sku: Optional[str]
  upc: Optional[str]
  manufacturer: Optional[str]
  brand: Optional[str]
  model: Optional[str]
  gtin: Optional[str]
  mpn: Optional[str]
```

### ConversationStrategyInput
```
  type: Optional[ConversationStrategyTypes]
  message_limit: Optional[int]
  embed_citations: Optional[bool]
  flatten_citations: Optional[bool]
  enable_facets: Optional[bool]
  enable_summarization: Optional[bool]
  enable_entity_extraction: Optional[bool]
  enable_fact_extraction: Optional[bool]
  entity_extraction_limit: Optional[int]
  fact_extraction_limit: Optional[int]
  messages_weight: Optional[float]
  contents_weight: Optional[float]
  tool_result_token_limit: Optional[int]
  tool_round_limit: Optional[int]
  tool_budget_threshold: Optional[float]
```

### ConversationFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[ConversationTypes]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_conversations: Optional[list["EntityReferenceFilter"]]
  conversations: Optional[list["EntityReferenceFilter"]]
  collections: Optional[list["EntityReferenceFilter"]]
  has_collections: Optional[bool]
  collection_mode: Optional[FilterMode]
  observations: Optional[list["ObservationReferenceFilter"]]
  has_observations: Optional[bool]
  observation_mode: Optional[FilterMode]
```

### InvestmentFundFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_investment_funds: Optional[list["EntityReferenceFilter"]]
  investment_funds: Optional[list["EntityReferenceFilter"]]
```

### GoogleContactsCRMFeedPropertiesUpdateInput
```
  authentication_type: Optional[GoogleContactsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### MentionReferenceFilter
```
  type: Optional[ObservableTypes]
  observable: Optional["EntityReferenceFilter"]
```

### HubSpotCRMFeedPropertiesInput
```
  authentication_type: Optional[HubSpotAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
```

### DateRangeFilter
```
  from_: Optional[Any]
  to: Optional[Any]
```

### MedicalStudyInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
```

### InvestmentFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[InvestmentFacetTypes]
```

### SiteFeedPropertiesInput
```
  type: FeedServiceTypes
  is_recursive: Optional[bool]
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
  s_3: Optional["AmazonFeedPropertiesInput"]
  azure_blob: Optional["AzureBlobFeedPropertiesInput"]
  azure_file: Optional["AzureFileFeedPropertiesInput"]
  google: Optional["GoogleFeedPropertiesInput"]
  share_point: Optional["SharePointFeedPropertiesInput"]
  one_drive: Optional["OneDriveFeedPropertiesInput"]
  google_drive: Optional["GoogleDriveFeedPropertiesInput"]
  github: Optional["GitHubFeedPropertiesInput"]
  dropbox: Optional["DropboxFeedPropertiesInput"]
  box: Optional["BoxFeedPropertiesInput"]
  read_limit: Optional[int]
```

### PersonaUpdateInput
```
  id: str
  name: Optional[str]
  role: Optional[str]
  instructions: Optional[str]
```

### TrelloFeedPropertiesInput
```
  key: str
  token: str
  type: TrelloTypes
  identifiers: list[str]
```

### GitHubPullRequestsFeedPropertiesUpdateInput
```
  authentication_type: Optional[GitHubPullRequestAuthenticationTypes]
  repository_owner: Optional[str]
  repository_name: Optional[str]
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalProcedureInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### MondayFeedPropertiesUpdateInput
```
  api_token: Optional[str]
  board_id: Optional[str]
```

### ArcadeAuthenticationPropertiesInput
```
  authorization_id: str
  provider: ArcadeProviders
  metadata: Optional[str]
```

### GoogleDriveFeedPropertiesUpdateInput
```
  authentication_type: Optional[GoogleDriveAuthenticationTypes]
  files: Optional[list[Optional[str]]]
  folder_id: Optional[str]
  refresh_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  service_account_json: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalDrugClassFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalDrugClassFacetTypes]
```

### WorkflowUpdateInput
```
  id: str
  name: Optional[str]
  ingestion: Optional["IngestionWorkflowStageInput"]
  indexing: Optional["IndexingWorkflowStageInput"]
  preparation: Optional["PreparationWorkflowStageInput"]
  extraction: Optional["ExtractionWorkflowStageInput"]
  enrichment: Optional["EnrichmentWorkflowStageInput"]
  classification: Optional["ClassificationWorkflowStageInput"]
  storage: Optional["StorageWorkflowStageInput"]
  actions: Optional[list[Optional["WorkflowActionInput"]]]
```

### JiraProjectsInput
```
  authentication_type: Optional[JiraAuthenticationTypes]
  uri: Optional[str]
  email_address: Optional[str]
  token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  cloud_id: Optional[str]
```

### ContentCriteriaInput
```
  in_last: Optional[Any]
  date_range: Optional["DateRangeInput"]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeInput"]
  types: Optional[list[ContentTypes]]
  file_types: Optional[list[FileTypes]]
  formats: Optional[list[Optional[str]]]
  file_extensions: Optional[list[str]]
  file_size_range: Optional["Int64RangeInput"]
  similar_contents: Optional[list["EntityReferenceInput"]]
  contents: Optional[list["EntityReferenceInput"]]
  feeds: Optional[list["EntityReferenceInput"]]
  workflows: Optional[list["EntityReferenceInput"]]
  collections: Optional[list["EntityReferenceInput"]]
  observations: Optional[list["ObservationCriteriaInput"]]
  or_: Optional[list["ContentCriteriaLevelInput"]]
  and_: Optional[list["ContentCriteriaLevelInput"]]
  has_observations: Optional[bool]
  has_feeds: Optional[bool]
  has_collections: Optional[bool]
  has_workflows: Optional[bool]
  collection_mode: Optional[FilterMode]
  observation_mode: Optional[FilterMode]
```

### MedicalGuidelineFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  similar_guidelines: Optional[list["EntityReferenceFilter"]]
  medical_guidelines: Optional[list["EntityReferenceFilter"]]
```

### AzureBlobFeedPropertiesUpdateInput
```
  storage_access_key: Optional[str]
  account_name: Optional[str]
  container_name: Optional[str]
  prefix: Optional[str]
  list_type: Optional[BlobListingTypes]
```

### ImageMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  width: Optional[int]
  height: Optional[int]
  bits_per_component: Optional[int]
  components: Optional[int]
  projection_type: Optional[ImageProjectionTypes]
  orientation: Optional[OrientationTypes]
  resolution_x: Optional[int]
  resolution_y: Optional[int]
  description: Optional[str]
  software: Optional[str]
  identifier: Optional[str]
  make: Optional[str]
  model: Optional[str]
  lens: Optional[str]
  lens_specification: Optional[str]
  focal_length: Optional[float]
  exposure_time: Optional[str]
  f_number: Optional[str]
  iso: Optional[str]
  color_space: Optional[str]
  heading: Optional[float]
  pitch: Optional[float]
```

### EventMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  subject: Optional[str]
  event_id: Optional[str]
  calendar_id: Optional[str]
  start_date_time: Optional[Any]
  end_date_time: Optional[Any]
  is_all_day: Optional[bool]
  timezone: Optional[str]
  status: Optional[CalendarEventStatus]
  visibility: Optional[CalendarEventVisibility]
  meeting_link: Optional[str]
  organizer: Optional["CalendarAttendeeInput"]
  attendees: Optional[list[Optional["CalendarAttendeeInput"]]]
  categories: Optional[list[Optional[str]]]
  reminders: Optional[list[Optional["CalendarReminderInput"]]]
  recurrence: Optional["CalendarRecurrenceInput"]
  recurring_event_id: Optional[str]
  is_recurring: Optional[bool]
  links: Optional[list[Optional["LinkReferenceInput"]]]
```

### GitHubCommitsFeedPropertiesUpdateInput
```
  authentication_type: Optional[GitHubCommitAuthenticationTypes]
  repository_owner: Optional[str]
  repository_name: Optional[str]
  branch: Optional[str]
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### FeedInput
```
  name: str
  identifier: Optional[str]
  description: Optional[str]
  type: FeedTypes
  sync_mode: Optional[FeedSyncMode]
  site: Optional["SiteFeedPropertiesInput"]
  calendar: Optional["CalendarFeedPropertiesInput"]
  email: Optional["EmailFeedPropertiesInput"]
  crm: Optional["CRMFeedPropertiesInput"]
  hris: Optional["HRISFeedPropertiesInput"]
  issue: Optional["IssueFeedPropertiesInput"]
  pull_request: Optional["PullRequestFeedPropertiesInput"]
  commit: Optional["CommitFeedPropertiesInput"]
  rss: Optional["RSSFeedPropertiesInput"]
  web: Optional["WebFeedPropertiesInput"]
  search: Optional["SearchFeedPropertiesInput"]
  reddit: Optional["RedditFeedPropertiesInput"]
  youtube: Optional["YouTubeFeedPropertiesInput"]
  notion: Optional["NotionFeedPropertiesInput"]
  confluence: Optional["ConfluenceFeedPropertiesInput"]
  twitter: Optional["TwitterFeedPropertiesInput"]
  slack: Optional["SlackFeedPropertiesInput"]
  microsoft_teams: Optional["MicrosoftTeamsFeedPropertiesInput"]
  discord: Optional["DiscordFeedPropertiesInput"]
  attio: Optional["AttioFeedPropertiesInput"]
  salesforce: Optional["SalesforceFeedPropertiesInput"]
  hub_spot_conversations: Optional["HubSpotConversationsFeedPropertiesInput"]
  intercom: Optional["IntercomFeedPropertiesInput"]
  zendesk: Optional["ZendeskFeedPropertiesInput"]
  intercom_conversations: Optional["IntercomConversationsFeedPropertiesInput"]
  research: Optional["ResearchFeedPropertiesInput"]
  entity: Optional["EntityFeedPropertiesInput"]
  meeting: Optional["MeetingFeedPropertiesInput"]
  schedule_policy: Optional["FeedSchedulePolicyInput"]
  workflow: Optional["EntityReferenceInput"]
```

### PersonFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  disable_inheritance: Optional[bool]
  feeds: Optional[list["EntityReferenceFilter"]]
  feed_mode: Optional[FilterMode]
  address: Optional["AddressFilter"]
  location: Optional["PointFilter"]
  h_3: Optional["H3Filter"]
  boundaries: Optional[list[str]]
  search_type: Optional[SearchTypes]
  query_type: Optional[SearchQueryTypes]
  number_similar: Optional[int]
  given_name: Optional[str]
  family_name: Optional[str]
  phone_number: Optional[str]
  email: Optional[str]
  uri: Optional[Any]
  similar_persons: Optional[list["EntityReferenceFilter"]]
  persons: Optional[list["EntityReferenceFilter"]]
```

### OpenAIVideoPublishingPropertiesInput
```
  model: Optional[OpenAIVideoModels]
  seconds: Optional[int]
  size: Optional[VideoSizeTypes]
  seed: Optional["EntityReferenceInput"]
```

### BambooHRHRISFeedPropertiesUpdateInput
```
  authentication_type: Optional[BambooHRAuthenticationTypes]
  api_key: Optional[str]
  company_domain: Optional[str]
```

### StorageWorkflowStageInput
```
  policy: Optional["StoragePolicyInput"]
  gate: Optional["StorageGateInput"]
```

### CategoryUpdateInput
```
  id: str
  name: Optional[str]
  description: Optional[str]
```

### MessageMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  identifier: Optional[str]
  conversation_identifier: Optional[str]
  channel_identifier: Optional[str]
  channel_name: Optional[str]
  attachment_count: Optional[int]
  links: Optional[list[Optional["LinkReferenceInput"]]]
  author: Optional["PersonReferenceInput"]
  mentions: Optional[list[Optional["PersonReferenceInput"]]]
```

### DropboxFeedPropertiesUpdateInput
```
  authentication_type: Optional[DropboxAuthenticationTypes]
  path: Optional[str]
  app_key: Optional[str]
  app_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### DiscordFeedPropertiesUpdateInput
```
  type: Optional[FeedListingTypes]
  token: Optional[str]
  channel: Optional[str]
  include_attachments: Optional[bool]
  read_limit: Optional[int]
```

### ConfluenceDistributionPropertiesInput
```
  space_id: str
  parent_page_id: Optional[str]
  title: Optional[str]
```

### MicrosoftTeamsChannelsInput
```
  authentication_type: Optional[MicrosoftTeamsAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### CollectionFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[CollectionTypes]]
  disable_inheritance: Optional[bool]
```

### MedicalDrugFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalDrugFacetTypes]
```

### CRMFeedPropertiesUpdateInput
```
  attio: Optional["AttioCRMFeedPropertiesUpdateInput"]
  google_contacts: Optional["GoogleContactsCRMFeedPropertiesUpdateInput"]
  microsoft_contacts: Optional["MicrosoftContactsCRMFeedPropertiesUpdateInput"]
  salesforce: Optional["SalesforceCRMFeedPropertiesUpdateInput"]
  hub_spot: Optional["HubSpotCRMFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### IntercomConversationsFeedPropertiesInput
```
  authentication_type: Optional[IntercomConversationsAuthenticationTypes]
  access_token: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  state: Optional[str]
  include_notes: Optional[bool]
  include_attachments: Optional[bool]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### MedicalGuidelineInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### ConnectorFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[ConnectorTypes]]
```

### LinkStrategyInput
```
  enable_crawling: Optional[bool]
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
  allowed_domains: Optional[list[str]]
  excluded_domains: Optional[list[str]]
  allow_content_domain: Optional[bool]
  allowed_links: Optional[list[LinkTypes]]
  excluded_links: Optional[list[LinkTypes]]
  allowed_files: Optional[list[FileTypes]]
  excluded_files: Optional[list[FileTypes]]
  allowed_content_types: Optional[list[ContentTypes]]
  excluded_content_types: Optional[list[ContentTypes]]
  maximum_links: Optional[int]
```

### ConnectorInput
```
  name: str
  type: ConnectorTypes
  authentication: Optional["AuthenticationConnectorInput"]
  integration: Optional["IntegrationConnectorInput"]
```

### AttioTasksFeedPropertiesUpdateInput
```
  authentication_type: Optional[AttioIssueAuthenticationTypes]
  api_key: Optional[str]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### OrganizationInput
```
  name: str
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
  address: Optional["AddressInput"]
  founding_date: Optional[Any]
  email: Optional[str]
  telephone: Optional[str]
  legal_name: Optional[str]
  industries: Optional[list[Optional[str]]]
  revenue_currency: Optional[str]
  revenue: Optional[Any]
  investment_currency: Optional[str]
  investment: Optional[Any]
```

### PersonFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[PersonFacetTypes]
```

### HubSpotTasksFeedPropertiesInput
```
  authentication_type: Optional[HubSpotIssueAuthenticationTypes]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalStudyFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[MedicalStudyFacetTypes]
```

### CalendarRecurrenceInput
```
  pattern: Optional[CalendarRecurrencePattern]
  interval: Optional[int]
  count: Optional[int]
  until: Optional[Any]
  days_of_week: Optional[list[Optional[str]]]
  day_of_month: Optional[int]
  month_of_year: Optional[int]
```

### XAIModelPropertiesUpdateInput
```
  model: Optional[XAIModels]
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
```

### GitHubIssuesFeedPropertiesUpdateInput
```
  repository_owner: Optional[str]
  repository_name: Optional[str]
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
```

### DrawingMetadataInput
```
  creation_date: Optional[Any]
  modified_date: Optional[Any]
  location: Optional["PointInput"]
  x: Optional[float]
  y: Optional[float]
  width: Optional[float]
  height: Optional[float]
  depth: Optional[float]
  unit_type: Optional[UnitTypes]
```

### SalesforceTasksFeedPropertiesUpdateInput
```
  authentication_type: Optional[SalesforceIssueAuthenticationTypes]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### LabelInput
```
  name: str
  description: Optional[str]
```

### ResearchFeedPropertiesUpdateInput
```
  type: Optional[FeedServiceTypes]
  query: Optional[str]
  parallel: Optional["ParallelFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### SalesforceFeedPropertiesUpdateInput
```
  authentication_type: Optional[SalesforceFeedAuthenticationTypes]
  is_sandbox: Optional[bool]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
  type: Optional[FeedListingTypes]
  read_limit: Optional[int]
```

### PlaceFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[PlaceFacetTypes]
```

### OpenAIModelPropertiesInput
```
  model: OpenAIModels
  model_name: Optional[str]
  key: Optional[str]
  endpoint: Optional[Any]
  temperature: Optional[float]
  probability: Optional[float]
  token_limit: Optional[int]
  completion_token_limit: Optional[int]
  chunk_token_limit: Optional[int]
  detail_level: Optional[OpenAIVisionDetailLevels]
  reasoning_effort: Optional[OpenAIReasoningEffortLevels]
```

### IssueFeedPropertiesInput
```
  type: FeedServiceTypes
  include_attachments: Optional[bool]
  jira: Optional["AtlassianJiraFeedPropertiesInput"]
  linear: Optional["LinearFeedPropertiesInput"]
  github: Optional["GitHubIssuesFeedPropertiesInput"]
  intercom: Optional["IntercomTicketsFeedPropertiesInput"]
  zendesk: Optional["ZendeskTicketsFeedPropertiesInput"]
  trello: Optional["TrelloFeedPropertiesInput"]
  attio: Optional["AttioTasksFeedPropertiesInput"]
  salesforce: Optional["SalesforceTasksFeedPropertiesInput"]
  hub_spot: Optional["HubSpotTasksFeedPropertiesInput"]
  asana: Optional["AsanaFeedPropertiesInput"]
  monday: Optional["MondayFeedPropertiesInput"]
  read_limit: Optional[int]
```

### PagePreparationPropertiesInput
```
  enable_screenshot: Optional[bool]
```

### FactInput
```
  content: Optional["EntityReferenceInput"]
  persona: Optional["EntityReferenceInput"]
  text: str
  valid_at: Optional[Any]
  invalid_at: Optional[Any]
  feeds: Optional[list[Optional["EntityReferenceInput"]]]
  assertions: Optional[list[Optional["FactAssertionInput"]]]
  category: Optional[FactCategory]
  confidence: Optional[float]
```

### BambooHROptionsInput
```
  company_domain: str
  api_key: str
```

### MicrosoftOutlookDistributionPropertiesInput
```
  to: list[str]
  subject: str
  cc: Optional[list[str]]
  bcc: Optional[list[str]]
  importance: Optional[str]
```

### EntityReferenceFilter
```
  id: str
```

### EnrichmentWorkflowJobInput
```
  connector: Optional["EntityEnrichmentConnectorInput"]
```

### GitHubPullRequestsFeedPropertiesInput
```
  authentication_type: Optional[GitHubPullRequestAuthenticationTypes]
  repository_owner: str
  repository_name: str
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### MedicalContraindicationUpdateInput
```
  id: str
  name: Optional[str]
  uri: Optional[Any]
  identifier: Optional[str]
  description: Optional[str]
  location: Optional["PointInput"]
  boundary: Optional[str]
```

### RevisionStrategyInput
```
  type: Optional[RevisionStrategyTypes]
  custom_revision: Optional[str]
  count: Optional[int]
```

### ParallelPublishingPropertiesInput
```
  processor: Optional[ParallelProcessors]
```

### CommitFeedPropertiesUpdateInput
```
  github: Optional["GitHubCommitsFeedPropertiesUpdateInput"]
  read_limit: Optional[int]
```

### JinaModelPropertiesUpdateInput
```
  model: Optional[JinaModels]
  model_name: Optional[str]
  key: Optional[str]
  chunk_token_limit: Optional[int]
```

### TwitterDistributionPropertiesInput
```
  reply_to_tweet_id: Optional[str]
```

### RepoFacetInput
```
  time_interval: Optional[TimeIntervalTypes]
  time_offset: Optional[int]
  facet: Optional[RepoFacetTypes]
```

### GitHubFeedPropertiesUpdateInput
```
  authentication_type: Optional[GitHubAuthenticationTypes]
  repository_owner: Optional[str]
  repository_name: Optional[str]
  uri: Optional[Any]
  client_id: Optional[str]
  client_secret: Optional[str]
  refresh_token: Optional[str]
  personal_access_token: Optional[str]
  connector: Optional["EntityReferenceInput"]
```

### AlertFilter
```
  search: Optional[str]
  order_by: Optional[OrderByTypes]
  direction: Optional[OrderDirectionTypes]
  offset: Optional[int]
  limit: Optional[int]
  relevance_threshold: Optional[float]
  id: Optional[str]
  name: Optional[str]
  states: Optional[list[EntityState]]
  created_in_last: Optional[Any]
  creation_date_range: Optional["DateRangeFilter"]
  modified_in_last: Optional[Any]
  modified_date_range: Optional["DateRangeFilter"]
  types: Optional[list[AlertTypes]]
```

### ContentGraphInput
```
  types: Optional[list[ObservableTypes]]
```

### WebFeedPropertiesInput
```
  uri: Any
  allowed_paths: Optional[list[str]]
  excluded_paths: Optional[list[str]]
  include_files: Optional[bool]
  read_limit: Optional[int]
```

## Enums

### FactCategory
`RELATIONSHIP, EVENT, FACT, PREFERENCE, CHANGE, QUANTITATIVE, GOAL, CAPABILITY, CONSTRAINT, DECISION, APPROVAL, EXCEPTION, ESCALATION, OVERRIDE, PRECEDENT, RATIONALE, COMMITMENT, DELEGATION`

### TwitterAuthenticationTypes
`TOKEN, CONNECTOR`

### AzureOpenAIModels
`GPT35_TURBO_16K, GPT4, GPT4_TURBO_128K, CUSTOM`

### TwelveLabsModels
`MARENGO_3_0`

### LinkTypes
`DROPBOX, TYPE_FORM, AIRTABLE, MICROSOFT_TEAMS, DISCORD, APPLE, SLACK, ANGEL_LIST, CRUNCHBASE, LINKED_IN, DIFFBOT, REDDIT, GOOGLE, IFTTT, FACEBOOK, WIKIPEDIA, WIKIMEDIA, WIKIDATA, INSTAGRAM, TWITCH, POCKET_CASTS, SPOTIFY, TUNE_IN, STITCHER, ANCHOR_FM, TRANSISTOR_FM, I_TUNES, PANDORA, SOUND_CLOUD, BANDCAMP, TIK_TOK, YOU_TUBE, TWITTER, X, MEDIUM, NOTION, HUB_SPOT, LINEAR, GIT_HUB, GIT_HUB_PAGES, RSS, EMAIL, MEDIA, WEB, FILE`

### CollectionTypes
`COLLECTION, CONVERSATION, THREAD, SERIES, FOLDER`

### MedicalProcedureFacetTypes
`CREATION_DATE`

### SlackAuthenticationTypes
`TOKEN, CONNECTOR`

### FeedTypes
`INTERCOM, ZENDESK, NOTION, TWITTER, SLACK, MICROSOFT_TEAMS, DISCORD, REDDIT, WEB, RSS, SITE, YOU_TUBE, EMAIL, ISSUE, PULL_REQUEST, COMMIT, SEARCH, CALENDAR, CRM, RESEARCH, ENTITY, ATTIO, SALESFORCE, HUB_SPOT, HUB_SPOT_CONVERSATIONS, CONFLUENCE, MEETING, HRIS, INTERCOM_CONVERSATIONS`

### H3ResolutionTypes
`R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15`

### DropboxAuthenticationTypes
`USER, CONNECTOR`

### GoogleDriveAuthenticationTypes
`SERVICE_ACCOUNT, USER, CONNECTOR`

### AnthropicEffortLevels
`LOW, MEDIUM, HIGH, MAX`

### RerankingModelServiceTypes
`COHERE, JINA, VOYAGE`

### AttioAuthenticationTypes
`API_KEY, ACCESS_TOKEN, CONNECTOR`

### PlaceFacetTypes
`CREATION_DATE`

### SourceTypes
`CONTENT, CONVERSATION, PERSONA`

### InvestmentFacetTypes
`CREATION_DATE`

### IntercomAuthenticationTypes
`ACCESS_TOKEN, CONNECTOR`

### MedicalDrugFacetTypes
`CREATION_DATE`

### RetrievalStrategyTypes
`CONTENT, CHUNK, SECTION`

### MedicalGuidelineFacetTypes
`CREATION_DATE`

### OpenAIVisionDetailLevels
`HIGH, LOW`

### ContentPublishingFormats
`PNG, JPEG, WEBP, MP3, MP4, TEXT, MARKDOWN, HTML`

### AzureDocumentIntelligenceModels
`READ_OCR, LAYOUT, INVOICE, RECEIPT, IDENTIFICATION_DOCUMENT, US_HEALTH_INSURANCE_CARD, US_TAX_FORM, US_TAX_FORM_W2, US_TAX_FORM1098, US_TAX_FORM1098_E, US_TAX_FORM1098_T, US_TAX_FORM1099, US_MARRIAGE_CERTIFICATE, US_MORTGAGE1003, US_MORTGAGE1008, US_MORTGAGE_DISCLOSURE, CREDIT_CARD, US_PAY_STUB, US_BANK_CHECK, US_BANK_STATEMENT`

### GitHubAuthenticationTypes
`PERSONAL_ACCESS_TOKEN, O_AUTH, CONNECTOR`

### GoogleEmailAuthenticationTypes
`USER, CONNECTOR`

### JinaModels
`CLIP_IMAGE, EMBED, EMBED_3_0, EMBED_4_0, CUSTOM`

### OneDriveAuthenticationTypes
`USER, CONNECTOR`

### GraphStrategyTypes
`EXTRACT_ENTITIES_FILTER, EXTRACT_ENTITIES_GRAPH, NONE`

### MicrosoftTeamsAuthenticationTypes
`USER, CONNECTOR`

### AuthenticationServiceTypes
`AUTH0, MICROSOFT_GRAPH, CLERK, GOOGLE, O_AUTH, ARCADE, TOKEN, API_KEY`

### LinearIssueAuthenticationTypes
`API_KEY, O_AUTH, CONNECTOR`

### RevisionStrategyTypes
`REVISE, CUSTOM, NONE`

### DeepseekModels
`REASONER, CHAT, CODER, CUSTOM`

### AnthropicModels
`CLAUDE_2, CLAUDE_2_0, CLAUDE_2_1, CLAUDE_INSTANT_1, CLAUDE_INSTANT_1_2, CLAUDE_3_OPUS, CLAUDE_3_OPUS_20240229, CLAUDE_3_SONNET, CLAUDE_3_SONNET_20240229, CLAUDE_3_HAIKU, CLAUDE_3_HAIKU_20240307, CLAUDE_3_5_SONNET, CLAUDE_3_5_SONNET_20241022, CLAUDE_3_5_SONNET_20240620, CLAUDE_3_5_HAIKU, CLAUDE_3_5_HAIKU_20241022, CLAUDE_3_7_SONNET, CLAUDE_3_7_SONNET_20250219, CLAUDE_4_SONNET, CLAUDE_4_SONNET_20250514, CLAUDE_4_5_SONNET, CLAUDE_4_5_SONNET_20250929, CLAUDE_4_6_SONNET, CLAUDE_4_6_SONNET_20260217, CLAUDE_4_6_SONNET_1_M, CLAUDE_4_6_SONNET_1_M_20260217, CLAUDE_4_5_OPUS, CLAUDE_4_5_OPUS_20251101, CLAUDE_4_6_OPUS, CLAUDE_4_6_OPUS_20260205, CLAUDE_4_6_OPUS_1_M, CLAUDE_4_6_OPUS_1_M_20260205, CLAUDE_4_OPUS, CLAUDE_4_OPUS_20250514, CLAUDE_4_1_OPUS, CLAUDE_4_1_OPUS_20250805, CLAUDE_4_5_HAIKU, CLAUDE_4_5_HAIKU_20251001, CUSTOM`

### TwelveLabsSegmentationMethods
`DYNAMIC, FIXED`

### TimedPolicyRecurrenceTypes
`ONCE, REPEAT, MONITOR`

### ElevenLabsModels
`MULTILINGUAL_V1, MULTILINGUAL_V2, ENGLISH_V1, FLASH_V2, FLASH_V2_5, TURBO_V2, TURBO_V2_5`

### BlobListingTypes
`PAST, NEW`

### AttioFeedAuthenticationTypes
`API_KEY, ACCESS_TOKEN, CONNECTOR`

### GroqModels
`LLAMA_4_MAVERICK_17B, LLAMA_4_SCOUT_17B, DEEPSEEK_R1_LLAMA_70B_PREVIEW, MIXTRAL_8X7B_INSTRUCT, LLAMA_3_3_70B, LLAMA_3_2_90B_VISION_PREVIEW, LLAMA_3_2_11B_VISION_PREVIEW, LLAMA_3_2_3B_PREVIEW, LLAMA_3_2_1B_PREVIEW, LLAMA_3_1_8B, LLAMA_3_70B, LLAMA_3_8B, KIMI_K2_32B, QWEN_3_32B, CUSTOM`

### OrderByTypes
`NAME, CREATION_DATE, ORIGINAL_DATE, RELEVANCE`

### OpenAIVideoModels
`SORA_2, SORA_2_PRO, CUSTOM`

### ConnectorTypes
`INTEGRATION, AUTHENTICATION, SITE`

### ModelTypes
`COMPLETION, TEXT_EMBEDDING, IMAGE_EMBEDDING, MULTIMODAL_EMBEDDING, RERANKING`

### AssemblyAIModels
`BEST, NANO`

### FileTypes
`VIDEO, AUDIO, IMAGE, ANIMATION, DOCUMENT, EMAIL, CODE, DATA, PACKAGE, SHAPE, POINT_CLOUD, GEOMETRY, DRAWING, SUBTITLES, MANIFEST, UNKNOWN`

### DeepgramModels
`NOVA3_MEDICAL, NOVA3, NOVA2, NOVA2_MEETING, NOVA2_PHONECALL, NOVA2_VOICEMAIL, NOVA2_FINANCE, NOVA2_CONVERSATIONAL_AI, NOVA2_VIDEO, NOVA2_MEDICAL, NOVA2_DRIVETHRU, NOVA2_AUTOMOTIVE, WHISPER_TINY, WHISPER_SMALL, WHISPER_BASE, WHISPER_MEDIUM, WHISPER_LARGE`

### MedicalContraindicationFacetTypes
`CREATION_DATE`

### MCPServerTypes
`REMOTE_SSE, REMOTE_HTTP, LOCAL_NPX`

### MailPriority
`NORMAL, LOW, HIGH`

### ConversationTypes
`CONTENT`

### OpenAIImageModels
`GPT_IMAGE_1, GPT_IMAGE_1_MINI, GPT_IMAGE_1_5, CUSTOM`

### SummarizationTypes
`SUMMARY, KEYWORDS, BULLETS, HEADLINES, POSTS, CHAPTERS, QUESTIONS, QUOTES, GEOTAG, CUSTOM`

### OrderDirectionTypes
`ASCENDING, DESCENDING`

### CalendarEventVisibility
`DEFAULT, PUBLIC, PRIVATE, CONFIDENTIAL`

### MedicalDeviceFacetTypes
`CREATION_DATE`

### OperationTypes
`QUERY, MUTATION`

### SpecificationTypes
`COMPLETION, AGENTIC, TEXT_EMBEDDING, IMAGE_EMBEDDING, EXTRACTION, CLASSIFICATION, SUMMARIZATION, PREPARATION, MULTIMODAL_EMBEDDING`

### CalendarEventStatus
`CONFIRMED, TENTATIVE, CANCELLED`

### MetadataTypes
`CONTENT, CONVERSATION`

### VoyageModels
`VOYAGE, VOYAGE_3_5, VOYAGE_3_5_LITE, VOYAGE_3_0_LARGE, VOYAGE_3_0, VOYAGE_LITE_3_0, VOYAGE_CODE_3_0, VOYAGE_FINANCE_2_0, VOYAGE_MULTILINGUAL_2_0, VOYAGE_LAW_2_0, VOYAGE_CODE_2_0, CUSTOM`

### AlertTypes
`PROMPT`

### MeetingContentTypes
`TRANSCRIPT, RECORDING, PREFERRED`

### SalesforceAuthenticationTypes
`USER, CONNECTOR`

### ContentTypes
`FILE, PAGE, MESSAGE, TEXT, POST, EMAIL, EVENT, ISSUE, PULL_REQUEST, COMMIT, MEMORY, TRANSCRIPT`

### EntityExtractionServiceTypes
`MODEL_TEXT, MODEL_IMAGE, OPEN_AI_IMAGE, AZURE_COGNITIVE_SERVICES_IMAGE, AZURE_COGNITIVE_SERVICES_TEXT, HUME_EMOTION`

### TwitterListingTypes
`POSTS, MENTIONS, RECENT_SEARCH`

### RenditionTypes
`CONTENT`

### ConversationRoleTypes
`SYSTEM, ASSISTANT, USER, TOOL`

### GoogleCalendarAuthenticationTypes
`USER, CONNECTOR`

### MailImportance
`NORMAL, LOW, HIGH`

### GitHubIssueAuthenticationTypes
`PERSONAL_ACCESS_TOKEN, O_AUTH, CONNECTOR`

### SalesforceIssueAuthenticationTypes
`USER, CONNECTOR`

### FeedListingTypes
`PAST, NEW`

### HubSpotAuthenticationTypes
`USER, PRIVATE_APP, CONNECTOR`

### HubSpotIssueAuthenticationTypes
`USER, PRIVATE_APP, CONNECTOR`

### NotionAuthenticationTypes
`TOKEN, CONNECTOR`

### SalesforceFeedAuthenticationTypes
`USER, CONNECTOR`

### GoogleVideoModels
`VEO_3, VEO_3_FAST, VEO_3_1_PREVIEW, VEO_3_1_FAST_PREVIEW, CUSTOM`

### MedicalIndicationFacetTypes
`CREATION_DATE`

### ViewTypes
`CONTENT`

### RepoFacetTypes
`CREATION_DATE`

### GustoAuthenticationTypes
`USER, CONNECTOR`

### BedrockModels
`LLAMA_4_MAVERICK_17B, LLAMA_4_SCOUT_17B, CLAUDE_3_7_SONNET, NOVA_PREMIER, NOVA_PRO, CUSTOM`

### AzureDocumentIntelligenceVersions
`V2023_07_31, V2024_02_29_PREVIEW, V2024_07_31_PREVIEW, V2024_11_30`

### ArcadeProviders
`GOOGLE, GIT_HUB, MICROSOFT`

### LabelFacetTypes
`CREATION_DATE`

### ContentFacetTypes
`CREATION_DATE, ORIGINAL_DATE, OBSERVABLE, CONTENT_TYPE, FILE_TYPE, FORMAT, FORMAT_NAME, FILE_EXTENSION, FILE_SIZE, DEVICE_TYPE, IMAGE_MAKE, IMAGE_MODEL, IMAGE_SOFTWARE, AUDIO_AUTHOR, AUDIO_SERIES, AUDIO_PUBLISHER, VIDEO_MAKE, VIDEO_MODEL, VIDEO_SOFTWARE, DOCUMENT_AUTHOR, DOCUMENT_PUBLISHER, DOCUMENT_IS_ENCRYPTED, DOCUMENT_HAS_DIGITAL_SIGNATURE, EMAIL_PRIORITY, EMAIL_SENSITIVITY, ISSUE_PROJECT, ISSUE_TEAM, ISSUE_PRIORITY, ISSUE_STATUS, ISSUE_TYPE`

### RegexSourceTypes
`MARKDOWN, METADATA`

### OccurrenceTypes
`IMAGE, TIME, TEXT, TURN`

### InvestmentFundFacetTypes
`CREATION_DATE`

### ElevenLabsScribeModels
`SCRIBE_V1, SCRIBE_V2`

### EmailListingTypes
`PAST, NEW`

### BambooHRAuthenticationTypes
`API_KEY`

### ResourceConnectorTypes
`AMAZON, AZURE, GOOGLE`

### DistributionServiceTypes
`NOTION, GOOGLE_DRIVE, ONE_DRIVE, CONFLUENCE, SLACK, GMAIL, MICROSOFT_OUTLOOK, HUB_SPOT, SALESFORCE, ATTIO, GOOGLE_CALENDAR, MICROSOFT_CALENDAR, LINEAR, JIRA, GOOGLE_DOCS, MICROSOFT_WORD, SHARE_POINT, DISCORD, MICROSOFT_TEAMS, TWITTER, GIT_HUB, ATTIO_TASKS`

### ReductoExtractionModes
`OCR, METADATA, HYBRID`

### MedicalConditionFacetTypes
`CREATION_DATE`

### EntityState
`INITIALIZED, RESTARTED, CREATED, INGESTED, INDEXED, PREPARED, SANITIZED, EXTRACTED, ENRICHED, CLASSIFIED, CHANGED, ARCHIVED, APPROVED, REJECTED, PENDING, QUEUED, OPENED, CLOSED, FINISHED, PAUSED, RUNNING, SUBSCRIBED, ERRORED, ENABLED, RESOLVED, DISABLED, DELETED`

### GitHubPullRequestAuthenticationTypes
`PERSONAL_ACCESS_TOKEN, O_AUTH, CONNECTOR`

### TextRoles
`PAGE_HEADER, PAGE_FOOTER, PAGE_NUMBER, TITLE, SECTION_HEADING, FOOTNOTE, CODE, LIST_ITEM, HEADING1, HEADING2, HEADING3, HEADING4, HEADING5, HEADING6, TABLE_COLUMN_HEADER, TABLE_ROW_HEADER, TABLE_CORNER_HEADER, TABLE_CELL, TABLE_CAPTION, TABLE_HEADER, TABLE, IMAGE, IMAGE_CAPTION, FIGURE, FIGURE_CAPTION, BUTTON, DIAGRAM, DIAGRAM_CAPTION, WATERMARK, EQUATION, PARAGRAPH, CHECKBOX, RADIO_BUTTON, COLUMN_HEADER, ROW_HEADER, CORNER_HEADER`

### YouTubeTypes
`VIDEO, VIDEOS, PLAYLIST, CHANNEL`

### NotionTypes
`PAGE, DATABASE`

### PromptStrategyTypes
`OPTIMIZE_SEARCH, REWRITE, NONE`

### ReductoOcrModes
`STANDARD, AGENTIC`

### ConfluenceTypes
`SPACE, PAGE`

### EmbeddingTypes
`TEXT, IMAGE, AUDIO, VIDEO, MULTIMODAL`

### MedicalTestFacetTypes
`CREATION_DATE`

### ReductoOcrSystems
`HIGHRES, MULTILINGUAL, COMBINED`

### SoftwareFacetTypes
`CREATION_DATE`

### MailSensitivity
`NONE, NORMAL, PERSONAL, PRIVATE, COMPANY_CONFIDENTIAL`

### MedicalStudyFacetTypes
`CREATION_DATE`

### SdkTypes
`DOTNET, PYTHON, NODE_JS`

### GoogleThinkingLevels
`MINIMAL, LOW, MEDIUM, HIGH`

### SearchTypes
`KEYWORD, VECTOR, HYBRID`

### MedicalTherapyFacetTypes
`CREATION_DATE`

### FacetValueTypes
`VALUE, RANGE, OBJECT`

### ZendeskIssueAuthenticationTypes
`ACCESS_TOKEN, CONNECTOR`

### ReductoEnrichmentModes
`STANDARD, PAGE, TABLE`

### TrelloTypes
`CARD, BOARD`

### ContentPublishingServiceTypes
`ELEVEN_LABS_AUDIO, OPEN_AI_IMAGE, GOOGLE_IMAGE, OPEN_AI_VIDEO, GOOGLE_VIDEO, TEXT, PARALLEL_RESEARCH`

### StorageGateTypes
`MODEL, WEBHOOK`

### ParallelProcessors
`LITE, BASE, CORE, CORE2X, PRO, ULTRA, ULTRA2X, ULTRA4X, ULTRA8X, LITE_FAST, BASE_FAST, CORE_FAST, CORE2X_FAST, PRO_FAST, ULTRA_FAST, ULTRA2X_FAST, ULTRA4X_FAST, ULTRA8X_FAST`

### ObservableTypes
`CATEGORY, LABEL, EMOTION, EVENT, INVESTMENT, INVESTMENT_FUND, ORGANIZATION, PERSON, PLACE, PRODUCT, REPO, SOFTWARE, MEDICAL_STUDY, MEDICAL_CONDITION, MEDICAL_GUIDELINE, MEDICAL_DRUG, MEDICAL_DRUG_CLASS, MEDICAL_INDICATION, MEDICAL_CONTRAINDICATION, MEDICAL_TEST, MEDICAL_DEVICE, MEDICAL_THERAPY, MEDICAL_PROCEDURE`

### CalendarReminderMethod
`EMAIL, POPUP, SMS`

### MedicalDrugClassFacetTypes
`CREATION_DATE`

### GitHubCommitAuthenticationTypes
`PERSONAL_ACCESS_TOKEN, O_AUTH, CONNECTOR`

### EmotionFacetTypes
`CREATION_DATE`

### EntityTypes
`ACTIVITY, ALERT, CATEGORY, COLLECTION, CONNECTOR, CONTENT, CONVERSATION, EVENT, FACT, FEED, INVESTMENT, INVESTMENT_FUND, JOB, LABEL, EMOTION, METADATA, MEDICAL_STUDY, MEDICAL_CONDITION, MEDICAL_GUIDELINE, MEDICAL_DRUG, MEDICAL_DRUG_CLASS, MEDICAL_INDICATION, MEDICAL_CONTRAINDICATION, MEDICAL_TEST, MEDICAL_DEVICE, MEDICAL_THERAPY, MEDICAL_PROCEDURE, OBSERVATION, ORGANIZATION, PERSON, PERSONA, PLACE, PRODUCT, PROJECT, RENDITION, REPO, SITE, SOFTWARE, SPECIFICATION, USER, VIEW, WORKFLOW`

### ConversationSearchTypes
`NONE, VECTOR, HYBRID`

### EventFacetTypes
`CREATION_DATE`

### ZendeskAuthenticationTypes
`ACCESS_TOKEN, CONNECTOR`

### EntityResolutionStrategyTypes
`NONE, AUTOMATIC`

### AttioMeetingAuthenticationTypes
`API_KEY, ACCESS_TOKEN, CONNECTOR`

### OpenAIModels
`GPT35_TURBO, GPT35_TURBO_0613, GPT35_TURBO_16K, GPT35_TURBO_16K_0613, GPT35_TURBO_16K_1106, GPT35_TURBO_16K_0125, GPT4, GPT4_0613, GPT4_TURBO_VISION_128K, GPT4_TURBO_VISION_128K_1106, GPT4_32K, GPT4_32K_0613, GPT4_TURBO_128K, GPT4_TURBO_128K_1106, GPT4_TURBO_128K_0125, GPT4_TURBO_128K_20240409, GPT4O_128K_20240513, GPT4O_128K_20240806, GPT4O_128K_20241120, GPT4O_128K, GPT4O_MINI_128K_20240718, GPT4O_MINI_128K, GPT4O_CHAT_128K, GPT41_NANO_1024K, GPT41_NANO_1024K_20250414, GPT41_MINI_1024K, GPT41_MINI_1024K_20250414, GPT41_1024K, GPT41_1024K_20250414, GPT45_PREVIEW_128K, GPT45_PREVIEW_128K_20250227, GPT5_CHAT_400K, GPT5_NANO_400K, GPT5_NANO_400K_20250807, GPT5_MINI_400K, GPT5_MINI_400K_20250807, GPT5_400K, GPT5_400K_20250807, GPT51_400K, GPT51_400K_20251113, GPT52_400K, GPT52_400K_20251211, O1_MINI_128K, O1_MINI_128K_20240912, O1_PREVIEW_128K, O1_PREVIEW_128K_20240912, O1_200K, O1_200K_20241217, O3_MINI_200K, O3_MINI_200K_20250131, O3_200K, O3_200K_20250416, O4_MINI_200K, O4_MINI_200K_20250416, ADA_002, EMBEDDING_3_SMALL, EMBEDDING_3_LARGE, CUSTOM`

### FeedServiceTypes
`GOOGLE_BLOB, S3_BLOB, AZURE_BLOB, AZURE_FILE, SHARE_POINT, ONE_DRIVE, GOOGLE_DRIVE, DROPBOX, BOX, GOOGLE_EMAIL, MICROSOFT_EMAIL, ATLASSIAN_JIRA, ATLASSIAN_CONFLUENCE, TRELLO, LINEAR, GIT_HUB_ISSUES, GIT_HUB_PULL_REQUESTS, GIT_HUB_COMMITS, GIT_HUB, INTERCOM_ARTICLES, ZENDESK_ARTICLES, INTERCOM_TICKETS, ZENDESK_TICKETS, GOOGLE_CALENDAR, MICROSOFT_CALENDAR, GOOGLE_CONTACTS, MICROSOFT_CONTACTS, ATTIO_OBJECTS, ATTIO_TASKS, ATTIO_NOTES, SALESFORCE_OBJECTS, SALESFORCE_TASKS, SALESFORCE_NOTES, HUB_SPOT_OBJECTS, HUB_SPOT_TASKS, HUB_SPOT_TICKETS, ASANA, MONDAY, HUB_SPOT_NOTES, HUB_SPOT_MEETING, HUB_SPOT_CONVERSATIONS, FIREFLIES, ATTIO_MEETING, FATHOM, KRISP, SALESFORCE_ECI, PARALLEL, BAMBOO_HR, GUSTO_HRIS, INTERCOM_CONVERSATIONS`

### TextTypes
`PLAIN, MARKDOWN, HTML`

### SearchServiceTypes
`PARALLEL, TAVILY, EXA, EXA_CODE, PERPLEXITY, PODSCAN`

### FeedSyncMode
`ARCHIVE, MIRROR`

### FilePreparationServiceTypes
`AZURE_DOCUMENT_INTELLIGENCE, DEEPGRAM, DOCUMENT, EMAIL, PAGE, REDUCTO_DOCUMENT, MODEL_DOCUMENT, ASSEMBLY_AI, MISTRAL_DOCUMENT, ELEVEN_LABS_SCRIBE`

### GitHubRepositorySortTypes
`ALPHABETICAL, RANKED`

### UserTypes
`HUMAN, AGENT`

### CalendarAttendeeResponseStatus
`NEEDS_ACTION, DECLINED, TENTATIVE, ACCEPTED`

### SearchQueryTypes
`SIMPLE, FULL`

### OrganizationFacetTypes
`CREATION_DATE`

### OpenAIReasoningEffortLevels
`MINIMAL, LOW, MEDIUM, HIGH`

### MistralModels
`MIXTRAL_8X7B_INSTRUCT, MISTRAL_NEMO, MISTRAL_SMALL, MISTRAL_MEDIUM, MISTRAL_LARGE, PIXTRAL_12B_2409, PIXTRAL_LARGE, MISTRAL_EMBED, CUSTOM`

### StorageGateRejectionActions
`DELETE, REJECT`

### ImageProjectionTypes
`EQUIRECTANGULAR, CYLINDRICAL`

### HubSpotFeedAuthenticationTypes
`USER, PRIVATE_APP, CONNECTOR`

### IntegrationServiceTypes
`SLACK, WEB_HOOK, EMAIL, TWITTER, MCP`

### CerebrasModels
`LLAMA_4_SCOUT_17B, LLAMA_3_3_70B, LLAMA_3_1_8B, QWEN_3_32B, CUSTOM`

### IntercomIssueAuthenticationTypes
`ACCESS_TOKEN, CONNECTOR`

### CohereModels
`EMBED_ENGLISH_3_0, EMBED_MULTILINGUAL_3_0, COMMAND_R, COMMAND_R_202403, COMMAND_R_202408, COMMAND_R_PLUS, COMMAND_R_PLUS_202404, COMMAND_R_PLUS_202408, COMMAND_R7_B_202412, COMMAND_A, COMMAND_A_202503, CUSTOM`

### SharePointAuthenticationTypes
`APPLICATION, USER, CONNECTOR`

### ConversationStrategyTypes
`WINDOWED, SUMMARIZED`

### AsanaAuthenticationTypes
`PERSONAL_ACCESS_TOKEN, O_AUTH`

### MicrosoftEmailAuthenticationTypes
`USER, CONNECTOR`

### EnvironmentTypes
`DEVELOPMENT, PRODUCTION`

### ExaSearchTypes
`AUTO, INSTANT, FAST, DEEP, NEURAL`

### GoogleContactsAuthenticationTypes
`USER, CONNECTOR`

### CalendarRecurrencePattern
`DAILY, WEEKLY, MONTHLY, YEARLY`

### RelationshipDirections
`INCOMING, OUTGOING`

### ModelServiceTypes
`GOOGLE, ANTHROPIC, AZURE_AI, AZURE_OPEN_AI, OPEN_AI, REPLICATE, GROQ, CEREBRAS, MISTRAL, COHERE, DEEPSEEK, JINA, VOYAGE, BEDROCK, XAI, TWELVE_LABS`

### MicrosoftCalendarAuthenticationTypes
`USER, CONNECTOR`

### ReplicateModels
`MISTRAL_7B, MISTRAL_7B_INSTRUCT, LLAMA_2_7B, LLAMA_2_13B, LLAMA_2_70B, LLAMA_2_7B_CHAT, LLAMA_2_13B_CHAT, LLAMA_2_70B_CHAT, CUSTOM`

### SiteTypes
`WATCH, SWEEP, STORAGE`

### ExtractionTypes
`ENTITIES, FACTS`

### TimeIntervalTypes
`MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR`

### OrientationTypes
`TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT, LEFT_TOP, RIGHT_TOP, RIGHT_BOTTOM, LEFT_BOTTOM`

### ProductFacetTypes
`CREATION_DATE`

### FilterMode
`ANY, ONLY, ALL`

### OAuthProviders
`DROPBOX, BOX, GOOGLE, MICROSOFT, GIT_HUB, SLACK, HUB_SPOT, NOTION, ATLASSIAN, INTERCOM, ZENDESK, ATTIO, SALESFORCE, LINEAR, TWITTER`

### ConfluenceAuthenticationTypes
`TOKEN, CONNECTOR`

### UnitTypes
`KILOMETER, METER, CENTIMETER, MILLIMETER, MICROMETER, NANOMETER, ANGSTROM, DECIMETER, DECAMETER, HECTOMETER, GIGAMETER, ASTRONOMICAL_UNIT, LIGHT_YEAR, PARSEC, MILE, YARD, FOOT, INCH, MIL, MICRO_INCH, CUSTOM, UNITLESS`

### ParallelGenerators
`BASE, CORE, PRO`

### AttioIssueAuthenticationTypes
`API_KEY, ACCESS_TOKEN, CONNECTOR`

### ContentIndexingServiceTypes
`AZURE_AI_LANGUAGE`

### MicrosoftContactsAuthenticationTypes
`USER, CONNECTOR`

### CategoryFacetTypes
`CREATION_DATE`

### PersonFacetTypes
`CREATION_DATE`

### VideoAspectRatioTypes
`LANDSCAPE_16X9, PORTRAIT_9X16`

### StoragePolicyTypes
`ARCHIVE, MINIMIZE`

### TwelveLabsEmbeddingOptions
`VISUAL, AUDIO, TRANSCRIPTION`

### CalendarListingTypes
`PAST, NEW`

### EntityEnrichmentServiceTypes
`PARALLEL, DIFFBOT, WIKIPEDIA, CRUNCHBASE, FHIR, RADAR`

### DeviceTypes
`DRONE, ROBOT, MOBILE, CAMERA, STREAM, SCREEN, GEOSPATIAL, UNKNOWN`

### VideoSizeTypes
`HD_PORTRAIT, HD_LANDSCAPE, FULL_HD_PORTRAIT, FULL_HD_LANDSCAPE`

### ContentClassificationServiceTypes
`REGEX, MODEL`

### BoxAuthenticationTypes
`USER, CONNECTOR`

### ContentSourceTypes
`FRAME, DOCUMENT, TRANSCRIPT`

### GoogleModels
`GEMINI_2_5_PRO, GEMINI_2_5_PRO_PREVIEW, GEMINI_2_5_PRO_EXPERIMENTAL, GEMINI_3_PRO_PREVIEW, GEMINI_3_1_PRO_PREVIEW, GEMINI_3_FLASH_PREVIEW, GEMINI_2_5_FLASH, GEMINI_FLASH_LATEST, GEMINI_2_5_FLASH_PREVIEW, GEMINI_2_5_FLASH_LITE, GEMINI_FLASH_LITE_LATEST, GEMINI_2_0_PRO_EXPERIMENTAL, GEMINI_2_0_FLASH_THINKING_EXPERIMENTAL, GEMINI_2_0_FLASH_EXPERIMENTAL, GEMINI_2_0_FLASH, GEMINI_2_0_FLASH_001, GEMINI_1_5_FLASH_8B, GEMINI_1_5_FLASH_8B_001, GEMINI_1_5_FLASH, GEMINI_1_5_FLASH_001, GEMINI_1_5_PRO, GEMINI_1_5_PRO_001, GEMINI_1_5_FLASH_002, GEMINI_1_5_PRO_002, EMBEDDING_004, GEMINI_EMBEDDING_001, CUSTOM`

### ApplyPolicy
`BEFORE_RESOLVER, AFTER_RESOLVER, VALIDATION`

### FeedConnectorTypes
`GOOGLE, AMAZON, AZURE, SHARE_POINT, ONE_DRIVE, GOOGLE_DRIVE, DROPBOX, BOX, GOOGLE_EMAIL, MICROSOFT_EMAIL, ATLASSIAN, LINEAR, GIT_HUB, INTERCOM, ZENDESK, GOOGLE_CALENDAR, MICROSOFT_CALENDAR, GOOGLE_CONTACTS, MICROSOFT_CONTACTS, ATTIO, SALESFORCE, HUB_SPOT, ASANA, MONDAY, FIREFLIES, ATTIO_MEETING, FATHOM, KRISP, SALESFORCE_ECI, PARALLEL, BAMBOO_HR, GUSTO`

### BillableMetrics
`BYTES, TOKENS, LENGTH, TIME, UNITS, COST, REQUESTS, CREDITS`

### TwelveLabsEmbeddingScopes
`CLIP, ASSET`

### JiraAuthenticationTypes
`TOKEN, CONNECTOR`

### IntercomConversationsAuthenticationTypes
`ACCESS_TOKEN, CONNECTOR`

### GoogleImageModels
`GEMINI_2_5_FLASH_IMAGE_PREVIEW, GEMINI_3_PRO_IMAGE_PREVIEW, CUSTOM`

### XAIModels
`GROK_4, GROK_3, GROK_3_MINI, CUSTOM`
