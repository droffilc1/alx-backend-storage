#!/usr/bin/env python3
""" exercise.py """

from typing import Union, Optional
import uuid
import redis


class Cache:
    """Cache class."""

    def __init__(self):
        """Creates a connection with the db and clears cache."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates keys and stores data in the db."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[callable]) -> Union[str, bytes, int, float]:
        """Takes a key string argument and an optional Callable
        argument named fn. This callable will be used to convert
        the data back to the desired format.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Automatically parametrize Cache.get with the correct
        conversion function.
        """
        value = self._redis.get(key).decode('utf-8')
        return value

    def get_int(self, key: str) -> int:
        """Automatically parametrize Cache.get with the correct
          conversion function.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
