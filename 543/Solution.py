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
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        
        def helper(root):
            nonlocal res
            
            if not root:
                return 0
            
            left = helper(root.left) 
            right = helper(root.right)
            
            res = max(res, left + right)
            
            return left+1 if left > right else right+1
        
        helper(root)
        
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = 0

        def helper(root):
            nonlocal res

            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            res = max(res, left + right)

            return max(left, right) + 1

        helper(root)

        return res
            
        