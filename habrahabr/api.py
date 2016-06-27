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

from .comments import CommentsResource
from .company import CompanyResource
from .feed import FeedResource
from .flow import FlowResource
from .hub import HubResource
from .poll import PollResource
from .post import PostResource
from .search import SearchResource
from .settings import SettingsResource
from .tracker import TrackerResource
from .user import UserResource
from .errors import ApiHandlerError


class Api(object):
    def __init__(self, auth=None):
        if auth is None:
            raise ApiHandlerError('Auth handler is not defined')

        self.auth = auth
        self.comments = CommentsResource(self.auth)
        self.company = CompanyResource(self.auth)
        self.feed = FeedResource(self.auth)
        self.flow = FlowResource(self.auth)
        self.hub = HubResource(self.auth)
        self.poll = PollResource(self.auth)
        self.post = PostResource(self.auth)
        self.search = SearchResource(self.auth)
        self.settings = SettingsResource(self.auth)
        self.tracker = TrackerResource(self.auth)
        self.user = UserResource(self.auth)
