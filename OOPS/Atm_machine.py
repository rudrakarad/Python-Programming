
class Atm:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        else:
            return False

    def deposit(self, pin, amount):
        if self.check_pin(pin):
            if amount > 0:
                self.balance += amount
                print(f"Successfully deposited {amount} rs")
            else:
                print("The amount should be greater than 0")
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if self.check_pin(pin):
            if amount <= 0:
                print("Invalid amount")
            elif 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrawed {amount} rs")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")

    def check_balance(self, pin):
        if self.check_pin(pin):
            print(f"Your account balance is {self.balance} rs")
        else:
            print("Invalid PIN")
            
obj = Atm(1234, 5000)

obj.check_balance(1234)
obj.deposit(1234,1000)
obj.withdraw(1234,2000)
obj.check_balance(1234)