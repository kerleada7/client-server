"""
Задание 6.
Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.
При сдаче задания в папке должен лежать текстовый файл!
Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.
"""
import chardet

with open('test_file.txt', 'rb') as f:
    file_content = f.read()
    encoding = chardet.detect(file_content)['encoding']

if encoding != 'utf-8':
    file_content = file_content.decode(encoding=encoding)
    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write(file_content)

with open('test_file.txt', encoding='utf-8') as f:
    file_content = f.read()

print(file_content, end='')