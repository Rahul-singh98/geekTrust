from src.products import *


class Builder:
    def __init__(self):
        self.__products = {
            "TSHIRT" : TShirt,
            "JACKET" : Jacket,
            "CAP" : Cap,
            "NOTEBOOK" : Notebook,
            "PENS": Pens,
            "MARKERS" : Markers
        }

    def get_product(self, product_name):
        product = self.__products.get(product_name)
        return product()