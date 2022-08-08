import argparse
import logging
import re
import select
from socket import *
from time import time

import logs.logs_config.server_log_config
from logs.logs_config.function_log import log
from variables import DEFAULT_PORT
from utilities import send_message, get_message

server_log = logging.getLogger('server')


@log
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
        server_log.error('Wrong IP address')
    if not 1024 <= args.p <= 65535:
        print('The port address must be in the range 1024-65535')
        args_correct = False
        server_log.error('Wrong port address')
    if not args_correct:
        exit(1)
    server_log.info(f'CLI arguments are correct. IP: {args.a} Port: {args.p}')
    return args.a, args.p


@log
def connect_server_socket(ip, port):
    socket_ = socket(AF_INET, SOCK_STREAM)
    try:
        socket_.bind((ip, port))
    except OSError:
        print(f'Address {ip} or port {port} already in use')
        server_log.critical('Socket connection error')
        exit(1)
    else:
        server_log.info('Socket connected successfully')
    socket_.listen(5)
    socket_.settimeout(0.2)
    return socket_


@log
def process_client_message():
    server_message = {
        "response": 200,
        "time": time(),
        "alert": 'OK'
    }
    server_log.info('Server message created')
    return server_message


@log
def create_client_message(message):
    send_message = {
        "action": "msg",
        "time": time(),
        "to": "#room_name",
        "from": "account_name",
        "message": message
    }
    return send_message


@log
def handle_clients(clients):
    recv_socket_list = []
    send_socket_list = []
    err_list = []

    try:
        recv_socket_list, send_socket_list, err_list = select.select(clients, clients, [], 0)
    except OSError:
        pass

    if recv_socket_list:
        for recv_socket in recv_socket_list:
            message = get_message(recv_socket)
            if message['action'] == 'leave':
                recv_socket.close()
                clients.remove(recv_socket)
            if message['action'] == 'msg' and send_socket_list:
                message = create_client_message(message['message'])
                for send_socket in send_socket_list:
                    send_message(send_socket, message)


def main():
    ip, port = get_server_cli_args()
    server_socket = connect_server_socket(ip, port)
    print(f'Server started on port {port}')
    server_log.info(f'Server started on port {port}')

    clients = []

    while True:
        try:
            client, address = server_socket.accept()
            print(f'Connection request received from {address}')
            server_log.info(f'Connection request received from {address}')
        except OSError:
            pass
        else:
            client_message = get_message(client)
            server_log.info('Client message received')
            if client_message['action'] == 'presence':
                server_message = process_client_message()
                send_message(client, server_message)
                server_log.info('Server message sent')
                clients.append(client)

        if clients:
            handle_clients(clients)


if __name__ == '__main__':
    main()
