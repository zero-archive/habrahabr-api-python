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

"""This module contains a object that represents Tests for PostResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class PostResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for PostResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')
        api = habrahabr.Api(auth)

        self.resource = api.post
        self.resource._request = MockRequest()

    def test_get(self):
        """Test PostResource.get(post_id) method"""
        self.resource._request.register_uri(
            'GET', '/post/259787', 'fixture_post.json')

        response = self.resource.get(259787)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_get_fail(self):
        """Test Fail PostResource.get(post_id) method"""
        with self.assertRaises(AssertionError):
            self.resource.get('foobar')

    def test_meta(self):
        """Test PostResource.meta(posts_ids) method"""
        self.resource._request.register_uri(
            'GET', '/posts/meta?ids=259787%2C259788')

        response = self.resource.meta(259787, 259788)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_meta_fail(self):
        """Test Fail PostResource.meta() method"""
        with self.assertRaises(ValueError):
            self.resource.meta()

    def test_vote(self):
        """Test PostResource.vote(post_id, vote) method"""
        self.resource._request.register_uri(
            'PUT', '/post/259787/vote')

        response = self.resource.vote(259787, 1)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_vote_fail(self):
        """Test Fail PostResource.vote() method"""
        with self.assertRaises(AssertionError):
            self.resource.vote('foobar')

        with self.assertRaises(ValueError):
            self.resource.vote(259787, 2)

    def test_add_to_favorite(self):
        """Test PostResource.add_to_favorite(post_id) method"""
        self.resource._request.register_uri(
            'PUT', '/post/259787/favorite')

        response = self.resource.add_to_favorite(259787)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_remove_from_favorite_fail(self):
        """Test Fail PostResource.add_to_favorite() method"""
        with self.assertRaises(AssertionError):
            self.resource.add_to_favorite('foobar')

    def test_remove_from_favorite(self):
        """Test PostResource.remove_from_favorite(post_id) method"""
        self.resource._request.register_uri(
            'DELETE', '/post/259787/favorite')

        response = self.resource.remove_from_favorite(259787)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_remove_from_favorite_fail(self):
        """Test Fail PostResource.remove_from_favorite() method"""
        with self.assertRaises(AssertionError):
            self.resource.remove_from_favorite('foobar')

    def test_increment_view_counter(self):
        """Test PostResource.increment_view_counter(post_id) method"""
        self.resource._request.register_uri(
            'PUT', '/post/259787/viewcount')

        response = self.resource.increment_view_counter(259787)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_increment_view_counter_fail(self):
        """Test Fail PostResource.increment_view_counter() method"""
        with self.assertRaises(AssertionError):
            self.resource.increment_view_counter('foobar')


if __name__ == '__main__':
    unittest.main()
