'''
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
'''
a = int(input())
b = [[0 for j in range(a)] for i in range(a)]
new_a = 0
c = 0
d = 0
n = 'верх'

for x in range(a * 2):
    if new_a == a ** 2:
        break
    elif new_a == a ** 2 - 1 and b[a//2][a//2] == 0:
        for i in range(c, c+1):
            for j in range(c, a-d):
                new_a += 1
                b[i][j] = new_a
                break
    elif n == 'верх':
        for i in range(c, c+1):
            for j in range(c, a-1-d):
                new_a += 1
                b[i][j] = new_a
        n = 'право'
    elif n == 'право':
        for i in range(c, a-1-d):
            for j in range(a-1-d, a-d):
                new_a += 1
                b[i][j] = new_a
        n = 'низ'
    elif n == 'низ':
        for i in range(a-1-d, a-d):
            for j in range(a-1-d, c, -1):
                new_a += 1
                b[i][j] = new_a
        n = 'лево'
    elif n == 'лево':
        for i in range(a-1-d, c, -1):
            for j in range(c, c+1):
                new_a += 1
                b[i][j] = new_a
        c += 1
        d += 1
        n = 'верх'

for row in b:
    print(" ".join(str(num) for num in row))