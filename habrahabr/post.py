# -*- coding: utf-8 -*-

from .base import BaseResource
from .utils import accepts


class PostResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(PostResource, self).__init__(*args, **kwargs)

    @accepts(int)
    def get(self, post_id):
        return self._request('/post/%d' % post_id)

    def meta(self, *args):
        if not len(args):
            raise ValueError('Empty args list')

        return self._request('/posts/meta', data={
            'ids': ','.join(str(x) for x in args)
        })

    @accepts(int, int)
    def vote(self, post_id, vote):
        if vote not in [-1, 1]:
            raise ValueError('Vote must be -1 or 1')

        return self._request('/post/%d/vote' % post_id, 'PUT', {
            'vote': vote
        })

    @accepts(int)
    def add_to_favorite(self, post_id):
        return self._request('/post/%d/favorite' % post_id, 'PUT')

    @accepts(int)
    def remove_from_favorite(self, post_id):
        return self._request('/post/%d/favorite' % post_id, 'DELETE')

    @accepts(int)
    def increment_view_counter(self, post_id):
        return self._request('/post/%d/viewcount' % post_id, 'PUT')
