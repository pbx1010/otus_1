class Car():
    """Описание автомобиля"""

    def __init__(self, brand, model, years):
        """Инициализирует атрибуты brand и model"""
        self.brand = brand
        self.model = model
        self.years = years
        self.mileage = 0

    def get_full_name(self):
        """Автомобиль"""
        name = f"Автомобиль {self.brand} {self.model} {self.years}"
        return name.title()

    def read_mileage(self):
        """Пробег автомобиля"""
        print(f"Пробег автомобиля {self.mileage} км.")

    def update_mileage(self, new_mileage):
        """Устанавливает новое значение пробега"""
        self.mileage = new_mileage

    def add_mileage(self, km):
        """Добавляет пробег"""
        self.mileage += km


class ElectricCar(Car):
    """Описывает электромобиль"""

    def __init__(self, brand, model, years):
        """Инициализирует атрибуты класса родителя"""
        super().__init__(brand, model, years)
        # атрибут класса-потомка
        self.battery_size = 100

    def battery_power(self):
        """Выводит мощность аккумулятора авто"""
        print(f"Мощность аккумулятора {self.battery_size} кВт⋅ч")

class ElectricCar(Car):
    """Описывает электромобиль"""
    def __init__(self, brand, model, years):
        """Инициализирует атрибуты класса родителя"""
        super().__init__(brand, model, years)
        # атрибут класса-потомка
        self.battery_size = 100

    def battery_power(self):
        """Выводит мощность аккумулятора авто"""
        print(f"Мощность аккумулятора {self.battery_size} кВт⋅ч")

    def get_full_name(self):
        """Автомобиль"""
        name = f"Автомобиль {self.brand} {self.model} {self.years} {self.battery_size}-кВт⋅ч "
        return name.title()

tesla_1 = ElectricCar('tesla', 'model x', 2021)
print(tesla_1.get_full_name())
tesla_1.battery_power()