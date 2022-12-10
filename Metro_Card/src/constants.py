from enum import Enum


class MetroCharges(Enum):
    SERVICE_PCT_FEES, DISCOUNT_PCT = 0.02, 0.5


class PassengerCharges(Enum):
    ADULT, SENIOR_CITIZEN, KID = 200, 100, 50


class InputPrefix(Enum):
    BALANCE = "BALANCE"
    CHECK_IN = "CHECK_IN"
    PRINT_SUMMARY = "PRINT_SUMMARY"


class BalanceIndexes(Enum):
    ID, AMT = 1, 2


class CheckInIndexes(Enum):
    T_ID, P_TYPE, S_NAME = 1, 2, 3


class OutputPrefix(Enum):
    TOTAL_COLLECTION = "TOTAL_COLLECTION"
    PASSENGER_TYPE_SUMMARY = "PASSENGER_TYPE_SUMMARY"
