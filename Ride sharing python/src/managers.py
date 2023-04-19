from abc import ABC
from typing import Any, List, Union
from drivers.driver import ADriver
from riders.rider import ARider
from strategies.abstract import IStrategy


class IHashStoreManager(ABC):
    _objects = {}

    def add(self, key: Any, item: Any):
        self._objects[key] = item

    def get(self, key) -> Union(None, Any):
        return None if not self.is_present(key) else self._objects[key]

    def is_present(self, key: Any) -> bool:
        return True if key in self._objects else False


class IStrategableManager(ABC):
    _strategy: IStrategy

    def __init__(self, strategy: IStrategy):
        self.Strategy = strategy

    @property
    def Strategy(self) -> IStrategy:
        return self._strategy

    @Strategy.setter
    def Strategy(self, n_strategy: IStrategy):
        self._strategy = n_strategy


class DriverManager(IHashStoreManager, IStrategableManager):

    def match(self, n: int, rider: ARider) -> List[ADriver]:
        pass


class RidesManager(IHashStoreManager, IStrategableManager):
    billing_strategy: IStrategy

    def __init__(self, dist_strategy: IStrategy, bill_strategy: IStrategy):
        super.__init__(dist_strategy)
        self.billing_strategy = bill_strategy

    def bill(self, ride_id):
        self.billing_strategy.get_bill()


class RidersManager(IHashStoreManager):
    pass
