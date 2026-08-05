from datetime import datetime
from zoneinfo import ZoneInfo

from classes.account import Account
from classes.client import Client


class SpecialAccount(Account):
    def __init__(self, clients: Client, number, balance, limit):
        super().__init__(clients, number, balance)
        self.limit = limit

    def withdraw(self, ammount):
        if (self.balance + self.limit) < ammount:
            return False
        else:
            self.balance -= ammount
            if self.balance < 0:
                self.limit += self.balance
            self.statement.transactions.append(
                [
                    "withdraw",
                    ammount,
                    datetime.now(ZoneInfo("America/Fortaleza")),
                ]
            )
            return True
