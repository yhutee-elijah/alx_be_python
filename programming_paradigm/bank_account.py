class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current Balance: {self.get_balance()}")
    
if __name__ == "__main__":
    def main():
        account = BankAccount(100)
        account.deposit(50)
        account.withdraw(30)
        account.display_balance()
    main()