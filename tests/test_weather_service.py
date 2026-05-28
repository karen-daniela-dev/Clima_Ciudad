# tests/test_weather_service.py

from unittest.mock import patch

import pytest
from services.weather_service import WeatherService
import requests


# 🔧 Helper mock
class MockResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError("HTTP Error")


# ✅ Caso exitoso completo
@patch("services.weather_service.requests.get")
def test_get_weather_success(mock_get):

    mock_get.side_effect = [
        # Geocoding
        MockResponse({
            "results": [{
                "name": "Bogotá",
                "latitude": 4.71,
                "longitude": -74.07,
                "country": "Colombia"
            }]
        }, 200),

        # Weather
        MockResponse({
            "current": {
                "temperature_2m": 20,
                "wind_speed_10m": 5,
                "precipitation": 0,
                "is_day": 1
            },
            "timezone": "America/Bogota"
        }, 200)
    ]

    result = WeatherService.get_weather_by_city("Bogotá")

    assert result["city"] == "Bogotá"
    assert result["temperature_2m"] == 20
    assert result["wind_speed_10m"] == 5


# ❌ Ciudad no encontrada
@patch("services.weather_service.requests.get")
def test_city_not_found(mock_get):

    mock_get.return_value = MockResponse({"results": []}, 200)

    with pytest.raises(ValueError):
        WeatherService.get_coordinates("CiudadFake")


# ❌ Error HTTP (API devuelve error)
@patch("services.weather_service.requests.get")
def test_api_http_error(mock_get):

    mock_get.return_value = MockResponse({}, 500)

    with pytest.raises(Exception):
        WeatherService.get_weather(0, 0)


# ❌ Timeout (edge case 🔥)
@patch("services.weather_service.requests.get")
def test_api_timeout(mock_get):

    mock_get.side_effect = requests.exceptions.Timeout

    with pytest.raises(Exception):
        WeatherService.get_weather(0, 0)


# ✅ Respuesta incompleta (edge case)
@patch("services.weather_service.requests.get")
def test_missing_current_data(mock_get):

    mock_get.return_value = MockResponse({}, 200)

    # Esperamos que lance excepción porque falta el campo "current"
    with pytest.raises(Exception) as excinfo:
        WeatherService.get_weather(4.71, -74.07)

    # Opcional: verificamos que sea el mensaje exacto
    assert "Respuesta inválida de la API" in str(excinfo.value)