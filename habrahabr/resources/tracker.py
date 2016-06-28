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
"""This module contains a object that represents a TrackerResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class TrackerResource(BaseResource):
    """Ресурс работы с трекером."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(TrackerResource, self).__init__(*args, **kwargs)

    @accepts(str, str)
    def push(self, title, text):
        """Отправить сообщение в трекер на вкладку "Приложения".

        :param title: Заголовок для пуша.
        :param text: Текст для пуша.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker', 'PUT', {
            'title': title,
            'text': text
        })

    def counters(self):
        """Возвращает счетчики новых сообщений из трекера.

           Элементы не отмечаются как просмотренные.

        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker/counters')

    @accepts(int)
    def posts(self, page=1):
        """Возвращает список постов из трекера.

           Элементы не отмечаются как просмотренные.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker/posts?page=%d' % page)

    @accepts(int)
    def subscribers(self, page=1):
        """Возвращает список подписчиков из трекера.

           Элементы не отмечаются как просмотренные.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker/subscribers?page=%d' % page)

    @accepts(int)
    def mentions(self, page=1):
        """Возвращает список упоминаний из трекера.

           Элементы не отмечаются как просмотренные.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker/mentions?page=%d' % page)

    def apps(self):
        """Возвращает список сообщений приложений из трекера.

           Элементы не отмечаются как просмотренные.

        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/tracker/apps')
