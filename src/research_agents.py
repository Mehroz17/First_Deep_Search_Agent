from agents import function_tool, Agent, ModelSettings
from utils.utils import external_client, llm_simple, llm_main, TAVILY_API_KEY
from tavily import TavilyClient, AsyncTavilyClient


# To DO
# add error handling
@function_tool
async def deep_search_tool(query: str) -> str:
    tavClient = AsyncTavilyClient(api_key=TAVILY_API_KEY)
    try:
        response = await tavClient.search(query=query, search_depth="advanced")
        return response
    except Exception as e:
        print(f"Tavily API error ",e)




# conflict Agent
conflict_managment_agent: Agent = Agent(
    name="conflict_manager",
    instructions="""
        You are a conflict manager agent. 
        Analyze the provided facts (with URLs). 
        Return JSON with two keys:
        - "non_conflicting": list of facts with their sources
        - "conflicting": list of conflicting facts and their sources
        """,
    model=llm_simple,
    model_settings=ModelSettings(max_complition_tokens=400),
)


# deep search agent
deep_search_agent: Agent = Agent(
    name="deep_search_agent",
    instructions="""
            You are a deep search agent that searches queries to find data. 
            Make sure results are from reliable references.

            Workflow:
            1. Use `deep_search_tool` to fetch results from Tavily.
            2. Pass those results into `conflict_manager_tool` to detect conflicts.
            3. Forward the cleaned + conflict-analyzed data to the `report_creation_agent`.
    
""",
    model=llm_main,
    tools=[deep_search_tool,
           conflict_managment_agent.as_tool( 
               tool_name= "conflict_managment_agent",
               tool_description= " You are a conflict manager agent."

    )],
    model_settings=ModelSettings(max_complition_tokens=400, parallel_tool_calls=True),
)
