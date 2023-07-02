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

# Словарь для хранения количества каждой гласной буквы
vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Проходимся циклом по всем буквам слова
for letter in word:
    # Проверяем, является ли буква гласной или согласной
    if letter in vowels_dict:
        vowels += 1
        vowels_dict[letter] += 1
    elif letter.isalpha():
        consonants += 1

# Выводим количество каждой гласной буквы
print("Количество каждой гласной буквы:")
for vowel in vowels_dict:
    print(f"{vowel}: {vowels_dict[vowel]}")

# Задание 3
minSum = int(input("Введите минимальную сумму инвестиций: "))
mikeSum = int(input("Введите сумму Майка: "))
ivanSum = int(input("Введите сумму Ивана: "))

if mikeSum >= minSum and ivanSum >= minSum:
    print(2)
elif mikeSum >= minSum:
    print('Mike')
elif ivanSum >= minSum:
    print('Ivan')
else:
    if mikeSum + ivanSum >= minSum:
        print(1)
    else:
        print(0)
