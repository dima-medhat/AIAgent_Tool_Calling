from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.calculater import calculate
from tools.search_tool import web_search
from tools.weather_tool import get_weather


all_tools = [
    calculate,
    web_search,
    get_weather
]


def create_agent_executor_for_chat(memory, api_key: str):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.2,
        google_api_key=api_key,
    )

    system_prompt = """
    You are a helpful AI assistant with access to tools.

    Tools:
    1. calculate - for mathematical calculations
    2. get_weather - for current weather
    3. web_search - for current information and news

    Use the appropriate tool when needed.
    Answer directly when no tool is needed.
    """

    agent = create_agent(
        model=llm,
        tools=all_tools,
        system_prompt=system_prompt,
    )

    return agent