class LRUCache:

    def __init__(self, capacity: int):
        self.age = 0
        self.capacity = capacity
        self.age_lookup = {}
        self.cache = {}

    def _update_age(self, key):
        self.age += 1
        self.age_lookup[key] = self.age

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self._update_age(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        keys = list(self.cache.keys())
        if key in keys:
            self._update_age(key)
            self.cache[key] = value
            return
        
        if len(keys) < self.capacity:
            self._update_age(key)
            self.cache[key] = value
        else:
            # find youngest key
            min_key = keys[0]
            min_key_age = self.age_lookup[min_key]
            for k in keys:
                key_age = self.age_lookup[k]
                if key_age < min_key_age:
                    min_key_age = key_age
                    min_key = k
            # remove young key
            self.cache.pop(min_key)
            self.age_lookup.pop(min_key)

            # add new key
            self.cache[key] = value
            self._update_age(key)

        return


        
