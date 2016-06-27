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
    posts = api.search.posts('python')
    users = api.search.users('python')
    hubs = api.search.hubs('python')
except habrahabr.ApiHandlerError as e:
    logging.error(e)
