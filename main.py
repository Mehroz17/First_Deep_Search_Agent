import gradio as gr
import asyncio
import os
from src.deep_research_system import lead_search_agent
from agents import Runner
from utils.utils import u1

# Main async function: sends a message to the lead_search_agent and streams results
async def main(message: str):
    # Run the agent in streaming mode with a message and some context
    results = Runner.run_streamed(lead_search_agent, message, context=u1)

  
 # Stream events as they come from the agent
    async for event in results.stream_events():
        # --- Case 1: Agent is initialized or updated ---
        if event.type == "agent_updated_stream_event":
            print(f"\n🔹 Agent started: {event.new_agent.name}")
        #--- Case 2: Raw response from the model (text chunks etc.) ---
        elif event.type == "raw_response_event":
            data_type = getattr(event.data, "type", None)
            # Detect incremental text chunks (delta events)
            if data_type == "response.output_text.delta":
                delta = getattr(event.data, "delta", "")
                print(delta, end="", flush=True)

        elif event.type == "run_item_stream_event":
            print(f"\n[RunItem Event: {event.name}]")
            print(f"   Item: {getattr(event.item,"output",None)}")
            if hasattr(event.item, "raw_item"):
                print(f"Raw Item {event.item.raw_item}")

    # Fallback in case completion didn't fire
    if results.final_output:
        print("\n\n✅ Final Output:\n")
        print(results.final_output)


if __name__ == "__main__":
    asyncio.run(main("What will be the impact of Agentic AI on Software Development?"))
