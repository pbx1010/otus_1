"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    message = "LowFuel___Error"

class NotEnoughFuel(Exception):
    message = "NotEnoughFuel"

class CargoOverload(Exception):
    message = "CargoOverload"

    def fuuel(self,fuel):
        if fuel == 0:
            raise Exception("LowFuelError")

    def zerofuel(self,fuel):
        if fuel == 0:
            raise Exception("NotEnoughFuel")

    def overweight(self,cargo):
        if cargo > 10000:
            raise Exception("CargoOverload")