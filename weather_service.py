from dotenv import load_dotenv
import os
import requests


load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")




def getData(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    r = requests.get(URL)

    r.raise_for_status()

    data = r.json()

    return data
