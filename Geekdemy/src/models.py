from abc import ABC, abstractmethod
from collections import defaultdict
from src.constants import *


class AbstractUser(ABC):
    """
        Abstract base class for user
    """
    def __init__(self):
        self._enrolled_programmes = defaultdict(lambda : [0, 0.00])
        self._total_purchased_courses = 0.00
        self._sub_total = 0.00
        self._total_pro_discount = 0.00
        self._pro_membership_fee = 0.00
        self._enrollment_fee = 0.00
        self._total = 0.00
        self._applied_coupon_cost = 0.00

        self._isPromember = False
        self._applied_coupon = None
        self._coupons_class = list()


    def addProgramme(self, category, quantity):
        """
            Add programme to the user.

            Args:
                category (str, Required): course category
                quantity (float, Required): Number of course 
                in which user wanted to enroll
        """
        self._total_purchased_courses += quantity
        self._enrolled_programmes[category][0] = quantity
        self._enrolled_programmes[category][1] += (
            quantity * ProgramCharges[category].value
        )


    def addCoupon(self, coupon_code):
        """
            Add coupons to the list.

            Args:
                coupon_code (str, Required): inputs str as parameter
                which need to be process later
        """
        self._coupons_class.append(coupon_code)

    def applyCoupon(self):
        """
            Applies coupon to the total_purchase
        """
        self.getSubtotal()

        if (self._applied_coupon == None 
            and  self._total_purchased_courses >= Constants.ATMOST_COURSES.value):
            self.applyB4G1()
        else:
            self._coupons_class.sort()
            for coupon_code in self._coupons_class:                
                if(self._applied_coupon == None
                    and coupon_code == Coupons.DEAL_G20.value
                    and self._sub_total >= Coupons.DEAL_G20_MINIMUM_AMOUNT.value):
                    self.applyCouponHelper(coupon_code)

                elif (self._applied_coupon == None
                    and coupon_code == Coupons.DEAL_G5.value
                    and self._total_purchased_courses >= Coupons.DEAL_G5_MINIMUM_COURSES.value):
                    self.applyCouponHelper(coupon_code)

        
    def getSubtotal(self):
        """
            Calculates the subtotal of the purchase
        """        
        for category in self._enrolled_programmes:
            amount = self._enrolled_programmes.get(category)[1]
            self._sub_total += amount

        if(self._sub_total < Constants.ENROLLMENT_THRESHOLD_AMOUNT.value):
            self._enrollment_fee = Constants.ENROLLMENT_FEE.value

        return self._sub_total

    def applyCouponHelper(self, coupon_name):
        """
            Apply Coupon
        """
        self._applied_coupon = Coupons[coupon_name].value
        self._applied_coupon_cost = self._sub_total * Discount[coupon_name].value
                

    def applyB4G1(self):
        """
           Apply the B4G1 Coupon
        """
        min_cost = 1000000007

        for category in self._enrolled_programmes:
            price = self._enrolled_programmes.get(category)[1]
            qty = self._enrolled_programmes.get(category)[0]

            if(min_cost > (price/qty)):
                min_cost = (price/qty)
        self._applied_coupon = Coupons.B4G1.value
        self._applied_coupon_cost = min_cost


    @abstractmethod
    def getTotal(self):
        """
            Abstract method which should be implemented
        """
        raise NotImplementedError