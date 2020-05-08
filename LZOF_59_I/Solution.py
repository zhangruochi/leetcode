"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []

        for i, num in enumerate(nums):

            while len(queue) != 0 and num > nums[queue[-1]]:
                queue.pop()
            
            while len(queue) > 0 and i - queue[0] >= k:
                queue.popleft() 

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])
        
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

# @total_ordering
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


