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

def cross_threshold(
    base_case,
    field_name,
    threshold,
):
    variant = copy.deepcopy(base_case)

    current_value = variant[field_name]

    if current_value < threshold:
        variant[field_name] = threshold * 2
    else:
        variant[field_name] = threshold // 2

    return variant

def paraphrase_template(
    base_case,
    field_name,
    templates,
    rng,
):
    variant = copy.deepcopy(base_case)

    current_value = variant[field_name]

    choices = [
        template
        for template in templates
        if template != current_value
    ]

    variant[field_name] = rng.choice(choices)

    return variant

def remove_key_document(
    base_case,
    field_name,
    key_documents,
):
    variant = copy.deepcopy(base_case)

    documents = list(variant[field_name])

    present_key_documents = [
        document
        for document in documents
        if document in key_documents
    ]

    if not present_key_documents:
        return variant

    document_to_remove = present_key_documents[0]

    documents.remove(document_to_remove)

    variant[field_name] = documents

    return variant