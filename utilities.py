import json

from Lesson_5.util.variables import MAX_MESSAGE_LEN, ENCODING


def send_message(socket_, message):
    data = json.dumps(message).encode(ENCODING)
    socket_.send(data)


def get_message(socket_):
    data = socket_.recv(MAX_MESSAGE_LEN)
    message = json.loads(data.decode(ENCODING))
    return message