# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if not root: return False
        
        queue = deque([(None,0,root)])
        levels = []
        fathers = []
        while queue:
            father,level,root = queue.popleft()
            if root.val == x or root.val == y:
                levels.append(level)
                fathers.append(father)
            if root.left:
                queue.append((root,level+1,root.left))
            if root.right:
                queue.append((root,level+1,root.right))
        
        return True if levels[0] == levels[1] and fathers[0] != fathers[1] else False

        