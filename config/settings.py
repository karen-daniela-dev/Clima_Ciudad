# config/settings.py

# Cargar variables del archivo .env
import os

from dotenv import load_dotenv


load_dotenv()

GEOCODING_URL = os.getenv("GEOCODING_URL")
WEATHER_URL = os.getenv("WEATHER_URL")

DEFAULT_WEATHER_PARAMS = {
    "current": "temperature_2m,wind_speed_10m,precipitation,is_day"
}