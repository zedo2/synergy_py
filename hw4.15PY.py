# Задание 1
class Transport:

    def __init__(self, name, max_speed, mileage):

self.name = name
self.max_speed = max_speed
self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Создаем объект Autobus
autobus = Autobus("Mersedes", 100, 50000)

# Выводим значения его переменных
print(f"Название автомобиля: {autobus.name}, Скорость: {autobus.max_speed}, Пробег: {autobus.mileage}")


# Задание 2

# Выводим значение
print(autobus.seating_capacity())