# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class CountMedicalTests(BaseModel):
    count_medical_tests: Optional["CountMedicalTestsCountMedicalTests"] = Field(
        alias="countMedicalTests"
    )


class CountMedicalTestsCountMedicalTests(BaseModel):
    count: Optional[Any]


CountMedicalTests.model_rebuild()
