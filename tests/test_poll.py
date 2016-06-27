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

"""This module contains a object that represents Tests for PollResource"""

import unittest
import sys

sys.path.append('.')

import habrahabr
from tests.base import BaseTest
from tests.base import MockRequest


class PollResourceTest(BaseTest, unittest.TestCase):
    """This object represents Tests for PollResource."""

    def setUp(self):
        auth = habrahabr.Auth(client='foo.bar', token='foobar')

        self.resource = habrahabr.PollResource(auth)
        self.resource._request = MockRequest()

    def test_get(self):
        """Test PollResource.get(poll_id) method"""
        self.resource._request.register_uri(
            'GET', '/polls/15636', 'fixture_poll.json')

        response = self.resource.get(15636)

        self.assertTrue('data' in response)
        self.assertTrue('server_time' in response)

    def test_vote(self):
        """Test PollResource.vote(poll_id, vote_id, votes_ids) method"""
        self.resource._request.register_uri(
            'PUT', '/polls/15636/vote')

        response = self.resource.vote(15636, vote_id=76357)

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_votes(self):
        """Test PollResource.vote(poll_id, vote_id, votes_ids) method"""
        self.resource._request.register_uri(
            'PUT', '/polls/15636/vote')

        response = self.resource.vote(15636, votes_ids=[76357, 76359])

        self.assertEqual(response['ok'], 1)
        self.assertTrue('server_time' in response)

    def test_vote_fail(self):
        """Test Fail PollResource.vote(poll_id, vote_id, votes_ids) method"""
        with self.assertRaises(ValueError):
            self.resource.vote(15636)


if __name__ == '__main__':
    unittest.main()
