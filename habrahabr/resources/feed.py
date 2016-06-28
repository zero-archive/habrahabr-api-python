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
"""This module contains a object that represents a FeedResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class FeedResource(BaseResource):
    """Ресурс работы с "основной" лентой постов."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(FeedResource, self).__init__(*args, **kwargs)

    @accepts(int)
    def habred(self, page=1):
        """Возвращает "Захабренные" посты из "основной" лентой постов.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/feed/habred?page=%d' % page)

    @accepts(int)
    def unhabred(self, page=1):
        """Возвращает "Отхабренные" посты из "основной" лентой постов.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/feed/unhabred?page=%d' % page)

    @accepts(int)
    def new(self, page=1):
        """Возвращает "Новые" посты из "основной" лентой постов.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/feed/new?page=%d' % page)
