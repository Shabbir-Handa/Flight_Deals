from twilio.rest import Client
import config

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data, today, final_day):
        self.price = flight_data["price"]
        self.city_from = flight_data["cityFrom"]
        self.city_to = flight_data["cityTo"]
        self.fly_from = flight_data["flyFrom"]
        self.fly_to = flight_data["flyTo"]
        self.start_date = today
        self.end_date = final_day
        self.url = flight_data["deep_link"]

    def send_msg(self):
        msg = f"Low price alert! Only €{self.price} to fly from {self.city_from}-{self.fly_from} to" \
              f" {self.city_to}-{self.fly_to}, from {self.start_date} to {self.end_date}. For more information refer to this" \
              f" URL :- {self.url}"
        account_sid = config.TWILIO_ACCOUNT_SID
        auth_token = config.TWILIO_AUTH_KEY
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=msg,
            from_=config.TWILIO_NUMBER,
            to=config.MY_NUMBER
        )

