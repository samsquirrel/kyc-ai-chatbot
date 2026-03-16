from agents.search_agent import search_agent
from agents.rag_agent import rag_agent

def router(query):

    q = query.lower()

    if "kyc" in q or "document" in q:
        return rag_agent(query)

    else:
        return search_agent(query)