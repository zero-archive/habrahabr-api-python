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
"""This module contains a object that represents a PollResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class PollResource(BaseResource):
    """Ресурс работы с опросами."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(PollResource, self).__init__(*args, **kwargs)

    @accepts(int)
    def get(self, poll_id):
        """Возвращает опрос по номеру.

        :param poll_id: Номер опроса.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/polls/%d' % poll_id)

    @accepts(int, [int], [list])
    def vote(self, poll_id, vote_id=None, votes_ids=None):
        """Голосование в опросе за один или несколько варинатов ответа.

        :param poll_id: Номер опроса.
        :param vote_id: Номер варината ответа.
        :param votes_ids: Номера варинатов ответа.
        :returns: ответ API сервера.
        :rtype: dict
        """
        if not vote_id and not votes_ids:
            raise ValueError('Vote or votes is not defined')

        if vote_id:
            votes_ids = [vote_id]

        return self._request('/polls/%d/vote' % poll_id, 'PUT', {
            'id': votes_ids
        })
