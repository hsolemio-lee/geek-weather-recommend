from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import weather_summary_parser, fashion_style_parser

llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo-1106")


def get_weather_chain() -> LLMChain:
    summary_template = """
        given the weather information {information}, I want you to create:
        1. current temperature
        2. weather in a word
        3. Recommend fashion styles following temperature and weather with top, bottom, shoes, outerwear and accessory.
        
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
        I want to get a geek and nerdy style male fashion with below clothes for both woman and man. 
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
