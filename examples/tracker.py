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
    push = api.tracker.push('title', 'message')
    counters = api.tracker.counters()
    posts = api.tracker.posts()
    subscribers = api.tracker.subscribers()
    mentions = api.tracker.mentions()
    apps = api.tracker.apps()
except habrahabr.ApiHandlerError as e:
    logging.error(e)
