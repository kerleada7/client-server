"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import subprocess
import chardet


def ping(url):
    subproc_ping = subprocess.Popen(['ping', url], stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        encoding = chardet.detect(line)['encoding']
        line_unicode = line.decode(encoding).encode('utf-8')
        print(line_unicode.decode('utf-8'), end='')

ping('yandex.ru')
ping('youtube.com')
