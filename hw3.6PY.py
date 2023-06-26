#  Задание 1
N = int(input())
count_zero = 0

for i in range(N):
    x = int(input())
    if x == 0:
        count_zero += 1

print(count_zero)

#  Задание 2
import math

x = int(input())
count = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        count += 1
        if x // i != i:
            count += 1

print(count)

# Задание 3
a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')