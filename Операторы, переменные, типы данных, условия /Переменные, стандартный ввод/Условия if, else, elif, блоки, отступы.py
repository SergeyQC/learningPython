# A = int(input())
# if A == 0:
#     A = int(input())
#     print('снова введите В')
#
# B = int(input())
# if B < A:
#     B = int(input())
#     print('снова введите В')
#
# H = int(input())
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# else:
#     print('Пересып')

##############################################

a = int(input())
if a <= 1900 or a >= 3000:
    a = int(input())
elif a % 4 == 0 and a % 100 != 0:
    print('Високосный')
elif a % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
