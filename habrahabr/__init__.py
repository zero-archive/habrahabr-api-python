#!/usr/bin/env python
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
"""A library that provides a Python interface to the Habrahabr.ru API."""

from .api import Api
from .auth import Auth
from .resources.base import BaseResource
from .resources.comments import CommentsResource
from .resources.company import CompanyResource
from .resources.feed import FeedResource
from .resources.flow import FlowResource
from .resources.hub import HubResource
from .resources.poll import PollResource
from .resources.post import PostResource
from .resources.search import SearchResource
from .resources.settings import SettingsResource
from .resources.tracker import TrackerResource
from .resources.user import UserResource
from .errors import AuthHandlerError, ApiHandlerError

# Set default logging handler to avoid "No handler found" warnings.
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:  # pragma: no cover
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'mail@dotzero.ru'
__version__ = '0.1.1'
__all__ = ('Api', 'ApiHandlerError', 'Auth', 'AuthHandlerError',
           'BaseResource', 'CommentsResource', 'CompanyResource',
           'FeedResource', 'FlowResource', 'HubResource', 'PollResource',
           'PostResource', 'SearchResource', 'SettingsResource',
           'TrackerResource', 'UserResource')
