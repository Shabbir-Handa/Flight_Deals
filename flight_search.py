import requests
import config


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, from_city, to_city, start_date, end_date):
        self.header = {
            "apikey": config.FLIGHT_API_KEY
        }
        self.url = config.FLIGHT_API_URL
        self.from_city = from_city
        self.to_city = to_city
        self.start_date = start_date
        self.end_date = end_date

    def get_iata(self, city_name):
        location_endpoint = "locations/query"
        param = {
            "term": city_name
        }
        response = requests.get(f"{self.url}/{location_endpoint}", params=param, headers=self.header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flights(self):
        from_iata_code = self.get_iata(self.from_city)
        to_iata_code = self.get_iata(self.to_city)
        search_param = {
            "fly_from": from_iata_code,
            "fly_to": to_iata_code,
            "date_from": self.start_date,
            "date_to": self.end_date,
            "stop_overs": 0
        }
        search_endpoint = "search"
        response = requests.get(f"{self.url}/{search_endpoint}", params=search_param, headers=self.header)
        response.raise_for_status()
        data = response.json()["data"]
        return data
