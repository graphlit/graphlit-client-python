# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class CountConnectors(BaseModel):
    count_connectors: Optional["CountConnectorsCountConnectors"] = Field(
        alias="countConnectors"
    )


class CountConnectorsCountConnectors(BaseModel):
    count: Optional[Any]


CountConnectors.model_rebuild()
