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
    post = api.post.get(241191)
    posts = api.post.meta(241191, 244691)
    vote = api.post.vote(241191, 1)
    favorite = api.post.add_to_favorite(241191)
    favorite = api.post.remove_from_favorite(241191)
    counter = api.post.increment_view_counter(241191)
except habrahabr.ApiHandlerError as e:
    logging.error(e)
