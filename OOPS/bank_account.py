
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


acc = BankAccount("Rudra", 5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.show_balance()
