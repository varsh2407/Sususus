def parse_query(user_input):
    filters = []

    text = user_input.lower()

    if "high income" in text or "high salary" in text:
        filters.append("wages gt 100000")

    if "california" in text or "ca" in text:
        filters.append("state eq 'CA'")

    if "new york" in text or "ny" in text:
        filters.append("state eq 'NY'")

    if "no ssn" in text or "missing ssn" in text:
        filters.append("missing_ssn eq true")

    return " and ".join(filters)
