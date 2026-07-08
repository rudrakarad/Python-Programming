
class Salary:
    def __init__(self, name, salary):
        self.name =  name
        self.salary = salary

    def salary_increment(self, percent):

        if 0 < percent <= 25:
            increment = self.salary * percent / 100
            self.salary += increment
        else:
            print("The salary cannot be incremented more than 25%")

    def display(self):
        print()
        print(f"The name of the employee is {self.name}")
        print()
        print(f"The salary of the employee is {self.salary} rs")
        print()

obj = Salary("Rudra", 10000000)

obj.display()
obj.salary_increment(20)
obj.display()