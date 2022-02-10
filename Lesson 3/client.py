import argparse
import json
import re
from socket import *
from time import time

DEFAULT_PORT = 7777
MAX_MESSAGE_LEN = 1024
ENCODING = 'utf-8'


def get_cli_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("address", type=str, help='Server address')
    args_parser.add_argument("port", nargs='?', type=int, default=DEFAULT_PORT, help='Server port')
    args = args_parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if re.match(ip_re_tpl, args.address) is None:
        print('Please enter a valid IP address')
        exit(1)
    if not 1024 <= args.port <= 65535:
        print('The port address must be in the range 1024-65535')
        exit(1)
    return args.address, args.port


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    server_ip_address, server_port = get_cli_args()
    try:
        client_socket.connect((server_ip_address, server_port))
    except ConnectionError:
        print('Server connection error')
        print('Check if IP address and port are correct')
        exit(1)

    client_message = {
        "action": "presence",
        "time": time(),
        "type": "status",
        "user": {
            "account_name": "Игорь",
            "status": "Yep, I am here!"
        }
    }

    data = json.dumps(client_message).encode(ENCODING)
    client_socket.send(data)

    data = client_socket.recv(MAX_MESSAGE_LEN)
    server_message = json.loads(data.decode(ENCODING))

    print(f'Server response code: {server_message["response"]}')
    print(f'Server message: {server_message["alert"]}')

    client_socket.close()


if __name__ == '__main__':
    main()