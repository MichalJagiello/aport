
from aport.exceptions import CacheKeyNotExistError


class Cache(object):
    """
    Base cache class
    """

    def set(self, key, value):
        """
        Set value for given key.
        If key already exists replace it's value.
        """
        raise NotImplementedError

    def get(self, key):
        """
        Get the key's value
        """
        raise NotImplementedError

    def pop(self, key):
        """
        Get the key's value and remove it from cache
        """
        raise NotImplementedError

    def delete(self, key):
        """
        Delete given key.
        """
        raise NotImplementedError

    def exists(self, key):
        """
        Return True if key exists in cache. False otherwise
        """
        raise NotImplementedError


class CacheData(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class MemoryCache(Cache):

    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        try:
            value = self.cache[key]
            return CacheData(key, value)
        except KeyError:
            raise CacheKeyNotExistError

    def delete(self, key):
        try:
            del self.cache[key]
        except KeyError:
            raise CacheKeyNotExistError

    def pop(self, key):
        try:
            value = self.get(key)
            self.delete(key)
            return CacheData(key, value)
        except CacheKeyNotExistError:
            raise CacheKeyNotExistError  # need to add logger for that

    def exists(self, key):
        try:
            self.get(key)
            return True
        except CacheKeyNotExistError:
            return False
