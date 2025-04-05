from langchain_ollama import ChatOllama
from browser_use import Agent
#from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()
import asyncio


# Initialize the model
llm=ChatOllama(model="qwen2.5:7b", num_ctx=32000)

async def letsgo():
    # Create agent with the model
    agent = Agent(
        task="go to https://www.google.com and search for 'images of puppies', then open up the first image from the search results in a separate tab, and then finally download the image from the separate tab.",
        llm=llm
    )
    result = await agent.run(max_steps=15)
    print(result)

# Run the agent
asyncio.run(letsgo())