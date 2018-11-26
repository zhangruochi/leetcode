"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [ None for i in range(1000000)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = key
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = None
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.set[key] != None
 




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
            
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)