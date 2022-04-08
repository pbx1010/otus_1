from abc import ABC
#from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=800, started=True, fuel=1000, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

 #   добавьте метод start.При вызове этого метода необходимо проверить состояние started.И если не started, то
 #   нужно проверить, что топлива больше нуля, и  обновить состояние started, иначе нужно выкинуть  исключение exceptions.LowFuelError

    def start(self):
        if self.started != True:
            if self.fuel <= 0:
                print("Нет топлива")
                raise ValueError("Нет топлива")
        else:
            if self.fuel > 0:
                self.started = True

# добавьте метод `move`, который проверяет, что топлива достаточно для преодоления переданной дистанции
# (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает
# исключение `exceptions.NotEnoughFuel`

    def move(self, distance):
        if self.fuel-distance*self.fuel_consumption <0:
            raise ValueError("NotEnoughFuel")
        else:
            self.fuel -= distance*self.fuel_consumption


car2=Vehicle()
print(car2.weight)
print(car2.fuel)
car2.start()
car2.move(50)
print(car2.fuel)


