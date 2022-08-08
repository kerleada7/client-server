import json
from time import time

from variables import MAX_MESSAGE_LEN, ENCODING


def send_message(socket_, message):
    data = json.dumps(message).encode(ENCODING)
    socket_.send(data)


def get_message(socket_):
    data = socket_.recv(MAX_MESSAGE_LEN)
    if data.decode(ENCODING):
        message = json.loads(data.decode(ENCODING))
    else:
        message = {
            "action": "leave",
            "time": time(),
            "room": "#room_name"
        }
    return message
