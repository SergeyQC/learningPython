#  Генерация двухмерных списков
n = 3
a = [[0]*n for i in range(n)]
a = [[0 for j in range(n)] for i in range(n)]  # Оба варианта отработают одинаково
print(a)