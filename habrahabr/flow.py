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

from .base import BaseResource
from .utils import accepts


class FlowResource(BaseResource):
    """Ресурс работы с потоками."""

    def __init__(self, *args, **kwargs):
        super(FlowResource, self).__init__(*args, **kwargs)

    def list(self):
        """Возвращает список потоков.

        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/flows')

    @accepts(str, int)
    def interesting(self, alias, page=1):
        """Возвращает "Захабренные" посты из "основной" лентой постов.

        :param alias: Алиаса потока.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/flows/%s/interesting?page=%d' % (alias, page))

    @accepts(str, int)
    def all(self, alias, page=1):
        """Возвращает "Все" посты посты из потока.

        :param alias: Алиаса потока.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/flows/%s/all?page=%d' % (alias, page))

    @accepts(str, int)
    def best(self, alias, page=1):
        """Возвращает "Лучшие" посты из потока.

        :param alias: Алиаса потока.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/flows/%s/best?page=%d' % (alias, page))

    @accepts(str, int)
    def hubs(self, alias, page=1):
        """Возвращает список хабов потока.

        :param alias: Алиаса потока.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/flows/%s/hubs?page=%d' % (alias, page))