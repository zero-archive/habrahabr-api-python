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

"""This module contains a object that represents Tests for CommentsResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class CommentsResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for CommentsResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.CommentsResource(auth)
        self.resource._request = MockRequest()

    def test_get(self):
        """Test CommentsResource.get(post_id) method"""
        self.resource._request.register_uri(
            'GET', '/comments/259787')

        response = self.resource.get(259787)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_add(self):
        """Test CommentsResource.add(post_id, message, comment_id) method"""
        self.resource._request.register_uri(
            'PUT', '/comments/8841783')

        response = self.resource.add(8841783, 'foobar')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_add_fail(self):
        """Test Fail CommentsResource.get(post_id) method"""
        with self.assertRaises(AssertionError):
            self.resource.add('foobar')

        with self.assertRaises(AssertionError):
            self.resource.add(8841783, 1000)

        with self.assertRaises(AssertionError):
            self.resource.add(8841783, 'foo', 'bar')

    def test_get_fail(self):
        """Test Fail CommentsResource.get(post_id) method"""
        with self.assertRaises(AssertionError):
            self.resource.get('foobar')

    def test_vote(self):
        """Test CommentsResource.vote(post_id, vote) method"""
        self.resource._request.register_uri(
            'PUT', '/comments/8841783/vote')

        response = self.resource.vote(8841783, 1)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_vote_fail(self):
        """Test Fail CommentsResource.vote() method"""
        with self.assertRaises(AssertionError):
            self.resource.vote('foobar')

        with self.assertRaises(ValueError):
            self.resource.vote(8841783, 2)


if __name__ == '__main__':
    unittest.main()
