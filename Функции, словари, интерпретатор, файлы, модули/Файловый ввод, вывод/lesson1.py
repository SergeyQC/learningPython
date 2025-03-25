#  Чтение из файла
import os.path

inf = open('fixle.txt', 'r')  # открывается файл 'fixle.txt'
s1 = inf.readline()  # выполняет чтение одной строки
s2 = inf.readline()
inf.close()  # функция закрывет файл

# конструкция для чтения файл
with open('text.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
    #  в конце выполнения конструкция сама закроет файл

s = inf.readline().strip()  # убирает все служебные символы при чтении строки
'\t abc \n'.strip() # -> ábc -- пример работы фнукции

os.path.join('.', 'dirname', 'filename.txt')  # функция принимает в качестве оргуентов строки которые склеивает их
#  в единый путь к файлу, пример: './dirname/filename.txt'

#  просто чтение из файла
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()  # это позволяет нам убрать все переносы строки в тексте
        print(line)

#  запись в файл
ouf = open('file.txt', 'w')  # 'w' - это режим открытия
ouf.write('Some text\n')  # то что хотим записать в строку
ouf.write(str(25))  # для записи числа в строку нужно его преобразовать в строку, потому используем str
ouf.close()  # закрытие файла

with open('file.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))
    # в конце выполнения функции файл автоматом закроется
