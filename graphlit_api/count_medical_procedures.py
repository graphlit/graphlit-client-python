# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class CountMedicalProcedures(BaseModel):
    count_medical_procedures: Optional[
        "CountMedicalProceduresCountMedicalProcedures"
    ] = Field(alias="countMedicalProcedures")


class CountMedicalProceduresCountMedicalProcedures(BaseModel):
    count: Optional[Any]


CountMedicalProcedures.model_rebuild()
