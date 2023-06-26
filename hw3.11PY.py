import math

#  Задание 1
def factorial(n):
    return math.factorial(n)

def factorial_list(n):
    result = []
    fact = factorial(n)
    while fact > 1:
        result.append(fact)
        n -= 1
        fact = factorial(n)
    result.append(1)
    return result

# пример использования
n = 6
fact = factorial(n)
fact_list = factorial_list(fact)
print(fact_list)
