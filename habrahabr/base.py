# -*- coding: utf-8 -*-

import json
import logging
from .errors import ApiHandlerError

log = logging.getLogger(__name__)

try:
    # python3
    from urllib.request import build_opener, Request, HTTPHandler
    from urllib.error import HTTPError
    from urllib.parse import urlencode
except ImportError:  # pragma: no cover
    # python2
    from urllib2 import build_opener, Request, HTTPHandler, HTTPError
    from urllib import urlencode


class BaseResource(object):
    def __init__(self, auth=None):
        if auth is None:
            raise ApiHandlerError('Auth handler is not defined')

        self._auth = auth

    def _request(self, url, method='GET', data=None):
        url = self._auth.get_request_endpoint() + url
        headers = self._auth.get_request_headers()

        if data is not None:
            data = urlencode(data)
            if method in ['GET', 'DELETE']:
                url = url + '?' + data
                data = None

        log.debug(method + ' ' + url)
        log.debug(data)

        try:
            opener = build_opener(HTTPHandler)
            request = Request(url, data=data, headers=headers)
            request.get_method = lambda: method
            response = opener.open(request).read()
            data = self._parse_response(response)
        except HTTPError as e:
            log.error(e)
            data = self._parse_response(e.read())
            raise ApiHandlerError('Invalid server response', data)
        except ValueError as e:
            log.error(e)
            raise ApiHandlerError('Invalid server response')

        return data

    @staticmethod
    def _parse_response(response):
        try:
            return json.loads(response.decode('utf-8'))
        except ValueError:
            return False
