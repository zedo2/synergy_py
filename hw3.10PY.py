#  Задание 1
pets = {}

pet_name = input("Введите имя питомца: ")
pet_kind = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# проверяем склонение слова "год"
if pet_age % 10 == 1 and pet_age != 11:
    age_word = "год"
elif pet_age % 10 in [2, 3, 4] and pet_age not in [12, 13, 14]:
    age_word = "года"
else:
    age_word = "лет"

# создаем словарь для питомца
pets[pet_name] = {
    "Вид питомца": pet_kind,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

# форматируем и выводим информацию о питомце
info_str = f'Это {pet_kind.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}'
print(info_str)


#  Задание 2
my_dict = {}

for num in range(10, -6, -1):
    my_dict[num] = num ** num

print(my_dict)