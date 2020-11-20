from enum import Enum, auto
from http import HTTPStatus
from typing import Dict, Union, Mapping, List

from columbus.exceptions import BadRequest


class HTTPMethod(Enum):
    GET = auto()
    POST = auto()
    DELETE = auto()
    PUT = auto()
    HEAD = auto()
    OPTIONS = auto()


class NoneType(object):
    pass


class HttpResponse:
    def __init__(self, body=None, status: HTTPStatus = HTTPStatus.OK,
                 headers: Union[Mapping[str, str], NoneType] = None, mimetype: str = None,
                 charset: str = None):
        self.body = body
        self.status = status
        self.headers = headers
        self.mimetype = mimetype
        self.charset = charset

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def add_headers(self, headers):
        self.headers = headers

    def set_body(self, body):
        self.body = body

    def set_status(self, status: HTTPStatus):
        self.status = status

    def as_dict(self):
        return {
            'statusCode': self.status,
            'body': self.body,
            'headers': self.headers
        }


class HttpRequest:
    def __init__(self, method: HTTPMethod, path, params: Mapping[str, Union[List[str], str]], body=None, headers=None,
                 mime_type=None,
                 context=None):
        self.method = method
        self.path = path
        self.params = params
        self.body = body
        self.headers = headers
        self.context = context
        self.mime_type = mime_type

        self.lambda_context = None

    def get_param(self, key, optional=False, default=None):
        values = self.params.get(key, default)
        if values is None and not optional:
            raise BadRequest('Missing param %s' % key)
        else:
            val = values[0] if isinstance(values, List) else values
        return val

    def get_params(self, key, optional=False, default: List = None):
        values = self.params.get(key, default)
        if values is None and not optional:
            raise BadRequest('Missing param %s' % key)
        else:
            val = values[0] if isinstance(values, List) else values
        return val

    def get_all_params(self):
        return self.params

    def get_body(self):
        return self.body

    def get_headers(self):
        return self.headers

    def get_header(self, key, optional=False, default=None):
        val = self.headers.get(key)
        if val is None and not optional:
            raise BadRequest('Missing header %s' % key)
        return val

    def add_context(self, key, val):
        self.context[key] = val
        return self

    def get_context(self, key):
        return self.context[key]

    def get_method(self):
        return self.method

    def get_path(self):
        return self.path

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
