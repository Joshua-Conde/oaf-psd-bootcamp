import requests
from abc import ABC, abstractmethod

class WeatherDataProvider(ABC):
    @abstractmethod
    def fetch_weather_forecast(self, latitude, longitude):
        """
        Abstract method to fetch weather forecast for a given latitude and longitude.
        """
        pass
      
class WeatherAPIDataProvider(WeatherDataProvider):
    def fetch_weather_forecast(self, latitude, longitude):
        """
        Fetch weather forecast using Open-Meteo API.
        """
        api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch weather forecast from API")
          
class MockWeatherDataProvider(WeatherDataProvider):
    def fetch_weather_forecast(self, latitude, longitude):
        """
        Mocked method to return a dummy weather forecast.
        """
        return {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": {}
        }
        
class WeatherDataHandler:
    def __init__(self, data_provider):
        """
        Initialize WeatherDataHandler with a data provider.
        """
        self.data_provider = data_provider

    def get_weather_forecast(self, latitude, longitude):
        """
        Get weather forecast for a given latitude and longitude.
        """
        return self.data_provider.fetch_weather_forecast(latitude, longitude)
      
class FancyWeatherDataHandler(WeatherDataHandler):
    def __init__(self, data_provider):
        """
        Initialize FancyWeatherDataHandler with a data provider.
        """
        super().__init__(data_provider)

    def fancy_get_weather_forecast(self, latitude, longitude):
        """
        A fancy way to get weather forecast.
        """
        print("Fetching weather forecast in a fancy way...")
        return self.get_weather_forecast(latitude, longitude)

providers = {
    "live": WeatherAPIDataProvider(),
    "mock": MockWeatherDataProvider()
}

print("Available weather data providers:")
[print(f"- {key.capitalize()}") for key in providers]

selected_provider = providers["live"]
handler = WeatherDataHandler(selected_provider)

latitude = 41.85
longitude = -87.65
print("Fetching weather forecast...")
forecast = handler.get_weather_forecast(latitude, longitude)
print("Weather forecast:", forecast)

