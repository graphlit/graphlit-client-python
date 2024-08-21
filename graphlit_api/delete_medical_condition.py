# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalCondition(BaseModel):
    delete_medical_condition: Optional[
        "DeleteMedicalConditionDeleteMedicalCondition"
    ] = Field(alias="deleteMedicalCondition")


class DeleteMedicalConditionDeleteMedicalCondition(BaseModel):
    id: str
    state: EntityState


DeleteMedicalCondition.model_rebuild()