'''
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами xi, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа xi программа должна на отдельной строке вывести значение f(xi). Функция f(x) уже реализована
и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
'''


def function(n):
    dictionary = {}
    for x in range(n):
        x = int(input())
        if x not in dictionary.keys():
            dictionary[x] = f(x)
        print(dictionary[x])


function(int(input()))