"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from heapq import *

class MyHeap(object):
    def __init__(self, array):
        self.key = lambda x: -x
        self.data = [(self.key(_), _) for _ in array]
        heapify(self.data)
    
    def pop(self):
        if not self.empty():
            return heappop(self.data)[-1]
    
    def push(self, x):
        heappush(self.data, (self.key(x), x))
        
    def empty(self):
        return len(self.data) == 0
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return str([_[-1] for _ in self.data])
        
            

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MyHeap(stones)
        while len(heap) > 1:
            y = heap.pop()
            x = heap.pop()
            if y != x:
                heap.push(y-x)
        
        if heap.empty():
            return 0
        
        return heap.pop()
            
            
        
        
        