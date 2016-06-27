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
    flows = api.flow.list()
    interesting = api.flow.interesting('develop')
    posts = api.flow.all('develop')
    best = api.flow.best('develop')
    hubs = api.flow.hubs('develop')
except habrahabr.ApiHandlerError as e:
    logging.error(e)
