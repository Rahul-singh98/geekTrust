from locations import Location


class Rider:
    def __init__(self, rider_id: str, location: Location):
        """Rider class.

        Parameters:
        -----------
            rider_id: str
                Unique id for the rider.
            location: Location
                instance of location class to store the location
        """
        self.rider_id = rider_id
        self.location = location
        self.matched_drivers = []
        self.current_ride = None

    def match(self, driver):
        if self.current_ride is not None:
            return False
        return driver.match(self)

    def start_ride(self, ride):
        self.current_ride = ride

    def stop_ride(self):
        self.current_ride = None
