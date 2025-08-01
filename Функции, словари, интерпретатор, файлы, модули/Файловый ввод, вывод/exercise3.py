'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте
полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой
со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
'''


from itertools import count


# чтение из файла
wholeList = ''
with open('dataset_3363_5.txt') as inf:
    for line in inf:
        wholeList += line

# Разделение на строки
wholeList = wholeList.strip().split('\n')
wholeList = [line.split(';') for line in wholeList]

# вывод стредней оценки для каждого абитуриента
average = []
numb = 0  # сумма по трем предметам
counter = 0  # счетчик
for row in range(len(wholeList)):  # итерирование по строкам
    for column in range(1, len(wholeList[row])): # итерирование внутри одной строки
        numb += int(wholeList[row][column])
        counter += 1
        if counter == 3:
            average += [float(numb/3)]
            counter = 0
            numb = 0
        elif column or row > len(wholeList)+1:
            continue

math = 0  # сумма по трем предметам
pith = 0  # сумма по трем предметам
lang = 0  # сумма по трем предметам
aver = []

for row in range(len(wholeList)):  # итерирование по строкам
    for column in range(1, len(wholeList[row])): # итерирование внутри одной строки
        if column == 1:
            math += int(wholeList[row][column])
        elif column == 2:
            pith += int(wholeList[row][column])
        elif column == 3:
            lang += int(wholeList[row][column])

aver += [math/len(wholeList)]
aver += [pith/len(wholeList)]
aver += [lang/len(wholeList)]

with open('dataset_3363_6.txt', 'w') as ouf:
    ouf.write('\n'.join(map(str, average)) + '\n')
    ouf.write(' '.join(map(str, aver)))