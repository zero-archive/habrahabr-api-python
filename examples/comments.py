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
    comments = api.comments.get(259787)
    comment = api.comments.add(259787, 'New comment')
    reply = api.comments.add(259787, 'New comment', 8841783)
    vote = api.comments.vote(8841783, 1)
except habrahabr.ApiHandlerError as e:
    logging.error(e)
