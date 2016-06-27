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

"""This module contains a object that represents Tests for SearchResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class SearchResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for SearchResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')
        api = habrahabr.Api(auth)

        self.resource = api.search
        self.resource._request = MockRequest()

    def test_posts(self):
        """Test SearchResource.posts(q, page) method"""
        self.resource._request.register_uri(
            'GET', '/search/posts/python?page=2', 'fixture_post.json')

        response = self.resource.posts('python', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_posts_fail(self):
        """Test Fail SearchResource.posts(q, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.posts(-1)

    def test_users(self):
        """Test SearchResource.users(q, page) method"""
        self.resource._request.register_uri(
            'GET', '/search/users/python?page=2', 'fixture_user.json')

        response = self.resource.users('python', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_users_fail(self):
        """Test Fail SearchResource.users(q, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.users(-1)

    def test_hubs(self):
        """Test SearchResource.hubs(q) method"""
        self.resource._request.register_uri(
            'GET', '/hubs/search/python', 'fixture_hub.json')

        response = self.resource.hubs('python')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_hubs_fail(self):
        """Test Fail SearchResource.hubs(q) method"""
        with self.assertRaises(AssertionError):
            self.resource.hubs(-1)


if __name__ == '__main__':
    unittest.main()
