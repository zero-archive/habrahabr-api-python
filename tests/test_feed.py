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

"""This module contains a object that represents Tests for FeedResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class FeedResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for FeedResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.FeedResource(auth)
        self.resource._request = MockRequest()

    def test_habred(self):
        """Test FeedResource.habred(page) method"""
        self.resource._request.register_uri(
            'GET', '/feed/habred?page=2', 'fixture_post.json')

        response = self.resource.habred(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_habred_fail(self):
        """Test Fail FeedResource.habred(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.habred('foobar')

    def test_unhabred(self):
        """Test FeedResource.unhabred(page) method"""
        self.resource._request.register_uri(
            'GET', '/feed/unhabred?page=2', 'fixture_post.json')

        response = self.resource.unhabred(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_unhabred_fail(self):
        """Test Fail FeedResource.unhabred(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.unhabred('foobar')

    def test_new(self):
        """Test FeedResource.new(page) method"""
        self.resource._request.register_uri(
            'GET', '/feed/new?page=2', 'fixture_post.json')

        response = self.resource.new(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_new_fail(self):
        """Test Fail FeedResource.new(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.new('foobar')


if __name__ == '__main__':
    unittest.main()
