"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
"""

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        print(bytes(word, 'ascii'))
    except UnicodeError:
        print(f'Слово «{word}» невозможно записать в байтовом типе с помощью маркировки b\'\'')