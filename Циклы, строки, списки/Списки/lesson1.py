students = ['Ivan', 'Masha', 'Sasha']
for student in students:
    print("Hello, " + student + "!")
print(students[0])  # тут как со строками, каждому объекту списка присваивается свой индекс, начиная с 0
print(students[1])
print(students[2])

print(len(students))  # Длина списка, в нашем случаем будет - 3, т.к. ри объекта
print(students[:2])  # распечатать объекты списка с 0 по 1 индекс (2 не включается)
print(students[::-1])  # распечатать список в обратном порядке

teachers = ['Oleg', 'Alex']
print(teachers + students)  # Сложение списков, где прибавляемый встает в конец
print(teachers * 3)  # Умножение списков
print(students[:2] * 2)  # Умножение списков
students[1] = 'Noone'  # элементы списка можно изменять (в отличие от строк)
students.append("new one")  # добавление нового элемента списка, он встает в конец списка
students += ["Anna"]  # сложение списка с другими элементами
students += ["Vano", 'Marmok']  # сложение списка с другими списком
students.insert(1, 'Volga')  #  вставка элемента в список с указанием его позиции по индексу
students.remove('Vano')  # удаление из списка, удаляет только первое вхождение, остальные аналогичные - остаются
del students[0]  # удаление элемента по индексу

# поиск элемента в списке
if 'Vano' in students:
    print('Ivan is here')

if 'Anna' not in students:
    print('Anna is out')

x = students.index('Anna')  # показывает индекс первого вхождения иского элемента
ordered_students = sorted(students)  # упорядочивает список, но при этом не меняет изначальный
students.sort()  # упорядочивает список и меняет его
print(min(students))  # Выдает минимальное значение списка
print(max(students))  # Выдает максимальное значение списка
students.reverse()  # переворачивает список и изменяет его
reversed(students)  # позволяет получить список в противоположном порядке не изменяя оригинал

# Генерация списков
a = [0] * 5
b = [0 for z in range(5)]  #  Генератор списка или list comprehension
c = [z * z for z in range(5)]  #  возводит каждый элемент из range в квадрат
print(c)