import streamlit as st
import requests

API_URL = "http://localhost:8000/search"

st.title("🧠 AI Tax Investigator")

query = st.text_input("Ask anything about tax data...")

if st.button("Search"):
    response = requests.get(API_URL, params={"query": query})
    data = response.json()

    results = data["results"]

    for r in results:
        st.markdown("---")
        st.subheader(r.get("client"))

        st.write(f"🏢 {r.get('employer')}")
        st.write(f"💰 {r.get('wages')}")
        st.write(f"📍 {r.get('state')} | {r.get('year')}")

        st.write(f"⚠️ Risk: {r.get('risk_level')} ({r.get('risk_score')})")

        st.write("🧠 Why:")
        for e in r.get("explanation"):
            st.write(e)
