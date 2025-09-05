from agents import function_tool, Agent, ModelSettings, RunContextWrapper
from utils.utils import llm_simple, llm_main
from src.planning import planning_agent
from src.research_agents import deep_search_agent
from src.report import report_agent
from utils.utils import User


lead_search_agent: Agent = Agent[User](
    name="lead_search_orchestrator_agent",
    instructions="""
     You are the Orchestrator Agent responsible for managing the deep search workflow. 
    Your role is only to coordinate between agents and pass along their outputs. 
    You must strictly follow these steps:
    1. Send the user query to the planning_agent that will break that complex query into simple 3 quries. 
    2  Then for each sub query, call the deep_search_agent tool to gather data with sources.
    3. Collect all results from deep_search_agent and send them to report_creation_agent.
    4. Return ONLY the final response from  report_creation_agent to the user.
    
    Do not add, explain, or modify anything yourself. 
    Just orchestrate tool calls and return the synthesis_agent output.
    """,
model = llm_main,
tools=[
    planning_agent.as_tool(
    tool_name="planning_agent",
    tool_description="Convert complex qury into simple quries ans pass them to deep_search_agent."
),
deep_search_agent.as_tool(
    tool_name="deep_search_agent",
    tool_description="Search the quries deeply"
),
report_agent.as_tool(
    tool_name="report_creation_agent",
    tool_description="Create a report from the reults of deep search agent"
)


],

)