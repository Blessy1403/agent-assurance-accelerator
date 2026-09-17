from aaa.domain.loader import load_domain_config


def test_valid_config_loads():
    config = load_domain_config(
        "aaa/aaa/domain/insurance.yaml"
    )

    assert config.domain == "insurance_claims"
    assert len(config.case_types) == 3
    assert len(config.varied_attributes) == 6