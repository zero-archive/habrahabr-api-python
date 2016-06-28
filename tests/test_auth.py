#!/usr/bin/env python
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

"""This module contains a object that represents Tests for Auth"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest


class AuthTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Auth."""

    def setUp(self):
        self.auth = habrahabr.Auth()

    def test_auth_init_empty(self):
        """Test Auth.__init__() method"""
        auth = habrahabr.Auth()

        self.assertEqual(auth._client, None)
        self.assertEqual(auth._token, None)
        self.assertEqual(auth._api_key, None)
        self.assertNotEqual(auth._endpoint, None)

    def test_auth_init_oauth(self):
        """Test Auth.__init__(client, token) method"""
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.assertEqual(auth._client, 'foo.bar')
        self.assertEqual(auth._token, 'foobar')
        self.assertEqual(auth._api_key, None)

    def test_auth_init_apikey(self):
        """Test Auth.__init__(api_key) method"""
        auth = habrahabr.Auth(api_key='foobar')

        self.assertEqual(auth._client, None)
        self.assertEqual(auth._token, None)
        self.assertEqual(auth._api_key, 'foobar')

    def test_set_request_client(self):
        """Test Auth.set_request_client(client) method"""
        self.auth.set_request_client('foo.bar')
        self.assertEqual(self.auth._client, 'foo.bar')

    def test_set_request_token(self):
        """Test Auth.set_request_token(token) method"""
        self.auth.set_request_token('foobar')
        self.assertEqual(self.auth._token, 'foobar')

    def test_set_request_apikey(self):
        """Test Auth.set_request_apikey(api_key) method"""
        self.auth.set_request_apikey('foobar')
        self.assertEqual(self.auth._api_key, 'foobar')

    def test_endpoint(self):
        """Test Auth.auth.endpoint property"""
        url = self.auth.endpoint
        self.assertEqual(self.auth._endpoint, url)

    def test_headers(self):
        """Test Auth.headers property"""
        auth = habrahabr.Auth(client='foo.bar', token='foobar')
        headers = auth.headers
        self.assertTrue(self.is_dict(headers))
        self.assertEqual(headers['client'], 'foo.bar')
        self.assertEqual(headers['token'], 'foobar')

        auth = habrahabr.Auth(api_key='foobar')
        headers = auth.headers
        self.assertTrue(self.is_dict(headers))
        self.assertEqual(headers['apikey'], 'foobar')

    def test_get_authorization_url(self):
        """Test Auth.get_authorization_url() method"""
        self.auth.set_request_client('foo.bar')
        url = self.auth.get_authorization_url('https://tmtm.ru/', 'token')

        self.assertTrue('/auth/o/login/' in url)
        self.assertTrue('response_type=token' in url)
        self.assertTrue('client_id=foo.bar' in url)
        self.assertTrue('redirect_uri=https%3A%2F%2Ftmtm.ru%2F' in url)


if __name__ == '__main__':
    unittest.main()
