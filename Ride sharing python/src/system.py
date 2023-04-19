from .managers import DriverManager, RidersManager, RidesManager
from .strategies.billingStrategies import SimpleBilling
from .strategies.distanceStrategies import EuclideanStrategy
from .location import Location
from .drivers.driver import Driver
from .riders.rider import Rider


class System:
    MATCHES_RETURN_LENGTH = 5

    def __init__(self):
        self._drivers_manager = DriverManager(SimpleBilling())
        self._riders_manager = RidersManager()
        self._rides_manager = RidesManager(EuclideanStrategy())

    def add_driver(self, driver_id: str, x: int, y: int):
        if self._drivers_manager.is_present(driver_id):
            raise ValueError(f'{driver_id} is already present')

        location = Location(x, y)
        driver = Driver(id, location)
        self._drivers_manager.add(driver_id, driver)

    def add_rider(self, rider_id: str, x: int, y: int):
        if self._riders_manager.is_present(rider_id):
            raise ValueError(f'{rider_id} is already present')

        location = Location(x, y)
        rider = Rider(id, location)
        self._riders_manager.add(rider_id, rider)

    def match(self, rider_id):
        _ = self._drivers_manager.match(self.MATCHES_RETURN_LENGTH,
                                        self._riders_manager.get(rider_id))
        # write logic here

    def start_ride(self, ride_id: str, n: int, rider_id: str):
        pass

    def stop_ride(self, ride_id: str, dest_x: int, dest_y: int, time_taken: int):
        pass

    def bill(self, ride_id):
        pass
