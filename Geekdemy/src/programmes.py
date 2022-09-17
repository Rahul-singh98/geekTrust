from operator import truediv
from src.constants import (
    Discount,
    ProgramChargesEnum,
    ConstantsEnum
)


class ManagementSystem:
    def __init__(self):
        self._programmes_list = []
        self._coupons_list = []
        self.total_pro_discount = 0
        self.pro_membership_fees = 0
        self.is_pro_member = False
        self.enrollment_fees = ConstantsEnum.ENROLLMENT_FEE.value
        self.coupon_name = None
        self.coupon_discount = 0

    def add_programme(self, programme):
        self._programmes_list.append(programme)

    def get_programme(self):
        return self._programmes_list

    def add_coupon(self, coupon):
        self._coupons_list.append(coupon)

    def get_coupons(self):
        return self._coupons_list

    def add_promembership(self, programmes):
        self.pro_membership_fees = ConstantsEnum.PRO_MEMBERSHIP_FEE.value
        # self.is_pro_member = True
        for course in programmes:
            discount = Discount[course.name].value * course.price
            course.price -= discount
            self.total_pro_discount += discount

    def apply_coupons(self, programmes, coupons):
        self.sub_total = self.apply_coupons(programmes)
        for coupon in coupons:
            if coupon.is_applicable(programmes):                                                                                                                                                                                                                                                                                                                                                                                                    
                self.coupon_discount = coupon.apply_coupon(
                    programmes
                )
                self.coupon_name = coupon.name
                break

    def get_subtotal(self, programmes):
        total = 0
        for course in programmes:
            total += course.price
        if total >= ConstantsEnum.ENROLLMENT_THRESHOLD_AMOUNT.value:
            self.enrollment_fees = 0
        total += (
            + self.total_pro_discount
            + self.pro_membership_fees
            + self.enrollment_fees
            - self.coupon_discount
        )
        return total

    def get_total(self):
        total = (        
            
        )
        return total

    def print_bill(self, programmes, coupons):
        print("SUB_TOTAL {0:.2f}".format(subtotal))
        print("COUPON_DISCOUNT {0} {1:.2f}".format(self.coupon_name, self.coupon_discount))
        print("TOTAL_PRO_DISCOUNT {0:.2f}".format(self.total_pro_discount))
        print("PRO_MEMBERSHIP_FEE {0:.2f}".format(self.pro_membership_fees))
        print("ENROLLMENT_FEE {0:.2f}".format(self.enrollment_fees))
        print("TOTAL {0:.2f}".format(self.get_total() + subtotal))

    @staticmethod
    def list_to_string(_list):
        """
            Converts list to string
            Args:
                _list (list): parameter which needed to 
                convert in string
            Return:
                string (str)
        """
        string = ""

        for _l in _list:
            if(_l is None):
                string += "NONE"
            elif(isinstance(_l, float)
                 or isinstance(_l, int)):
                string += "{0:.2f}".format(_l)
            else:
                string += _l
            string += " "

        return string[:-1]


class ProgrammeDetails:
    def __init__(self, title, qty):
        self.name = title
        self.qty = qty
        self.price = ProgramChargesEnum[title].value * qty
