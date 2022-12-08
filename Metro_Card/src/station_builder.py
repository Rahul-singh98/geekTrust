from .base import BaseStation, BaseToken
from .constants import OutputFormat, PassengerCharges
from typing import List


class MetroStation(BaseStation):

    def __init__(self, name: str):
        super().__init__(name)

    def addPassenger(self, token: BaseToken, passenger_type: PassengerCharges, discount: int):
        return super().addPassenger(token, passenger_type, discount)

    def printSummary(self):
        print(OutputFormat.TOTAL_COLLECTION.value,
              self.getName(), self.getEarnings(), self.getDiscountsGiven())
        print(OutputFormat.PASSENGER_TYPE_SUMMARY.value)
        for passenger in self.getPassengersList():
            print(passenger[0], passenger[1])


class StationBuilder:

    def __init__(self):
        self.station_pool = dict()

    def addStation(self, station: BaseStation) -> bool:
        if station.getName() in self.station_pool:
            return False
        self.station_pool[station.getName()] = station
        return True

    def getStation(self, station_name: str) -> BaseStation:
        return self.station_pool.get(station_name)

    def getAllStations(self) -> List[BaseStation]:
        return [station for station in self.station_pool.values()]
