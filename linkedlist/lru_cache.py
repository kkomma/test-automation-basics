class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            del self.cache[self.order[0]]
            self.order = self.order[1:]
        self.cache[key] = value
        self.order.append(key)
        
def main():
    # Create an LRU cache with capacity 3
    cache = LRUCache(3)

    # Put key-value pairs into the cache
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")

    # Get values from the cache
    print(cache.get(1))  # Output: A
    print(cache.get(2))  # Output: B
    print(cache.get(3))  # Output: C

    # Put a new key-value pair, which will evict the least recently used item
    cache.put(4, "D")

    # Get values from the cache
    print(cache.get(1))  # Output: -1 (not found)
    print(cache.get(2))  # Output: B
    print(cache.get(3))  # Output: C
    print(cache.get(4))  # Output: D

if __name__ == "__main__":
    main()