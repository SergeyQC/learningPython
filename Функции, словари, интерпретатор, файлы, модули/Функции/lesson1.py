# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))

# произвольное число аргументов
def min(*a): #  * - звездочка означает что функция принимает в себя произвольное число аргументов
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(min(5))
print(min(5, 3))
print(min(5, 3, 6))
print(min(5, 3, 6, 10))

#  Значен я параметров по умолчанию

def my_range(start, stop, step=1):
    res =[] #  создали пустой список куда накапливаем элементы которые нам нужно вернуть
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop: #идем в обратную сторону, от больше к меньшему
            res += [x]
            x += step
    return res
print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))

# локальные переменные
def init_values():
    a = 100
    b = 200

 print(a+b) #  ошибка, переменные a и b не объявлены