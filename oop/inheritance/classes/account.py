from datetime import datetime
from zoneinfo import ZoneInfo

from classes.bank_statement import BankStatement
from classes.client import Client


class Account:
    def __init__(self, clients: Client, number, balance):
        self.number = number
        self.balance = balance
        self.clients = clients
        self.statement = BankStatement(self)

    def deposit(self, ammount):
        self.balance += ammount
        self.statement.transactions.append(
            ["Deposit", ammount, datetime.now(ZoneInfo("America/Fortaleza"))]
        )

    def withdraw(self, ammount):
        if self.balance < ammount:
            return False
        else:
            self.balance -= ammount
            self.statement.transactions.append(
                ["Withdraw", ammount, datetime.now(ZoneInfo("America/Fortaleza"))]
            )
            return True

    def transfer_to(self, account, ammount):
        if self.balance < ammount:
            return False
        else:
            self.balance -= ammount
            account.deposit(ammount)
            self.statement.transactions.append(
                ["Transfer", ammount, datetime.now(ZoneInfo("America/Fortaleza"))]
            )
            return True

    def info(self):
        print("Account info: ")
        print(f"Number: {self.number}")
        print(f"Balance: R$ {self.balance}")
