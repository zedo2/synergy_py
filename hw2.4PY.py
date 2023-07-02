# Задание 1
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

perimeter = 2 * (a + b)
area = a * b

print(f"Периметр прямоугольника: {perimeter:.2f}")
print(f"Площадь прямоугольника: {area:.2f}")

# Задание 2
num = int(input("Введите пятизначное число: "))

# Разбиваем число на цифры
ones = num % 10
tens = num // 10 % 10
hundreds = num // 100 % 10
thousands = num // 1000 % 10
ten_thousands = num // 10000 % 10

# Возводим количество десятков в степень количества единиц
result = tens ** ones

# Умножаем результат на количество сотен
result *= hundreds

# Вычисляем разность между количеством десятков тысяч и количеством тысяч
diff = ten_thousands - thousands

# Делим результат на diff
result /= diff

# Выводим результат
print(f"Результат: {result}")
