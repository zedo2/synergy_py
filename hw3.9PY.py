#  Задание 1
n = int(input())
lst = list(map(int, input().split()))

unique = set(lst)

print(len(unique))


#  Задание 2
lst1 = set(map(int, input().split()))
lst2 = set(map(int, input().split()))

common_elements = lst1.intersection(lst2)

print(len(common_elements))


#  Задание 3
sequence = list(map(int, input().split()))
seen_numbers = set()

for num in sequence:
    if num in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(num)