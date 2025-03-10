#  Перебор элементов словаря
d = {'C': 14, 'A': 12, 'T': 9, 'G': 18} #  словарь
for key in d: #  перебор и вывод ключей словаря
    print(key, end=' ')
print()

for key in d.keys(): #   перебор и вывод ключей словаря, но тут смотрим только на ключи, т.к. d.keys()
    print(key, end=' ')
print()

for values in d.values(): #   перебор и вывод значений словаря
    print(values, end=' ')
print()

for key, values in d.items(): #   перебор и вывод значений и ключей словаря
    print(key, values, end=' ')
print()
