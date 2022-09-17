from src.products import *
from src.constants import *

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
        self.products_list = []

    def add_item(self, product_name, qty):
        product = self.get_product(product_name)
        if(self.set_quantity(product, qty)):
            self.products_list.append(product)

    def get_product(self, product_name) -> IProducts:
        product = self.__products.get(product_name)
        return product()

    def set_quantity(self, product, qty) -> str:
        return product.set_quantity(qty)

    def get_subtotal(self) -> float:
        total = 0
        for product in self.products_list:
            total += product.get_total_cost()

        return total

    def get_discounted_value(self) -> float:
        total = 0.0
        for product in self.products_list:
            total += product.get_discount_price()
        return total
    
    def deduct_tax(self, total_amount) -> float:
        total_tax = total_amount * WAVIER_TAX_PERCENTAGE
        return total_amount + total_tax

    def print_bill(self) -> None:
        total_discount = 0.0
        total_amount = self.get_subtotal()
        if(total_amount >= MIN_PURCHASE_AMOUNT):
            total_discount = self.get_discounted_value()
        if(total_amount >= MIN_EXTRA_DISCOUNT_AMOUNT):
            total_discount += (total_amount * EXTRA_DISCOUNT_PERCENTAGE)
        total_amount -= total_discount
        print("TOTAL_DISCOUNT {0:.2f}".format(total_discount))
        print("TOTAL_AMOUNT_TO_PAY {0:.2f}".format(
            self.deduct_tax(total_amount))
        )
        