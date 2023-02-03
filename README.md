# Weather Forecast Library
A simple Python library to fetch the weather updates for a specified location.

## Installation

You can install the library using pip:

```bash
pip install weather-forecast
```

## Usage

Before you can use the library, you need to set your OpenWeatherMap API key. The library will prompt you to enter the API key the first time you run it. The API key will be stored in a configuration file for subsequent use.

To get the weather updates for a location, use the get_weather function:

```python
from weather_update.weather import get_weather

weather = get_weather("London,UK")
print(f"Weather in London: {weather['weather'][0]['description']}, {weather['main']['temp']}°C")
```

## API Reference

* `get_weather(location: str) -> dict`
Get the weather updates for the specified location.

    Arguments

    * `location`: str -- location for which the weather updates are needed

    Returns

    A dictionary containing the weather updates for the specified location.

* `set_api_key()`

Set the OpenWeatherMap API key in the configuration file. The library will prompt you to enter the API key if it has not been set already.