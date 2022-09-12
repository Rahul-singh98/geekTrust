from src.models import AbstractUser
from src.constants import *

class User(AbstractUser):

    def __init__(self):
        super().__init__()
    
    def getTotal(self):
        """
            Calculates the total.
        """
        self._total = self._sub_total - self._applied_coupon_cost \
                    + self._enrollment_fee
        
        return self._total

    def addProBenefits(self):
        """
            Promote member to pro user
        """
        for category in self._enrolled_programmes:
            amount = self._enrolled_programmes.get(category)[1]
                        
            discount = (amount 
                * Discount[category].value)
            self._enrolled_programmes[category][1] = amount - discount

            self._total_pro_discount += discount
        
        self._pro_membership_fee = Constants.PRO_MEMBERSHIP_FEE.value
        self._sub_total += self._pro_membership_fee


    def printBill(self, output_filepath=None):
        """
            Print Bill.            
            Args: 
                output_filepath (str, Optional) = Output file 
                path is optional, Default is none.
        """
        self.applyCoupon()
        self.getTotal()

        print(self.list_to_string([
                OutputFormat.SUB_TOTAL.value,
                self._sub_total]))
        print(self.list_to_string([
                OutputFormat.COUPON_DISCOUNT.value,
                self._applied_coupon,
                self._applied_coupon_cost]))
        print(self.list_to_string([
                OutputFormat.TOTAL_PRO_DISCOUNT.value,
                self._total_pro_discount]))
        print(self.list_to_string([
                OutputFormat.PRO_MEMBERSHIP_FEE.value,
                self._pro_membership_fee ]))
        print(self.list_to_string([
                OutputFormat.ENROLLMENT_FEE.value,
                self._enrollment_fee ]))
        print(self.list_to_string([
            OutputFormat.TOTAL.value,
            self._total ]))

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