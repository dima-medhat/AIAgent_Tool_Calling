import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def get_weather(location: str) -> str:

    """ 
    Get the current weather for a city.
    Use this when the user asks about temperature, weather conditions,
    rain, wind, or humidity in a specific location.
    
    Input should be a city name like 'Cairo', 'London', or 'Tokyo'.
    """

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return "Error: WEATHER_API_KEY not found. Please set it in your .env file."
    

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code}"
        
        data = response.json()
        
        # Parse the simple JSON
        city = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        
        return f"Weather in {city}, {country}: {condition}, {temp}°C, Humidity: {humidity}%"
        
    except Exception as e:
        return f"Error fetching weather: {str(e)}"