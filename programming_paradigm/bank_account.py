class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    if __name__ == "__main__":
        def main():
            account = BankAccount(100)
            account.deposit(50)
            account.withdraw(30)
            print(account.get_balance())
        main()