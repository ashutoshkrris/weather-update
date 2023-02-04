import requests_mock
import pytest

from src.weather_update.weather import get_api_key, get_weather

# Global variable for the configuration file
CONFIG_FILE = "config.ini"
API_KEY = get_api_key()


def test_get_weather():
    # create a mock response for the API call
    with requests_mock.Mocker() as mock:
        mock.get(
            f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric",
            json={"weather": [{"description": "cloudy"}], "main": {"temp": 15.0}},
        )

        # test the get_weather function
        weather = get_weather("London")
        assert weather == {
            "weather": [{"description": "cloudy"}],
            "main": {"temp": 15.0},
        }


def test_get_weather_failure():
    # create a mock response for the API call to return a failure
    with requests_mock.Mocker() as mock:
        mock.get(
            f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric",
            status_code=400,
        )

        # test the get_weather function
        with pytest.raises(Exception):
            get_weather("London")
