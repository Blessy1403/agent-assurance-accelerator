import random
from datetime import datetime
import json
from pathlib import Path
import argparse


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

def write_jsonl(cases, output_path):
    output_path = Path(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        for case in cases:
            f.write(json.dumps(case) + "\n")

def write_manifest(
    config,
    cases,
    seed,
    generated_at,
    manifest_path,
):
    counts_by_type = {}

    for case in cases:
        case_type = case["case_type"]

        counts_by_type[case_type] = (
            counts_by_type.get(case_type, 0) + 1
        )

    manifest = {
        "generated_at": generated_at.isoformat(),
        "seed": seed,
        "config_domain": config.domain,
        "config_version": config.version,
        "total_cases": len(cases),
        "counts_by_type": counts_by_type,
    }

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)            


def main():
    parser = argparse.ArgumentParser(
        description="Generate synthetic insurance claims dataset"
    )

    parser.add_argument(
        "--n",
        type=int,
        default=100,
        help="Number of cases to generate"
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for deterministic generation"
    )

    parser.add_argument(
        "--out",
        default="data/cases.jsonl",
        help="Output JSONL file path"
    )

    args = parser.parse_args()

    from aaa.domain.loader import load_domain_config

    config = load_domain_config(
    "aaa/domain/insurance.yaml"
)

    generated_at = datetime(2026, 1, 1)

    cases = generate_cases(
        config=config,
        n=args.n,
        seed=args.seed,
        generated_at=generated_at,
    )

    write_jsonl(cases, args.out)

    write_manifest(
        config=config,
        cases=cases,
        seed=args.seed,
        generated_at=generated_at,
        manifest_path="data/generation_manifest.json",
    )

    print(
        f"Generated {len(cases)} cases into {args.out}"
    )


if __name__ == "__main__":
    main()