# -*- coding: utf-8 -*-

from .base import BaseResource


class PostResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(PostResource, self).__init__(*args, **kwargs)

    def get(self, post_id):
        return self._request('/post/%d' % post_id)

    def meta(self, posts_ids):
        return self._request('/posts/meta', params={
            'ids': ','.join(posts_ids)
        })

    def vote(self, post_id, vote):
        return self._request('/post/%d/vote' % post_id, 'PUT', {
            'vote': vote
        })

    def add_to_favorite(self, post_id):
        return self._request('/post/%d/favorite' % post_id, 'PUT')

    def remove_from_favorite(self, post_id):
        return self._request('/post/%d/favorite' % post_id, 'DELETE')

    def increment_view_counter(self, post_id):
        return self._request('/post/%d/viewcount' % post_id, 'PUT')
