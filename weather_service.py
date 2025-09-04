from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

location = "Zuerich"

URL = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key + "&units=metric"


def getData():
    r = requests.get(URL)

    r.raise_for_status()

    data = r.json()

    return data
