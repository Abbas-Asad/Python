import requests
from pprint import pprint

def get_weather_data():
    API_KEY = "108d06ac9af5f78058a16234acced4fc"

    city = input("Enter the city: ")

    base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city

    weather_data = requests.get(base_url).json()

    pprint(weather_data)

get_weather_data()