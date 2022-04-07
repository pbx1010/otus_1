from abc import ABC


class Vehicle(ABC):

    def __init__(self, weight=8000, started=True, fuel=400, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            pass
        https: // www.youtube.com / watch?v = -Zdu4ntX_DU


