class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.balance -= amount
        return True
    else:
        return False

def display_balance(self):
    print(f"current balance: ${self.account_balance:.2f}")
