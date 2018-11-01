"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def recursive(self,preorder,inorder):
        if not inorder: return 
        index = inorder.index(preorder.pop())
        root = TreeNode(inorder[index])
        root.left = self.recursive(preorder,inorder[:index])
        root.right = self.recursive(preorder,inorder[index+1:])
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        preorder.reverse()
        return self.recursive(preorder,inorder)