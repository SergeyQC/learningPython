#  Словари

dictionary = dict #  создает словарь
key = 3

dictionary = {'lol': 'not lol'}

if 'lol' in dictionary:
    print(True)

if 'loll' not in dictionary:
    print(False)

dictionary['not lol'] = 35
dictionary.get('lol') #  возвращает значение ключа, если ключа нет - Noun
print(dictionary)
print(dictionary.get('lol'))