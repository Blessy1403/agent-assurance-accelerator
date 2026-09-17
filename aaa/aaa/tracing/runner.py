from typing import Any

from aaa.models import (
    RunSummary,
    SyntheticCase,
)


def run_and_trace(
    case: SyntheticCase,
    backend,
    overrides: dict[str, Any] | None = None,
    parent_run_id: str | None = None,
) -> RunSummary:
    """Run one case through the pipeline, recording a full trace.

    overrides: field values to apply to the case before running.
        Validated against the case schema. Unknown fields are errors.

    parent_run_id: set when this run is a counterfactual re-run.
        The original run is never modified.
    """
    raise NotImplementedError