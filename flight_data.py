from flight_search import FlightSearch


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, from_city, to_city, start_date, end_date):
        self.check = FlightSearch(from_city, to_city, start_date, end_date)

    def check_cheapest(self):
        data = self.check.get_flights()
        cheapest_flight = data[0]
        for flight in data:
            if flight["price"] < cheapest_flight["price"]:
                cheapest_flight = flight
        return cheapest_flight
