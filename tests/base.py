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

import os
import json

cwd = os.path.dirname(os.path.abspath(__file__))


class MockRequest(object):
    def __init__(self):
        self.registry = {}

    def __call__(self, *args, **kwargs):
        return self._request(*args, **kwargs)

    def register_uri(self, method, url, fixture):
        key = '%s:%s' % (method, url)
        with open(os.path.join(cwd, 'fixtures', fixture)) as f:
            self.registry[key] = json.load(f)

    def _request(self, url, method='GET', params=None):
        key = '%s:%s' % (method, url)
        if key not in self.registry:
            raise Exception('Mock not found ' + key)

        return self.registry[key]


class BaseTest(object):
    """This object represents a Base test and its sets of functions."""

    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)

    @staticmethod
    def is_json(string):
        try:
            json.loads(string)
        except ValueError:
            return False

        return True

    @staticmethod
    def is_dict(dictionary):
        if isinstance(dictionary, dict):
            return True

        return False

    @staticmethod
    def to_json(string):
        try:
            data = json.loads(string)
        except ValueError:
            return False

        return data
