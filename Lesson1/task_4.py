"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    print(word, type(word))
    word_byte = word.encode('utf-8')
    print(word_byte, type(word_byte))
    word_str = word_byte.decode('utf-8')
    print(word_str, type(word_str))
