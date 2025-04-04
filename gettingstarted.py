from langchain_ollama import ChatOllama
from browser_use import Agent
#from pydantic import SecretStr
import asyncio


# Initialize the model
llm=ChatOllama(model="qwen2.5", num_ctx=32000)

async def letsgo():
    # Create agent with the model
    agent = Agent(
        task="go to https://www.google.com",
        llm=llm
    )
    result = await agent.run()
    print(result)

# Run the agent
asyncio.run(letsgo())