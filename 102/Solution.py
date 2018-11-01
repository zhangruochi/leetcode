"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        level = 0
        queue = deque([(root,level)])
        table = defaultdict(list)
        while queue:
            cur,level = queue.popleft()
            table[level].append(cur.val)
            if cur.left:
                queue.append((cur.left,level+1))
            if cur.right:
                queue.append((cur.right,level+1))
                
        return [table[i] for i in range(len(table))]
