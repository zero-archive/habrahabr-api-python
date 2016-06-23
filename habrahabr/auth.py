# -*- coding: utf-8 -*-

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
    def __init__(self, client=None, token=None, api_key=None):
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
        return self._endpoint

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__dict__)

    def set_request_client(self, client):
        if not re.match(r'([a-z0-9]+)\.([a-z0-9]+)', client):
            raise AuthHandlerError('Incorrect API Client: ' + client)
        self._client = client

    def set_request_token(self, token):
        if not re.match(r'([a-z0-9]+)', token):
            raise AuthHandlerError('Incorrect API Token: ' + token)
        self._token = token

    def set_request_apikey(self, api_key):
        if not re.match(r'([a-z0-9]+)', api_key):
            raise AuthHandlerError('Incorrect API Key: ' + api_key)
        self._api_key = api_key

    def get_request_endpoint(self):
        return self._endpoint

    def get_request_headers(self):
        headers = {}
        if (self._client is not None) and (self._token is not None):
            headers = {'client': self._client, 'token': self._token}
        elif self._api_key is not None:
            headers = {'apikey': self._api_key}
        return headers

    def get_authorization_url(self, redirect_uri, response_type='code'):
        if self._client is None:
            raise AuthHandlerError('Incorrect API Client')
        if self._endpoint is None:
            raise AuthHandlerError('Incorrect API Endpoint')

        payload = {
            'response_type': response_type,
            'client_id': self._client,
            'redirect_uri': redirect_uri
        }

        return API_AUTH_HOST + '?' + urlencode(payload)
