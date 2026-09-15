import random

from aaa.data.variants import (
    swap_enum,
    shift_range,
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

    assert (
        variant["customer_tenure_months"]
        != 24
    )