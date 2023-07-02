# Задание 1
class CashRegister:
    def __init__(self, money):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            raise ValueError("Недостаточно денег в кассе.")

# Создаем объект CashRegister
cash_register = CashRegister(5000)

# Вызываем методы объекта CashRegister и выводим результаты
cash_register.top_up(3000)
print(f"Текущее количество денег в кассе: {cash_register.money}")
print(f"Количество целых тысяч в кассе: {cash_register.count_1000()}")

cash_register.take_away(7000)
print(f"Текущее количество денег в кассе: {cash_register.money}")


# Задание 2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Черепашка не может двигаться дальше.")

    def count_moves(self, x2, y2):
        distance = ((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5
        if distance > self.s * (10 ** 9): # Максимальное расстояние
            return None
        steps_x = abs(self.x - x2) // self.s
        steps_x += int((abs(self.x - x2) % self.s) != 0)
        steps_y = abs(self.y - y2) // self.s
        steps_y += int((abs(self.y - y2) % self.s) != 0)
        return steps_x + steps_y

# Создаем объект Turtle
turtle = Turtle(0, 0, 2)

# Вызываем методы объекта Turtle и выводим результаты
turtle.go_right()
turtle.evolve()
turtle.go_up()
turtle.go_up()
turtle.go_left()

try:
    turtle.degrade()
    turtle.degrade()
    turtle.degrade()
except ValueError as e:
    print("Ошибка:", e)

print(f"Текущая позиция черепашки: ({turtle.x}, {turtle.y})")
print(f"Текущая длина шага черепашки: {turtle.s}")
print(f"Количество шагов для достижения (5, 5): {turtle.count_moves(5, 5)}")
