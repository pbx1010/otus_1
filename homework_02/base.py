from abc import ABC


class Vehicle(ABC):

    def __init__(self, weight=8000, started=True, fuel=400, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started != True and self.fuel <= 0:
            raise ValueError("Нет топлива")
        else:
            # raise LowFuelError
            raise ValueError("Нет топлива")


