# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalTest(BaseModel):
    delete_medical_test: Optional["DeleteMedicalTestDeleteMedicalTest"] = Field(
        alias="deleteMedicalTest"
    )


class DeleteMedicalTestDeleteMedicalTest(BaseModel):
    id: str
    state: EntityState


DeleteMedicalTest.model_rebuild()
