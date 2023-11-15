from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class WeatherFashion(BaseModel):
    temperature: float = Field(description="temperature")
    weather: str = Field(description="weather")
    fashion: str = Field(description="fashion style")

    def to_dict(self):
        return {
            "temperature": self.temperature,
            "weather": self.weather,
            "fashion": self.fashion,
        }


class FashionImage(BaseModel):
    url: str = Field(description="url")

    def to_dict(self):
        return {"url": self.url}


weather_summary_parser = PydanticOutputParser(pydantic_object=WeatherFashion)
fashion_style_parser = PydanticOutputParser(pydantic_object=FashionImage)
