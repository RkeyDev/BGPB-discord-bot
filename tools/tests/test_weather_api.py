import requests
import os
from dotenv import load_dotenv
from test_data_manager import DataManager

class WeatherApi:
    def __init__(self) -> None:
        """
        This class represents the weather api.
        It contains methods that are using the 'open weather map' API.
        
        For more information about 'open weather map' check https://home.openweathermap.org/
        """

        load_dotenv(".env") #Load enviroment variables
        self.API_KEY: str = os.getenv("WEATHER_API") #Load the weather API key

    def getWeatherDetails(self,city: str) -> tuple:
        """
        Return the temprature and the weather description of a certain city.
        """
        #Create DataManager object
        dataManager: DataManager = DataManager() 

        #Load main weather data
        weather_data:dict = requests.get(dataManager.getData("Weather_API","weather_data").format(
            city,dataManager.getData("Weather_API","temp_unit"),self.API_KEY)
            ).json()
        
        #Return a tuple of weather data dictionary
        return weather_data["main"].get("temp"), weather_data["weather"][0].get("description") 
    

print(WeatherApi().getWeatherDetails("new york"))