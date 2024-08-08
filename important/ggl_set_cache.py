class GglCacheHashSetMe:
    def __init__(self, cache_size: int):
        self.cache = []
        self.cache_size = cache_size
    
    def add(self, c: str):
        if c in self.cache:
            self.cache.remove(c)
        self.cache.append(c)
        if len(self.cache) > self.cache_size:
            self.cache.pop(0)
    
    def display(self):
        for c in self.cache:
            print(c)

if __name__ == "__main__":
    obj = GglCacheHashSetMe(2)
    obj.add('a')
    obj.add('b')
    obj.add('c')
    obj.add('d')
    
    print("Print set values:")
    obj.display()
