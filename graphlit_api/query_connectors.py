# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ArcadeProviders,
    AuthenticationServiceTypes,
    ConnectorTypes,
    EntityState,
    IntegrationServiceTypes,
    MCPServerTypes,
    OAuthProviders,
)


class QueryConnectors(BaseModel):
    connectors: Optional["QueryConnectorsConnectors"]


class QueryConnectorsConnectors(BaseModel):
    results: Optional[List["QueryConnectorsConnectorsResults"]]


class QueryConnectorsConnectorsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "QueryConnectorsConnectorsResultsOwner"
    state: EntityState
    type: Optional[ConnectorTypes]
    authentication: Optional["QueryConnectorsConnectorsResultsAuthentication"]
    integration: Optional["QueryConnectorsConnectorsResultsIntegration"]


class QueryConnectorsConnectorsResultsOwner(BaseModel):
    id: str


class QueryConnectorsConnectorsResultsAuthentication(BaseModel):
    type: AuthenticationServiceTypes
    microsoft: Optional["QueryConnectorsConnectorsResultsAuthenticationMicrosoft"]
    google: Optional["QueryConnectorsConnectorsResultsAuthenticationGoogle"]
    oauth: Optional["QueryConnectorsConnectorsResultsAuthenticationOauth"]
    arcade: Optional["QueryConnectorsConnectorsResultsAuthenticationArcade"]


class QueryConnectorsConnectorsResultsAuthenticationMicrosoft(BaseModel):
    tenant_id: str = Field(alias="tenantId")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class QueryConnectorsConnectorsResultsAuthenticationGoogle(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class QueryConnectorsConnectorsResultsAuthenticationOauth(BaseModel):
    refresh_token: str = Field(alias="refreshToken")
    provider: OAuthProviders
    metadata: Optional[str]


class QueryConnectorsConnectorsResultsAuthenticationArcade(BaseModel):
    authorization_id: str = Field(alias="authorizationId")
    provider: ArcadeProviders
    metadata: Optional[str]


class QueryConnectorsConnectorsResultsIntegration(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["QueryConnectorsConnectorsResultsIntegrationSlack"]
    email: Optional["QueryConnectorsConnectorsResultsIntegrationEmail"]
    twitter: Optional["QueryConnectorsConnectorsResultsIntegrationTwitter"]
    mcp: Optional["QueryConnectorsConnectorsResultsIntegrationMcp"]


class QueryConnectorsConnectorsResultsIntegrationSlack(BaseModel):
    token: str
    channel: str


class QueryConnectorsConnectorsResultsIntegrationEmail(BaseModel):
    from_: str = Field(alias="from")
    subject: str
    to: List[str]


class QueryConnectorsConnectorsResultsIntegrationTwitter(BaseModel):
    consumer_key: str = Field(alias="consumerKey")
    consumer_secret: str = Field(alias="consumerSecret")
    access_token_key: str = Field(alias="accessTokenKey")
    access_token_secret: str = Field(alias="accessTokenSecret")


class QueryConnectorsConnectorsResultsIntegrationMcp(BaseModel):
    token: Optional[str]
    type: MCPServerTypes


QueryConnectors.model_rebuild()
QueryConnectorsConnectors.model_rebuild()
QueryConnectorsConnectorsResults.model_rebuild()
QueryConnectorsConnectorsResultsAuthentication.model_rebuild()
QueryConnectorsConnectorsResultsIntegration.model_rebuild()
