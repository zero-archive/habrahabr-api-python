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

"""This module contains a object that represents Tests for TrackerResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class TrackerResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for TrackerResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.TrackerResource(auth)
        self.resource._request = MockRequest()

    def test_push(self):
        """Test TrackerResource.push(title, text) method"""
        self.resource._request.register_uri(
            'PUT', '/tracker')

        response = self.resource.push('foo', 'bar')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_push_fail(self):
        """Test Fail TrackerResource.push(title, text) method"""
        with self.assertRaises(AssertionError):
            self.resource.push(-1)

        with self.assertRaises(AssertionError):
            self.resource.push('foobar', -1)

    def test_counters(self):
        """Test TrackerResource.counters() method"""
        self.resource._request.register_uri(
            'GET', '/tracker/counters')

        response = self.resource.counters()

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_posts(self):
        """Test TrackerResource.posts(page) method"""
        self.resource._request.register_uri(
            'GET', '/tracker/posts?page=2')

        response = self.resource.posts(2)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_posts_fail(self):
        """Test Fail TrackerResource.posts(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.posts('foobar')

    def test_subscribers(self):
        """Test TrackerResource.subscribers(page) method"""
        self.resource._request.register_uri(
            'GET', '/tracker/subscribers?page=2')

        response = self.resource.subscribers(2)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_subscribers_fail(self):
        """Test Fail TrackerResource.subscribers(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.subscribers('foobar')

    def test_mentions(self):
        """Test TrackerResource.mentions(page) method"""
        self.resource._request.register_uri(
            'GET', '/tracker/mentions?page=2')

        response = self.resource.mentions(2)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_mentions_fail(self):
        """Test Fail TrackerResource.mentions(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.mentions('foobar')

    def test_apps(self):
        """Test TrackerResource.apps() method"""
        self.resource._request.register_uri(
            'GET', '/tracker/apps')

        response = self.resource.apps()

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)


if __name__ == '__main__':
    unittest.main()
