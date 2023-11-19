from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import weather_summary_parser, fashion_style_parser

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


def get_coordinates_chain() -> LLMChain:
    summary_template = """
        given the region {region_name}, I want you to get it me longitude and latitude of the given region.
        Your answer should be only a number and format have to be json format and each value need to be float.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["region_name"],
        template=summary_template
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)

def get_weather_chain() -> LLMChain:
    summary_template = """
        given the weather information {information}, I want you to create:
        1. current temperature
        2. weather in a word
        3. Recommend fashion styles following temperature and weather with top, bottom, shoes, outerwear and accessory as a string.
        
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": weather_summary_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_fashion_image_chain() -> LLMChain:
    image_template = """
        With below image description, give me only url including the following 
        https://image.pollinations.ai/prompt/[description]), where [description] = {region_name},%20[adjective1],%20[charactersDetailed],%20[adjective2],%20[visualStyle1],%20[visualStyle2],%20[visualStyle3],%20[genre],%20[artistReference]
        Description : 
        I want to get a geek and nerdy style fashion with below clothes only for male. 
        {fashion_style}
        
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["fashion_style", "region_name"],
        template=image_template,
        partial_variables={
            "format_instructions": fashion_style_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)
