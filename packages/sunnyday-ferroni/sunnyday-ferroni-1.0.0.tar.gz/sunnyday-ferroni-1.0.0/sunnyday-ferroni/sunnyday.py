import requests
from decouple import config


class Weather:
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates
    ...
    """

    base_url = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self,
                 api_key: str,
                 city=None,
                 lat=None,
                 lon=None,
                 units="metric") -> None:
        self.city = city
        self.lat = lat
        self.lon = lon
        self.api_key = api_key
        self.units = units

        self._get_data()

    def _get_data(self):
        if self.city is not None:
            url = f"{self.base_url}?" \
                  f"q={self.city}&" \
                  f"appid={self.api_key}&" \
                  f"units={self.units}"
        elif None not in [self.lat, self.lon]:
            url = f"{self.base_url}?" \
                  f"lat={self.lat}&" \
                  f"lon={self.lon}&" \
                  f"appid={self.api_key}&" \
                  f"units={self.units}"
        else:
            raise TypeError("You need to inform city or lat and lon")

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Fail getting the data: {response.text}")
        self.data = response.json()

    def next_12_hours(self):
        return self.data['list'][:4]

    def next_12_hours_simplified(self):
        my_list = []
        for dicty in self.data['list'][:4]:
            my_list.append(
                (dicty['dt_txt'],
                 dicty['main']['temp'],
                 dicty['weather'][0]['description'])
            )
        return my_list


if __name__ == '__main__':
    api_key = config("API_KEY")
    weather = Weather(api_key=api_key, city="Porto Alegre")
    print(weather.next_12_hours_simplified())
