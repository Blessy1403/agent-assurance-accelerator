import copy


def swap_enum(
    base_case,
    field_name,
    allowed_values,
    rng,
):
    variant = copy.deepcopy(base_case)

    current_value = variant[field_name]

    choices = [
        value
        for value in allowed_values
        if value != current_value
    ]

    variant[field_name] = rng.choice(choices)

    return variant


def shift_range(
    base_case,
    field_name,
    min_value,
    max_value,
    rng,
):
    variant = copy.deepcopy(base_case)

    current_value = variant[field_name]

    new_value = current_value

    while new_value == current_value:
        new_value = rng.randint(
            min_value,
            max_value,
        )

    variant[field_name] = new_value

    return variant