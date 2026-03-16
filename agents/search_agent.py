from langchain.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def search_agent(query):

    result = search.run(query)

    return f"Search Result:\n{result}"