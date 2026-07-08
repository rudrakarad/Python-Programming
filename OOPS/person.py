
class Person:
    def introduce(self):
        print("Hello i am a person")


class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student")


obj = Student()
obj.introduce()
