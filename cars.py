"""
Car Module
@ChristianMorgado
"""

class Car:
    __slots__ = ["__vin", "__make", "__model", "__year", "__mileage", "__fuel"]

    def __init__(self, vin, make, model, year):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0.0
        self.__fuel = 0.0

    def filler_up(self, gallons):
        self.__fuel += gallons
        if self.__fuel > 15:
            self.__fuel = 15

    def drive(self, miles):
        if self.__fuel * 30 < miles:
            self.__mileage += self.__fuel * 30
            self.__fuel = 0
        else:
            self.__mileage += miles
            self.__fuel -= (miles / 30)

    def print_car(self):
        print("VIN: ", self.__vin, " Make: ", self.__make, " Model: ", self.__model, " Year: ", self.__year, " Mileage: ", self.__mileage, " Fuel: ", self.__fuel, sep = "")

    def __lt__(self, other):
        if type(self) == type(other):   #The type() function returns the TYPE of the object you are using
            return self.__vin < other.__vin
        else:
            return False

    def __eq__(self, other):
        if type(self) == type(other):   #The type() function returns the TYPE of the object you are using
            return self.__vin == other.__vin
        else:
            return False

    def __hash__(self):
        return hash(self.__vin)

    def __str__(self):
        return str(self.__year) + " " + self.__make + " " + self.__model + "."

    def __repr__(self):
        return "Car: " + "\nvin=" + self.__vin + "\nMake=" + self.__make + "\nModel=" + self.__model + "\nYear=" + str(self.__year) + "\nMileage=" + str(self.__mileage) + "\nFuel=" + str(self.__fuel)