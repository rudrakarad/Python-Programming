
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("Successfully deposited", amount,"$")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Successfully withrawed ", amount,"$")
        else:
            print("Insufficient Balance ")

    def check_balance(self):
        print("Your account balance is:",self.balance,"$")

b1 = BankAccount("Rudra", 1000)
b1.check_balance()
b1.deposit(2000)
b1.withdraw(1500)
b1.check_balance()