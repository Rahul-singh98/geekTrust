# from src.constants import *

class IProducts:
    def __init__(self,  price, discount):
        self._price = price
        self._discount = discount
        self._max_purchase_qty = 0
        self._qty = 0

    def check_max_limit(self, qty) -> bool:
        return qty <= self._max_purchase_qty

    def set_quantity(self, qty) -> bool:
        if(self.check_max_limit(qty)):
            self._qty = qty
            print("ITEM_ADDED")
            return True
        else:
            print("ERROR_QUANTITY_EXCEEDED")
            return False

    def get_discount_price(self) -> float:
        return float(self.get_total_cost() * self._discount)

    def get_total_cost(self) -> float:
        return float(self._price * self._qty)


class ClothingPolicy(IProducts):
    def __init__(self, price, discount):
        super().__init__(price, discount)
        self._max_purchase_qty = 2


class StationaryPolicy(IProducts):
    def __init__(self, price, discount):
        super().__init__(price, discount)
        self._max_purchase_qty = 3


class TShirt(ClothingPolicy):
    def __init__(self):
        super().__init__(1000, 0.10)


class Jacket(ClothingPolicy):
    def __init__(self):
        super().__init__(2000, 0.05)


class Cap(ClothingPolicy):
    def __init__(self):
        super().__init__(500, 0.20)


class Notebook(StationaryPolicy):
    def __init__(self):
        super().__init__(200, 0.20)


class Pens(StationaryPolicy):
    def __init__(self):
        super().__init__(300, 0.10)

class Markers(IProducts):
    def __init__(self):
        super().__init__(500, 0.05)