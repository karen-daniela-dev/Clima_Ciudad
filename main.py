# main.py

from services.weather_service import WeatherService
from utils.formatter import format_weather
from utils.user_input import get_city_input


def main():
    try:
        city = get_city_input()

        data = WeatherService.get_weather_by_city(city)

        result = format_weather(data)

        print(result)

    except ValueError as ve:
        print(f"Error de entrada: {ve}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
    