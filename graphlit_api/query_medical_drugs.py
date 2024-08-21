# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMedicalDrugs(BaseModel):
    medical_drugs: Optional["QueryMedicalDrugsMedicalDrugs"] = Field(
        alias="medicalDrugs"
    )


class QueryMedicalDrugsMedicalDrugs(BaseModel):
    results: Optional[List[Optional["QueryMedicalDrugsMedicalDrugsResults"]]]


class QueryMedicalDrugsMedicalDrugsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    thing: Optional[str]
    relevance: Optional[float]


QueryMedicalDrugs.model_rebuild()
QueryMedicalDrugsMedicalDrugs.model_rebuild()