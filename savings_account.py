from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount > self.balance:
            return "insufficient funds"
        self.balance -= amount
        return f"withdrawn: {amount}, New Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"