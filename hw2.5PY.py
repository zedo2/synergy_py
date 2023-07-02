# Задание 1
num = int(input("Введите целое число: "))

# Проверяем число на равенство нулю, если да, то выводим соответствующее сообщение.
if num == 0:
    print("Введенное число равно нулю.")
else:
    # Проверяем, является ли число положительным или отрицательным
    if num > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"
    
    # Проверяем, является ли число четным или нечетным
    if num % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"
    
    # Выводим строку-описание числа
    print("Введенное число", sign, end=" ")
    
    if parity:
        print(parity, "число.")
    else:
        print("и не является четным числом.")


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
