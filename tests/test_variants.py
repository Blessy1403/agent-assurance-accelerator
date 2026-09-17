import random

from aaa.data.variants import (
    swap_enum,
    shift_range,
    cross_threshold,
    paraphrase_template,
    remove_key_document,
)


def test_swap_enum_changes_value():

    rng = random.Random(42)

    base = {
        "region": "midlands"
    }

    variant = swap_enum(
        base,
        "region",
        [
            "north",
            "midlands",
            "scotland",
        ],
        rng,
    )

    assert variant["region"] != "midlands"


def test_shift_range_changes_value():

    rng = random.Random(42)

    base = {
        "customer_tenure_months": 24
    }

    variant = shift_range(
        base,
        "customer_tenure_months",
        1,
        240,
        rng,
    )

    assert variant["customer_tenure_months"] != 24


def test_cross_threshold_changes_side():

    base = {
        "claim_value_gbp": 5000
    }

    variant = cross_threshold(
        base,
        "claim_value_gbp",
        10000,
    )

    assert variant["claim_value_gbp"] > 10000

def test_paraphrase_template_changes_text():

    rng = random.Random(42)

    base = {
        "incident_description":
            "Vehicle damaged in parking lot"
    }

    variant = paraphrase_template(
        base,
        "incident_description",
        [
            "Vehicle damaged in parking lot",
            "Car was damaged while parked",
            "Damage occurred to parked vehicle",
        ],
        rng,
    )

    assert (
        variant["incident_description"]
        !=
        base["incident_description"]
    )

def test_remove_key_document_removes_document():

    base = {
        "documents_provided": [
            "police_report",
            "repair_invoice",
        ]
    }

    variant = remove_key_document(
        base,
        "documents_provided",
        [
            "police_report",
            "repair_invoice",
        ],
    )

    assert len(
        variant["documents_provided"]
    ) == 1

    assert (
        "police_report"
        not in variant["documents_provided"]
    )