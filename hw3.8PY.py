#  Задание 1
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

lst.reverse()

for i in lst:
    print(i, end=" ")

#  Задание 2
n = int(input()) # вводим количество чисел
lst = list(map(int, input().split())) # вводим числа и создаем список

for i in range(n//2): # выполняем цикл для смены мест элементов
    lst[i], lst[n-i-1] = lst[n-i-1], lst[i] # меняем местами i-ый элемент с (n-i-1)-ым элементом

print(*lst) # выводим полученный список


#  Задание 3
m = int(input())
n = int(input())
weights = [int(input()) for i in range(n)]
weights.sort()

i = 0
j = n-1
boats = 0

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1
    j -= 1
    boats += 1

print(boats)
