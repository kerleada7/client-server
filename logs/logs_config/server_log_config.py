import logging.handlers
import os

from variables import LOGGING_LEVEL

log_file_path = os.path.dirname(__file__)
log_file_path = os.path.split(log_file_path)[0]
log_file_path = os.path.join(log_file_path, 'server.log')

log_format = logging.Formatter('%(asctime)s - %(levelname)-8s - %(module)s: %(message)s')

file_handler = logging.handlers.TimedRotatingFileHandler(
    log_file_path, encoding='utf-8', interval=1, when='midnight')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)

server_log = logging.getLogger('server')
server_log.setLevel(LOGGING_LEVEL)
server_log.addHandler(file_handler)

if __name__ == '__main__':
    server_log.debug('Это отладка')
    server_log.info('Это информационное сообщение')
    server_log.error('Упс, ошибочка...')
    server_log.critical('Это уже критическая ошибка!!!')
