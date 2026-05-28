# utils/formatter.py

def format_weather(data: dict) -> str:
    is_day = "Día ☀️" if data["is_day"] == 1 else "Noche 🌙"

    return (
        f"\nClima en {data['city']}, {data['country']}:\n"
        f"-----------------------------------\n"
        f"Temperatura: {data['temperature_2m']} °C\n"
        f"Viento: {data['wind_speed_10m']} km/h\n"
        f"Precipitación: {data['precipitation']} mm\n"
        f"Momento: {is_day}\n"
    )