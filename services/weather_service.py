# services/weather_service.py

import requests
from config.settings import GEOCODING_URL, WEATHER_URL, DEFAULT_WEATHER_PARAMS


class WeatherService:

    @staticmethod
    def get_coordinates(city: str) -> dict:
        try:
            response = requests.get(GEOCODING_URL, params={"name": city, "count": 1})
            response.raise_for_status()
            data = response.json()

            if "results" not in data or not data["results"]:
                raise ValueError("Ciudad no encontrada")

            result = data["results"][0]

            return {
                "name": result["name"],
                "latitude": result["latitude"],
                "longitude": result["longitude"],
                "country": result.get("country", "")
            }

        except requests.RequestException as e:
            raise Exception("Error al conectar con la API de geocoding: {e}")

    @staticmethod
    def get_weather(latitude: float, longitude: float) -> dict:
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                **DEFAULT_WEATHER_PARAMS
            }

            response = requests.get(WEATHER_URL, params=params)
            response.raise_for_status()

            data = response.json()

            if "current" not in data:
                raise Exception("Respuesta inválida de la API")

            return data["current"]

        except requests.RequestException:
            raise Exception("Error al conectar con la API del clima")

    @classmethod
    def get_weather_by_city(cls, city: str) -> dict:
        location = cls.get_coordinates(city)
        weather = cls.get_weather(location["latitude"], location["longitude"])

        return {
            "city": location["name"],
            "country": location["country"],
            **weather
        }