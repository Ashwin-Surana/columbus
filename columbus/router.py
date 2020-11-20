import json
from typing import Tuple, Set
from columbus.exceptions import *
from columbus.interceptors import Interceptor, AuthInterceptor, CORSInterceptor
from columbus.models import *
from columbus.parser import AWSHttpParser, AWSResponseParser
import config as CONFIG


class Route:
    def __init__(
            self,
            path: str,
            methods: Set[str]
    ):
        self.path = path
        self.methods = methods


class Router:
    def __init__(self):
        self.__filters = []
        self.routes = {}

    def with_filter(self, _filter: Interceptor):
        self.__filters.append(_filter)

    def get(self, path: str):
        return self.route(HTTPMethod.GET, path)

    def post(self, path: str):
        return self.route(HTTPMethod.POST, path)

    def delete(self, path: str):
        return self.route(HTTPMethod.DELETE, path)

    def put(self, path: str):
        return self.route(HTTPMethod.PUT, path)

    def route(self, method: HTTPMethod, path: str, ):
        def decorator(handler):
            self.routes[(method, path)] = handler
            return handler

        return decorator

    def get_handler(self, method: HTTPMethod, path: str):
        try:
            return self.routes[(method, path)]
        except KeyError:
            raise ResourceNotFound('Resource not found for : %s' % path)

    def get_router(self):
        def request_handler(event, context={}):
            response = HttpResponse()
            # choose request parser
            req_parser = AWSHttpParser(event, context)

            request = req_parser.parse_request()  # return http request

            try:
                for _filter in self.__filters:
                    _filter.on_request(request)
                    filter_context = _filter.on_response(request, response)
                    if filter_context is not None:
                        request.add_context(*filter_context)

                handler = self.get_handler(request.get_method(), request.get_path())
                res = handler(request)

                http_response = AWSResponseParser(res, response).parse_response()

            except HttpException as e:
                http_response = HttpResponse(body=e.msg, status=e.status)

            except Exception as e:
                http_response = HttpResponse(body=str(e), status=HTTPStatus.INTERNAL_SERVER_ERROR)

            print(http_response.as_dict())
            return http_response.as_dict()

        return request_handler


class CloudAuthRouter(Router):
    def __init__(self):
        super().__init__()
        self.with_filter(AuthInterceptor(CONFIG.AUTH_SECRET, CONFIG.BEARER))
        self.with_filter(CORSInterceptor())
