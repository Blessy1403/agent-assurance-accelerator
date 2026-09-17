from datetime import datetime
from pydantic import BaseModel, field_validator

class SyntheticCase(BaseModel):
    """Represents a generated insurance claim used for assurance testing."""
    case_id: str
    case_type: str
    generated_at: datetime
    claim_value_gbp: int
    customer_tenure_months: int
    region: str
    channel: str
    prior_claims_count: int

    @field_validator("generated_at")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        """Ensures generated timestamps include timezone information."""
        if value.tzinfo is None:
            raise ValueError(
                "generated_at must be timezone-aware"
            )
        return value

class TraceEvent(BaseModel):
    """Represents a single event captured during pipeline execution."""

    event_id: str

    # Decision:
    # Store timestamps as timezone-aware UTC values
    # to avoid incorrect duration calculations.
    timestamp: datetime

    # Decision:
    # Assigned by the recorder instead of timestamps.
    sequence_number: int

    event_type: str

    # Decision:
    # Reserved for future replay support.
    checkpoint_id: str | None = None

    # Decision:
    # Truncation is enforced through validation.
    payload_summary: str


    @field_validator("payload_summary")
    @classmethod
    def truncate_payload_summary(cls, value: str) -> str:
         """Ensures payload summaries remain a manageable length."""
         return value[:200]

    @field_validator("timestamp")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        """Ensures event timestamps include timezone information."""
        if value.tzinfo is None:
            raise ValueError(
                "timestamp must be timezone-aware"
            )
        return value
