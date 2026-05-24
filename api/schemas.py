from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

class AssessRequest(BaseModel):
    prompt: str = Field(..., description="The user prompt to analyze.")
    role: str = Field(default="GENERAL", description="The user capability tier.")

class AssessResponse(BaseModel):
    decision: str = Field(..., description="BLOCK, RESTRICT, or ALLOW")
    risk_level: str = Field(..., description="HIGH, MEDIUM, or LOW")
    details: Dict[str, Any] = Field(default_factory=dict, description="Metadata and scores.")
    clean_prompt: str = Field(..., description="Prompt after PII redaction.")
    redacted_items: List[str] = Field(default_factory=list, description="List of redacted PII items.")
    process_time_ms: float = Field(default=0.0, description="Server-side processing latency in milliseconds.")
