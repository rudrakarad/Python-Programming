
class Mobile:
    def __init__(self, battery):
        self.__battery = battery

    def charge(self, amount):
        self.amount = amount
        if amount + self.__battery <= 100:
            self.__battery += amount
        else:
            print("Battery cannot exceed 100%")
    
    def show_battery(self):
        print(f"The battery is {self.__battery}% charged")

obj = Mobile(69)

obj.show_battery()
obj.charge(20)
obj.show_battery()
