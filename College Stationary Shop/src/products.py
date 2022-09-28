from src.constants import *

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
            return True
        else:
            return False

    def get_discount_price(self) -> float:
        return float(self.get_total_cost() * self._discount)

    def get_total_cost(self) -> float:
        return float(self._price * self._qty)


class ClothingPolicy(IProducts):
    def __init__(self, price, discount):
        super().__init__(price, discount)
        self.set_max_limit()

    def set_max_limit(self):
        self._max_purchase_qty = MAX_CLOTHING_ITEMS_QTY


class StationaryPolicy(IProducts):
    def __init__(self, price, discount):
        super().__init__(price, discount)
        self.set_max_limit()

    def set_max_limit(self):
        self._max_purchase_qty = MAX_STATIONARY_ITEMS_QTY


class TShirt(ClothingPolicy):
    def __init__(self):
        super().__init__(
            TShirtEnum.price.value, 
            TShirtEnum.discount.value
        )


class Jacket(ClothingPolicy):
    def __init__(self):
        super().__init__(
            JacketEnum.price.value, 
            JacketEnum.discount.value
        )


class Cap(ClothingPolicy):
    def __init__(self):
        super().__init__(
            CapEnum.price.value, 
            CapEnum.discount.value
        )


class Notebook(StationaryPolicy):
    def __init__(self):
        super().__init__(
            NotebookEnum.price.value, 
            NotebookEnum.discount.value
        )


class Pens(StationaryPolicy):
    def __init__(self):
        super().__init__(
            PensEnum.price.value, 
            PensEnum.discount.value
        )

class Markers(StationaryPolicy):
    def __init__(self):
        super().__init__(
            MarkersEnum.price.value, 
            MarkersEnum.discount.value
        )