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
"""This module contains a object that represents a CommentsResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class CommentsResource(BaseResource):
    """Ресурс работы с комментариями."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(CommentsResource, self).__init__(*args, **kwargs)

    @accepts(int)
    def get(self, post_id):
        """Возвращает список комментариев к посту по номеру.

        :param post_id: Номер поста.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/comments/%d' % post_id)

    @accepts(int, str, [int])
    def add(self, post_id, message, comment_id=None):
        """Добавление комментария к посту по номеру.

        :param post_id: Номер поста.
        :param message: Текст комментария.
        :param comment_id: Номер комментария для ответа на комментарий.
        :returns: ответ API сервера.
        :rtype: dict
        """
        data = {
            'text': message
        }

        if comment_id is not None:
            data.update({'parent_id': comment_id})

        return self._request('/comments/%d' % post_id, 'PUT', data)

    @accepts(int, int)
    def vote(self, comment_id, vote):
        """Голосование за комментарий.

        :param comment_id: Номер комментария для голосования.
        :param vote: Голос 1 или -1.
        :returns: ответ API сервера.
        :rtype: dict
        """
        if vote not in [-1, 1]:
            raise ValueError('Vote must be -1 or 1')

        return self._request('/comments/%d/vote' % comment_id, 'PUT', {
            'vote': vote
        })
