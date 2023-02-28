import requests
from flight_data import FlightData
from notification_manager import NotificationManager
import config

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, from_city, start_date, end_date):
        self.url = config.SHEETY_API_URL
        self.header = {
            "Authorization": config.SHEETY_API_KEY
        }
        self.from_city = from_city
        self.start_date = start_date
        self.end_date = end_date

    def get(self):
        response = requests.get(self.url, headers=self.header)
        data = response.json()
        return data["prices"]

    def update(self):
        data = self.get()
        data_dict = {cities["city"]: cities for cities in data}
        responses = []
        for key in data_dict:
            city = key
            flight = FlightData(
                from_city=self.from_city,
                to_city=city,
                start_date=self.start_date,
                end_date=self.end_date
            )
            cheapest_flight = flight.check_cheapest()
            if data_dict[key]["lowestPrice"] >= cheapest_flight["price"]:
                data_dict[key]["lowestPrice"] = cheapest_flight["price"]
                iata = cheapest_flight["flyTo"]
                param = {
                    "price": {
                        "city": key,
                        "iataCode": iata,
                        "lowestPrice": data_dict[key]["lowestPrice"]
                    }
                }
                response = requests.put(url=f"{self.url}/{data_dict[key]['id']}", json=param, headers=self.header)
                responses.append(response.json())
                send_sms = NotificationManager(cheapest_flight, self.start_date, self.end_date)
                send_sms.send_msg()

        return responses
