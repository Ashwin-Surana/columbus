from abc import ABC, abstractmethod
from logging import Logger
from typing import Set

from columbus.authorizer import Authorizer
from columbus.exceptions import *
from columbus.models import HTTPMethod, HttpRequest, HttpResponse
from columbus.parser import LambdaRequestParser


class Interceptor(ABC):

    @abstractmethod
    def on_request(self, request: HttpRequest):
        pass

    @abstractmethod
    def on_response(self, request: HttpRequest, response: HttpResponse):
        pass


class AuthInterceptor(Interceptor):
    def __init__(self, secret, bearer):
        self.authorizer = Authorizer(secret, bearer)

    def __verify_bearer_and_token(self, token):
        decoded_data = self.authorizer.decode_auth(token)
        if isinstance(decoded_data, str):
            raise Exception(decoded_data)
        return decoded_data

    def on_request(self, request: HttpRequest):
        # auth_token = request.get_header('Authorization')

        sample_auth = 'BEARER eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU5NzMzNDYsImlhdCI6MTYwNTg4Njk0Niwic3ViIjoxMn0.OOpxHRNi_S_yAgkpG5S-MSpQy5PKsQap_IPBaTGlm_0'

        bearer, token = sample_auth.split(' ')
        if self.authorizer.bearer != bearer:
            raise Exception('ERROR ::: BEARER doesnt match')

    def on_response(self, request: HttpRequest, response: HttpResponse):
        sample_auth = 'BEARER eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU5NzMzNDYsImlhdCI6MTYwNTg4Njk0Niwic3ViIjoxMn0.OOpxHRNi_S_yAgkpG5S-MSpQy5PKsQap_IPBaTGlm_0'
        try:
            bearer, token = sample_auth.split(' ')
            decoded = self.__verify_bearer_and_token(token)
            return 'userinfo', decoded
        except Exception as e:
            raise Exception('Error while decoding auth')


class CORSInterceptor(Interceptor):

    def __init__(
            self,
            origin: str = '*',
            allowed_methods: Set[HTTPMethod] = frozenset(
                {HTTPMethod.GET, HTTPMethod.POST, HTTPMethod.PUT, HTTPMethod.DELETE})
    ) -> None:
        self.origin = origin
        self.allowed_methods = allowed_methods
        self.headers = {
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Credentials': True,
            'Access-Control-Allow-Methods': ', '.join([x.name for x in self.allowed_methods])
        }

    def __is_valid_request(self, request: HttpRequest):
        method = request.get_method()
        return method in self.allowed_methods

    def on_request(self, request: HttpRequest):
        if not self.__is_valid_request(request):
            raise MethodNotAllowed('%s method not allowed' % request.get_method())

    def on_response(self, request: HttpRequest, response: HttpResponse):
        headers = {}
        headers.update(response.headers)
        headers.update(self.headers)
        return headers


class LogInterceptor(Interceptor):
    def __init__(self, logger: Logger):
        self.log = logger

    def on_request(self, request: HttpRequest):
        self.log.info(
            '{}: {}  Params: {}'.format(request.get_method(), request.get_path(), str(request.get_all_params())))
