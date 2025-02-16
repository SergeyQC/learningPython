'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

# a = sorted([int(i) for i in input().split()])
# s = 0
# for x in range(0, len(a)):
#     if x == len(a)-1 and s == 0:
#         break
#     elif x == len(a)-1 and s > 0:
#         print(a[x], end=' ')
#     elif a[x] == a[x + 1]:
#         s += 1
#     elif a[x] != a[x + 1] and s > 0:
#         print(a[x], end=' ')
#         s = 0

a,b=[int(i) for i in input().split()],''
a.sort()
for i in range(len(a)-1):
    if a[i]==a[i+1] and a[i]!=b:
        print(a[i], end=' ')
        b=a[i]
