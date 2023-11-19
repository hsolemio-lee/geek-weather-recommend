from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_coordinates_region
from dotenv import load_dotenv
load_dotenv()

def lookup(country_name: str) -> str:
    llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo-1106")
    template = """
        Given the country {country_name}, give me the 5 movies which is high rated released in 2023 in the given country.
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 movie searcher",
            func=get_coordinates_region,
            description="useful for when you need to get highest-rated movie",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agents=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(template=template, input_variables=["country_name"])

    coordinates = agent.run(prompt_template.format_prompt(country_name=country_name))
    return coordinates

if __name__ == '__main__':
    print(lookup("Africa"))