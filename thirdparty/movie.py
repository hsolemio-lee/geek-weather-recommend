import os
import requests

API_KEY = "58dff79"


def get_movie_info(title: str):
    apiEndpoint = "http://www.omdbapi.com/?t=" + title + "&apikey=" + API_KEY

    response = requests.get(apiEndpoint)
    return response
