class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Honda", "City")
car2 = Car("Toyota", "Fortuner")

print(car1.brand)
print(car2.model)