from drivers import Driver
from riders import Rider
from locations import Location
from typing import List


class System:

    def __init__(self):
        self._riders_manager = {}
        self._drivers_manager = {}
        self._rides_manager = {}
        self._matched_drivers = {}

    def add_rider(self, id: str, x: int, y: int) -> None:
        """Add a new rider to the system.

        Parameters:
        -----------
            id : str
                Unique id of the rider
            x : int
                X Coordinate of the rider
            y : int
                Y Coordinate of the rider 
        """
        if id not in self._riders_manager:
            location = Location(x, y)
            rider = Rider(id, location)

            self._riders_manager[id] = rider

    def add_driver(self, id: str, x: int, y: int) -> None:
        """Add a new driver to the system.

        Parameters:
        -----------
            id : str
                Unique id of the driver
            x : int
                X Coordinate of the driver
            y : int
                Y Coordinate of the driver 
        """
        if id not in self._drivers_manager:
            location = Location(x, y)
            driver = Driver(id, location)

            self._drivers_manager[id] = driver

    def match(self, rider_id: str) -> None:
        """Find nearest drivers to the locatio of rider_id

        Parameters:
        -----------
            rider_id : string
                Unique id of the rider
        """
        drivers_list = list(self._drivers_manager.values())
        rider = self._riders_manager.get(rider_id)

        # get list of drivers who are near to rider
        def get_closest_drivers() -> List[Driver]:
            ans = []

    def start_ride(self, ride_id: str, n: int, rider_id: str) -> None:
        """Start a ride

        Parameters:
        -----------
            ride_id: string
                Unique id for the ride.
            n: int
                Index of the driver to start ride with.
            rider_id: string
                Unique id for the rider.
        """
        pass

    def stop_ride(self, ride_id: str, dest_x: int, dest_y: int, time_taken: int) -> None:
        """Stop a ride.

        Parameters:
        -----------
            ride_id: str
                Unique id of the ride.
            dest_x: int
                X coordinate of ride's destination
            dest_y: int
                Y coordinate of ride's destination
            time_taken: int
                Total time taken for the journey.
        """
        pass

    def bill(self, ride_id: str) -> None:
        """Print the bill of the ride.

        Parameters:
        -----------
            ride_id : str
                Unique id of the ride.
        """
        pass
