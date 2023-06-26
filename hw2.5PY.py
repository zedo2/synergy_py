# Задание 1
num = int(input("Введите целое число: "))

# Проверяем, является ли число нулем, положительным или отрицательным
if num == 0:
    sign = "нулевое число"
elif num > 0:
    sign = "положительное"
else:
    sign = "отрицательное"

# Если число не равно 0, проверяем, является ли число четным или нечетным
if num != 0:
    if num % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"
else:
    parity = ""

# Выводим строку-описание числа
if parity:
    print(sign, parity, "число")
else:
    print("число не является четным")


# Задание 2
word = input("Введите слово: ").lower()

# Инициализируем счетчики гласных и согласных букв
vowels = 0
consonants = 0

# Проходимся циклом по всем буквам слова
for letter in word:
    # Проверяем, является ли буква гласной или согласной
    if letter in "aeiou":
        vowels += 1
    elif letter.isalpha():
        consonants += 1

# Проверяем, исчерпан ли список гласных букв
if vowels == 5:
    print(f"Количество гласных букв: {vowels}, количество согласных букв: {consonants}")
else:
    print(False)


# Задание 3
minSum = int(input("Введите минимальную сумму инвестиций: "))
mikeSum = int(input("Введите сумму Майка: "))
ivanSum = int(input("Введите сумму Ивана: "))

if mikeSum + ivanSum >= minSum:
    print(2)
elif mikeSum >= minSum:
    print('Mike')
elif ivanSum >= minSum:
    print('Ivan')
elif mikeSum + ivanSum >= minSum:
    print(1)
else:
    print(0)
