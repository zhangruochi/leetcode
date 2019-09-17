# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        
        def helper(root):
            nonlocal res
            if not root: return
            
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        
        helper(root)
        
        return res
            
            
        