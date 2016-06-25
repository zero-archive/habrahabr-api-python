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

"""This module contains a object that represents Tests for FlowResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class FlowResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for PostResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.FlowResource(auth)
        self.resource._request = MockRequest()

    def test_list(self):
        """Test FlowResource.list() method"""
        self.resource._request.register_uri(
            'GET', '/flows')

        response = self.resource.list()

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_interesting(self):
        """Test FlowResource.interesting(alias, page=1) method"""
        self.resource._request.register_uri(
            'GET', '/flows/develop/interesting?page=2', 'fixture_post.json')

        response = self.resource.interesting('develop', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_interesting_fail(self):
        """Test Fail FlowResource.interesting(alias, page=1) method"""
        with self.assertRaises(AssertionError):
            self.resource.interesting(100)

        with self.assertRaises(AssertionError):
            self.resource.interesting('foo', 'bar')

    def test_all(self):
        """Test FlowResource.all(alias, page=1) method"""
        self.resource._request.register_uri(
            'GET', '/flows/develop/all?page=2', 'fixture_post.json')

        response = self.resource.all('develop', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_all_fail(self):
        """Test Fail FlowResource.all(alias, page=1) method"""
        with self.assertRaises(AssertionError):
            self.resource.all(100)

        with self.assertRaises(AssertionError):
            self.resource.all('foo', 'bar')

    def test_best(self):
        """Test FlowResource.best(alias, page=1) method"""
        self.resource._request.register_uri(
            'GET', '/flows/develop/best?page=2', 'fixture_post.json')

        response = self.resource.best('develop', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_best_fail(self):
        """Test Fail FlowResource.best(alias, page=1) method"""
        with self.assertRaises(AssertionError):
            self.resource.best(100)

        with self.assertRaises(AssertionError):
            self.resource.best('foo', 'bar')

    def test_hubs(self):
        """Test FlowResource.hubs(alias, page=1) method"""
        self.resource._request.register_uri(
            'GET', '/flows/develop/hubs?page=2', 'fixture_hub.json')

        response = self.resource.hubs('develop', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_hubs_fail(self):
        """Test Fail FlowResource.hubs(alias, page=1) method"""
        with self.assertRaises(AssertionError):
            self.resource.hubs(100)

        with self.assertRaises(AssertionError):
            self.resource.hubs('foo', 'bar')


if __name__ == '__main__':
    unittest.main()
