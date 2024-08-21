# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalDevice(BaseModel):
    delete_medical_device: Optional["DeleteMedicalDeviceDeleteMedicalDevice"] = Field(
        alias="deleteMedicalDevice"
    )


class DeleteMedicalDeviceDeleteMedicalDevice(BaseModel):
    id: str
    state: EntityState


DeleteMedicalDevice.model_rebuild()