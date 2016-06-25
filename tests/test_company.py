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

"""This module contains a object that represents Tests for CompanyResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class CompanyResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for CompanyResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.CompanyResource(auth)
        self.resource._request = MockRequest()

    def test_posts(self):
        """Test CompanyResource.posts(alias, page) method"""
        self.resource._request.register_uri(
            'GET', '/company/tm?page=2', 'fixture_company.json')

        response = self.resource.posts('tm', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_posts_fail(self):
        """Test Fail CompanyResource.posts(alias, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.posts(100)

        with self.assertRaises(AssertionError):
            self.resource.posts('foo', 'bar')

    def test_info(self):
        """Test CompanyResource.info(alias) method"""
        self.resource._request.register_uri(
            'GET', '/company/tm/info', 'fixture_company.json')

        response = self.resource.info('tm')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_info_fail(self):
        """Test Fail CompanyResource.info(alias) method"""
        with self.assertRaises(AssertionError):
            self.resource.info(100)

    def test_list(self):
        """Test CompanyResource.list(page) method"""
        self.resource._request.register_uri(
            'GET', '/companies?page=2', 'fixture_company.json')

        response = self.resource.list(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_list_fail(self):
        """Test Fail CompanyResource.list(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.list('foobar')


if __name__ == '__main__':
    unittest.main()
