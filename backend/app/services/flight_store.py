class FlightStore:
    def __init__(self):
        self.flights = {}

    def update(self, flight): # Overwrite old data with newest update
        self.flights[flight["icao24"]] = flight # Use aircraft ID as unique key

    def all(self):
        return list(self.flights.values())