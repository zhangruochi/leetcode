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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return 
        
    
        root_indx = {node:index for index, node in enumerate(inorder)}
        preorder = preorder[::-1]

        def tree_build(left,right):
            nonlocal preorder,inorder
            
            if not preorder or left >= right:
                return 
            
            root = TreeNode(preorder.pop())
            indx = root_indx[root.val]
            
            root.left = tree_build(left,indx)
            root.right = tree_build(indx+1,right)
            
            return root
            
        
        return tree_build(0,len(preorder))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        index = { root: i for i, root in enumerate(inorder) }

        def helper(preorder, inorder, l, r):

            if not preorder:
                return None

            if l > r:
                return None

            root = TreeNode(preorder.pop(0))
            i = index[root.val]

            root.left = helper(preorder,inorder,  l, i-1)
            root.right = helper(preorder, inorder,  i+1, r)
            
            return root 

        return helper(preorder, inorder, 0, len(preorder)-1)