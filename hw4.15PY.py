class Transport:

    def __init__(self, name, max_speed, mileage):

self.name = name
self.max_speed = max_speed
self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

# Создаем объект Autobus
autobus = Autobus("Междугородний", 100, 50000)

# Выводим значения его переменных
print(autobus.name)
print(autobus.max_speed)
print(autobus.mileage)