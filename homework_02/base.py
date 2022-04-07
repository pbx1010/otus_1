from abc import ABC
#from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=800, started=True, fuel=400, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started != True and self.fuel <= 0:
            raise ValueError ("Нет топлива")
        else:
            # raise LowFuelError
            #raise ValueError ("Нет топлива")
            if self.fuel > 0:
                self.started = True

    def move(self,distance):
        if self.fuel-distance*self.fuel_consumption <0:
            raise ValueError("NotEnoughFuel")
        else:
            self.fuel -= distance*self.fuel_consumption


car2=Vehicle()
print(car2.weight)

