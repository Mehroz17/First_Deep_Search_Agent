
from agents import function_tool, Agent, RunContextWrapper,ModelSettings
from utils.utils import  llm_simple, llm_main, User
import datetime
from src.synthesis import synthesis_agent

@function_tool
def current_date():
    return str(datetime.date.today())


@function_tool
def user_name(local_context:RunContextWrapper[User])->str:
    return local_context.context.name


# Report Creation agnet to create a report
report_agent: Agent = Agent[User](
    name= "report_creation_agent",
    instructions ="""
     You are a research report writing agent  
        Your job:
        - Collect data, statistics, dates, and names from deep_web_search_agent.
        - Then send all the data along with the links to the synthesis_agent to get some insights or realtions form the data
        - Organize the findings into a clear, professional research report.

        Report Guidelines:
        - Always call the `current_date` tool to get today's date for the report header.
        - Also, call the `synthesis_agent` to get insights or realtion between the data
        - Start with a header containing the **Report Title**, and **Date: **.
        - 
        Report Format:
        ------------------------
        Report Title: [Topic Name]
        Author: {user_name}
        Date: {current_date}

        ## Introduction
        - Brief overview of the topic.

        ## Key Facts
        
        ### non-conflicting-data
         `Summary of non-conflicting data`
        
        #### non-conflicting-links 
         - link of non-conflicting website

        ### conflicting-facts
        `Summary of conflicting data`
        
        #### conflicting-links
        - link of conflicting website

        ## Analysis / Insights
        - insighs form the synthesis_agent

        

        ## Conclusion
        - Final summary of the findings.
        ------------------------
     
 """      ,
 model=llm_main,
 tools=[current_date,user_name,
        synthesis_agent.as_tool(
            tool_name="synthesis_agent",
            tool_description="You are a synthesis tool"
        )],

)