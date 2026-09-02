import random
from datetime import datetime

from aaa.domain.loader import DomainConfig


def generate_cases(
    config: DomainConfig,
    n: int,
    seed: int,
    generated_at: datetime,
):

    rng = random.Random(seed)

    cases = []

    for _ in range(n):

        case_type = rng.choices(
            population=[c.name for c in config.case_types],
            weights=[c.weight for c in config.case_types],
            k=1,
        )[0]

        case = {
            "case_id": f"case_{rng.getrandbits(48):012x}",
            "case_type": case_type,
            "generated_at": generated_at.isoformat(),
            "claim_value_gbp": rng.randint(200, 25000),
            "customer_tenure_months": rng.randint(1, 240),
            "region": rng.choice(
                [
                    "north",
                    "midlands",
                    "south_east",
                    "south_west",
                    "scotland",
                    "wales",
                ]
            ),
            "channel": rng.choice(
                [
                    "phone",
                    "web",
                    "app",
                ]
            ),
            "prior_claims_count": rng.randint(0, 4),
        }

        cases.append(case)

    return cases