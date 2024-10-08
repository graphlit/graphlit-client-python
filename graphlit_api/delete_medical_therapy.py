# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalTherapy(BaseModel):
    delete_medical_therapy: Optional["DeleteMedicalTherapyDeleteMedicalTherapy"] = (
        Field(alias="deleteMedicalTherapy")
    )


class DeleteMedicalTherapyDeleteMedicalTherapy(BaseModel):
    id: str
    state: EntityState


DeleteMedicalTherapy.model_rebuild()
