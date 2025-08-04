'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepik.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests
from sympy.codegen import While


#  вычитываем текст из файла
with open('dataset_3378_3.txt') as inf:
    for line in inf:
        text = line.strip()  # удаляем пробелы в начале и конце

r = requests.get(text)  # записываю в переменную r данные из файла полученого методом GET

while 'We' not in r.text:
    # перезаписываю в переменную r данные с учтом ссылки и нового имени файла из r.text
    r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + r.text)
    print(r.text)

# запись результата в файл
with open('dataset_3378_4.txt', 'w') as ouf:
    ouf.write(r.text)

