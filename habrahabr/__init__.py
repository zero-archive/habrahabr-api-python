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

from .api import Api
from .auth import Auth
from .resources import *

# from .comments import CommentsResource
# from .company import CompanyResource
# from .feed import FeedResource
# from .flow import FlowResource
# from .hub import HubResource
# from .poll import PollResource
# from .post import PostResource
# from .search import SearchResource
# from .settings import SettingsResource
# from .tracker import TrackerResource
# from .user import UserResource
from .errors import AuthHandlerError, ApiHandlerError

# Set default logging handler to avoid "No handler found" warnings.
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'mail@dotzero.ru'
__version__ = '0.1.0'
__all__ = ('Api', 'ApiHandlerError', 'Auth', 'AuthHandlerError',
           'BaseResource', 'CommentsResource', 'CompanyResource',
           'FeedResource', 'FlowResource', 'HubResource', 'PollResource',
           'PostResource', 'SearchResource', 'SettingsResource',
           'TrackerResource', 'UserResource')
