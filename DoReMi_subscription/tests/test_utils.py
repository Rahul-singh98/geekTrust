import unittest
from src.utils.date import (validate_date, get_renewal_reminder_date)


class TestDateModule(unittest.TestCase):

    def test_validate_test(self):
        empty_string_date = ''
        wrong_format_string = '06-24-2023'
        wrong_format_string_2 = '06/24/2023'
        correct_format_string = '24-06-2023'

        self.assertFalse(validate_date(empty_string_date))
        self.assertFalse(validate_date(wrong_format_string))
        self.assertFalse(validate_date(wrong_format_string_2))
        self.assertTrue(validate_date(correct_format_string))

    def test_get_renewal_reminder_date(self):
        wrong_renewal_reminder_format = ['', 0]
        correct_renewal_reminder_format = ['24-06-2023', 3]

        self.assertEqual(
            get_renewal_reminder_date(
                wrong_renewal_reminder_format[0],
                wrong_renewal_reminder_format[1]
            ), ''
        )

        self.assertEqual(
            get_renewal_reminder_date(
                correct_renewal_reminder_format[0],
                correct_renewal_reminder_format[1]
            ), '14-09-2023'
        )


if __name__ == '__main__':
    unittest.main()
