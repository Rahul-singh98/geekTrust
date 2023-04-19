from src.location import Location
from abc import ABC


class ADriver(ABC):
    """Abstract Driver class so that we can extend it to more
    type of drivers like, If we want BikeDriver, CarDriver"""

    def __init__(self, id: str, location: Location):
        self._id = id
        self._location = Location


class Driver(ADriver):
    pass
