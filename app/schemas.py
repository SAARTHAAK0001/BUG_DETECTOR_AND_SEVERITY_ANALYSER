from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

Severity = Literal["low", "medium", "high", "critical"]


class BugReportCreate(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=10)


class BugReportResponse(BaseModel):
    id: int
    title: str
    description: str
    predicted_severity: Severity
    model_used: str
    created_at: datetime

    model_config = {"from_attributes": True}


class AnalyzeResponse(BaseModel):
    bug: BugReportResponse
