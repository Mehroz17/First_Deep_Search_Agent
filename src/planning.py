from agents import function_tool, Agent, ModelSettings, RunContextWrapper
from utils.utils import llm_simple, llm_main


# This agent's role is to break down a complex query into 3 concise sub-queries to keep tokens in the limit
# # Each sub-query should be clear and not exceed 40 characters
# The sub-queries are then passed to the deep_search_agent for further processing
planning_agent: Agent = Agent(
    name = "planning_agent",
    instructions="""
     You are a planning agent. Break a complex query into 3 smaller, clear sub-queries of not more than 40 characters.
     And pass them to deep_search_agent
    """,
    model=llm_simple, # Gemini Model here
    model_settings=ModelSettings(max_completion_tokens = 200,temperature=1.5)
) 