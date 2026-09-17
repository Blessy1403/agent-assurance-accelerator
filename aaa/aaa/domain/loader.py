from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel


class FieldSpec(BaseModel):
    type: Literal["money", "int", "date", "enum", "multi_enum", "text"]
    min: float | None = None
    max: float | None = None
    values: list[str] | None = None
    within_days: int | None = None
    templates: str | None = None


class VariedAttributeSpec(BaseModel):
    field: str
    strategy: Literal[
        "shift_range",
        "swap_enum",
        "cross_threshold",
        "paraphrase_template",
        "remove_key_document",
    ]
    expected_outcome_change: bool
    rationale: str
    threshold: float | None = None


class CaseTypeSpec(BaseModel):
    name: str
    weight: float
    fields: dict[str, FieldSpec]


class DomainConfig(BaseModel):
    domain: str
    version: int
    case_types: list[CaseTypeSpec]
    varied_attributes: list[VariedAttributeSpec]
    outcome_fields: dict[str, str]


def _validate_config(config: DomainConfig) -> None:
    """
    Project-specific validation rules.
    """

    # Rule 1: Weights must sum to approximately 1.0
    total_weight = sum(case.weight for case in config.case_types)

    if abs(total_weight - 1.0) > 0.001:
        raise ValueError(
            f"Case type weights must sum to 1.0, got {total_weight}"
        )

    # Collect all field names
    all_fields = set()

    for case_type in config.case_types:
        for field_name, field_spec in case_type.fields.items():
            all_fields.add(field_name)

            # Rule 2: enum fields must have values
            if field_spec.type == "enum":
                if not field_spec.values:
                    raise ValueError(
                        f"Enum field '{field_name}' must define values"
                    )

    # Rule 3: varied attributes must exist
    for varied in config.varied_attributes:
        if varied.field not in all_fields:
            raise ValueError(
                f"Varied attribute '{varied.field}' does not exist in any case type"
            )

        # Rule 4: cross_threshold must have threshold
        if varied.strategy == "cross_threshold":
            if varied.threshold is None:
                raise ValueError(
                    f"Varied attribute '{varied.field}' uses "
                    f"'cross_threshold' but no threshold is defined"
                )


def load_domain_config(path: str) -> DomainConfig:
    """
    Load insurance.yaml and convert it into a validated
    DomainConfig object.
    """

    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(config_path, "r", encoding="utf-8") as f:
        raw_config = yaml.safe_load(f)

    config = DomainConfig.model_validate(raw_config)

    _validate_config(config)

    return config