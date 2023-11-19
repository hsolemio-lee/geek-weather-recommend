from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_movie_region


def lookup(region_name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
        given the region {region_name}, I want you to get it me longitude and latitude of the given region.
        Your answer should be only a number and format have to be json format and each value need to be float.
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 coordinates region",
            func=get_movie_region,
            description="useful for when you need to get coordinates of region",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agents=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(template=template, input_variables=["region_name"])

    coordinates = agent.run(prompt_template.format_prompt(region_name=region_name))
    return coordinates
