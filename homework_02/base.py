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
        self.started = True

 #   добавьте метод start.При вызове этого метода необходимо проверить состояние started. И если не started, то
 #   нужно проверить, что топлива больше нуля, и  обновить состояние started, иначе нужно выкинуть  исключение exceptions.LowFuelError
#     def test_start_ok(self, vehicle):
    #         assert vehicle.fuel > 0
    #         assert vehicle.started is False
    #         vehicle.start()
    #         assert vehicle.started is True

    def start(self,started):
        if not started:
            if self.fuel <= 0:
                started = False
                #print("Нет топлива")
                raise LowFuelError()
            else:
                started = True
                print(32)
        if started:
            if self.fuel <= 0:
                started = False
                #print("Нет топлива")
                raise LowFuelError()


# добавьте метод `move`, который проверяет, что топлива достаточно для преодоления переданной дистанции
# (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает
# исключение `exceptions.NotEnoughFuel`

    def move(self, distance):
        if self.fuel-distance*self.fuel_consumption < 0:
            raise NotEnoughFuel("NotEnoughFuel")
        else:
            self.fuel -= distance*self.fuel_consumption


#class Car(Vehicle):

#    def __init__(self,engine="disel"):
#        self.engine=engine




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
