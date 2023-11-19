from langchain.serpapi import SerpAPIWrapper


def get_coordinates_region(text: str) -> str:
    search = SerpAPIWrapper()
    res = search.run(f"{text} longitude latitude")
    return res

def get_movie_region(text: str) -> str:
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
