from abc import ABC
from src.location import Location


class ARider(ABC):
    """Abstract Rider class which is used to reduce the dependency
    of concrete class. So, that if in future some requirement changed
    then we won't depend on concrete class."""

    def __init__(self, id: str, location: Location):
        self._id = id
        self._location = Location


class Rider(ARider):
    pass
