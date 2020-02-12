from collections import namedtuple
import heapq

class MyHeap(object):
    def __init__(self, initial=None):
        self.key = lambda x: -x.priority
       
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        # print(self._data)
        heapq.heappush(self._data, (self.key(item), item))
      
    def pop(self):
        return heapq.heappop(self._data)[1]

    def empty(self):
        return False if self._data else True
    
    def peak(self):
        return self._data[0][1]
    
    def __str__(self):
        return self._data
    
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        length = len(nums)
        queue = MyHeap()
        
        Item = namedtuple("Item",["priority","index"])
        
        for index, num in enumerate(nums):
            while (not queue.empty()) and queue.peak().index <= index - k:
                queue.pop()
            
            queue.push(Item(num,index))

            
            if index >= k - 1:
                res.append(queue.peak().priority)
        
        return res

                
            
            
        