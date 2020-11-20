import json
from abc import ABC, abstractmethod
from urllib.parse import parse_qs
from columbus.models import HTTPMethod, HttpRequest, HttpResponse
from columbus.structures import CaseInsensitiveDict
from requests_toolbelt.multipart import decoder
from http import HTTPStatus
import azure.functions as func


class HttpRequestParser(ABC):

    def __init__(self, context):
        self.context = context

    @abstractmethod
    def get_method(self):
        pass

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def get_mimetype(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    def parse_request(self) -> HttpRequest:
        return HttpRequest(self.get_method(), self.get_path(), self.get_params(),
                           self.get_body(), self.get_headers(), self.get_mimetype(), self.context)


class AWSHttpParser(HttpRequestParser, ABC):
    def __init__(self, event, context):
        super().__init__(context)
        self.event = event

    def get_method(self):
        return HTTPMethod[self.event['httpMethod']]

    def get_path(self):
        return self.event['path']

    def get_headers(self):
        return CaseInsensitiveDict(self.event['headers'])

    def get_mimetype(self):
        return self.event['headers']['Content-Type'] if self.get_method() is HTTPMethod.PUT or HTTPMethod.POST else None

    def get_body(self):
        return self.__parse_body()

    def get_params(self):
        params = {}
        if self.event.get('queryStringParameters'):
            params.update(self.event.get('queryStringParameters'))
        if self.event.get('pathParameters'):
            params.update(self.event.get('pathParameters'))
        return params if params else {}

    def __parse_body(self):
        content_type = self.get_mimetype()
        body = self.event['body']
        if 'application/json' in content_type:
            return json.loads(body)
        elif 'application/x-www-form-urlencoded' in content_type:
            return parse_qs(body)
        elif 'multipart/form-data' in content_type:
            result = {}
            name = None
            filename = None
            for part in decoder.MultipartDecoder(body.encode(), content_type).parts:
                form_data = part.headers.get(b'Content-Disposition')
                key = form_data.decode('utf-8').split("; ")[1:]
                value = part.text
                if part.headers.get(b'Content-Type'):
                    if part.headers.get(b'Content-Type').decode('utf-8') == 'text/html':
                        name, filename = [x.split('=')[1].strip('/"') for x in key]
                    if part.headers.get(b'Content-Type').decode('utf-8') == 'text/plain':
                        name, filename = [x.split('=')[1].strip('/"') for x in key]
                else:
                    name = key[0].split("=")[1].strip('/"')
                result[name] = {value, filename}
            return result
        return None


class AzureHttpParser(HttpRequestParser, ABC):
    def __init__(self, context: func.HttpRequest):
        super().__init__(context)

    def get_method(self):
        return HTTPMethod[self.context.method()]

    def get_path(self):
        return self.context.url()

    def get_params(self):
        return self.context.params()

    def get_body(self):
        return self.context.get_json()

    def get_headers(self):
        return self.context.headers

    def get_mimetype(self):
        return self.context.headers.get('Content-Type', '')


class HTTPResponseParser(ABC):

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_mimetype(self):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_charset(self):
        pass

    def parse_response(self) -> HttpResponse:
        return HttpResponse(self.get_body(), self.get_status(), self.get_headers(), self.get_mimetype(), self.get_charset())


class AWSResponseParser(HTTPResponseParser, ABC):
    def __init__(self, body=None, headers={}):
        self.body = body
        self.headers = headers
        self.status = HTTPStatus.OK

    def get_body(self):
        return self.body

    def get_headers(self):
        return self.headers

    def add_headers(self, headers):
        self.headers.update(headers)

    def get_status(self):
        return HTTPStatus.OK

    def get_mimetype(self):
        return 'application/json'

    def get_charset(self):
        return None


class AzureResponseParser(HTTPResponseParser, ABC):
    def __init__(self, req: func.HttpResponse):
        self.req = req

    def get_body(self):
        return self.req.get_body

    def get_headers(self):
        return self.req.headers

    def get_status(self):
        return self.req.status_code

    def get_mimetype(self):
        return self.req.mimetype

    def get_charset(self):
        return self.req.charset

    def parse_response(self) -> func.HttpResponse:
        return func.HttpResponse(self.get_body())