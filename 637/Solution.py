"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:

The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        level = 0
        queue = deque([(root,0)])
        table = {}
        while queue:
            cur,level = queue.popleft()
            if level not in table:
                table[level] = [cur.val]
            else:
                table[level].append(cur.val)
            if cur.left:
                queue.append((cur.left,level+1))

            if cur.right:
                queue.append((cur.right,level+1))
        
        return [sum(table[i])/len(table[i]) for i in range(len(table))]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        queue = deque([(0,root)])
        table = defaultdict(list)
        while queue:
            level,node = queue.popleft()
            table[level].append(node.val)
            if node.left:
                queue.append((level+1,node.left))
            if node.right:
                queue.append((level+1,node.right))
                
        
        return [sum(vals)/len(vals) for key,vals in table.items()]
        