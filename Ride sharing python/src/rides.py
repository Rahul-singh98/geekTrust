from drivers import Driver
from riders import Rider
from collections import defaultdict


class Ride:
    BASE_FARE = 50
    DISTANCE_RATE = 6.5
    TIME_RATE = 2
    TAX_RATE = 0.2

    def __init__(self, ride_id, rider, driver, start_time):
        self.ride_id = ride_id
        self.rider = rider
        self.driver = driver
        self.start_time = start_time
        self.end_time = None
        self.destination = None

    def stop(self, end_time, destination):
        self.end_time = end_time
        self.destination = destination

    def distance(self):
        return self.driver.location.distance(self.destination)

    def time(self):
        return self.end_time - self.start_time

    def fare(self):
        distance_fare = self.distance() * self.DISTANCE_RATE
        time_fare = self.time() * self.TIME_RATE
        total_fare = self.BASE_FARE + distance_fare + time_fare
        tax = total_fare * self.TAX_RATE
        return round(total_fare + tax, 2)


class RideService:
    MAX_DISTANCE = 5

    def __init__(self):
        self.riders = defaultdict(Rider)  # Dictionary to store rider objects
        # Dictionary to store driver objects
        self.drivers = defaultdict(Driver)
        self.rides = defaultdict(Ride)  # Dictionary to store ride objects

    def add_driver(self, driver_id, x_coord, y_coord):
        """Adds a driver to the system"""
        driver = Driver(driver_id, x_coord, y_coord)
        self.drivers[driver_id] = driver

    def add_rider(self, rider_id, x_coord, y_coord):
        """Adds a rider to the system"""
        rider = Rider(rider_id, x_coord, y_coord)
        self.riders[rider_id] = rider

    def match(self, rider_id):
        """Matches the rider with the nearest available drivers within 5 kms distance"""
        rider = self.riders.get(rider_id)
        if not rider:
            print("INVALID_RIDER")
            return

        # Get all available drivers within max distance
        available_drivers = [driver for driver in self.drivers.values()
                             if driver.is_available and driver.get_distance(rider) <= self.MAX_DISTANCE]

        if not available_drivers:
            print("NO_DRIVERS_AVAILABLE")
            return

        # Sort drivers by distance from rider
        sorted_drivers = sorted(available_drivers, key=lambda driver: (
            driver.get_distance(rider), driver.driver_id))

        # Print driver ids of nearest 5 drivers
        driver_ids = [driver.driver_id for driver in sorted_drivers[:5]]
        print("DRIVERS_MATCHED", *driver_ids)

    def start_ride(self, ride_id, n, rider_id):
        """Starts a ride with the Nth nearest driver"""
        rider = self.riders.get(rider_id)
        if not rider:
            print("INVALID_RIDER")
            return

        # Check if ride with ride_id already exists
        if ride_id in self.rides:
            print("INVALID_RIDE")
            return

        # Get all available drivers within max distance
        available_drivers = [driver for driver in self.drivers.values(
        ) if driver.is_available and driver.get_distance(rider) <= self.MAX_DISTANCE]

        # Sort drivers by distance from rider
        sorted_drivers = sorted(available_drivers, key=lambda driver: (
            driver.get_distance(rider), driver.driver_id))

        # Check if driver is not available or if requested driver number is greater than available drivers
        if n > len(sorted_drivers) or not sorted_drivers[n-1].is_available:
            print("INVALID_RIDE")
            return

        # Get the selected driver and mark them as unavailable
        driver = sorted_drivers[n-1]
        driver.is_available = False

        # Create a new ride object
        ride = Ride(ride_id, rider, driver)
        self.rides[ride_id] = ride

        print("RIDE_STARTED", ride_id)

    def stop_ride(self, ride_id, dest_x, dest_y, time_taken):
        """Stops a ride"""
        ride = self.rides.get(ride_id)
        if not ride or ride.is_completed:
            print("INVALID_RIDE")
            return

        # Calculate distance and bill amount
        distance = ride.get_distance(dest_x, dest_y)
        bill_amount = round((distance * 6.5) + (time_taken * 2) + 50, 2)
        final_amount = round(bill_amount * 1.2, 2)  # Final bill
