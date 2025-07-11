# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ConnectorTypes, EntityState


class CreateConnector(BaseModel):
    create_connector: Optional["CreateConnectorCreateConnector"] = Field(
        alias="createConnector"
    )


class CreateConnectorCreateConnector(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ConnectorTypes]


CreateConnector.model_rebuild()
