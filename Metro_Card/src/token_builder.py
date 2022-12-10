from .base import BaseToken
from typing import List


class MetroCard(BaseToken):

    def __init__(self, id: str, balance: int):
        super().__init__(id, balance)

    def deduct(self, amount: int) -> bool:
        return super().deduct(amount)

    def isEnoughBalance(self, required: int) -> int:
        return super().isEnoughBalance(required)

    def topUp(self, amount: int):
        return super().topUp(amount)


class TokenBuilder:

    def __init__(self):
        self._token_pool = dict()

    def getAllTokens(self) -> List:
        return [token for token in self._token_pool.values()]

    def addToken(self, token: BaseToken) -> bool:
        if token.getId() in self._token_pool:
            return False
        self._token_pool[token.getId()] = token
        return True

    def getToken(self, token_id: str) -> BaseToken:
        return self._token_pool.get(token_id)
