# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 dotzero <mail@dotzero.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
