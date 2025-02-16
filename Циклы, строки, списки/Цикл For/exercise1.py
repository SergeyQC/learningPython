'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа
a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка
[a;b] на все числа отрезка [c;d].

Числа a, b,c и d являются натуральными и не превосходят 10, a ≤ b, c ≤ d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец
и строка таблицы.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c <= d and (c <= 10 and d <= 10) and a <= b and (a <= 10 and b <= 10):
    print(end='\t')
    for x in range(c, d+1):
        print(x, end='\t')

    print()

    for y in range(a, b+1):
        print(y, end='\t')
        for x in range(c, d + 1):
            print(x * y, end='\t')
        print()
