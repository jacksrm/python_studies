class Account:
    def __init__(self, number, cpf, owner_name, balance):
        self.number = number
        self.owner_name = owner_name
        self.balance = balance
        self.cpf = cpf

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def transfer_to(self, account, ammount):
        if self.balance < ammount:
            return False
        else:
            self.withdraw(ammount)
            account.deposit(ammount)
            return True

    def info(self):
        print("Account info: ")
        print(f"Number: {self.number}")
        print(f"Owner: {self.owner_name}")
        print(f"CPF: {self.cpf}")
        print(f"Balance: R$ {self.balance}")


account = Account(1, "123.456.789-00", "Jacson", 20000.43)
account.info()
account2 = Account(2, "123.123.123-11", "Pamela", 40000.55)
account2.info()

account.transfer_to(account2, 200)
account.info()
account2.info()
