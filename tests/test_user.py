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

"""This module contains a object that represents Tests for UserResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class UserResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for UserResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.UserResource(auth)
        self.resource._request = MockRequest()

    def test_me(self):
        """Test UserResource.me() method"""
        self.resource._request.register_uri(
            'GET', '/users/me', 'fixture_user.json')

        response = self.resource.me()

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_get(self):
        """Test UserResource.get(login) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero', 'fixture_user.json')

        response = self.resource.get('dotzero')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_get_fail(self):
        """Test Fail UserResource.get(login) method"""
        with self.assertRaises(AssertionError):
            self.resource.get(-1)

    def test_list(self):
        """Test UserResource.list(page) method"""
        self.resource._request.register_uri(
            'GET', '/users?page=2', 'fixture_user.json')

        response = self.resource.list(2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_list_fail(self):
        """Test Fail UserResource.list(page) method"""
        with self.assertRaises(AssertionError):
            self.resource.get(-1)

    def test_comments(self):
        """Test UserResource.comments(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/comments?page=2', 'fixture_user.json')

        response = self.resource.comments('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_comments_fail(self):
        """Test Fail UserResource.comments(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.comments(-1)

        with self.assertRaises(AssertionError):
            self.resource.comments('foo', 'bar')

    def test_posts(self):
        """Test UserResource.posts(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/posts?page=2', 'fixture_post.json')

        response = self.resource.posts('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_posts_fail(self):
        """Test Fail UserResource.posts(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.posts(-1)

        with self.assertRaises(AssertionError):
            self.resource.posts('foo', 'bar')

    def test_hubs(self):
        """Test UserResource.hubs(login) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/hubs', 'fixture_hub.json')

        response = self.resource.hubs('dotzero')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_hubs_fail(self):
        """Test Fail UserResource.hubs(login) method"""
        with self.assertRaises(AssertionError):
            self.resource.hubs(-1)

    def test_companies(self):
        """Test UserResource.companies(login) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/companies', 'fixture_company.json')

        response = self.resource.companies('dotzero')

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_companies_fail(self):
        """Test Fail UserResource.companies(login) method"""
        with self.assertRaises(AssertionError):
            self.resource.companies(-1)

    def test_followers(self):
        """Test UserResource.followers(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/followers?page=2', 'fixture_post.json')

        response = self.resource.followers('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_followers_fail(self):
        """Test Fail UserResource.followers(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.followers(-1)

    def test_followed(self):
        """Test UserResource.followed(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/followed?page=2', 'fixture_post.json')

        response = self.resource.followed('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_followed_fail(self):
        """Test Fail UserResource.followed(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.followed(-1)

    def test_vote_plus(self):
        """Test UserResource.vote_plus(login) method"""
        self.resource._request.register_uri(
            'PUT', '/users/dotzero/vote')

        response = self.resource.vote_plus('dotzero')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_vote_minus(self):
        """Test UserResource.vote_minus(login) method"""
        self.resource._request.register_uri(
            'DELETE', '/users/dotzero/vote')

        response = self.resource.vote_minus('dotzero')

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_favorites_posts(self):
        """Test UserResource.favorites_posts(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/favorites/posts?page=2', 'fixture_post.json')

        response = self.resource.favorites_posts('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_favorites_posts_fail(self):
        """Test Fail UserResource.favorites_posts(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.favorites_posts(-1)

        with self.assertRaises(AssertionError):
            self.resource.favorites_posts('foo', 'bar')

    def test_favorites_comments(self):
        """Test UserResource.favorites_comments(login, page) method"""
        self.resource._request.register_uri(
            'GET', '/users/dotzero/favorites/comments?page=2',
            'fixture_post.json')

        response = self.resource.favorites_comments('dotzero', 2)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_favorites_comments_fail(self):
        """Test Fail UserResource.favorites_comments(login, page) method"""
        with self.assertRaises(AssertionError):
            self.resource.favorites_comments(-1)

        with self.assertRaises(AssertionError):
            self.resource.favorites_comments('foo', 'bar')


if __name__ == '__main__':
    unittest.main()
