from abc import ABC
from drivers.driver import ADriver
from riders.rider import ARider
from location import Location


class ARide(ABC):
    """Abstract ride class which can be used to increase the
    capability of ride like for premium ride and normal ride."""

    def __init__(self, id: str, driver: ADriver, rider: ARider):
        self._id = id
        self._driver = driver
        self._rider = rider
        self._location = None
        self._time_taken = None
        self._is_ended = False

    @property
    def IsEnded(self) -> bool:
        return self._is_ended

    @IsEnded.setter
    def IsEnded(self, value: bool):
        self._is_ended = value

    def start(self):
        pass

    def stop(self, location: Location, time_taken: int):
        self._location = location
        self._time_taken = time_taken
        self.IsEnded = True


class Ride(ARide):
    pass
