
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        return(self.__salary)


obj = Employee("Rudra", 100000)
print(obj.get_salary())
obj.set_salary(150000)
print(obj.get_salary())
