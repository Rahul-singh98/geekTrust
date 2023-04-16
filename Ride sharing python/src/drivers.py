from heapq import heappush, heappop
from locations import Location
from rides import Ride


class Driver:
    def __init__(self, driver_id: str, location: Location):
        """Driver class.

        Parameters:
        -----------
            driver_id: str
                Unique id for the driver.
            location: Location
                instance of location class to store the location
        """
        self.driver_id = driver_id
        self.location = location
        self.available = True
        self.matched_riders = []
        self.current_ride = None

    def match(self, rider):
        if not self.available:
            return False
        distance = self.location.distance(rider.location)
        heappush(self.matched_riders, (distance, rider))
        return True

    def start_ride(self, ride_id, rider, time):
        if not self.available or self.current_ride is not None:
            return False
        if rider not in [r for _, r in self.matched_riders]:
            return False
        _, rider = [(d, r) for d, r in self.matched_riders if r == rider][0]
        self.matched_riders = []
        self.available = False
        self.current_ride = Ride(ride_id, rider, self, time)
        rider.start_ride(self.current_ride)
        return True

    def stop_ride(self, time):
        if self.current_ride is None:
            return False
        self.current_ride.stop(time)
        self.available = True
        self.current_ride = None
        return True