""" 
[SAMPLE OUTPUT] 
Available weather data providers:
- Live
- Mock
Fetching weather forecast...
Weather forecast: {'latitude': 41.85271, 'longitude': -87.653625, 'generationtime_ms': 0.03504753112792969, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 179.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'}, 'hourly': {'time': ['2024-03-14T00:00', '2024-03-14T01:00', '2024-03-14T02:00', '2024-03-14T03:00', '2024-03-14T04:00', '2024-03-14T05:00', '2024-03-14T06:00', '2024-03-14T07:00', '2024-03-14T08:00', '2024-03-14T09:00', '2024-03-14T10:00', '2024-03-14T11:00', '2024-03-14T12:00', '2024-03-14T13:00', '2024-03-14T14:00', '2024-03-14T15:00', '2024-03-14T16:00', '2024-03-14T17:00', '2024-03-14T18:00', '2024-03-14T19:00', '2024-03-14T20:00', '2024-03-14T21:00', '2024-03-14T22:00', '2024-03-14T23:00', '2024-03-15T00:00', '2024-03-15T01:00', '2024-03-15T02:00', '2024-03-15T03:00', '2024-03-15T04:00', '2024-03-15T05:00', '2024-03-15T06:00', '2024-03-15T07:00', '2024-03-15T08:00', '2024-03-15T09:00', '2024-03-15T10:00', '2024-03-15T11:00', '2024-03-15T12:00', '2024-03-15T13:00', '2024-03-15T14:00', '2024-03-15T15:00', '2024-03-15T16:00', '2024-03-15T17:00', '2024-03-15T18:00', '2024-03-15T19:00', '2024-03-15T20:00', '2024-03-15T21:00', '2024-03-15T22:00', '2024-03-15T23:00', '2024-03-16T00:00', '2024-03-16T01:00', '2024-03-16T02:00', '2024-03-16T03:00', '2024-03-16T04:00', '2024-03-16T05:00', '2024-03-16T06:00', '2024-03-16T07:00', '2024-03-16T08:00', '2024-03-16T09:00', '2024-03-16T10:00', '2024-03-16T11:00', '2024-03-16T12:00', '2024-03-16T13:00', '2024-03-16T14:00', '2024-03-16T15:00', '2024-03-16T16:00', '2024-03-16T17:00', '2024-03-16T18:00', '2024-03-16T19:00', '2024-03-16T20:00', '2024-03-16T21:00', '2024-03-16T22:00', '2024-03-16T23:00', '2024-03-17T00:00', '2024-03-17T01:00', '2024-03-17T02:00', '2024-03-17T03:00', '2024-03-17T04:00', '2024-03-17T05:00', '2024-03-17T06:00', '2024-03-17T07:00', '2024-03-17T08:00', '2024-03-17T09:00', '2024-03-17T10:00', '2024-03-17T11:00', '2024-03-17T12:00', '2024-03-17T13:00', '2024-03-17T14:00', '2024-03-17T15:00', '2024-03-17T16:00', '2024-03-17T17:00', '2024-03-17T18:00', '2024-03-17T19:00', '2024-03-17T20:00', '2024-03-17T21:00', '2024-03-17T22:00', '2024-03-17T23:00', '2024-03-18T00:00', '2024-03-18T01:00', '2024-03-18T02:00', '2024-03-18T03:00', '2024-03-18T04:00', '2024-03-18T05:00', '2024-03-18T06:00', '2024-03-18T07:00', '2024-03-18T08:00', '2024-03-18T09:00', '2024-03-18T10:00', '2024-03-18T11:00', '2024-03-18T12:00', '2024-03-18T13:00', '2024-03-18T14:00', '2024-03-18T15:00', '2024-03-18T16:00', '2024-03-18T17:00', '2024-03-18T18:00', '2024-03-18T19:00', '2024-03-18T20:00', '2024-03-18T21:00', '2024-03-18T22:00', '2024-03-18T23:00', '2024-03-19T00:00', '2024-03-19T01:00', '2024-03-19T02:00', '2024-03-19T03:00', '2024-03-19T04:00', '2024-03-19T05:00', '2024-03-19T06:00', '2024-03-19T07:00', '2024-03-19T08:00', '2024-03-19T09:00', '2024-03-19T10:00', '2024-03-19T11:00', '2024-03-19T12:00', '2024-03-19T13:00', '2024-03-19T14:00', '2024-03-19T15:00', '2024-03-19T16:00', '2024-03-19T17:00', '2024-03-19T18:00', '2024-03-19T19:00', '2024-03-19T20:00', '2024-03-19T21:00', '2024-03-19T22:00', '2024-03-19T23:00', '2024-03-20T00:00', '2024-03-20T01:00', '2024-03-20T02:00', '2024-03-20T03:00', '2024-03-20T04:00', '2024-03-20T05:00', '2024-03-20T06:00', '2024-03-20T07:00', '2024-03-20T08:00', '2024-03-20T09:00', '2024-03-20T10:00', '2024-03-20T11:00', '2024-03-20T12:00', '2024-03-20T13:00', '2024-03-20T14:00', '2024-03-20T15:00', '2024-03-20T16:00', '2024-03-20T17:00', '2024-03-20T18:00', '2024-03-20T19:00', '2024-03-20T20:00', '2024-03-20T21:00', '2024-03-20T22:00', '2024-03-20T23:00'], 'temperature_2m': [10.1, 9.2, 9.1, 8.4, 8.3, 7.8, 8.5, 7.8, 7.2, 7.5, 7.3, 7.4, 7.8, 9.0, 8.7, 9.4, 9.3, 11.3, 15.0, 15.3, 16.7, 7.4, 6.9, 6.8, 6.9, 6.7, 6.7, 6.6, 6.5, 6.2, 6.1, 6.0, 5.9, 5.6, 5.3, 4.9, 4.9, 5.5, 5.6, 5.8, 6.0, 5.9, 5.3, 5.6, 6.1, 5.6, 5.7, 5.6, 5.2, 5.8, 6.0, 6.5, 6.8, 6.7, 6.4, 6.1, 6.0, 5.9, 6.0, 6.1, 6.1, 6.6, 7.7, 9.5, 10.8, 11.9, 13.0, 13.2, 13.6, 13.9, 12.7, 11.7, 10.6, 9.8, 8.9, 8.0, 7.0, 6.1, 5.5, 5.0, 4.4, 4.0, 3.5, 3.0, 2.5, 2.4, 2.6, 3.3, 4.2, 5.1, 5.7, 6.0, 6.0, 5.9, 5.6, 5.3, 4.8, 4.0, 3.4, 2.8, 2.3, 1.8, 1.3, 0.9, -0.2, -0.9, -0.4, -0.6, -0.9, -0.8, -0.4, 0.2, 0.5, 0.3, 0.6, 0.8, 1.0, 1.2, 1.2, 1.0, 0.9, 0.7, 0.4, 0.2, -0.0, -0.2, -0.3, -0.4, -0.5, -0.6, -0.8, -1.0, -0.9, -0.6, -0.0, 0.7, 1.6, 2.7, 3.7, 4.6, 5.4, 6.0, 6.0, 5.8, 5.5, 5.1, 4.8, 4.4, 4.0, 3.7, 3.4, 3.2, 3.0, 2.9, 2.6, 2.3, 2.5, 3.5, 5.1, 6.8, 8.4, 10.2, 11.7, 13.0, 14.0, 14.7, 14.7, 14.4]}}
"""