from src.constants import *

class IProducts:
    def __init__(
            self,  price, 
            discount, qty,
            category=Category.Clothing
        ):
        self.__price = price
        self.__discount = discount
        self.__qty = qty
        self.__category = category


class TShirt(IProducts):
    def __init__(self, qty):
        super().__init__(TShirtEnum.price, TShirtEnum.discount, qty)


class Jacket(IProducts):
    def __init__(self, qty):
        super().__init__(JacketEnum.price, JacketEnum.discount, qty)


class Cap(IProducts):
    def __init__(self, qty):
        super().__init__(CapEnum.price, CapEnum.discount, qty)


class Notebook(IProducts):
    def __init__(self, qty):
        super().__init__(
            NotebookEnum.price, NotebookEnum.discount,
            qty, Category.Stationary
        )


class Pens(IProducts):
    def __init__(self, qty):
        super().__init__(
            PensEnum.price, PensEnum.discount,
            qty, Category.Stationary
        )

class Markers(IProducts):
    def __init__(self, qty):
        super().__init__(
            MarkersEnum.price, MarkersEnum.discount, 
            qty, Category.Stationary
        )