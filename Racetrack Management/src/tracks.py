from typing import Any
from .constants import (
    RegularBookingQuatity,
    PremiumBookingQuantity,
    Outcome,
    TrackTimming,
    BookingConditions,
    GlobalResponses
)


class SingletonMeta:
    instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.instance is None:
            self.instance = self()

        return self.instance


class Track(metaclass=SingletonMeta):
    def get_available_track(self):
        pass


class VehiclesManager:

    def __init__(self):
        self.__REGULAR_BIKE = RegularBookingQuatity.BIKE.value
        self.__REGULAR_CARS = RegularBookingQuatity.CAR.value
        self.__REGULAR_SUV = RegularBookingQuatity.SUV.value
        self.__PREMIUM_CARS = PremiumBookingQuantity.CAR.value
        self.__PREMIUM_SUV = PremiumBookingQuantity.SUV.value

    def book_vehicle(self, time: str, vehicle_type: str):
        if(self.check_timming(time, BookingConditions.MIN_RESERVE_TIME.value)):
            if(self.is_available(vehicle_type)):
                pass

    def check_timming(self, time: str, extra_time:int=0) -> bool:
        time = int(time)
        if(time <= TrackTimming.OPEN.value):
            print(GlobalResponses.INVALID_ENTRY_TIME.value)
            return Outcome.RET_NOT_OK.value
        if(time + extra_time >
            TrackTimming.CLOSE.value):
            print(GlobalResponses.INVALID_EXIT_TIME.value)
            return Outcome.RET_NOT_OK.value
        return Outcome.RET_OK.value
        

    def is_available(self, vehicle_type: str) -> bool:
        if(vehicle_type == RegularBookingQuatity.BIKE.name):
            if(self.is_bike_available()):
                pass

    def is_bike_available(self) -> bool:
        return self.__REGULAR_BIKE > 0

    def is_car_available(self) -> bool:
        return self.__


class Manager:

    def book(
        self, vehicle_type: str,
        vehicle_number: str, entry_time: str
        ) -> str:
        pass

    def extend_time(self, vehicle_number: str, time: str) -> str:
        pass

    def get_revenue(self):
        pass