from abc import ABC
# from homework_02.exceptions import LowFuelError

class Strange(Exception):
    pass


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        #self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        #print(self.fuel)
        #print(self.started)

# добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`,
#     - то нужно проверить, что топлива больше нуля,
    def start(self, started):
        print ("20 started=", started, " fuel=",self.fuel)
        #if started == False and self.fuel == 0:
        if started == False and self.fuel == 0:
            print("Не достаточно топлива")
            #raise Strange("Не достаточно топлива")
            raise ValueError("Не достаточно топлива")
        else:
            car1.started = True
            print("25 car fuel=",self.fuel, "started=", self.started)

            # exceptions (LowFuelError)
        return ValueError

    def test_start_ok(self, fuel):
        print("30", car1.fuel)
        assert car1.fuel > 0
        assert car1.started is False




car1 = Vehicle(100,333,15)
#print(car1.fuel)
print("43",car1.start(False))
# print(car1.test_start_ok(10))
print("45",car1.start)
print(car1.started)

