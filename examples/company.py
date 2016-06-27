#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import habrahabr

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)-8s %(asctime)s - %(message)s'
)

auth = habrahabr.Auth(client="000000.00000000", token="0000000000")
api = habrahabr.Api(auth)

try:
    posts = api.company.posts('tm')
    info = api.company.info('tm')
    companies = api.company.list()
except habrahabr.ApiHandlerError as e:
    logging.error(e)
