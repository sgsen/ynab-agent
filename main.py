from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import asyncio

# Load environment variables
load_dotenv()

llm = ChatGoogleGenerativeAI(
    google_api_key=SecretStr(getenv("GEMINI_API_KEY")),
    model="gemini-2.0-flash"
)

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path=getenv("CHROME_PATH"),
    )
)

async def findpuppies():

    intial_actions = [
        {'open_tab': {'url':'https://unsplash.com'}},
    ]
        # Create agent with the model
    agent = Agent(
        task="search for 'puppies' in the text box and hit enter to search. then open up the first free image from the search results (free images do not have a plus sign watermark in the upper left of the thumbnail). Then finally click on the download button and save the image to the downloads folder.",
        llm=llm,
        browser=browser,
        initial_actions=intial_actions
    )
    result = await agent.run(max_steps=10)
    print(result)


async def main():
    # Run the agent
    await findpuppies()

    input("Press Enter to close the browser...")
    await browser.close()



if __name__ == "__main__":
    asyncio.run(main())
