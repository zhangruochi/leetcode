# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = float('inf')
        prev = None
        
        def in_order(root):
            nonlocal prev,res
            if not root:
                return 
            
            in_order(root.left)
            
            if prev == None:
                prev = root.val
            else:
                res = min(root.val - prev, res)
                prev = root.val 
            
            in_order(root.right)
        
        in_order(root)
        
        return res