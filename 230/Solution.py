# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []
        count = 0
        res = None
        
        def inorder(root):
            nonlocal nodes,count, res
            if not root:
                return 
            
            inorder(root.left)
            
            nodes.append(root.val)
            count += 1
            if count == k:
                res = root.val
                return 
            
            inorder(root.right)
        
        inorder(root)
        
        return res
            
        
        