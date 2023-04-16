from enum import Enum


class Fare(Enum):
    BASE_FARE = 50
    PER_KILOMETER = 6.5
    PER_MINUTE = 2
    SERVICE_TAX = 0.2
