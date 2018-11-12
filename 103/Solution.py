"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = 0
        queue = deque([(root,level)])
        ans_table = defaultdict(list)
        
        while queue:
            cur,level = queue.popleft()
            ans_table[level].append(cur.val)

            if cur.left:
                queue.append((cur.left,level+1))
            if cur.right:
                queue.append((cur.right,level+1))

        return [ans_table[i] if i % 2 == 0 else list(reversed(ans_table[i])) for i in range(len(ans_table)) ]
        
        
                
        
        