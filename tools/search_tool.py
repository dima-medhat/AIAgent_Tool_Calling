from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def web_search(query: str) -> str:
    """
    Search the web for current information, news, or facts.
    Use this when the user asks about recent events, current data,
    or anything beyond your training knowledge.
    
    Input should be a clear search query like 'latest AI news' or 'NVIDIA stock price'.
    """
    try:
        search = DuckDuckGoSearchRun()
        result = search.run(query)
        return f"Search results for '{query}':\n\n{result}"
    except Exception as e:
        return f"Search error: {str(e)}"