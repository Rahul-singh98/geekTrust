from typing import Any


class SingletonMeta:
    instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.instance is None:
            self.instance = self()

        return self.instance


class Track(metaclass=SingletonMeta):
    def get_available_track(self):
        pass


class Vehicle:

    def __init__(
        self, vehicle_type: str,
        vehicle_number: str, entry_time: str
        ) -> str:
        pass


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