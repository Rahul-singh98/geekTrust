from .constants import PassengerCharges, MetroCharges
from .token_builder import MetroCard, TokenBuilder
from .station_builder import MetroStation, StationBuilder


class MetroAuthority:

    def __init__(self):
        self._travelling_passengers = set()
        self._tokens = TokenBuilder()
        self._stations = StationBuilder()
        self.initial_stations()

    def initial_stations(self):
        self.addStation("CENTRAL")
        self.addStation("AIRPORT")

    def addStation(self, name: str):
        n_station = MetroStation(name)
        self._stations.addStation(n_station)

    def addToken(self, id: str, balance: int):
        n_token = MetroCard(id, balance)
        self._tokens.addToken(n_token)

    def checkIn(self, token_id: str, passenger_type: str, station_name: str):
        discount = self.getDiscounts(token_id, passenger_type)
        token = self._tokens.getToken(token_id)
        station = self._stations.getStation(station_name)

        station.addPassenger(token, PassengerCharges[passenger_type], discount)

    def getDiscounts(self, token_id: str, passenger_type: str) -> int:
        discount = 0
        if (token_id in self._travelling_passengers):
            discount = (
                PassengerCharges[passenger_type].value * MetroCharges.DISCOUNT_PCT.value)
            self._travelling_passengers.remove(token_id)
        else:
            self._travelling_passengers.add(token_id)
        return int(discount)

    def print_summary(self):
        for station in self._stations.getAllStations():
            station.printSummary()
