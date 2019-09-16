# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        if not root: return
        
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        
        
        if left and (not left.left) and (not left.right) and left.val == 0:
            left = None
        if right and (not right.left) and (not right.right) and right.val == 0:
            right = None
            
        root.left = left
        root.right = right
            
        
        return root
        