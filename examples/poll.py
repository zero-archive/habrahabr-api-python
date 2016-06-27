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
    poll = api.poll.get(15636)
    vote = api.poll.vote(15636, vote_id=76357)
    votes = api.poll.vote(15636, votes_ids=[76357, 76359])
except habrahabr.ApiHandlerError as e:
    logging.error(e)
