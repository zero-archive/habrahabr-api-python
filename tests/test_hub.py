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

"""This module contains a object that represents Tests for HubResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class HubResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for HubResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')
        api = habrahabr.Api(auth)

        self.resource = api.hub
        self.resource._request = MockRequest()

    def test_info(self):
        """Test HubResource.info(alias) method"""
        self.resource._request.register_uri(
            'GET', '/hub/python/info', 'fixture_hub.json')

        response = self.resource.info('python')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_info_fail(self):
        """Test Fail HubResource.info(alias) method"""
        with self.assertRaises(AssertionError):
            self.resource.info(-1)

    def test_habred(self):
        """Test HubResource.habred(alias, page) method"""
        self.resource._request.register_uri(
            'GET', '/hub/python/habred?page=2', 'fixture_hub.json')

        response = self.resource.habred('python', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_habred_fail(self):
        """Test Fail HubResource.habred(alias, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.habred(-1)

        with self.assertRaises(AssertionError):
            self.resource.habred('foo', 'bar')

    def test_unhabred(self):
        """Test HubResource.unhabred(alias, page) method"""
        self.resource._request.register_uri(
            'GET', '/hub/python/unhabred?page=2', 'fixture_hub.json')

        response = self.resource.unhabred('python', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_unhabred_fail(self):
        """Test Fail HubResource.unhabred(alias, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.unhabred(-1)

        with self.assertRaises(AssertionError):
            self.resource.unhabred('foo', 'bar')

    def test_new(self):
        """Test HubResource.new(alias, page) method"""
        self.resource._request.register_uri(
            'GET', '/hub/python/new?page=2', 'fixture_hub.json')

        response = self.resource.new('python', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_new_fail(self):
        """Test Fail HubResource.new(alias, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.new(-1)

        with self.assertRaises(AssertionError):
            self.resource.new('foo', 'bar')

    def test_list(self):
        """Test HubResource.list(page) method"""
        self.resource._request.register_uri(
            'GET', '/hubs?page=2', 'fixture_hub.json')

        response = self.resource.list(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_list_fail(self):
        """Test Fail HubResource.list(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.list('foobar')

    def test_subscribe(self):
        """Test HubResource.subscribe(alias) method"""
        self.resource._request.register_uri(
            'PUT', '/hub/python')

        response = self.resource.subscribe('python')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_subscribe_fail(self):
        """Test Fail HubResource.subscribe(alias) method"""
        with self.assertRaises(AssertionError):
            self.resource.subscribe(-1)

    def test_unsubscribe(self):
        """Test HubResource.unsubscribe(alias) method"""
        self.resource._request.register_uri(
            'DELETE', '/hub/python')

        response = self.resource.unsubscribe('python')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_unsubscribe_fail(self):
        """Test Fail HubResource.unsubscribe(alias) method"""
        with self.assertRaises(AssertionError):
            self.resource.unsubscribe(-1)


if __name__ == '__main__':
    unittest.main()
