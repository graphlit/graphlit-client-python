# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllMedicalConditions(BaseModel):
    delete_all_medical_conditions: Optional[
        List[Optional["DeleteAllMedicalConditionsDeleteAllMedicalConditions"]]
    ] = Field(alias="deleteAllMedicalConditions")


class DeleteAllMedicalConditionsDeleteAllMedicalConditions(BaseModel):
    id: str
    state: EntityState


DeleteAllMedicalConditions.model_rebuild()
