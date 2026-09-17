# Interface Contract

## SyntheticCase

Represents a generated insurance claim used for assurance testing.

### Fields

| Field | Type |
|---------|---------|
| case_id | str |
| case_type | str |
| generated_at | datetime |
| claim_value_gbp | int |
| customer_tenure_months | int |
| region | str |
| channel | str |
| prior_claims_count | int |

### Example

```json
{
  "case_id": "case_001",
  "case_type": "motor",
  "generated_at": "2026-09-18T09:00:00Z",
  "claim_value_gbp": 5000,
  "customer_tenure_months": 24,
  "region": "midlands",
  "channel": "web",
  "prior_claims_count": 0
}
```
## TraceEvent

Represents a single event captured during pipeline execution.

### Fields

| Field | Type |
|---------|---------|
| event_id | str |
| timestamp | datetime |
| sequence_number | int |
| event_type | str |
| checkpoint_id | str \| null |
| payload_summary | str |

### Example

```json
{
  "event_id": "evt_001",
  "timestamp": "2026-09-18T09:00:00Z",
  "sequence_number": 1,
  "event_type": "validation_started",
  "checkpoint_id": null,
  "payload_summary": "Claim validation started."
}
```
## RunSummary

Summarizes the result of one pipeline execution.

### Fields

| Field | Type |
|---------|---------|
| run_id | str |
| case_id | str |
| parent_run_id | str \| null |
| status | str |
| started_at | datetime |
| completed_at | datetime |
| trace_event_count | int |

### Example

```json
{
  "run_id": "run_001",
  "case_id": "case_001",
  "parent_run_id": null,
  "status": "completed",
  "started_at": "2026-09-18T09:00:00Z",
  "completed_at": "2026-09-18T09:00:05Z",
  "trace_event_count": 4
}
```
## TraceBackend

Planned interface for storing trace events.

### Methods

```python
record_event(event: TraceEvent)
flush()
close()
```
## run_and_trace()
Supports future counterfactual and pair-based evaluation workflows described in ADR-004.



Run one case through the pipeline while recording a complete trace.

### Parameters

| Parameter | Type |
|------------|------------|
| case | SyntheticCase |
| backend | TraceBackend |
| overrides | dict[str, Any] \| null |
| parent_run_id | str \| null |

### Overrides Example

```json
{
  "claim_value_gbp": 20000
}
```

### Rules

- Overrides are validated against the case schema.
- Unknown field names are errors.
- Unknown field names are never silently ignored.
- The original case is never modified.
- parent_run_id is used when a run is a counterfactual re-run of an earlier run.


## JSONL Format

Generated cases are stored as one JSON document per line.

### Example

```json
{"case_id":"case_001"}
{"case_id":"case_002"}
```
## Pair Metadata Semantics

Pair metadata links a variant to its base case.

### Fields

| Field | Meaning |
|---------|---------|
| pair_id | Identifies the pair |
| variant_of | Base case identifier |
| varied_field | Field intentionally changed |
| expected_outcome_change | Whether the outcome is expected to change |

### Example

```json
{
  "pair_id": "pair_001",
  "variant_of": "case_001",
  "varied_field": "region",
  "expected_outcome_change": false
}
```

For additional context see ADR-004 Pair Semantics.