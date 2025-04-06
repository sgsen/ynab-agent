from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr

import asyncio
#from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain

# Load environment variables
load_dotenv()


# Initialize the model
# llm=ChatOpenAI(
#     openai_api_key=getenv("OPENROUTER_API_KEY"),
#     openai_api_base=getenv("OPENROUTER_API_BASE"),
#     model_name="deepseek/deepseek-chat-v3-0324:free"
#     )

llm = ChatGoogleGenerativeAI(
    google_api_key=SecretStr(getenv("GEMINI_API_KEY")),
    model="gemini-2.0-flash"
)


## Toy Example 
# Create a prompt template
# template = """Question: {question}"""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# # Create a chain
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# # Run the chain
# question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
# response = llm_chain.run(question)
# print(response)



async def letsgo():
    # Create agent with the model
    agent = Agent(
        task="go to https://www.google.com and search for 'images of puppies', then open up the first image from the search results in a separate tab, and then finally download the image from the separate tab.",
        llm=llm
    )
    result = await agent.run(max_steps=10)
    print(result)

async def test_search():
    # Create agent with the model
    agent = Agent(
        task=(
            'go to google flights and find the cheapest flight from bangalore to nyc in july 2025 for a family of 2 adults and 1 children? i\'m only ok with one stop or direct flights.'
        ),
        llm=llm,
        max_actions_per_step=4
        
    )
    result = await agent.run(max_steps=10)
    print(result)

# Run the agent
#asyncio.run(letsgo())
asyncio.run(test_search())
