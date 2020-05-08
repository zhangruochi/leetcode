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

       
         
from heapq import *
from collections import namedtuple
from functools import total_ordering

class MyHeap():
    def __init__(self):
        self.data = []
    
    def push(self, x):
        heappush(self.data, x)
    
    def pop(self):
        return heappop(self.data)
    
    @property
    def size(self):
        return len(self.data)

    def top(self):
        return self.data[0]

@total_ordering
class Item():
    def __init__(self, num, i):
        self.num = num
        self.priority = -num
        self.index = i

    def __eq__(self, other):
        return self.priority == other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = MyHeap()
        res = []


        for i, num in enumerate(nums):
            
            while heap.size > 0 and i - heap.top().index >= k:
                heap.pop()

            heap.push(Item(num, i))

            if i >= k - 1:
                res.append(heap.top().num)
        
        return res




from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []

        for i, num in enumerate(nums):

            while len(queue) != 0 and num > nums[queue[-1]]:
                queue.pop()
            
            if len(queue) > 0 and i - queue[0] >= k:
                queue.popleft() 

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res

            
            
        