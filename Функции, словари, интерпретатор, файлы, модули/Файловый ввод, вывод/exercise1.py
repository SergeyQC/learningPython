'''
нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
'''

# чтение из файла
with open('dataset_3363_2.txt') as inf:
    for line in inf:
        line = line.strip()
# заполнение списка "а" и создание переменных
a = line
b = '0123456789'
c = ''
count = ''
result = []

# распаковска строк
for x in a:
    if x not in b:
        if c and count:
            result.append(c * int(count))
        c = x
        count = ''
    else:
        count += x
if c and count:
        result.append(c * int(count))

# запись результата в файл (перезапись)
with open('dataset_3363_2.txt', 'w') as ouf:
    for x in result:
        ouf.write(x)