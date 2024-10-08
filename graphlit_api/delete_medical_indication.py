# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalIndication(BaseModel):
    delete_medical_indication: Optional[
        "DeleteMedicalIndicationDeleteMedicalIndication"
    ] = Field(alias="deleteMedicalIndication")


class DeleteMedicalIndicationDeleteMedicalIndication(BaseModel):
    id: str
    state: EntityState


DeleteMedicalIndication.model_rebuild()
