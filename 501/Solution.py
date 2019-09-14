# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        table = defaultdict(int)
        
        def traverse(root):
            nonlocal table
            if not root:
                return 
            
            table[root.val] += 1
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        
        max_ = 0
        for key,val in table.items():
            if max_ < val:
                max_ = val
        
        return [key for key,val in table.items() if val == max_]