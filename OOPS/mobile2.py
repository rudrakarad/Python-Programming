
class Mobile:
    def __init__(self, brand, battery):
        self.brand =  brand
        self.battery = battery

    def call(self, minutes):
        if minutes <= 0:
            print("The call duration cannot be less then 1 minute")
            return
        else:
            battery_usage = minutes * 2
            self.battery -= battery_usage

        if self.battery <= 0:
            self.battery = 0
            print("Your device is switched off")

    def charge(self):
        self.battery = 100
        print("Battery charged to 100%")

    def display(self):
        print()
        print(f"The device is {self.brand}")
        print()
        print(f"The battery percent is  {self.battery}%")
        print()

obj = Mobile("Moto", 80)

obj.display()
obj.call(20)
obj.display()
obj.charge()
obj.display()