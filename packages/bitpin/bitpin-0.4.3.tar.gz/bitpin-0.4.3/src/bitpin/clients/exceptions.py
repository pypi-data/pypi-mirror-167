import typing as t
import json

from requests import Response
from aiohttp import ClientResponse


class APIException(Exception):
    def __init__(self, response: t.Union[Response, ClientResponse], status_code: int, text: str):
        try:
            json_res = json.loads(text)
        except ValueError:
            print('Could not parse json: %s' % text)
            self.message = 'Invalid JSON error message from Bitpin: {}'.format(response.text)
            self.result = None
        else:
            print('Got response: %s' % response.text)
            self.message = json_res.get('detail', 'Unknown error')
            self.result = json_res.get('result')

        self.status_code = status_code
        self.response = response
        self.request = getattr(response, 'request', None)
        self.url = getattr(response, 'url', None)

    def __str__(self):  # pragma: no cover
        return 'APIError(code=%s): %s | %s | %s' % (self.status_code, self.message, self.result, self.url)


class RequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'RequestException: %s' % self.message
