from fastapi import FastAPI
from backend.search_client import search_documents
from backend.query_parser import parse_query
from backend.risk_engine import calculate_risk
from backend.explain import generate_explanation

app = FastAPI()

@app.get("/search")
def search(query: str = ""):
    filter_query = parse_query(query)

    results, facets = search_documents(query, filter_query)

    enriched_results = []

    for r in results:
        record = dict(r)

        score, reasons = calculate_risk(record)
        explanation = generate_explanation(record, reasons)

        record["risk_score"] = score
        record["risk_level"] = (
            "HIGH" if score > 70 else "MEDIUM" if score > 40 else "LOW"
        )
        record["explanation"] = explanation

        enriched_results.append(record)

    return {
        "results": enriched_results,
        "facets": facets
    }
