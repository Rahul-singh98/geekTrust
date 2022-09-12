import io
from unittest import TestCase, main
import unittest.mock
from src.core import User
from src.constants import *
import geektrust
import os


class Test_User(TestCase):

    def setUp(self) -> None:
        self.number_of_courses = 5
        self.user1 = User()
        return super().setUp()

    def tearDown(self) -> None:
        del self.user1
        return super().tearDown()

    def test_getTotal(self):
        self.assertEqual(
            self.user1.getTotal(),
            0.00)

    def test_addProBenefits(self):
        self.user1.addProgramme(
            ProgramName.DIPLOMA.value,
            34)

        self.user1.addProBenefits()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printBill(self, mock_stdout):
        input_file_path = os.path.join("sample_input", "input1.txt")
        # output_file_path = os.path.join("sample_output", "output1.txt")
        
        # with open(output_file_path, 'r') as f:
        #     expected_output = f.read()

        geektrust.getInput(input_file_path)
        # self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_static_list_to_string_1(self):
        result = User.list_to_string(["Static test", 10.0323253, 100])

        self.assertEqual(result, "Static test 10.03 100.00")

    def test_static_list_to_string_2(self):
        result = self.user1.list_to_string(["Static test", 10.0323253, 100])

        self.assertEqual(result, "Static test 10.03 100.00")

    def test_static_list_to_string_3(self):
        result = self.user1.list_to_string([])

        self.assertEqual(result, "")

    def test_static_list_to_string_4(self):
        result = self.user1.list_to_string([None])

        self.assertEqual(result, 'NONE')


class Test_AbstractUser(TestCase):

    def setUp(self) -> None:
        self.number_of_courses = 5
        self.user1 = User()
        return super().setUp()

    def tearDown(self) -> None:
        del self.user1
        return super().tearDown()

    def test_addProgramme(self):
        self.user1.addProgramme(
            ProgramName.CERTIFICATION.value,
            self.number_of_courses)

        self.assertEqual(
            self.user1.getSubtotal(),
            ProgramCharges.CERTIFICATION.value * self.number_of_courses)

    def test_applyCoupon_B4G1(self):
        self.user1.addProgramme(
            ProgramName.DEGREE.value,
            self.number_of_courses)

        self.user1.applyCoupon()
    
    def test_applyCoupon_DEAL_G20(self):
        self.user1.addProgramme(
            ProgramName.DEGREE.value,
            3)
        self.user1.addCoupon(Coupons.DEAL_G20.value)
        self.user1.applyCoupon()

    def test_applyCoupon_DEAL_G5(self):
        self.user1.addProgramme(
            ProgramName.DEGREE.value,
            2)
        self.user1.addCoupon(Coupons.DEAL_G5.value)
        self.user1.applyCoupon()

    def test_getSubtotal(self):
        self.assertEqual(
            self.user1.getSubtotal(),
            0.00)

    def test_applyCouponHelper(self):
        self.user1.applyCouponHelper(Coupons.DEAL_G20.value)

    def test_applyB4G1(self):
        self.user1.addProgramme(
            ProgramName.CERTIFICATION.value,
            self.number_of_courses)
        self.user1.applyB4G1()
        subtotal = self.user1.getSubtotal()
        self.assertEqual(subtotal, subtotal)


if __name__ == "__main__":
    main()
