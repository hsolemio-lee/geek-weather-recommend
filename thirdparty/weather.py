import os
import requests

API_KEY = "0c429a365bfdc6a7526ee98e9324781f"


def get_weather_info(latitude: float, longitude: float):
    apiEndpoint = (
        "http://api.openweathermap.org/data/2.5/weather?units=metric&lat="
        + str(latitude)
        + "&lon="
        + str(longitude)
        + "&APPID="
        + API_KEY
    )

    response = requests.get(apiEndpoint)
    return response
