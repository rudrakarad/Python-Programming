
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self, percent):
        if percent <= 50:
            discount = self.price * percent / 100
            self.price -= discount
        else:
            print("Discount cannot exceed 50%")


    
    def display(self):
        print(f"The title of the book is {self.title}")
        print()
        print(f"The author of the book is {self.author}")
        print()
        print(f"The price of the book is {self.price:.2f} rs")
        print()

obj = Book("Learn Python", "Rudra", 1000)

obj.discount(50)
obj.display()

