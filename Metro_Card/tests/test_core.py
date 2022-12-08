from unittest import TestCase, main

import src
from src import MetroAuthority, PassengerCharges


class Test_MetroAuthority(TestCase):

    def setUp(self) -> None:
        self._authority = MetroAuthority()
        self.__id = "M1234"
        self.__balance = 500

        self._authority.addToken(self.__id, self.__balance)
        return super().setUp()

    def tearDown(self) -> None:
        del self._authority
        return super().tearDown()

    def test_addToken(self):
        t_id = "M4321"
        balance = 100
        self._authority.addToken(t_id, balance)

    def test_checkIn(self):
        self._authority.checkIn(self.__id, PassengerCharges.ADULT.name, 'CENTRAL')


if __name__ == "__main__":
    main()
