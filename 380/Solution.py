import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False
        
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.set.remove(val)
            return True
        except:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return list(self.set)[random.randint(0,len(self.set)-1)]
                             
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.table:
            self.table[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            return False
        
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.table:
            index = self.table[val]
            if index != len(self.nums)-1:
                self.nums[index],self.nums[-1] = self.nums[-1],self.nums[index]
                self.table[self.nums[index]] = index
            self.nums.pop()
            del self.table[val]
            return True
        else:
            return False 
            
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0,len(self.nums)-1)]
                             
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()