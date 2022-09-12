import unittest
from src import Subscriptions 
from src.constants import *

class TestRunner(unittest.TestCase):

    def setUp(self) -> None:
        # print("SetUp initiated")
        self.test_obj_1 = Subscriptions()
        self.test_obj_2 = Subscriptions()
        self.test_obj_1.stringToDatetime("02-02-2022")
        self.test_obj_2.stringToDatetime("02-19-2022")

    def test_stringToDatetime(self):
        # print("Testing stringToDatetime method")
        self.assertEqual(self.test_obj_1.stringToDatetime("20-02-2022"), VALID_DATE)
        self.assertEqual(self.test_obj_1.stringToDatetime("20-19-2022"), INVALID_DATE)

    def test_add_subscription(self):
        # print("Testing AddSubscriptions")
        self.assertEqual(self.test_obj_1.add_subscription("MUSIC", "FREE"), VALID)
        self.assertEqual(self.test_obj_2.add_subscription("MUSIC", "FREE"), SUBSCRIPTION_INVALID_DATE)
        self.assertEqual(self.test_obj_1.add_subscription("MUSIC", "FREE"), DUPLICATE_CATEGORY)

    def test_add_topup(self):
        # print("Testing topUpSubscription")
        self.assertEqual(self.test_obj_2.add_topup("FOUR_DEVICE" , 3), TOPUP_INVALID_DATE)
        self.assertEqual(self.test_obj_1.add_topup("FOUR_DEVICE" , 3), TOPUP_NO_SUSCRIPTION)
        self.test_obj_1.add_subscription("MUSIC", "FREE")
        self.assertEqual(self.test_obj_1.add_topup("FOUR_DEVICE" , 3), VALID)
        self.assertEqual(self.test_obj_1.add_topup("FOUR_DEVICE" , 3), DUPLICATE_TOPUP)

    def test_print_renewal_details(self):
        # print("Testing printRenewalDetails")
        self.assertEqual(self.test_obj_1.print_renewal_details() , SUBSCRIPTIONS_NOT_FOUND)

if __name__ == "__main__":
    unittest.main()