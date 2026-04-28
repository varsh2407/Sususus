import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_INDEX_NAME"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

def search_documents(query, filter_query=None):
    results = client.search(
        search_text=query or "*",
        filter=filter_query,
        facets=["state", "year", "form"],
        query_type="semantic",
        semantic_configuration_name="default"
    )
    return list(results), results.get_facets()
