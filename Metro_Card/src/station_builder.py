from .base import BaseStation, BaseToken
from .constants import OutputPrefix, PassengerCharges
from typing import List


class MetroStation(BaseStation):

    def __init__(self, name: str):
        super().__init__(name)

    def addPassenger(self, token: BaseToken, passenger_type: PassengerCharges, discount: int):
        return super().addPassenger(token, passenger_type, discount)

    def printSummary(self):
        print(OutputPrefix.TOTAL_COLLECTION.value,
              self.getName(), self.getEarnings(), self.getDiscountsGiven())
        print(OutputPrefix.PASSENGER_TYPE_SUMMARY.value)
        for passenger in self.getPassengersList():
            print(passenger[0], passenger[1])


class StationBuilder:

    def __init__(self):
        self._station_pool = dict()

    def addStation(self, station: BaseStation) -> bool:
        if station.getName() in self._station_pool:
            return False
        self._station_pool[station.getName()] = station
        return True

    def getStation(self, station_name: str) -> BaseStation:
        return self._station_pool.get(station_name)

    def getAllStations(self) -> List[BaseStation]:
        return [station for station in self._station_pool.values()]
