import argparse
import re
from socket import *
from time import time

from variables import DEFAULT_PORT
from utilities import send_message, get_message


def get_client_cli_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("address", type=str, help='Server IP address')
    args_parser.add_argument("port", nargs='?', type=int, default=DEFAULT_PORT,
                             help='Server port (must be in range 1024-65535)')
    args = args_parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    args_correct = True
    if re.match(ip_re_tpl, args.address) is None:
        print('Please enter a valid IP address')
        args_correct = False
    if not 1024 <= args.port <= 65535:
        print('The port address must be in the range 1024-65535')
        args_correct = False
    if not args_correct:
        exit(1)
    return args.address, args.port


def connect_client_socket(ip, port):
    socket_ = socket(AF_INET, SOCK_STREAM)
    try:
        socket_.connect((ip, port))
    except ConnectionError:
        print('Server connection error')
        print('Check if IP address and port are correct')
        exit(1)
    return socket_


def create_message_presence(account_name='Guest'):
    message = {
        "action": "presence",
        "time": time(),
        "type": "status",
        "user": {
            "account_name": account_name
        }
    }
    return message


def main():
    server_ip_address, server_port = get_client_cli_args()
    client_socket = connect_client_socket(server_ip_address, server_port)

    client_message = create_message_presence()
    send_message(client_socket, client_message)

    server_message = get_message(client_socket)
    print(f'Server response code: {server_message["response"]}')
    print(f'Server message: {server_message["alert"]}')

    client_socket.close()


if __name__ == '__main__':
    main()