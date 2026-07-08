
class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"The name of the student is {self.name}")
        print(f"The age of the student is {self.age}")
        print(f"The marks of the student are {self.marks}%")

    def is_pass(self):
        if self .marks >= 40:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")

obj1 = Student("Rudra",17,83)
obj2 = Student("Aryan",17,35)

obj1.display()
obj1.is_pass()
obj2.display()
obj2.is_pass()