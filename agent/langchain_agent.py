from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from agent.langchain_tools import *


def run_agent(user_query: str):
    # Create Claude model with system prompt built-in
    llm = ChatAnthropic(
        model="claude-3-haiku-20240307",
        temperature=0,
        max_tokens=4096
    )
    
    tools = [
        flight_search_tool,
        hotel_recommendation_tool,
        places_discovery_tool,
        weather_tool,
        budget_tool
    ]
    
    # Create the agent
    agent = create_react_agent(llm, tools)
    
    # Invoke with proper input format
    result = agent.invoke({"messages": [("user", user_query)]})
    
    # Extract the final message
    return {"output": result["messages"][-1].content}
