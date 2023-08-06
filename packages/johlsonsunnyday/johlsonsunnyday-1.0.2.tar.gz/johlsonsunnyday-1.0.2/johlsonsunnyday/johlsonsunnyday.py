import requests

class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own apikey from https://openweathermap.org
    # and wait a couple of hours for the apikey to be activated.
    >>> weather1 = Weather(apikey = "e0a28520c0abad49292ad3967ca671f7", city = "Madrid")

    # Using latitude and longitude coordinates
    >>> weather2 = Weather(apikey = "e0a28520c0abad49292ad3967ca671f7", lat = 41.1, lon = -4.1)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Get simplified data for the next 12 hours:
    >>> weather.next_12h_simplified()

    """


    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            req = requests.get(url)
            self.data = req.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            req = requests.get(url)
            self.data = req.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments!")

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dictionary
        """
        return self.data['list'][:5]

    def next_12h_simplified(self):
        """Returns date, temperature and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples.
        """
        simple_data = []
        for dicty in self.data['list'][:5]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
        return simple_data
