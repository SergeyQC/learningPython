'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:
'''

def modify_list(l):
    for x in range(len(l)-1, -1, -1):
        if l[x] % 2 == 0:
            l[x] = l[x] // 2
        else:
            lst.remove(lst[x])


lst = [1, 2, 3, 4, 5, 6, 7]
modify_list(lst)
print(lst)