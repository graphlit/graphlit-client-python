# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateMedicalCondition(BaseModel):
    update_medical_condition: Optional[
        "UpdateMedicalConditionUpdateMedicalCondition"
    ] = Field(alias="updateMedicalCondition")


class UpdateMedicalConditionUpdateMedicalCondition(BaseModel):
    id: str
    name: str


UpdateMedicalCondition.model_rebuild()
