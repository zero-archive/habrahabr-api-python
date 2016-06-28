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
"""This module contains a object that represents a PostResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class PostResource(BaseResource):
    """Ресурс работы с постами."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(PostResource, self).__init__(*args, **kwargs)

    @accepts(int)
    def get(self, post_id):
        """Возвращает пост по номеру.

        :param post_id: Номер поста.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/post/%d' % post_id)

    def meta(self, *args):
        """Получить мета-информацию постов (не более 30 постов за раз).

        :returns: ответ API сервера.
        :rtype: dict
        """
        if not len(args):
            raise ValueError('Empty args list')

        return self._request('/posts/meta', data={
            'ids': ','.join(str(x) for x in args)
        })

    @accepts(int, int)
    def vote(self, post_id, vote):
        """Голосование за пост.

        :param post_id: Номер поста.
        :param vote: Голос 1 или -1.
        :returns: ответ API сервера.
        :rtype: dict
        """
        if vote not in [-1, 1]:
            raise ValueError('Vote must be -1 or 1')

        return self._request('/post/%d/vote' % post_id, 'PUT', {
            'vote': vote
        })

    @accepts(int)
    def add_to_favorite(self, post_id):
        """Добавить пост в избранное.

        :param post_id: Номер поста.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/post/%d/favorite' % post_id, 'PUT')

    @accepts(int)
    def remove_from_favorite(self, post_id):
        """Удалить пост из избранного.

        :param post_id: Номер поста.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/post/%d/favorite' % post_id, 'DELETE')

    @accepts(int)
    def increment_view_counter(self, post_id):
        """Увеличить счетчик просмотров поста.

        :param post_id: Номер поста.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/post/%d/viewcount' % post_id, 'PUT')
