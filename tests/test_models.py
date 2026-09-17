from datetime import datetime
from datetime import timezone

import pytest

from aaa.models import (
    SyntheticCase,
    TraceEvent,
)


def test_payload_summary_is_truncated():

    event = TraceEvent(
        event_id="evt_001",
        timestamp=datetime.now(timezone.utc),
        sequence_number=1,
        event_type="test",
        payload_summary="a" * 300,
    )

    assert len(event.payload_summary) == 200


def test_generated_at_requires_timezone():

    with pytest.raises(ValueError):

        SyntheticCase(
            case_id="case_001",
            case_type="motor",
            generated_at=datetime.now(),
            claim_value_gbp=5000,
            customer_tenure_months=24,
            region="midlands",
            channel="web",
            prior_claims_count=0,
        )


def test_timestamp_requires_timezone():

    with pytest.raises(ValueError):

        TraceEvent(
            event_id="evt_001",
            timestamp=datetime.now(),
            sequence_number=1,
            event_type="test",
            payload_summary="hello",
        )


def test_timezone_aware_datetime_is_accepted():

    event = TraceEvent(
        event_id="evt_001",
        timestamp=datetime.now(timezone.utc),
        sequence_number=1,
        event_type="test",
        payload_summary="hello",
    )

    assert event.timestamp.tzinfo is not None