#!/usr/bin/python3
"""
cache implementation base class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    cache implementation class
    """
    def put(self, key, item):
        """
        add cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        get cache by key
        """
        return self.cache_data.get(key, None)
