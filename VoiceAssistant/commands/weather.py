from __future__ import annotations

import logging
import requests

logger = logging.getLogger("jarvis.commands.weather")

API_KEY = "YOUR_OPENWEATHER_API_KEY"


def get_weather(city):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        data = requests.get(url, timeout=10).json()

        if data.get("cod") != 200:
            return "I couldn't find that city."

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        return (
            f"The weather in {city} is {desc}. "
            f"The temperature is {temp} degrees Celsius "
            f"with humidity {humidity} percent."
        )

    except Exception as e:
        logger.exception(e)
        return "Unable to get weather."


def weather(command):
    command = command.lower()

    city = "Coimbatore"

    if "in " in command:
        city = command.split("in", 1)[1].strip()

    return get_weather(city)


def register(router):
    router.register("weather", weather)
    router.register("current weather", weather)
    router.register("weather in", weather)
    router.register("forecast", weather)