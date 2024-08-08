from collections import OrderedDict

class GoogleCacheMe:

    def __init__(self, n: int):
        self.cache = OrderedDict()
        self.capacity = n
    def put(self, k: int, v: int):
        if k in self.cache:
            self.cache.move_to_end(k)
        self.cache[k] = v
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    def display(self):
        for k, v in self.cache.items():
            print(f"{k}::::{v}")

if __name__ == "__main__":
    g = GoogleCacheMe(1)
    g.put(1, 2)
    g.put(2, 3)
    g.put(4, 5)
    g.put(6, 7)
    
    print("Print map values:")
    g.display()