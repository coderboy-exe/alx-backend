#!/usr/bin/env python3
""" Module definition """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initialize FIFOCache with custom params """
        super().__init__()
        self.keys = []
        self.freq = {}
        self.count = 0

    def put(self, key, item):
        """ set item for corresponding key; if number of items is
            more than BaseCaching.MAX_ITEMS, discard least frequently
            used item in cache and print 'DISCARD: {key}'
        """
        cache = self.cache_data
        if (key is None or item is None):
            pass
        if (len(cache) >= BaseCaching.MAX_ITEMS and key not in cache):
            min_freq = min(self.freq.values())
            if min_freq < self.count:
                self.count = min_freq

            while self.keys:
                del_key = self.keys.pop(0)
                if self.freq[del_key] == self.count:
                    break
            print('DISCARD: {}'.format(del_key))
            cache.pop(del_key)
            self.freq.pop(del_key)

        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        cache[key] = item

        self.freq[key] = self.freq[key] + 1 if key in self.freq else 1

    def get(self, key):
        """ returns the cache_data linked to a key """
        if (key is None or key not in self.cache_data.keys()):
            return None
        self.freq[key] = self.freq[key] + 1 if key in self.freq else 1
        self.keys.append(key)
        return self.cache_data[key]
