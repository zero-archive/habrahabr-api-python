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
"""This module contains a object that represents a UserResource."""

from .base import BaseResource
from habrahabr.utils import accepts


class UserResource(BaseResource):
    """Ресурс работы с пользователями."""

    def __init__(self, *args, **kwargs):
        """Конструктор ресурса."""
        super(UserResource, self).__init__(*args, **kwargs)

    def me(self):
        """Возвращает профиль пользователя API ключа.

        :returns: ответ API сервера.
        :rtype: dict
        """
        return self.get('me')

    @accepts(str)
    def get(self, login):
        """Возвращает профиль пользователя по логину.

        :param login: Логин пользователя на сайте.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s' % login)

    @accepts(int)
    def list(self, page=1):
        """Возвращает список пользователей.

        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users?page=%d' % page)

    @accepts(str, int)
    def comments(self, login, page=1):
        """Возвращает комментарии пользователя по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/comments?page=%d' % (login, page))

    @accepts(str, int)
    def posts(self, login, page=1):
        """Возвращает посты пользователя по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/posts?page=%d' % (login, page))

    @accepts(str)
    def hubs(self, login):
        """Возвращает хабы на которые подписан пользователь.

        :param login: Логин пользователя на сайте.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/hubs' % login)

    @accepts(str)
    def companies(self, login):
        """Возвращает компании в которых работает пользователь.

        :param login: Логин пользователя на сайте.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/companies' % login)

    @accepts(str, int)
    def followers(self, login, page=1):
        """Возвращает список подписчиков пользователя по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/followers?page=%d' % (login, page))

    @accepts(str, int)
    def followed(self, login, page=1):
        """Возвращает список на кого подписан пользователь по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/followed?page=%d' % (login, page))

    @accepts(str)
    def vote_plus(self, login):
        """Плюсовать карму пользователя по логину.

        :param login: Логин пользователя на сайте.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/vote' % login, 'PUT')

    @accepts(str)
    def vote_minus(self, login):
        """Минусовать карму пользователя по логину.

        :param login: Логин пользователя на сайте.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/vote' % login, 'DELETE')

    @accepts(str, int)
    def favorites_posts(self, login, page=1):
        """Возвращает список "избранных" постов пользователя по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/favorites/posts?page=%d' %
                             (login, page))

    @accepts(str, int)
    def favorites_comments(self, login, page=1):
        """Возвращает список "избранных" комментариев пользователя по логину.

        :param login: Логин пользователя на сайте.
        :param page: Номер страницы.
        :returns: ответ API сервера.
        :rtype: dict
        """
        return self._request('/users/%s/favorites/comments?page=%d' %
                             (login, page))
