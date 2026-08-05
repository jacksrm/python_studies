class BankStatement:
    def __init__(self, account):
        self.transactions = []
        self.account = account

    def generate_statement(self):
        print(f"Bank Statement for account: {self.account}")
        for transaction in self.transactions:
            print(
                f"{transaction[0]:15s} {transaction[1]:10.2f} {transaction[2].strftime('%d/%b/%Y')}"
            )

        print(f"Balance: R${self.account.balance} \n")
