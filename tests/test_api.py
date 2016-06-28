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

"""This module contains a object that represents Tests for Api"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest


class ApiTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Api."""

    def setUp(self):
        self.auth = habrahabr.Auth(client='foo.bar', token='bar')
        self.api = habrahabr.Api(self.auth)

    def test_comments(self):
        """Test Api.comments property"""
        obj = self.api.comments
        self.assert_is_instance(obj, habrahabr.CommentsResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_company(self):
        """Test Api.company property"""
        obj = self.api.company
        self.assert_is_instance(obj, habrahabr.CompanyResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_feed(self):
        """Test Api.feed property"""
        obj = self.api.feed
        self.assert_is_instance(obj, habrahabr.FeedResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_flow(self):
        """Test Api.flow property"""
        obj = self.api.flow
        self.assert_is_instance(obj, habrahabr.FlowResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_hub(self):
        """Test Api.flow property"""
        obj = self.api.hub
        self.assert_is_instance(obj, habrahabr.HubResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_poll(self):
        """Test Api.poll property"""
        obj = self.api.poll
        self.assert_is_instance(obj, habrahabr.PollResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_post(self):
        """Test Api.post property"""
        obj = self.api.post
        self.assert_is_instance(obj, habrahabr.PostResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_search(self):
        """Test Api.search property"""
        obj = self.api.search
        self.assert_is_instance(obj, habrahabr.SearchResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_settings(self):
        """Test Api.settings property"""
        obj = self.api.settings
        self.assert_is_instance(obj, habrahabr.SettingsResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_tracker(self):
        """Test Api.tracker property"""
        obj = self.api.tracker
        self.assert_is_instance(obj, habrahabr.TrackerResource)
        self.assertEqual(obj._auth._client, self.auth._client)

    def test_user(self):
        """Test Api.user property"""
        obj = self.api.user
        self.assert_is_instance(obj, habrahabr.UserResource)
        self.assertEqual(obj._auth._client, self.auth._client)


if __name__ == '__main__':
    unittest.main()
