# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalGuideline(BaseModel):
    delete_medical_guideline: Optional[
        "DeleteMedicalGuidelineDeleteMedicalGuideline"
    ] = Field(alias="deleteMedicalGuideline")


class DeleteMedicalGuidelineDeleteMedicalGuideline(BaseModel):
    id: str
    state: EntityState


DeleteMedicalGuideline.model_rebuild()
