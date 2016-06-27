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

"""This module contains a object that represents Tests for BaseResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest


class BaseResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for BaseResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')
        auth._endpoint = 'https://httpbin.org'
        self.base = habrahabr.BaseResource(auth)

    def test_request_get(self):
        """Test GET BaseResource._request(url, method, data) method"""
        r = self.base._request('/get', 'GET', {
            'foo': 'bar'
        })

        self.assertEqual(r['url'], 'https://httpbin.org/get?foo=bar')
        self.assertEqual(r['headers']['Client'], 'foo.bar')
        self.assertEqual(r['headers']['Token'], 'foobar')

    def test_request_post(self):
        """Test POST BaseResource._request(url, method, data) method"""
        r = self.base._request('/post', 'POST', {
            'foo': 'bar'
        })

        self.assertEqual(r['url'], 'https://httpbin.org/post')
        self.assertEqual(r['headers']['Client'], 'foo.bar')
        self.assertEqual(r['headers']['Token'], 'foobar')
        self.assertEqual(r['form']['foo'], 'bar')

    def test_request_put(self):
        """Test PUT BaseResource._request(url, method, data) method"""
        r = self.base._request('/put', 'PUT', {
            'foo': 'bar'
        })

        self.assertEqual(r['url'], 'https://httpbin.org/put')
        self.assertEqual(r['headers']['Client'], 'foo.bar')
        self.assertEqual(r['headers']['Token'], 'foobar')
        self.assertEqual(r['form']['foo'], 'bar')

    def test_request_delete(self):
        """Test DELETE BaseResource._request(url, method, data) method"""
        r = self.base._request('/delete', 'DELETE', {
            'foo': 'bar'
        })
        self.assertEqual(r['url'], 'https://httpbin.org/delete?foo=bar')
        self.assertEqual(r['headers']['Client'], 'foo.bar')
        self.assertEqual(r['headers']['Token'], 'foobar')


if __name__ == '__main__':
    unittest.main()
