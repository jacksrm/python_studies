from classes.account import Account
from classes.client import Client
from classes.special_account import SpecialAccount

client1 = Client("234", "Pedro", "Rua A")
client2 = Client("567", "Robert", "Rua B")
client3 = Client("890", "Julia", "Rua C")

account1 = Account(client1, 1, 2000)
account2 = Account(client2, 2, 2000)
account3 = SpecialAccount(client3, 3, 1000, 2000)

account1.deposit(300)
account1.transfer_to(account2, 500)

account2.withdraw(700)

account3.deposit(800)
account3.withdraw(2000)

account1.statement.generate_statement()
account2.statement.generate_statement()
account3.statement.generate_statement()
