from enum import Enum

MAX_CLOTHING_ITEMS_QTY = 2
MAX_STATIONARY_ITEMS_QTY = 3
MIN_PURCHASE_AMOUNT = 1000
MIN_EXTRA_DISCOUNT_AMOUNT = 3000
EXTRA_DISCOUNT_PERCENTAGE = 0.05
WAVIER_TAX_PERCENTAGE = 0.1


class Category(Enum):
    Clothing, Stationary = 1, 2


class TShirtEnum(Enum):
    price, discount = 1000, 0.10


class JacketEnum(Enum):
    price, discount = 2000, 0.05


class CapEnum(Enum):
    price, discount = 500, 0.20


class NotebookEnum(Enum):
    price, discount = 200, 0.20


class PensEnum(Enum):
    price, discount = 300, 0.10


class MarkersEnum(Enum):
    price, discount = 500, 0.05

