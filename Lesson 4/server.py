import argparse
import re
from socket import *
from time import time

from variables import DEFAULT_PORT
from utilities import send_message, get_message


def get_server_cli_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-a", type=str, default='', help='Listening IP')
    args_parser.add_argument("-p", type=int, default=DEFAULT_PORT,
                             help='TCP port (must be in range 1024-65535)')
    args = args_parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    args_correct = True
    if args.a != '' and re.match(ip_re_tpl, args.a) is None:
        print('Please enter a valid IP address')
        args_correct = False
    if not 1024 <= args.p <= 65535:
        print('The port address must be in the range 1024-65535')
        args_correct = False
    if not args_correct:
        exit(1)
    return args.a, args.p


def connect_server_socket(ip, port):
    socket_ = socket(AF_INET, SOCK_STREAM)
    try:
        socket_.bind((ip, port))
    except OSError:
        print(f'Address {ip} or port {port} already in use')
        exit(1)
    socket_.listen(5)
    return socket_


def process_client_message(message):
    server_message = ''
    if message['action'] == 'presence':
        server_message = {
            "response": 200,
            "time": time(),
            "alert": 'OK'
        }
    return server_message


def main():
    ip, port = get_server_cli_args()
    server_socket = connect_server_socket(ip, port)
    print(f'Server started on port {port}')

    while True:
        client, address = server_socket.accept()
        print(f"Connection request received from {address}")

        client_message = get_message(client)
        print(f'Message received: {client_message}')

        server_message = process_client_message(client_message)
        send_message(client, server_message)

        client.close()


if __name__ == '__main__':
    main()