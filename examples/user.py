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
    posts = api.user.me()
    user = api.user.get('dotzero')
    comments = api.user.comments('dotzero')
    posts = api.user.posts('dotzero')
    hubs = api.user.hubs('dotzero')
    companies = api.user.companies('dotzero')
    followers = api.user.followers('dotzero')
    followed = api.user.followed('dotzero')
    vote_plus = api.user.vote_plus('dotzero')
    vote_minus = api.user.vote_minus('dotzero')
    favorites_posts = api.user.favorites_posts('dotzero')
    favorites_comments = api.user.favorites_comments('dotzero')
except habrahabr.ApiHandlerError as e:
    logging.error(e)
