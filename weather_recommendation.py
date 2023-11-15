from dotenv import load_dotenv

load_dotenv()

from agents.region_lookup_agent import lookup as region_lookup_agent
from typing import Tuple

from chain.weather_fashion_chain import get_weather_chain, get_fashion_image_chain
from output_parsers import (
    weather_summary_parser,
    fashion_style_parser,
    WeatherFashion,
    FashionImage,
)
from thirdparty.weather import get_weather_info
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def recommend_weather(region: str) -> Tuple[WeatherFashion, FashionImage]:
    coordinates = json.loads(region_lookup_agent(region_name=region))
    weather_data = get_weather_info(coordinates["latitude"], coordinates["longitude"])

    weather_chain = get_weather_chain()
    weather_and_fashions = weather_chain.run(information=weather_data.json())

    weather_and_fashions = weather_summary_parser.parse(weather_and_fashions)

    fashion_image_chain = get_fashion_image_chain()
    fashion_image = fashion_image_chain.run(
        fashion_style=weather_and_fashions.fashion, region_name=region
    )

    fashion_image = fashion_style_parser.parse(fashion_image)

    return (weather_and_fashions, fashion_image)


if __name__ == "__main__":
    pass
