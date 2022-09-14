class LRUCache(object):
    def __init__(self, capacity):
        self.d = OrderedDict()
        self.cap = capacity
        
    def get(self, key):
        if key not in self.d:
            return -1
        value = self.d[key]
        del self.d[key]
        self.d[key] = value
        return value
        
    def put(self, key, value):
        if key not in self.d:
            if len(self.d) == self.cap:
                k = next(iter(self.d))
                del self.d[k]
            self.d[key] = value
        else:
            del self.d[key]
            self.d[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
