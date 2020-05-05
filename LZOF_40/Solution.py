"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from heapq import *


class MyHeap():
    def __init__(self):
        self.data = []
        self.k = lambda x: -x
    
    def push(self, x):
        heappush(self.data, (self.k(x), x))
    
    def pop(self):
        return heappop(self.data)[-1]

    def top(self):
        return self.data[0][-1]

    @property
    def length(self):
        return len(self.data)


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        if k == 0:
            return []

        heap = MyHeap()
        res = []

        for num in arr:
            if heap.length < k:
                heap.push(num)
            else:
                if num < heap.top():
                    heap.pop()
                    heap.push(num)

        while heap.length > 0:
            res.append(heap.pop())
        
        return res[::-1]

