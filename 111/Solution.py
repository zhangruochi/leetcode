"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if not root:
            return 0    
        elif not root.left and root.right:
            return self.minDepth(root.right) + 1 
        elif root.left and not root.right:
            return self.minDepth(root.left) + 1
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))


