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
        self.pro_membership_fees = ConstantsEnum.PRO_MEMBERSHIP_FEE
        for course in programmes:
            discount = Discount[course.name].value * course.price
            course.price -= discount
            self.total_pro_discount += discount

    def apply_coupons(self, programmes, coupons):
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
        return total
    
    def print_bill(self, programmes, coupons):
        subtotal = self.get_subtotal(programmes)
        self.apply_coupons(programmes, coupons)
        print("Subtotal", subtotal)

class ProgrammeDetails:
    def __init__(self, title, qty):
        self.name = title
        self.qty = qty
        self.price = ProgramChargesEnum[title].value * qty    
