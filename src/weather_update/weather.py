import os
import requests
import configparser

# Global variable for the configuration file
CONFIG_FILE = "config.ini"


def get_weather(location: str):
    """
    Get the weather updates for the specified location

    Arguments:
    location: str -- location for which the weather updates are needed

    Returns:
    dict -- weather updates for the specified location
    """
    api_key = get_api_key()
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    return response.json()


def set_api_key():
    """
    Set the OpenWeatherMap API key in the configuration file
    """
    try:
        config = configparser.ConfigParser()
        api_key = input("Enter your OpenWeatherMap API key: ")
        config["DEFAULT"] = {"api_key": api_key}
        with open(CONFIG_FILE, "w") as configfile:
            config.write(configfile)
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except configparser.Error:
        print("Error: Unable to write to the configuration file.")


def get_api_key():
    """
    Get the OpenWeatherMap API key from the configuration file
    """
    config = configparser.ConfigParser()
    api_key = None

    if not os.path.exists(CONFIG_FILE):
        print("You don't have an API Key set for OpenWeatherMap.")
        set_api_key()

    try:
        config.read(CONFIG_FILE)
        api_key = config.get("DEFAULT", "api_key")
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Error while reading the API key:\n {e}")
        set_api_key()
        api_key = config.get("DEFAULT", "api_key")

    return api_key