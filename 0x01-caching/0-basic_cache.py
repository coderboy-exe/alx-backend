#!/usr/bin/env python3
""" Module definition """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching system that inherits from BaseCaching class """
    def put(self, key, item):
        """ Assign to self.cache_data the item for 'key'"""
        if (key is None or item is None):
            pass
        cache = self.cache_data
        cache[key] = item

    def get(self, key):
        """ returns the vallue in cache_data linked to key """
        if (key is None or key not in self.cache_data.keys()):
            return None
        cache = self.cache_data
        return cache[key]
