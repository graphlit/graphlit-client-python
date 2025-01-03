# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryPersons(BaseModel):
    persons: Optional["QueryPersonsPersons"]


class QueryPersonsPersons(BaseModel):
    results: Optional[List[Optional["QueryPersonsPersonsResults"]]]


class QueryPersonsPersonsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    thing: Optional[str]
    relevance: Optional[float]
    address: Optional["QueryPersonsPersonsResultsAddress"]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")
    phone_number: Optional[str] = Field(alias="phoneNumber")
    birth_date: Optional[Any] = Field(alias="birthDate")
    title: Optional[str]
    occupation: Optional[str]
    education: Optional[str]


class QueryPersonsPersonsResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


QueryPersons.model_rebuild()
QueryPersonsPersons.model_rebuild()
QueryPersonsPersonsResults.model_rebuild()
