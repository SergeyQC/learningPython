'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
matrix = []

# Считываем матрицу из ввода
while True:
    row = input()
    if row == "end":
        break
    matrix.append([int(x) for x in row.split()])

rows, cols = len(matrix), len(matrix[0])
new_matrix = [[0] * cols for _ in range(rows)]

# Заполняем новую матрицу, учитывая замыкание по краям
for i in range(rows):
    for j in range(cols):
        top = matrix[i - 1][j]  # Элемент сверху (с замыканием)
        bottom = matrix[(i + 1) % rows][j]  # Элемент снизу (с замыканием)
        left = matrix[i][j - 1]  # Элемент слева (с замыканием)
        right = matrix[i][(j + 1) % cols]  # Элемент справа (с замыканием)

        new_matrix[i][j] = top + bottom + left + right
        print(new_matrix[i][j], end=' ')
    print()

# ======================================================

c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()