# 6. Bank System

class BankAccount:
    def info(self):
        print("Bank Account")

class SavingsAccount(BankAccount):
    def info(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def info(self):
        print("Current Account")

s = SavingsAccount()
c = CurrentAccount()

s.info()
c.info()