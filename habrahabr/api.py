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
"""This module contains a object that represents a Habrahabr Api."""

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
from habrahabr.errors import ApiHandlerError
from habrahabr.utils import lazy


class Api(object):
    """Этот объект содержит Habrahabr Api.

    Args:
        auth (object): Экземпляр класса Auth.
    """

    def __init__(self, auth=None):
        """Конструктор Api.

        :param auth: Экземпляр класса Auth.
        :rtype: object
        """
        if auth is None:
            raise ApiHandlerError('Auth handler is not defined')
        self.auth = auth

    @lazy
    def comments(self):
        """Ресурс работы с комментариями.

        :returns: CommentsResource.
        :rtype: object
        """
        return CommentsResource(self.auth)

    @lazy
    def company(self):
        """Ресурс работы с компаниями.

        :returns: CompanyResource.
        :rtype: object
        """
        return CompanyResource(self.auth)

    @lazy
    def feed(self):
        """Ресурс работы с основной лентой постов.

        :returns: FeedResource.
        :rtype: object
        """
        return FeedResource(self.auth)

    @lazy
    def flow(self):
        """Ресурс работы с потоками.

        :returns: FlowResource.
        :rtype: object
        """
        return FlowResource(self.auth)

    @lazy
    def hub(self):
        """Ресурс работы с хабами.

        :returns: HubResource.
        :rtype: object
        """
        return HubResource(self.auth)

    @lazy
    def poll(self):
        """Ресурс работы с опросами.

        :returns: PollResource.
        :rtype: object
        """
        return PollResource(self.auth)

    @lazy
    def post(self):
        """Ресурс работы с постами.

        :returns: PostResource.
        :rtype: object
        """
        return PostResource(self.auth)

    @lazy
    def search(self):
        """Ресурс работы с поиском.

        :returns: SearchResource.
        :rtype: object
        """
        return SearchResource(self.auth)

    @lazy
    def settings(self):
        """Ресурс работы с настройками профиля.

        :returns: SettingsResource.
        :rtype: object
        """
        return SettingsResource(self.auth)

    @lazy
    def tracker(self):
        """Ресурс работы с трекером.

        :returns: TrackerResource.
        :rtype: object
        """
        return TrackerResource(self.auth)

    @lazy
    def user(self):
        """Ресурс работы с пользователями.

        :returns: UserResource.
        :rtype: object
        """
        return UserResource(self.auth)
