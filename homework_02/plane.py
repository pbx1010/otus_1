"""
создайте класс `Plane`, наследник `Vehicle`
 в модуле `plane` создайте класс `Plane`
    - класс `Plane` должен быть наследником `Vehicle`
    - добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    - добавьте `max_cargo` в инициализатор (переопределите родительский)
    - объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение, в ином случае выкидывает исключение `exceptions.CargoOverload`
    - объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления

"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = None

    def load_cargo(self,cargo_weight):
        CargoOverload
