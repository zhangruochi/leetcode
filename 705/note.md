## 思路

- hashset 本质上是一个巨大的稀疏数组，根据 key 来计算数组的下标，然后把key存在对应的 bucket中


- 所有 hash_code 相等的key放入同一个链中
- 在链中的具体位置可由 pos 方法得到
- hash_code * pos 所有能容纳的数要比总的操作次数多


```Python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000                       
        self.itemsPerBuckect = 1001               
        self.set = [[] for _ in range(self.buckets)]
        
        
    def hash_code(self,key):
        return key % self.buckets
    
    def pos(self,key):
        return key // self.buckets
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hash_key = self.hash_code(key)
        if not self.set[hash_key]:
            self.set[hash_key] = [0] * self.itemsPerBuckect
        self.set[hash_key][self.pos(key)] = 1
            

        
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            hash_key = self.hash_code(key)
            self.set[hash_key][self.pos(key)] = 0
            if not any(self.set[hash_key]):
                self.set[hash_key] = []
                                


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self.hash_code(key)
        if self.set[hash_key] and self.set[hash_key][self.pos(key)]:
            return True
        return False
            
```

