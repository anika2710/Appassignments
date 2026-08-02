# Decorator
def showroom_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 35)
        print("   VEHICLE SHOWROOM")
        print("=" * 35)
        func(*args, **kwargs)
        print("=" * 35)
    return wrapper


# Vehicle Class
class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    @showroom_header
    def display(self):
        print("Vehicle Number :", self.number)
        print("Brand :", self.brand)
        print("Price :", self.price)

        if self.price >= 1000000:
            print("Category : Luxury")
        else:
            print("Category : Economy")


# Showroom Class
class Showroom:
    def add_vehicle(self, vehicle):
        print("Vehicle Added Successfully!\n")

    def display_vehicle(self, vehicle):
        vehicle.display()


# Main Program
v1 = Vehicle("MH42BN6993", "Defender", 11000000)

showroom = Showroom()
showroom.add_vehicle(v1)
showroom.display_vehicle(v1)


"""
===================================
   VEHICLE SHOWROOM
===================================
Vehicle Number : MH42BN6993
Brand : Defender
Price : 11000000
Category : Luxury
===================================
"""