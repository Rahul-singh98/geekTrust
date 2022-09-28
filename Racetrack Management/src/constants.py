from enum import Enum


class TrackTypes(Enum):
    REGULAR, PREMIUM = 0, 1


class RegularBookingQuatity(Enum):
    BIKE, CAR, SUV = 4, 2, 1


class RegularBookingRates(Enum):
    BIKE, CAR, SUV = 60, 120, 250


class PremiumBookingQuantity(Enum):
    CAR, SUV = 2, 1


class PremiumBookingRates(Enum):
    CAR, SUV = 200, 300


class TrackTimming(Enum):
    OPEN, CLOSE = 1300, 1700


class BookingConditions(Enum):
    MIN_RESERVE_TIME, BEYOND_CHARGES = 300, 50


class GlobalResponses(Enum):
    SUCCESS = "SUCCESS"
    RACETRACK_FULL = "RACETRACK_FULL"
    INVALID_ENTRY_TIME = "INVALID_ENTRY_TIME"
    INVALID_EXIT_TIME = "INVALID_EXIT_TIME"
