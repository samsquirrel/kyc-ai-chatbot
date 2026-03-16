from database.vector_store import create_vector_db
from utils.llm import get_llm

db = create_vector_db()

def rag_agent(query):

    docs = db.similarity_search(query, k=3)

    context = "\n".join([d.page_content for d in docs])

    llm = get_llm()

    prompt = f"""
You are a KYC compliance assistant.

Use the following information to answer:

{context}

Question: {query}
"""

    response = llm.invoke(prompt)

    return response.content