from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    @property
    def cache(self):
        if len(self.cache_dict) > 0:
            return next(iter(self.cache_dict))

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            del self.cache_dict[key]

        self.cache_dict[key] = value
        if len(self.cache_dict) > self.capacity:
            self.cache_dict.popitem(last=False)

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict.pop(key)
            self.cache_dict[key] = value
            return value
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key4", "value4")
cache.print_cache()
