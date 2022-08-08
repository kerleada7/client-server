import inspect
import logging
import sys

from . import client_log_config
from . import server_log_config

if sys.argv[0].endswith('client.py'):
    function_log = logging.getLogger('client')
else:
    function_log = logging.getLogger('server')


def log(func):
    def func_to_log(*args, **kwargs):
        function_log.info(f'Function "{func.__name__}" was called from function "{inspect.stack()[1][3]}"')
        return func(*args, **kwargs)
    return func_to_log
