import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dataclasses import dataclass
# loading the envs

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# setting tracing
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
set_tracing_disabled(False)

# creating External Client for Open AI
external_client : AsyncOpenAI = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)

# creating External Client for Gemini
# 
external_client2 : AsyncOpenAI = AsyncOpenAI(
    api_key= GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


### LLM Config
## Setting LLM for Main Agent


# Model 1 
llm_main : OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model = "gpt-5-nano",
    openai_client=external_client
    
    )

# Model 2
llm_simple : OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client=external_client2)


@dataclass
class User:
    name: str
    email: str
    institute: str


u1 = User(name="John Doe", email="john.doe@example.com", institute="Example University")