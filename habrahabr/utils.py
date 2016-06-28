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
"""This module contains a object that represents a Habrahabr Utils."""

from functools import wraps


def accepts(*types):
    """Декоратор для фильтрации входящих параметров."""
    def decorated(f):
        # don't forget self
        assert 1 + len(types) == f.__code__.co_argcount

        @wraps(f)
        def wrapped(*args, **kwargs):
            for (a, t) in zip(args[1:], types):
                if isinstance(t, list):
                    t = None if a is None else t[0]

                assert isinstance(a, t), "Arg %r does not match %s" % (a, t)
            return f(*args, **kwargs)

        return wrapped

    return decorated


def lazy(func):
    """Декоратор для ленивой загрузки."""
    @property
    def wrapper(self):
        attr_name = '__%s' % func.__name__
        try:
            value = getattr(self, attr_name)
        except AttributeError:
            value = func(self)
            setattr(self, attr_name, value)
        return value

    return wrapper
