"""Утилиты"""

import sys
import json
from Project_to_OOP.unit_tests.log_decorator import log
from Project_to_OOP.common.variables import *
from Project_to_OOP.errors import IncorrectDataReceivedError, NonDictInputError
sys.path.append('../')


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataReceivedError
    else:
        raise IncorrectDataReceivedError


@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
