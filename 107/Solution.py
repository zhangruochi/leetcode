# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from collections import defaultdict

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        table = defaultdict(list)
        level = 0
        queue = deque([(level,root)])
        
        while queue:
            level,root = queue.popleft()
            table[level].append(root.val)
            if root.left:
                queue.append((level+1,root.left))
            if root.right:
                queue.append((level+1,root.right))
        
        return [table[i] for i in range(len(table)-1,-1,-1)]