#!/usr/bin/env python3
''' Module for Redis basic mandotory '''


from typing import Callable, Union
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

    def get(self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''
            retrieves value from redis db
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''
            retrieves str from redis db
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
            retrieves int from redis db
        '''
        return self.get(key, lambda x: int(x))
