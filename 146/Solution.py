"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.queue = deque()
        self.map = {}
        self.cap = capacity
    
        
        
    def get(self, key: int) -> int:
        res = self.map.get(key,-1)
        if res != -1:
            self.queue.remove(key)
            self.queue.appendleft(key)
        
        return res
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            self.queue.remove(key)
            del self.map[key]
        
        if len(self.queue) >= self.cap:
            k = self.queue.pop()
            del self.map[k]
    
            
        self.queue.appendleft(key)
        self.map[key] = value
        
        # print(self.map)
        # print(self.queue)
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.map = OrderedDict()
        self.size = capacity
        

    def get(self, key: int) -> int:
        res = self.map.get(key,-1)
        if res != -1:
            self.map.move_to_end(key, last = True)
        return res
        
        

    def put(self, key: int, value: int) -> None:
                
        self.map[key] = value
        self.map.move_to_end(key, last = True)
        
        
        if len(self.map) > self.size:
            self.map.popitem(last = False)

        

class LRUCache:

    def __init__(self, capacity: int):
        from collections import deque, OrderedDict

        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)