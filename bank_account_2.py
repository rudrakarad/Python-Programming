

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.name,"Successfully deposited", amount,"$")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.name,"Successfully withrawed ", amount,"$")
        else:
            print("Insufficient Balance ")

    def check_balance(self):
        print("Your account balance is:",self.balance,"$")

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(self.name, "Successfully transferred ",amount,"$ to",other_account.name)
        else:
            print("Insufficient Balance")

b1 = BankAccount("Rudra", 1000)
b2 = BankAccount("Manali", 2000)
b1.check_balance()
b1.deposit(2000)