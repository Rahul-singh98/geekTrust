from src.constants import (
    ProgramChargesEnum,
    CouponsEnum, 
    ConstantsEnum
)
from abc import ABC, abstractmethod

class Coupons(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_coupon(self, programmes):
        raise NotImplementedError
    
    @abstractmethod
    def is_applicable(self, programme):
        raise NotImplementedError


class Coupon_B4G1(Coupons):
    def __init__(self, name):
        super().__init__(name)

    def is_applicable(self, programmes):
        total_quantity = 0
        for course in programmes:
            total_quantity += course.qty

        return total_quantity >= ConstantsEnum.ATMOST_COURSES.value

    def apply_coupon(self, programmes):
        return self.get_lowest_value_course(programmes)

    def get_lowest_value_course(self, programmes):
        min_course_value = 1e9
        for course in programmes:
            course_price = course.price / course.qty
            if(min_course_value > course_price):
                min_course_value = course_price
        return 0 if min_course_value == 1e9 else min_course_value


class CouponCostPolicy:
    def get_total_cost(self, programmes):
        cost = 0
        for course in programmes:
            cost += course.price
        return cost
        

class Coupon_G20(Coupons, CouponCostPolicy):
    def __init__(self, name):
        Coupons.__init__(self, name)
        
    def is_applicable(self, programmes):
        cost = CouponCostPolicy.get_total_cost(self, programmes)
        return cost >= CouponsEnum.DEAL_G20_MINIMUM_AMOUNT.value
        
    def apply_coupon(self, programmes):
        cost = self.get_total_cost(programmes)
        return float(CouponsEnum.DEAL_G20_DISCOUNT.value * cost)
    
    

class Coupon_G5(Coupons, CouponCostPolicy):
    def __init__(self, name):
        Coupons.__init__(self, name)
        
    def is_applicable(self, programmes):
        count = self.get_total_courses(programmes)
        return count >= CouponsEnum.DEAL_G5_MINIMUM_COURSES.value

    def apply_coupon(self, programmes):
        cost = CouponCostPolicy.get_total_cost(self, programmes)
        return float(cost * CouponsEnum.DEAL_G5_DISCOUNT.value)

    def get_total_courses(self, programmes):
        count = 0
        for course in programmes:
            count += course.qty
        return count
