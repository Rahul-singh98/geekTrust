from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List
from .constants import MetroCharges, PassengerCharges


class BaseToken(ABC):

    def __init__(self, id: str, balance: int):
        self._id = id
        self._balance = balance

    def __str__(self) -> str:
        return self._id

    def __eq__(self, __o: object) -> bool:
        return self.getId() == __o.getId()

    def getId(self):
        return self._id

    def getBalance(self):
        return self._balance

    @abstractmethod
    def deduct(self, amount: int) -> bool:
        if self.isEnoughBalance(amount) < 0:
            return False
        self._balance -= amount
        return True

    @abstractmethod
    def isEnoughBalance(self, required: int) -> int:
        return self.getBalance() - required

    @abstractmethod
    def topUp(self, amount: int):
        self._balance += amount


class BaseStation(ABC):

    def __init__(self, name: str):
        self._name = name
        self._earnings = 0
        self._discounts_given = 0
        self._passengers = defaultdict(lambda: 0)

    def __str__(self) -> str:
        return self._name

    def getName(self) -> str:
        return self._name

    def getEarnings(self) -> int:
        return self._earnings

    def getDiscountsGiven(self) -> int:
        return self._discounts_given

    def getPassengersList(self) -> List:
        passengers_list = []
        for pType, pCount in self._passengers.items():
            passengers_list.append([pType, pCount])
        passengers_list.sort()
        return passengers_list

    def addDiscountAmount(self, amount: int):
        self._discounts_given += amount

    def addEarnings(self, amount: int):
        self._earnings += int(amount)

    def checkAndTopup(self, token: BaseToken, fees: int):
        if token.isEnoughBalance(fees) < 0:
            remaining = fees - token.getBalance()
            token.topUp(remaining)
            self.addEarnings(
                remaining * MetroCharges.SERVICE_PCT_FEES.value)

    @abstractmethod
    def addPassenger(self, token: BaseToken, passenger_type: PassengerCharges, discount: int):
        name = passenger_type.name
        fees = passenger_type.value - discount
        self.checkAndTopup(token, fees)

        self._passengers[name] += 1
        token.deduct(fees)
        self.addDiscountAmount(discount)
        self.addEarnings(fees)

    @abstractmethod
    def printSummary(self):
        raise NotImplemented
