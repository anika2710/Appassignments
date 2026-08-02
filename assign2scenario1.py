# Decorator
def movie_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 35)
        print("      MOVIE DETAILS")
        print("=" * 35)
        func(*args, **kwargs)
        print("=" * 35)
    return wrapper


# Movie Class
class Movie:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price

    @movie_header
    def display(self):
        print("Movie Name :", self.name)
        print("Rating :", self.rating)
        print("Ticket Price :", self.price)

        if self.rating >= 8:
            print("Category : Hit")
        elif self.rating >= 5:
            print("Category : Average")
        else:
            print("Category : Flop")


# Cinema Class
class Cinema:
    def display_movie(self, movie):
        movie.display()


# Main Program
m1 = Movie("Doomsday", 10, 700)

cinema = Cinema()
cinema.display_movie(m1)


"""
===================================
      MOVIE DETAILS
===================================
Movie Name : Doomsday
Rating : 10
Ticket Price : 700
Category : Hit
===================================
"""