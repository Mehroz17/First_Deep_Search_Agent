from agents import Agent, ModelSettings
from utils.utils import llm_main

## Synthesis Agent

synthesis_agent: Agent = Agent(
    name="synthesis_agnet",
    instructions="""
            You are a synthesis agent responsible for transforming structured data, facts, 
    and conflict-managed insights into a coherent narrative. Your role is to:
    
    - Identify key patterns, trends, or relationships across the provided information.
    - Integrate evidence from multiple sources into a unified perspective.
    
""",
    model=llm_main,
    model_settings=ModelSettings(max_complition_tokens=300),
)
