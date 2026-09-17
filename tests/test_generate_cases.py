from datetime import datetime

from aaa.domain.loader import load_domain_config
from aaa.data.generate_cases import generate_cases


def test_generate_50_cases():

    config = load_domain_config(
        "aaa/aaa/domain/insurance.yaml"
    )

    cases = generate_cases(
        config=config,
        n=50,
        seed=42,
        generated_at=datetime(2026, 1, 1)
    )

    assert len(cases) == 50