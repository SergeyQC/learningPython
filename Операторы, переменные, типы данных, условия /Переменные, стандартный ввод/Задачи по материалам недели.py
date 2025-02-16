# a = int(input())
# b= int(input())
# c= int(input())
#
# p = (a + b + c)/2
#
# print(float((p * (p - a) * (p - b) * (p - c)) ** (1/2)))

##############################################

# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a < float('inf'):
#     print(True)
# else:
#     print(False)

##############################################

# a = int(input())
# b= int(input())
# c= int(input())
#
# p = (a + b + c)/2
#
# print(float((p * (p - a) * (p - b) * (p - c)) ** (1/2)))

##############################################

# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a < float('inf'):
#     print(True)
# else:
#     print(False)

##############################################

# first_number = float(input())
# second_number = float(input())
# oper = input()
#
# if second_number == 0 and oper == 'mod':
#     print("Деление на 0!")
# elif second_number == 0 and oper == 'div':
#     print("Деление на 0!")
# elif second_number == 0 and oper == '/':
#     print("Деление на 0!")
# elif oper == 'mod':
#     print(first_number % second_number)
# elif oper == 'pow':
#     print(first_number ** second_number)
# elif oper == 'div':
#     print(int(first_number / second_number))
# elif oper == '+':
#     print(first_number + second_number)
# elif oper == '-':
#     print(first_number - second_number)
# elif oper == '/':
#     print(first_number / second_number)
# elif oper == '*':
#     print(first_number * second_number)

##############################################

# form = input()
# pi = 3.14
#
# if form == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     c = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
# elif form == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     c = a * b
# elif form == 'круг':
#     r = int(input())
#     c = pi * r ** 2
#
# print(c)

##############################################

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a >= b and a >= c and b >= c:
#     print(a)
#     print(c)
#     print(b)
# elif a >= b and a >= c and c >= b:
#     print(a)
#     print(b)
#     print(c)
# elif b >= a and b >= c and a >= c:
#     print(b)
#     print(c)
#     print(a)
# elif b >= a and b >= c and c >= a:
#     print(b)
#     print(a)
#     print(c)
# elif c >= a and c >= b and a >= b:
#     print(c)
#     print(b)
#     print(a)
# elif c >= a and c >= b and b >= a:
#     print(c)
#     print(a)
#     print(b)
# elif c == a == b:
#     print(c)
#     print(a)
#     print(b)

##############################################

# a = int(input())
#
# if a == 1:
#     print(a, 'программист')
# elif 1 < a < 5:
#     print(a, 'программиста')
# elif a == 0 or 5 <= a <= 20:
#     print(a, 'программистов')
# elif 20 < a < 100:
#     x = a * 0.1
#     b = round((a * 0.1 - int(x)) * 10, 1)
#     if b == 1:
#         print(a, 'программист')
#     elif 1 < b < 5:
#         print(a, 'программиста')
#     elif b == 0 or 5 <= b < 10:
#         print(a, 'программистов')
# elif 100 < a < 1000:
#     y = a * 0.01
#     d = round((a * 0.01 - int(y)) * 100, 1)
#     if d == 0 or 11 <= d <= 20:
#         print(a, 'программистов')
#     elif d <= 10 or d > 20:
#         x = a * 0.1
#         c = round((a * 0.1 - int(x)) * 10, 1)
#         if c == 1:
#             print(a, 'программист')
#         elif 1 < c < 5:
#             print(a, 'программиста')
#         elif c == 0 or 5 <= c <= 10:
#             print(a, 'программистов')
# elif a == 100 or a == 1000:
#     print(a, 'программистов')

##############################################

# i=int(input())
# d=i%10
# h=i%100
# if d==1 and h!=11:
#     s=""
# elif 1<d<5 and not 11<h<15:
#     s="а"
# else:
#     s="ов"
# print(i," программист"+s)

##############################################

a = int(input())
b = a % 10
c = int((a % 100)/10)
d = int((a % 1000)/100)
f = int((a % 10000)/1000)
g = int((a % 100000)/10000)
h = int(a / 100000)

if b + c + d == f + g + h:
    print('Счастливый')
else:
    print('Обычный')