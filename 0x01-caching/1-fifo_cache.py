#!/usr/bin/env python3
""" Module definition """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize FIFOCache with custom params """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ set item for corresponding key; if number of items is
            more than BaseCaching.MAX_ITEMS, discard first item
            in cache and print 'DISCARD: {key}'
        """
        cache = self.cache_data
        if (key is None or item is None):
            pass
        if (len(cache) >= BaseCaching.MAX_ITEMS and key not in cache):
            print('DISCARD: {}'.format(self.keys[0]))
            cache.pop(self.keys.pop(0))

        self.keys.append(key)
        cache[key] = item

    def get(self, key):
        """ returns the cache_data linked to a key """
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
