def generate_explanation(record, reasons):
    explanation = []

    explanation.append(f"Employer: {record.get('employer')}")
    
    for r in reasons:
        explanation.append(f"✔ {r}")

    return explanation
