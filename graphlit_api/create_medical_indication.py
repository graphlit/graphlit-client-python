# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateMedicalIndication(BaseModel):
    create_medical_indication: Optional[
        "CreateMedicalIndicationCreateMedicalIndication"
    ] = Field(alias="createMedicalIndication")


class CreateMedicalIndicationCreateMedicalIndication(BaseModel):
    id: str
    name: str


CreateMedicalIndication.model_rebuild()
