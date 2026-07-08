
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            print("No marks available")
            return
        
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(f"The average marks of {self.name} are {avg}")

    def display(self):
        print(f"The name of the student is: {self.name}")
        print(f"The marks of the student are:")
        for mark in self.marks:
            print(mark)

obj = Student("Rudra")

obj.add_mark(80)
obj.add_mark(82)
obj.add_mark(79)
obj.add_mark(84)
obj.add_mark(77)
obj.add_mark(90)
obj.average()
obj.display()