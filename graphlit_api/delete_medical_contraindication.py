# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalContraindication(BaseModel):
    delete_medical_contraindication: Optional[
        "DeleteMedicalContraindicationDeleteMedicalContraindication"
    ] = Field(alias="deleteMedicalContraindication")


class DeleteMedicalContraindicationDeleteMedicalContraindication(BaseModel):
    id: str
    state: EntityState


DeleteMedicalContraindication.model_rebuild()
