"""
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from heapq import *

class MyHeap():
    def __init__(self, capacity):
        self.data = []
        self.k = lambda x: x
        self.capacity = capacity
    
    def push(self, x):
        if self.size < self.capacity:
            heappush(self.data, (self.k(x), x))
        else:
            if self.top() < x:
                self.pop()
                heappush(self.data, (self.k(x), x))

    def pop(self):
        return heappop(self.data)[-1]

    def top(self):
        return self.data[0][-1]
    
    @property
    def size(self):
        return len(self.data)


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        heap = MyHeap(k)

        def pre_order(root):
            if not root:
                return 
            
            heap.push(root.val)
            pre_order(root.left)
            pre_order(root.right)
        
        pre_order(root)

        return heap.top()



            
