from unittest import TestCase, main

import src
from src import token_builder


class Test_TokenBuilder(TestCase):

    def setUp(self) -> None:
        self._token_builder = token_builder.TokenBuilder()
        self._token1 = src.MetroCard("M1234", 500)
        self._token2 = src.MetroCard("M4321", 100)
        self._token_builder.addToken(self._token1)
        return super().setUp()

    def tearDown(self) -> None:
        del self._token1
        del self._token2
        del self._token_builder
        return super().tearDown()

    def test_addToken(self):
        self.assertTrue(
            self._token_builder.addToken(self._token2))

    def test_addToken2(self):
        self.assertFalse(
            self._token_builder.addToken(self._token1))

    def test_gettoken(self):
        self.assertIsNotNone(self._token_builder.getToken(self._token1.getId()))

    def test_getAlltokens(self):
        sz = len(self._token_builder.getAllTokens())
        self.assertEqual(sz, 1)


if __name__ == "__main__":
    main()
