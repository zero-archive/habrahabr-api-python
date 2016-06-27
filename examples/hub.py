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
    info = api.hub.info('python')
    habred = api.hub.habred('python')
    unhabred = api.hub.unhabred('python')
    new = api.hub.new('python')
    hubs = api.hub.list(2)
    subscribe = api.hub.subscribe('python')
    unsubscribe = api.hub.unsubscribe('python')
except habrahabr.ApiHandlerError as e:
    logging.error(e)
