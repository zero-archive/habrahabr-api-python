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
"""This module contains a object that represents a SearchResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class SearchResource(BaseResource):
    """Ресурс работы с поиском."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(SearchResource, self).__init__(*args, **kwargs)

    @accepts(str, int)
    def posts(self, q, page=1):
        """Поиск произвольного запроса по постам.

        :param q: Поисковая фраза.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/search/posts/%s?page=%d' % (q, page))

    @accepts(str, int)
    def users(self, q, page=1):
        """Поиск произвольного запроса по пользователям.

        :param q: Поисковая фраза.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/search/users/%s?page=%d' % (q, page))

    @accepts(str)
    def hubs(self, q):
        """Поиск произвольного запроса по хабам.

        :param q: Поисковая фраза.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hubs/search/%s' % q)
