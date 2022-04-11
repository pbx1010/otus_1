"""
create dataclass `Engine`
создайте датакласс `Engine` в модуле `engine`, добавьте атрибуты `volume` и `pistons`
"""
class Engine():

    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons
