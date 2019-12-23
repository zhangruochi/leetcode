"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""

from collections import  deque

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.genobj = self._iter()
    

    def _iter(self):
        while self.v1 and self.v2:
            yield self.v1.popleft()
            yield self.v2.popleft()

        while self.v1:
            yield self.v1.popleft() 
        
        while self.v2:
            yield self.v2.popleft() 

    def next(self):
        """
        :rtype: int
        """
        return next(self.genobj)
        


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1 or self.v2:
            return True
        else:
            return False    


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = deque(v1)
        self.v2 = deque(v2)


    def __iter__(self):
        while self.v1 and self.v2:
            yield self.v1.popleft()
            yield self.v2.popleft()

        while self.v1:
            yield self.v1.popleft() 
        
        while self.v2:
            yield self.v2.popleft() 


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1 or self.v2:
            return True
        else:
            return False   

        
if __name__ == '__main__':
    v1 = [1,2]
    v2 = [3,4,5,6]

    zig = ZigzagIterator(v1, v2)
    for item in zig:
        print(item)






