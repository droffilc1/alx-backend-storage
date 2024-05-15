#!/usr/bin/env python3
""" exercise.py """

from typing import Union
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
