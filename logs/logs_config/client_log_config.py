import logging
import os

from variables import LOGGING_LEVEL

log_file_path = os.path.dirname(__file__)
log_file_path = os.path.split(log_file_path)[0]
log_file_path = os.path.join(log_file_path, 'client.log')

log_format = logging.Formatter('%(asctime)s - %(levelname)-8s - %(module)s: %(message)s')

file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)

client_log = logging.getLogger('client')
client_log.setLevel(LOGGING_LEVEL)
client_log.addHandler(file_handler)

if __name__ == '__main__':
    client_log.debug('Это отладка')
    client_log.info('Это информационное сообщение')
    client_log.error('Упс, ошибочка...')
    client_log.critical('Это уже критическая ошибка!!!')
