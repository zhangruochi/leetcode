# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        level = 0
        queue = deque([(root,level)])
        res = {}
        while queue:
            root, level = queue.popleft()
            res[level] = root.val
            if root.left:
                queue.append((root.left,level+1))
            if root.right:
                queue.append((root.right,level+1))
                
        return [item[1] for item  in sorted(res.items(),key = lambda x:x[0])]   
        