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
    except FileNotFoundError:
        print("Error: The specified file path does not exist.")
    except PermissionError:
        print("Error: You do not have permission to write to the specified file.")
    except configparser.Error as e:
        print(f"Error while setting the API key: {e}")


def get_api_key():
    """
    Get the OpenWeatherMap API key from the configuration file
    """
    if not os.path.exists(CONFIG_FILE):
        set_api_key()
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_FILE)
    except PermissionError:
        print("Error: You do not have permission to read from the specified file.")
    except configparser.Error as e:
        print(f"Error while reading the API key: {e}")
    api_key = config.get("DEFAULT", "api_key")
    return api_key
