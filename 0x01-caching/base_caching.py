#!/usr/bin/python3
"""
base Caching
"""

class BaseCaching():
    """
    Base caching
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        init
        """
        self.cache_data = {}

    def print_cache(self):
        """
        print cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        add item to cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        get item from cache
        """
        raise NotImplementedError("get must be implemented in your cache class")
