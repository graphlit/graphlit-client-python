# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateMedicalContraindication(BaseModel):
    create_medical_contraindication: Optional[
        "CreateMedicalContraindicationCreateMedicalContraindication"
    ] = Field(alias="createMedicalContraindication")


class CreateMedicalContraindicationCreateMedicalContraindication(BaseModel):
    id: str
    name: str


CreateMedicalContraindication.model_rebuild()
