import random

N = 10
M = 10

# создание первой матрицы
matrix_1 = []
for i in range(N):
  row = []
  for j in range(M):
    row.append(random.randint(-100, 100))
  matrix_1.append(row)

# создание второй матрицы
matrix_2 = []
for i in range(N):
  row = []
  for j in range(M):
    row.append(random.randint(-100, 100))
  matrix_2.append(row)

# создание третьей матрицы - результат сложения
matrix_3 = []
for i in range(N):
  row = []
  for j in range(M):
    row.append(matrix_1[i][j] + matrix_2[i][j])
  matrix_3.append(row)

# вывод результатов
print("Матрица 1:")
for row in matrix_1:
  print(row)

print("Матрица 2:")
for row in matrix_2:
  print(row)

print("Результат сложения матриц:")
for row in matrix_3:
  print(row)