# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMedicalDevice(BaseModel):
    medical_device: Optional["GetMedicalDeviceMedicalDevice"] = Field(
        alias="medicalDevice"
    )


class GetMedicalDeviceMedicalDevice(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    thing: Optional[str]
    relevance: Optional[float]


GetMedicalDevice.model_rebuild()
