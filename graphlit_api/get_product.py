# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetProduct(BaseModel):
    product: Optional["GetProductProduct"]


class GetProductProduct(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    thing: Optional[str]
    relevance: Optional[float]
    address: Optional["GetProductProductAddress"]
    manufacturer: Optional[str]
    model: Optional[str]
    brand: Optional[str]
    upc: Optional[str]
    sku: Optional[str]
    release_date: Optional[Any] = Field(alias="releaseDate")
    production_date: Optional[Any] = Field(alias="productionDate")


class GetProductProductAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


GetProduct.model_rebuild()
GetProductProduct.model_rebuild()
