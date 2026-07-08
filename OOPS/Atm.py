
class Atm:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Incorrect Old Pin")

    def check_pin(self, pin):
        if self.__pin == pin:
            print("Correct Pin")
        else:
            print("Incorrect Pin")

obj = Atm(1234)

obj.change_pin(1234, 2009)
obj.check_pin(2009)