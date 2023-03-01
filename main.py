# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

# Import statements
from datetime import datetime, date
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager


def custom_travel(fromcity, tocity, fromdate, todate):
    """To find custom flights"""
    flight = FlightData(fromcity, tocity, fromdate, todate)
    data = flight.check_cheapest()
    print(f"INR {data['price']*88}")
    print(f"Refer to the link for more information :\n{data['deep_link']}")


def google_sheet_update():
    """To check and update google sheets"""
    BASE_COUNTRY = "india"
    now = datetime.now()
    today = now.strftime("%d/%m/%Y")
    final_day = date(now.year, now.month + 6, 28).strftime("%d/%m/%Y")

    sheet = DataManager(from_city=BASE_COUNTRY, start_date=today, end_date=final_day)
    print(sheet.update())


direction = int(input("Enter \n1. To search custom flights\n 2. To read and update existing google sheet\n"))
if direction == 1:
    from_city = input("Enter the city you want to travel from: ")
    to_city = input("Enter the city you want to travel to: ")
    from_date = input("Enter starting date of your date range: ")
    to_date = input("Enter ending date of your date range: ")
    custom_travel(from_city, to_city, from_date, to_date)
elif direction == 2:
    google_sheet_update()
else :
    print("Invalid Input.")
