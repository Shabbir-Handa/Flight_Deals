# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

# Import statements
from datetime import datetime,date
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

# To find custom flights
# flight = FlightData(fromcity, tocity, fromdate, todate)
# data = flight.check_cheapest()
# print(f"{data['price']} euros")
# print(data["deep_link"])

# To check and update google sheets
BASE_COUNTRY = "india"
now = datetime.now()
today = now.strftime("%d/%m/%Y")
final_day = date(now.year, now.month+6, 28).strftime("%d/%m/%Y")

sheet = DataManager(from_city=BASE_COUNTRY, start_date=today, end_date=final_day)
# print(sheet.update())

