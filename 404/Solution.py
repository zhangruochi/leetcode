"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iter(root,isleaft):
            if not root:
                return 0
            elif not root.left and not root.right and isleaft:
                return root.val
            else:
                return iter(root.left,True) + iter(root.right,False)   

        return iter(root,False)             


                             

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        def traverse(root,flag):
            nonlocal res
            if not root:
                return 
            
            if not root.left and not root.right and flag:
                res += root.val
            
            traverse(root.left,1)
            traverse(root.right,0)
            
        traverse(root,0)
        
        return res
        

                    

                