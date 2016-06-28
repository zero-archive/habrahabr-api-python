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
"""This module contains a object that represents a HubResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class HubResource(BaseResource):
    """Ресурс работы с хабами."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(HubResource, self).__init__(*args, **kwargs)

    @accepts(str)
    def info(self, alias):
        """Возвращает информацию о хабе по алиасу.

        :param alias: Алиаса хаба.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s/info' % alias)

    @accepts(str, int)
    def habred(self, alias, page=1):
        """Возвращает "Захабренные" посты связаные с хабом.

        :param alias: Алиаса хаба.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s/habred?page=%d' % (alias, page))

    @accepts(str, int)
    def unhabred(self, alias, page=1):
        """Возвращает "Отхабренные" посты связаные с хабом.

        :param alias: Алиаса хаба.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s/unhabred?page=%d' % (alias, page))

    @accepts(str, int)
    def new(self, alias, page=1):
        """Возвращает "Новые" посты связаные с хабом.

        :param alias: Алиаса хаба.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s/new?page=%d' % (alias, page))

    @accepts(int)
    def list(self, page=1):
        """Возвращает список хабов.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hubs?page=%d' % page)

    @accepts(str)
    def subscribe(self, alias):
        """Подписаться на хаб.

        :param alias: Алиаса хаба.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s' % alias, 'PUT')

    @accepts(str)
    def unsubscribe(self, alias):
        """Отписаться от хаба.

        :param alias: Алиаса хаба.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/hub/%s' % alias, 'DELETE')
