#!/usr/bin/env python3

# BoBoBo


import json
import re
from http.cookies import SimpleCookie


def parse_environ_parameters(method, environ):
    if method == 'GET':
        return parse_query_string(environ['QUERY_STRING'])
    elif method == 'POST':
        return parse_environ_body(environ)
    else:
        return {}


def parse_query_string(query):
    if not query:
        return {}
    querys = query.split('&')
    querys = list(map(lambda s: s.split('='), querys))
    querys_key = list(map(lambda s: s[0], querys))
    querys_value = list(map(lambda s: s[1], querys))
    return dict(zip(querys_key, querys_value))


def parse_environ_body(environ):
    environ_body_size = int(environ.get('CONTENT_LENGTH', 0))

    if 0 != environ_body_size:
        environ_body = environ['wsgi.input'].read(environ_body_size)
        nd = environ_body.decode('utf-8')
        try:
            parameters = json.loads(nd)
        except json.JSONDecodeError:
            return nd
        else:
            return parameters
    else:
        return {}


def convert_wsgi_request(method, pathes, headers, body):
    request = {}
    request['PATH_INFO'] = pathes[0]
    request['REQUEST_METHOD'] = method
    request['CONTENT_LENGTH'] = headers.get('Content-Length', 0)
    request['CONTENT_TYPE'] = headers.get(
        'Content-Type', 'application/json')

    class StrFile:

        def __init__(self, s):
            if str:
                self.content = s.encode('utf-8')
            else:
                self.content = None

        def read(self, size):
            if self.content:
                return self.content[:size]
            else:
                return []

    request['wsgi.input'] = StrFile(body)

    if len(pathes) > 1:
        request['QUERY_STRING'] = pathes[1]
    else:
        request['QUERY_STRING'] = None

    cookies = SimpleCookie(headers.get('Cookie'))
    request['HTTP_COOKIE'] = cookies

    return request


def parse_http_request_line(line):
    ret = re.match(r'([A-Z]+) ([^( )]+) (HTTP.+)', line)
    if ret:
        method = ret.group(1)
        pathes = ret.group(2)
        protocol = tuple(map(lambda v: int(v), ret.group(3)[5:].split('.')))

        ret = re.match(r'([^( |?)]+)[?]?(.*)', pathes)
        path = ret.group(1)
        query_string = ret.group(2)
        return {
            'REQUEST_METHOD': method, 'PATH_INFO': path,
            'QUERY_STRING': query_string, 'wsgi.version': protocol
        }
    else:
        return None
