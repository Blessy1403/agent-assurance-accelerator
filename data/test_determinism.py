from datetime import datetime, timezone

from aaa.domain.loader import load_domain_config
from aaa.data.generate_cases import generate_cases, write_jsonl


def test_generation_is_deterministic(tmp_path):

    config = load_domain_config(
        "aaa/aaa/domain/insurance.yaml"
    )

    fixed_time = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    a = tmp_path / "a.jsonl"
    b = tmp_path / "b.jsonl"

    write_jsonl(
        generate_cases(
            config,
            n=50,
            seed=42,
            generated_at=fixed_time,
        ),
        a,
    )

    write_jsonl(
        generate_cases(
            config,
            n=50,
            seed=42,
            generated_at=fixed_time,
        ),
        b,
    )

    assert a.read_bytes() == b.read_bytes()


def test_different_seeds_differ():

    config = load_domain_config(
    "aaa/aaa/domain/insurance.yaml"
)
    fixed_time = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    cases_a = generate_cases(
        config,
        n=50,
        seed=42,
        generated_at=fixed_time,
    )

    cases_b = generate_cases(
        config,
        n=50,
        seed=43,
        generated_at=fixed_time,
    )

    assert cases_a != cases_b


