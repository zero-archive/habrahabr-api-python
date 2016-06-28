# Python Habrahabr.ru API

[![PyPI](https://img.shields.io/pypi/v/habrahabr-api.svg)](https://pypi.python.org/pypi/habrahabr-api)
[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://travis-ci.org/dotzero/habrahabr-api-python)
[![Build Status](https://travis-ci.org/dotzero/habrahabr-api-python.svg?branch=master)](https://travis-ci.org/dotzero/habrahabr-api-python)
[![Code Coverage](https://scrutinizer-ci.com/g/dotzero/habrahabr-api-python/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/dotzero/habrahabr-api-python/?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dotzero/habrahabr-api-python/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/dotzero/habrahabr-api-python/?branch=master)

Имплементация API сайта Habrahabr.ru используя Python.

## Быстрый старт

    >>> import habrahabr
    >>> auth = habrahabr.Auth(client="000000.00000000", token="0000000000")
    >>> api = habrahabr.Api(auth)
    >>> print(api.user.me())

## Поддержка

* python >= 2.7
* python >= 3.2

## Установка

### Из Pypi

    $ pip install habrahabr-api

### Из исходников

    $ git clone https://github.com/dotzero/habrahabr-api-python
    $ cd habrahabr-api-python
    $ python setup.py install

## Использование

Получение экземпляра класса habrahabr.Api для доступа ко всем ресурсам:

    >>> import habrahabr
    >>> auth = habrahabr.Auth(client="000000.00000000", token="0000000000")
    >>> api = habrahabr.Api(auth)

Описание API ресурсов:

* `api.comments` - Ресурс работы с комментариями
* `api.company` - Ресурс работы с компаниями
* `api.feed` - Ресурс работы с "основной" лентой постов
* `api.flow` - Ресурс работы с потоками
* `api.hub` - Ресурс работы с хабами
* `api.poll` - Ресурс работы с постами
* `api.post` - Ресурс работы с опросами
* `api.search` - Ресурс работы с поиском
* `api.settings` - Ресурс работы с настройками профиля
* `api.tracker` - Ресурс работы с трекером
* `api.user` - Ресурс работы с пользователями

## Лицензия

Библиотека доступна на условиях лицензии MIT: http://www.opensource.org/licenses/mit-license.php
