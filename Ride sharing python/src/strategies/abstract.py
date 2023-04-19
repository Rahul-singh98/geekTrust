from abc import ABC
from rides.ride import ARide
from abc import ABC
from riders.rider import ARider
from drivers.driver import ADriver
from typing import List


class IStrategy(ABC):
    pass


class IBillingStrategy(IStrategy, ABC):
    def get_bill(self, ride: ARide):
        pass


class IDistanceStrategy(IStrategy, ABC):

    def find_first_n(self, n: int, rider: ARider, drivers: List[ADriver]):
        pass
