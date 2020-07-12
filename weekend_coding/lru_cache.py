from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_cache = OrderedDict()
    def __len__(self):
        return len(self.lru_cache)
    def get(self, key):
        value = self.lru_cache.pop(key, None)
        if value is None:
            return -1
        self.lru_cache[key]=value
        return value

    def put(self, key, value):
        if not self.lru_cache.pop(key, None) and len(self.lru_cache)>=self.capacity:
            self.lru_cache.popitem(last=False)
        self.lru_cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():

    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
if __name__ == '__main__':
    main()

