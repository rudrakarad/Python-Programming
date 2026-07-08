
class MovieTicket:
    def __init__(self,movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_ticket(self, seats):
        if seats <= 0:
            print("Invalid  number of seats")
        elif seats <= self.available_seats():
            self.booked_seats += seats
            print(f"{seats} booked successfully")
        else:
            print("Not enough seats available")
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
        
    def  display(self):
        print(f"The name of the movie is {self.movie_name}")
        print(f"The total number of seats are {self.total_seats}")
        print(f"The number of seats booked are {self.booked_seats}")
        print(f"{self.available_seats()} seats are available ")

obj = MovieTicket("Avengers", 250)

obj.display()
obj.book_ticket(4)
obj.book_ticket(10)
obj.book_ticket(5)
obj.book_ticket(2)
obj.available_seats()
obj.display()