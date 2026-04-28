def calculate_risk(record):
    score = 0
    reasons = []

    if record.get("missing_ssn"):
        score += 50
        reasons.append("Missing SSN")

    if record.get("wages", 0) > 100000:
        score += 30
        reasons.append("High income")

    if record.get("state") == "CA":
        score += 10
        reasons.append("High-risk state cluster")

    return score, reasons
