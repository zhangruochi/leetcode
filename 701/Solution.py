# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return 
        
        def helper(root):
            
            if not root:
                return 
            
            if not root.left and val < root.val:
                root.left = TreeNode(val)
                return 
            if not root.right and val > root.val:
                root.right = TreeNode(val)
                return 
            
            if root.val > val:
                helper(root.left)
            else:
                helper(root.right)
        
        helper(root)
        
        return root