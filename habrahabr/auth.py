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
"""This module contains a object that represents a Habrahabr Auth."""

import re
from .errors import AuthHandlerError

try:
    # python3
    from urllib.parse import urlencode
except ImportError:  # pragma: no cover
    # python2
    from urllib import urlencode

API_HOST = 'https://api.habrahabr.ru/v1'
API_AUTH_HOST = 'https://habrahabr.ru/auth/o/login/'


class Auth(object):
    """Этот объект содержит Habrahabr Auth.

    Args:
        client (Optional[str]): Habrahabr OAuth Client.
        token (Optional[str]): Habrahabr OAuth Token.
        api_key (Optional[str]): Habrahabr Api Key.
    """

    def __init__(self, client=None, token=None, api_key=None):
        """Конструктор Auth.

        :param client: Habrahabr OAuth Client.
        :param token: Habrahabr OAuth Token.
        :param api_key: Habrahabr Api Key.
        :returns:
        """
        self._client = None
        self._token = None
        self._api_key = None
        self._endpoint = API_HOST

        if (client is not None) and (token is not None):
            self.set_request_client(client)
            self.set_request_token(token)
        elif api_key is not None:
            self.set_request_apikey(api_key)

    def __str__(self):
        """Возвращает OAuth Endpoint для доступа к Habrahabr API."""
        return '%s' % self._endpoint

    def __repr__(self):
        """Возвращает строковое представление объекта."""
        return '%s(%r)' % (self.__class__, self.__dict__)

    @property
    def endpoint(self):
        """Получить OAuth Endpoint для доступа к Habrahabr API."""
        return self._endpoint

    @property
    def headers(self):
        """Получить Request Headers для доступа к Habrahabr API."""
        headers = {}
        if (self._client is not None) and (self._token is not None):
            headers = {'client': self._client, 'token': self._token}
        elif self._api_key is not None:
            headers = {'apikey': self._api_key}

        return headers

    def set_request_client(self, client):
        """Установить OAuth Client для доступа к Habrahabr API.

        :param client: OAuth Client для доступа к Habrahabr API.
        :returns:
        """
        if not re.match(r'([a-z0-9]+)\.([a-z0-9]+)', client):
            raise AuthHandlerError('Incorrect API Client: ' + client)
        self._client = client

    def set_request_token(self, token):
        """Установить OAuth Token для доступа к Habrahabr API.

        :param token: OAuth Token для доступа к Habrahabr API.
        :returns:
        """
        if not re.match(r'([a-z0-9]+)', token):
            raise AuthHandlerError('Incorrect API Token: ' + token)
        self._token = token

    def set_request_apikey(self, api_key):
        """Установить ключ для доступа к не персонализированным данным API.

        :param api_key: Ключ для доступа к не персонализированным данным API.
        :returns:
        """
        if not re.match(r'([a-z0-9]+)', api_key):
            raise AuthHandlerError('Incorrect API Key: ' + api_key)
        self._api_key = api_key

    def get_authorization_url(self, redirect_uri, response_type='code'):
        """Возращает URL для OAuth авторизации Habrahabr Api.

        :param redirect_uri: OAuth Redirect URL.
        :param response_type: OAuth Response type.
        :returns: OAuth authorization URL.
        :rtype: str
        """
        if self._client is None:
            raise AuthHandlerError('Incorrect API Client')

        payload = {
            'response_type': response_type,
            'client_id': self._client,
            'redirect_uri': redirect_uri
        }

        return API_AUTH_HOST + '?' + urlencode(payload)
