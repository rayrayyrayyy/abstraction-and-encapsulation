# create car class
class Car:
    def __init__ (self, year_model = "", make = "", speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # define methods
    #getters
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    # setters
    def set_year_model(self, model):
        self.__year_model = model

    def set_make(self, make):
        self.__make = make

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5 

    # define function to show data
    def car_speed(self):
        print('\033[0;33m' + "Car's current speed:" + '\033[0m', self.__speed, 'kph')