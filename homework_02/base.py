from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

#- доработайте базовый класс `base.Vehicle`:
#- добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
#- добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`

class Vehicle(ABC):

    def __init__(self, weight=800, fuel=1000, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

 #   добавьте метод start.При вызове этого метода необходимо проверить состояние started. И если не started, то
 #   нужно проверить, что топлива больше нуля, и  обновить состояние started, иначе нужно выкинуть  исключение exceptions.LowFuelError

    def start(self):
        if self.fuel <= 0:
            self.started = False
            raise LowFuelError()
        else:
            self.started = True

# добавьте метод `move`, который проверяет, что топлива достаточно для преодоления переданной дистанции
# (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает
# исключение `exceptions.NotEnoughFuel`

    def move(self, distance):
        if self.fuel-distance*self.fuel_consumption < 0:
            raise NotEnoughFuel("NotEnoughFuel")
        else:
            self.fuel -= distance*self.fuel_consumption


#car2=Vehicle()
#print(car2.weight)
#print(car2.fuel)
#car2.start(False)
#print(car2.started)
#car2.move(50)
#print(car2.fuel)
#car3=Car()
#print(car3.engine)
#print(car3.fuel)
