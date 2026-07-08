
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def display_brand(self):
        print(f"Brand: {self.brand}")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_details(self):
        self.display_brand()
        print(f"Model: {self.model}")


obj = Car("BMW", "M4")

obj.display_details()