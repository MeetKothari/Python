
# A project into OOP I'm using to re-familiarize myself with a few of the core concepts.

import math

class Vehicle():

    def __init__(self, years, mpg, tire_age, miles_since_last):
        self.years = years # years since inital purchase
        self.mpg = mpg # mpg
        self.tire_age = tire_age # since last replaced, measured in years
        self.miles_since_last = miles_since_last # in miles, ofc

    def next_change_dad(self):
        6 - self.years # Tesla recommends getting your Model 3 serviced every six years
        return self.years

    def next_change_mom(self):
        self.years = float (self.years/6) * self.miles_since_last # cars begin to deterioate quicker after six years
        4000 - self.years # the 2007 sienna is recommended to get its oil changed every 4000 miles
        return self.years


    
moms_car = Vehicle(15, 19, 1/2, 4000)
dads_car = Vehicle(4, 138, 4, 40000)

print(moms_car.next_change_mom())
print(dads_car.next_change_dad())



