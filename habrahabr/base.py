# -*- coding: utf-8 -*-

import json
import logging
from .errors import ApiHandlerError

try:
    # python3
    from urllib.request import urlopen, Request
    from urllib.error import URLError
    from urllib.parse import urlencode
except ImportError:  # pragma: no cover
    # python2
    from urllib2 import urlopen, Request, URLError
    from urllib import urlencode

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class BaseResource(object):
    def __init__(self, auth=None):
        if auth is None:
            raise ApiHandlerError('Auth handler is not defined')

        self._auth = auth

    def _request(self, url, method='GET', params=None):
        if params is not None:
            params = urlencode(params)

        url = self._auth.get_request_endpoint() + url
        headers = self._auth.get_request_headers()

        if params is not None:
            if method == 'GET' or method == 'DELETE':
                url = url + '?' + params
                params = None

        logging.info(method + ' ' + url)
        logging.info(params)

        try:
            request = Request(url, params, headers)
            request.get_method = lambda: method
            response = urlopen(request)
        except URLError as e:
            logging.error(e)
            response = e

        try:
            json_data = response.read()
            data = json.loads(json_data.decode('utf-8'))
        except ValueError as e:
            logging.error(e)
            raise ApiHandlerError('Invalid server response')

        return data
