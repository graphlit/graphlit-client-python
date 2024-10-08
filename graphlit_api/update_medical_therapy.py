# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateMedicalTherapy(BaseModel):
    update_medical_therapy: Optional["UpdateMedicalTherapyUpdateMedicalTherapy"] = (
        Field(alias="updateMedicalTherapy")
    )


class UpdateMedicalTherapyUpdateMedicalTherapy(BaseModel):
    id: str
    name: str


UpdateMedicalTherapy.model_rebuild()
