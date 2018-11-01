"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
            
        
    
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            nonlocal count
            if not root: return     
            
            left = helper(root.left)
            right = helper(root.right)
            
            if (not left or left == root.val) and (not right or right == root.val):
                count += 1
                return root.val      
            return "#"
        count = 0
        helper(root)
        
        return count