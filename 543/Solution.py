# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
      
    def diameterOfBinaryTree(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root):
            nonlocal diameter
            if not root:
                return 0

            left = max_depth(root.left)
            right = max_depth(root.right)

            diameter = max(diameter,left+right)

            return max(left,right) + 1 
    
        diameter = 0
        max_depth(root)
        
        return diameter
        
        