"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque(maxlen = size)

    
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size <= 0:
            return 0

        self.queue.append(val)
        return sum(list(self.queue)) / len(self.queue)

if __name__ == '__main__':
    obj = MovingAverage(0)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))
        

