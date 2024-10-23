#!/usr/bin/env python3
''' A module with tools for request caching and tracking '''
import redis
import requests
from functools import wraps


store = redis.Redis()
'''
    The module-level Redis instance
'''


def count_url_access(method):
    '''
        The wrapper function for caching the output
    '''
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    '''
        Returns the content of a URL after caching the request's response,
        and tracking the request
    '''
    res = requests.get(url)
    return res.text
