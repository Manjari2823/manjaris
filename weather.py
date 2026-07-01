import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    try:
        city = input("Enter place name: ")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        res = requests.get(url)
        data = res.json()

        if res.status_code == 200:
            print("Weather:", data["weather"][0]["description"])
            print("Temperature:", data["main"]["temp"], "°C")
        else:
            print("City not found")

    except Exception as e:
        print("Error:", e)


get_weather()