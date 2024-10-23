#!/usr/bin/env python3
''' Module for Redis basic mandotory '''


from typing import Union
import uuid
import redis


class Cache:
    '''
        store an instance of the Redis client
    '''
    def __init__(self) -> None:
        ''' intialize cache instance '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            stores value in redis
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
